"""
Pine Script Semantic Analyzer.
"""

from typing import Dict, List, Optional, Any, Union
from dataclasses import dataclass
from enum import Enum

from .ast_nodes import (
    ASTVisitor,
    ASTNode,
    Block,
    VersionDecl,
    ScriptDecl,
    VarDecl,
    Assignment,
    IfStatement,
    ForStatement,
    WhileStatement,
    SwitchStatement,
    ExpressionStatement,
    BinaryOp,
    UnaryOp,
    FunctionCall,
    Identifier,
    Literal,
    TernaryOp,
    ArrayAccess,
    ArrayLiteral,
    CallArgument,
    FunctionDef,
    TypeDef,
    ImportDecl,
)
from .pine_spec import (
    PINE_VARIABLES,
    PINE_FUNCTIONS,
    TypeQualifier,
    BuiltinFunction,
    BuiltinVariable,
)


@dataclass
class Symbol:
    name: str
    type: str  # Full type string, e.g., "series int"
    declared_at: ASTNode
    is_mutable: bool = False
    usage_count: int = 0


class Scope:
    def __init__(self, parent: Optional["Scope"] = None):
        self.parent = parent
        self.symbols: Dict[str, Symbol] = {}

    def define(self, name: str, symbol: Symbol):
        self.symbols[name] = symbol

    def resolve(self, name: str) -> Optional[Symbol]:
        if name in self.symbols:
            return self.symbols[name]
        if self.parent:
            return self.parent.resolve(name)
        return None


class SemanticError(Exception):
    def __init__(self, message: str, node: ASTNode):
        super().__init__(message)
        self.node = node
        self.line = node.line
        self.column = node.column


class TypeSystem:
    # Hierarchy: const -> input -> simple -> series
    QUALIFIERS = ["const", "input", "simple", "series"]
    BASE_TYPES = ["int", "float", "bool", "string", "color", "void", "na"]

    @staticmethod
    def parse_type(type_str: str) -> tuple[str, str]:
        """Returns (qualifier, base_type)."""
        parts = type_str.split(" ")
        if len(parts) == 1:
            if parts[0] in TypeSystem.BASE_TYPES:
                return ("series", parts[0])  # Default to series
            return ("series", parts[0])  # Objects, etc.
        return (parts[0], " ".join(parts[1:]))

    @staticmethod
    def get_qualifier_rank(q: str) -> int:
        if q in TypeSystem.QUALIFIERS:
            return TypeSystem.QUALIFIERS.index(q)
        return 3  # Assume series

    @staticmethod
    def is_compatible(target_type: str, source_type: str) -> bool:
        if target_type == "any" or source_type == "any":
            return True
        if source_type == "na":
            return True  # na is compatible with everything (nullable)

        t_qual, t_base = TypeSystem.parse_type(target_type)
        s_qual, s_base = TypeSystem.parse_type(source_type)

        if TypeSystem.get_qualifier_rank(s_qual) > TypeSystem.get_qualifier_rank(
            t_qual
        ):
            return False

        # Base type check
        if t_base == s_base:
            return True
        if t_base == "float" and s_base == "int":
            return True  # Implicit int->float
        return False

    @staticmethod
    def infer_binary_op(left_type: str, operator: str, right_type: str) -> str:
        l_qual, l_base = TypeSystem.parse_type(left_type)
        r_qual, r_base = TypeSystem.parse_type(right_type)

        # Result qualifier is max of operands
        res_rank = max(
            TypeSystem.get_qualifier_rank(l_qual), TypeSystem.get_qualifier_rank(r_qual)
        )
        res_qual = TypeSystem.QUALIFIERS[res_rank]

        # Result base
        if operator in ["+", "-", "*", "/", "%"]:
            if l_base == "float" or r_base == "float":
                return f"{res_qual} float"
            if l_base == "int" and r_base == "int":
                return f"{res_qual} int"
            # String concat
            if l_base == "string" or r_base == "string":
                if operator == "+":
                    return f"{res_qual} string"

        if operator in ["==", "!=", "<", ">", "<=", ">="]:
            return f"{res_qual} bool"

        if operator in ["and", "or"]:
            return f"{res_qual} bool"

        return f"{res_qual} {l_base}"  # Fallback


