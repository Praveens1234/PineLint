"""
Pine Script Abstract Syntax Tree (AST) Nodes.
Defined as immutable dataclasses.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List, Optional, Union, Any, Tuple

# ==============================================================================
# Visitor Interface
# ==============================================================================


class ASTVisitor(ABC):
    """
    Abstract base class for AST visitors.
    """

    @abstractmethod
    def visit_version_decl(self, node: VersionDecl) -> Any: ...

    @abstractmethod
    def visit_script_decl(self, node: ScriptDecl) -> Any: ...

    @abstractmethod
    def visit_block(self, node: Block) -> Any: ...

    @abstractmethod
    def visit_var_decl(self, node: VarDecl) -> Any: ...

    @abstractmethod
    def visit_assignment(self, node: Assignment) -> Any: ...

    @abstractmethod
    def visit_if_statement(self, node: IfStatement) -> Any: ...

    @abstractmethod
    def visit_for_statement(self, node: ForStatement) -> Any: ...

    @abstractmethod
    def visit_while_statement(self, node: WhileStatement) -> Any: ...

    @abstractmethod
    def visit_expression_statement(self, node: ExpressionStatement) -> Any: ...

    @abstractmethod
    def visit_binary_op(self, node: BinaryOp) -> Any: ...

    @abstractmethod
    def visit_unary_op(self, node: UnaryOp) -> Any: ...

    @abstractmethod
    def visit_function_call(self, node: FunctionCall) -> Any: ...

    @abstractmethod
    def visit_identifier(self, node: Identifier) -> Any: ...

    @abstractmethod
    def visit_literal(self, node: Literal) -> Any: ...

    @abstractmethod
    def visit_ternary_op(self, node: TernaryOp) -> Any: ...

    @abstractmethod
    def visit_array_access(self, node: ArrayAccess) -> Any: ...

    @abstractmethod
    def visit_array_literal(self, node: ArrayLiteral) -> Any: ...

    @abstractmethod
    def visit_switch_statement(self, node: SwitchStatement) -> Any: ...

    @abstractmethod
    def visit_function_def(self, node: FunctionDef) -> Any: ...

    @abstractmethod
    def visit_type_def(self, node: TypeDef) -> Any: ...

    @abstractmethod
    def visit_import_decl(self, node: ImportDecl) -> Any: ...


# ==============================================================================
# Base Nodes
# ==============================================================================


@dataclass(frozen=True)
class ASTNode(ABC):
    line: int
    column: int

    @abstractmethod
    def accept(self, visitor: ASTVisitor) -> Any:
        pass


@dataclass(frozen=True)
class Statement(ASTNode):
    pass


@dataclass(frozen=True)
class Expression(ASTNode):
    pass


# ==============================================================================
# Expression Nodes
# ==============================================================================


@dataclass(frozen=True)
class Literal(Expression):
    value: Union[int, float, str, bool, None]
    type_name: str  # 'int', 'float', 'string', 'bool', 'color', 'na'

    def accept(self, visitor: ASTVisitor) -> Any:
        return visitor.visit_literal(self)


@dataclass(frozen=True)
class Identifier(Expression):
    name: str

    def accept(self, visitor: ASTVisitor) -> Any:
        return visitor.visit_identifier(self)


@dataclass(frozen=True)
class BinaryOp(Expression):
    left: Expression
    operator: str
    right: Expression

    def accept(self, visitor: ASTVisitor) -> Any:
        return visitor.visit_binary_op(self)


@dataclass(frozen=True)
class UnaryOp(Expression):
    operator: str
    operand: Expression

    def accept(self, visitor: ASTVisitor) -> Any:
        return visitor.visit_unary_op(self)


@dataclass(frozen=True)
class CallArgument(ASTNode):
    """
    Represents an argument in a function call.
    Can be positional (name=None) or named (name="length").
    """

    value: Expression
    name: Optional[str] = None

    def accept(self, visitor: ASTVisitor) -> Any:
        # Usually handled within visit_function_call, but good to have
        pass


@dataclass(frozen=True)
class FunctionCall(Expression):
    name: str
    args: List[CallArgument]

    def accept(self, visitor: ASTVisitor) -> Any:
        return visitor.visit_function_call(self)


@dataclass(frozen=True)
class TernaryOp(Expression):
    condition: Expression
    true_expr: Expression
    false_expr: Expression

    def accept(self, visitor: ASTVisitor) -> Any:
        return visitor.visit_ternary_op(self)


@dataclass(frozen=True)
class ArrayAccess(Expression):
    array: Expression
    indices: List[Expression]  # Support a[x, y]

    def accept(self, visitor: ASTVisitor) -> Any:
        return visitor.visit_array_access(self)


@dataclass(frozen=True)
class ArrayLiteral(Expression):
    elements: List[Expression]

    def accept(self, visitor: ASTVisitor) -> Any:
        return visitor.visit_array_literal(self)


# ==============================================================================
# Statement Nodes
# ==============================================================================


@dataclass(frozen=True)
class Block(Statement):
    statements: List[Statement]

    def accept(self, visitor: ASTVisitor) -> Any:
        return visitor.visit_block(self)


@dataclass(frozen=True)
class VersionDecl(Statement):
    version: int

    def accept(self, visitor: ASTVisitor) -> Any:
        return visitor.visit_version_decl(self)


@dataclass(frozen=True)
class ScriptDecl(Statement):
    """
    Represents indicator(), strategy(), or library() declaration.
    """

    script_type: str  # 'indicator', 'strategy', 'library'
    args: List[CallArgument]

    def accept(self, visitor: ASTVisitor) -> Any:
        return visitor.visit_script_decl(self)


@dataclass(frozen=True)
class VarDecl(Statement):
    """
    Variable declaration.
    e.g., `var int x = 1`
    """

    name: str
    value: Expression
    type_hint: Optional[str] = None  # e.g. 'int'
    qualifier: Optional[str] = None  # 'var', 'varip' or None
    is_tuple: bool = False  # for [a, b] = func() declarations

    def accept(self, visitor: ASTVisitor) -> Any:
        return visitor.visit_var_decl(self)


@dataclass(frozen=True)
class Assignment(Statement):
    """
    Reassignment using :=
    """

    target: str  # Identifier name
    value: Expression

    def accept(self, visitor: ASTVisitor) -> Any:
        return visitor.visit_assignment(self)


# Control flow nodes are both Statement and Expression in Pine (mostly).
# We inherit from Expression to allow them in assignment contexts.
# But they are also Statements. (Expression inherits ASTNode, same as Statement).
# We might need to check instance if we really care about Statement vs Expression.


@dataclass(frozen=True)
class IfStatement(Expression):
    condition: Expression
    then_block: Block
    else_block: Optional[Block] = None

    def accept(self, visitor: ASTVisitor) -> Any:
        return visitor.visit_if_statement(self)


@dataclass(frozen=True)
class ForStatement(Expression):
    """
    for i = 0 to 10 by 2
    """

    var_name: str
    start_expr: Expression
    end_expr: Expression
    body: Block
    step_expr: Optional[Expression] = None

    def accept(self, visitor: ASTVisitor) -> Any:
        return visitor.visit_for_statement(self)


@dataclass(frozen=True)
class WhileStatement(Expression):
    condition: Expression
    body: Block

    def accept(self, visitor: ASTVisitor) -> Any:
        return visitor.visit_while_statement(self)


@dataclass(frozen=True)
class SwitchStatement(Expression):
    expression: Optional[Expression]  # switch x
    cases: List[
        Tuple[Optional[Expression], Block]
    ]  # (case_expr, body). Default is case_expr=None

    def accept(self, visitor: ASTVisitor) -> Any:
        return visitor.visit_switch_statement(self)


@dataclass(frozen=True)
class ParamDef(ASTNode):
    name: str
    type_name: Optional[str]
    default: Optional[Expression] = None

    def accept(self, visitor: ASTVisitor) -> Any:
        pass

@dataclass(frozen=True)
class FunctionDef(Statement):
    name: str
    params: List[ParamDef]
    body: Union[Block, Expression]
    return_type: Optional[str] = None
    is_exported: bool = False
    is_method: bool = False

    def accept(self, visitor: ASTVisitor) -> Any:
        return visitor.visit_function_def(self)

@dataclass(frozen=True)
class TypeDef(Statement):
    name: str
    fields: List[VarDecl]
    is_exported: bool = False

    def accept(self, visitor: ASTVisitor) -> Any:
        return visitor.visit_type_def(self)

@dataclass(frozen=True)
class ImportDecl(Statement):
    path: str
    alias: Optional[str] = None

    def accept(self, visitor: ASTVisitor) -> Any:
        return visitor.visit_import_decl(self)

@dataclass(frozen=True)
class ExpressionStatement(Statement):
    """
    An expression used as a statement (e.g., function call 'plot(close)')
    """

    expression: Expression

    def accept(self, visitor: ASTVisitor) -> Any:
        return visitor.visit_expression_statement(self)