class SemanticAnalyzer(ASTVisitor):
    def __init__(self):
        self.global_scope = Scope()
        self.current_scope = self.global_scope
        self.all_scopes: List[Scope] = [self.global_scope]
        self.errors: List[SemanticError] = []
        self.warnings: List[SemanticError] = []

        self._init_builtins()

    def _init_builtins(self):
        # Variables
        for name, var in PINE_VARIABLES.items():
            self.global_scope.define(
                name, Symbol(name, var.type, None, is_mutable=False)
            )

    def visit_version_decl(self, node: VersionDecl) -> Any:
        pass

    def visit_script_decl(self, node: ScriptDecl) -> Any:
        for arg in node.args:
            arg.accept(self)

    def visit_block(self, node: Block) -> Any:
        parent = self.current_scope
        self.current_scope = Scope(parent)
        self.all_scopes.append(self.current_scope)

        last_type = "void"
        for stmt in node.statements:
            res = stmt.accept(self)
            if res:
                last_type = res

        self.current_scope = parent
        return last_type

    def visit_var_decl(self, node: VarDecl) -> Any:
        val_type = node.value.accept(self)

        final_type = val_type
        if node.type_hint:
            target = f"series {node.type_hint}"  # Default to series for safety
            if not TypeSystem.is_compatible(target, val_type):
                self.error(
                    node,
                    f"Type mismatch: Cannot assign '{val_type}' to '{node.type_hint}'",
                )
            final_type = target

        # Redefinition check
        if node.name in self.current_scope.symbols:
            self.error(
                node, f"Variable '{node.name}' already declared in this scope."
            )
        
        # Shadowing check
        p = self.current_scope.parent
        while p:
            if node.name in p.symbols:
                self.warn(node, f"Shadowing variable '{node.name}' from outer scope.")
                break
            p = p.parent

        self.current_scope.define(
            node.name, Symbol(node.name, final_type, node, is_mutable=True)
        )
        return final_type

    def visit_assignment(self, node: Assignment) -> Any:
        val_type = node.value.accept(self)
        sym = self.current_scope.resolve(node.target)
        if not sym:
            self.error(node, f"Undefined variable '{node.target}'")
            return

        if not TypeSystem.is_compatible(sym.type, val_type):
            self.error(
                node,
                f"Type mismatch: Cannot assign '{val_type}' to '{sym.name}' (type '{sym.type}')",
            )

        return val_type

    def visit_identifier(self, node: Identifier) -> Any:
        sym = self.current_scope.resolve(node.name)
        if not sym:
            self.error(node, f"Undefined identifier '{node.name}'")
            return "series any"
        sym.usage_count += 1
        return sym.type

    def visit_literal(self, node: Literal) -> Any:
        return f"const {node.type_name}"

    def visit_binary_op(self, node: BinaryOp) -> Any:
        if node.operator == '.':
            # Try to resolve dotted name (e.g. strategy.long)
            def get_name(n):
                if isinstance(n, Identifier): return n.name
                if isinstance(n, BinaryOp) and n.operator == '.':
                    l = get_name(n.left)
                    r = get_name(n.right)
                    return f"{l}.{r}" if l and r else None
                return None
            
            full_name = get_name(node)
            if full_name:
                sym = self.global_scope.resolve(full_name)
                if sym:
                    return sym.type

        l_type = node.left.accept(self)
        r_type = node.right.accept(self)
        return TypeSystem.infer_binary_op(l_type, node.operator, r_type)

    def visit_unary_op(self, node: UnaryOp) -> Any:
        operand_type = node.operand.accept(self)
        return operand_type

    def visit_function_call(self, node: FunctionCall) -> Any:
        func_def = PINE_FUNCTIONS.get(node.name)
        if not func_def:
            # Check if it's a user-defined function in scope
            sym = self.current_scope.resolve(node.name)
            if sym and sym.type == "function":
                # User defined function. Check args?
                # ASTNode for func def is in sym.declared_at
                return "series any" # TODO: infer return type from Def
                
            self.error(node, f"Unknown function '{node.name}'")
            return "series any"

        # Check arguments count
        params = func_def.params
        is_variadic = params and ("..." in params[-1].name or "arg" in params[-1].name and "," in params[-1].name)
        
        if not is_variadic and len(node.args) > len(params):
            self.error(node, f"Too many arguments for '{node.name}'")

        for arg in node.args:
            arg.value.accept(self)

        return func_def.return_type

    def visit_expression_statement(self, node: ExpressionStatement) -> Any:
        return node.expression.accept(self)

    def visit_if_statement(self, node: IfStatement) -> Any:
        node.condition.accept(self)
        then_type = node.then_block.accept(self)
        if node.else_block:
            node.else_block.accept(self)
        return then_type

    def visit_for_statement(self, node: ForStatement) -> Any:
        parent = self.current_scope
        self.current_scope = Scope(parent)
        self.all_scopes.append(self.current_scope)

        self.current_scope.define(
            node.var_name, Symbol(node.var_name, "simple int", node)
        )

        node.start_expr.accept(self)
        node.end_expr.accept(self)
        if node.step_expr:
            node.step_expr.accept(self)

        node.body.accept(self)

        self.current_scope = parent
        return "void"

    def visit_while_statement(self, node: WhileStatement) -> Any:
        node.condition.accept(self)
        node.body.accept(self)
        return "void"

    def visit_switch_statement(self, node: SwitchStatement) -> Any:
        if node.expression:
            node.expression.accept(self)
        for case_expr, block in node.cases:
            if case_expr:
                case_expr.accept(self)
            block.accept(self)
        return "void"

    def visit_ternary_op(self, node: TernaryOp) -> Any:
        node.condition.accept(self)
        t = node.true_expr.accept(self)
        f = node.false_expr.accept(self)
        return t

    def visit_array_access(self, node: ArrayAccess) -> Any:
        arr_type = node.array.accept(self)
        for idx in node.indices:
            idx.accept(self)
        if "array<" in arr_type:
            import re
            m = re.search(r"array<(.+)>", arr_type)
            if m:
                return f"series {m.group(1)}"
        return "series any"

    def visit_array_literal(self, node: ArrayLiteral) -> Any:
        for el in node.elements:
            el.accept(self)
        return "series array<any>"

    def visit_function_def(self, node: FunctionDef) -> Any:
        parent = self.current_scope
        self.current_scope = Scope(parent)
        self.all_scopes.append(self.current_scope)
        
        for param in node.params:
            p_type = param.type_name if param.type_name else "series any"
            self.current_scope.define(param.name, Symbol(param.name, p_type, param))
            if param.default:
                param.default.accept(self)
        
        body_type = "void"
        if isinstance(node.body, ASTNode):
             body_type = node.body.accept(self)
        else:
             body_type = node.body.accept(self)
             
        parent.define(node.name, Symbol(node.name, "function", node))
        
        self.current_scope = parent
        return "void"

    def visit_type_def(self, node: TypeDef) -> Any:
        # Register type constructor?
        # For now just valid.
        return "void"

    def visit_import_decl(self, node: ImportDecl) -> Any:
        if node.alias:
            self.global_scope.define(node.alias, Symbol(node.alias, "namespace", node))
        return "void"

    def error(self, node: ASTNode, message: str):
        self.errors.append(SemanticError(message, node))

    def warn(self, node: ASTNode, message: str):
        self.warnings.append(SemanticError(message, node))
