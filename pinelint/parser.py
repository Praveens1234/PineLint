"""
Pine Script Recursive Descent Parser.
"""

from typing import List, Optional, Callable, Dict
from enum import IntEnum, auto

from .lexer import Token, TokenType
from .ast_nodes import (
    ASTNode,
    Statement,
    Expression,
    Literal,
    Identifier,
    BinaryOp,
    UnaryOp,
    FunctionCall,
    CallArgument,
    TernaryOp,
    ArrayAccess,
    ArrayLiteral,
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
    FunctionDef,
    ParamDef,
    TypeDef,
    ImportDecl,
)
from .pine_spec import PINE_TYPES


class Precedence(IntEnum):
    LOWEST = 1
    TERNARY = 2  # ? :
    OR = 3  # or
    AND = 4  # and
    EQUALITY = 5  # == !=
    COMPARISON = 6  # < > <= >=
    TERM = 7  # + -
    FACTOR = 8  # * / %
    UNARY = 9  # not - (unary)
    CALL = 10  # . () []


class ParseError(Exception):
    def __init__(self, message: str, token: Token):
        super().__init__(message)
        self.token = token
        self.line = token.line
        self.column = token.column


class Parser:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.current = 0
        self.errors: List[ParseError] = []
        self.indent_level = 0

        # Pratt Parsing Dispatch Tables
        self.prefix_parse_fns: Dict[TokenType, Callable[[], Expression]] = {
            TokenType.IDENTIFIER: self.parse_identifier,
            TokenType.LITERAL_INTEGER: self.parse_literal,
            TokenType.LITERAL_FLOAT: self.parse_literal,
            TokenType.LITERAL_STRING: self.parse_literal,
            TokenType.LITERAL_COLOR: self.parse_literal,
            TokenType.LPAREN: self.parse_grouping,
            TokenType.LBRACKET: self.parse_array_literal,
            TokenType.OPERATOR: self.parse_unary,  # For - and +
            TokenType.KEYWORD: self.parse_keyword_prefix,  # For true, false, na, var?, not, if, switch
        }

        self.infix_parse_fns: Dict[TokenType, Callable[[Expression], Expression]] = {
            TokenType.OPERATOR: self.parse_binary,
            TokenType.KEYWORD: self.parse_binary,  # and, or
            TokenType.LPAREN: self.parse_call,
            TokenType.LBRACKET: self.parse_array_access,
            TokenType.DOT: self.parse_method_call,
            TokenType.QUESTION: self.parse_ternary,
        }

        # Precedence map for operators
        self.precedences: Dict[str, int] = {
            "or": Precedence.OR,
            "and": Precedence.AND,
            "==": Precedence.EQUALITY,
            "!=": Precedence.EQUALITY,
            "<": Precedence.COMPARISON,
            ">": Precedence.COMPARISON,
            "<=": Precedence.COMPARISON,
            ">=": Precedence.COMPARISON,
            "+": Precedence.TERM,
            "-": Precedence.TERM,
            "*": Precedence.FACTOR,
            "/": Precedence.FACTOR,
            "%": Precedence.FACTOR,
        }

    # ==========================================================================
    # Helper Methods
    # ==========================================================================

    def peek(self) -> Token:
        return self.tokens[self.current]

    def peek_at(self, offset: int) -> Token:
        if self.current + offset >= len(self.tokens):
            return self.tokens[-1]
        return self.tokens[self.current + offset]

    def previous(self) -> Token:
        return self.tokens[self.current - 1]

    def is_at_end(self) -> bool:
        return self.peek().type == TokenType.EOF

    def check(self, type_: TokenType) -> bool:
        if self.is_at_end():
            return False
        return self.peek().type == type_

    def match(self, *types: TokenType) -> bool:
        for type_ in types:
            if self.check(type_):
                if type_ == TokenType.INDENT: self.indent_level += 1
                if type_ == TokenType.DEDENT: self.indent_level -= 1
                self.advance()
                return True
        return False

    def advance(self) -> Token:
        if not self.is_at_end():
            self.current += 1
        return self.previous()

    def consume(self, type_: TokenType, message: str) -> Token:
        if self.check(type_):
            if type_ == TokenType.INDENT: self.indent_level += 1
            if type_ == TokenType.DEDENT: self.indent_level -= 1
            return self.advance()
        found = self.peek()
        raise self.error(found, f"{message} Found {found.type.name} '{found.value}'")

    def error(self, token: Token, message: str) -> ParseError:
        err = ParseError(message, token)
        self.errors.append(err)
        return err

    def synchronize(self):
        self.advance()
        while not self.is_at_end():
            prev = self.previous()
            if prev.type == TokenType.NEWLINE:
                return
            
            if prev.type == TokenType.INDENT:
                self.indent_level += 1
            elif prev.type == TokenType.DEDENT:
                self.indent_level -= 1
                
            self.advance()

    def skip_newlines(self):
        while self.match(TokenType.NEWLINE, TokenType.INDENT):
            pass

    def skip_newlines_only(self):
        while self.match(TokenType.NEWLINE):
            pass

    # ==========================================================================
    # Core Parsing
    # ==========================================================================

    def parse(self) -> List[Statement]:
        statements = []
        try:
            # 1. Version Declaration
            if self.peek().value == "//@version":
                pass

            while not self.is_at_end():
                if self.match(TokenType.NEWLINE):
                    continue

                stmt = self.parse_statement()
                if stmt:
                    statements.append(stmt)

        except ParseError as e:
            self.synchronize()

        return statements

    # ==========================================================================
    # Statement Parsing
    # ==========================================================================

    def parse_statement(self) -> Optional[Statement]:
        try:
            is_export = False
            is_method = False
            
            if self.check(TokenType.KEYWORD) and self.peek().value == "export":
                self.advance()
                is_export = True
            
            if self.check(TokenType.KEYWORD) and self.peek().value == "method":
                self.advance()
                is_method = True
                
            if is_export or is_method:
                if self.check(TokenType.KEYWORD) and self.peek().value == 'type':
                    self.advance()
                    return self.parse_type_def(is_export)
                return self.parse_function_def(is_export, is_method)

            if self.match(TokenType.KEYWORD):
                kw = self.previous().value
                if kw == "if":
                    return self.parse_if_statement()
                elif kw == "for":
                    return self.parse_for_statement()
                elif kw == "while":
                    return self.parse_while_statement()
                elif kw == "switch":
                    return self.parse_switch_statement()
                elif kw == "type":
                    return self.parse_type_def(False)
                elif kw == "import":
                    return self.parse_import()
                elif kw == "version":
                    pass
                elif kw in ["indicator", "strategy", "library"]:
                    return self.parse_script_decl(kw)
                elif kw == "var" or kw == "varip":
                    return self.parse_var_decl(kw)

            if self.check(TokenType.IDENTIFIER) and self.is_function_def_lookahead():
                return self.parse_function_def(False, False)

            if self.check(TokenType.IDENTIFIER):
                if self.peek().value in PINE_TYPES:
                    if self.current + 1 < len(self.tokens) and self.tokens[self.current+1].type == TokenType.IDENTIFIER:
                        peek3 = self.tokens[self.current+2] if self.current+2 < len(self.tokens) else None
                        if peek3 and peek3.type == TokenType.LPAREN:
                            return self.parse_function_def(False, False)
                        
                        type_name = self.advance().value
                        name = self.advance().value
                        return self.parse_var_init(name, type_hint=type_name)

            expr = self.parse_expression(Precedence.LOWEST)

            if self.match(TokenType.OPERATOR):
                op = self.previous().value
                if op == "=":
                    if isinstance(expr, Identifier):
                        return self.parse_var_init(expr.name, is_reassignment=False)
                    elif isinstance(expr, ArrayLiteral):
                        # Tuple assignment [a, b] = ...
                        return self.parse_var_init(str(expr), is_reassignment=False)
                    self.error(self.previous(), "Invalid assignment target.")
                elif op == ":=":
                    if isinstance(expr, Identifier):
                        val = self.parse_expression(Precedence.LOWEST)
                        return Assignment(
                            self.previous().line,
                            self.previous().column,
                            target=expr.name,
                            value=val,
                        )
                    elif isinstance(expr, ArrayLiteral):
                        val = self.parse_expression(Precedence.LOWEST)
                        return Assignment(
                            self.previous().line,
                            self.previous().column,
                            target=str(expr),
                            value=val,
                        )
                    self.error(self.previous(), "Invalid reassignment target.")

            return ExpressionStatement(expr.line, expr.column, expression=expr)

        except ParseError as e:
            self.synchronize()
            return None

    def parse_type_signature(self) -> str:
        base_tok = self.advance()
        val = base_tok.value
        
        if self.match(TokenType.OPERATOR) and self.previous().value == '<':
            args = []
            while True:
                args.append(self.parse_type_signature())
                if not self.match(TokenType.COMMA):
                    break
            
            if not self.check(TokenType.OPERATOR) or self.peek().value != '>':
                 raise self.error(self.peek(), "Expect '>' after type args.")
            self.advance()
            val = f"{val}<{','.join(args)}>"
            
        while self.match(TokenType.LBRACKET):
            self.consume(TokenType.RBRACKET, "Expect ']' after '['.")
            val += "[]"
            
        return val

    def is_function_def_lookahead(self) -> bool:
        if self.current + 1 >= len(self.tokens): return False
        if self.tokens[self.current+1].type != TokenType.LPAREN: return False
        
        idx = self.current + 2
        depth = 1
        while idx < len(self.tokens):
            t = self.tokens[idx]
            if t.type == TokenType.LPAREN: depth += 1
            elif t.type == TokenType.RPAREN:
                depth -= 1
                if depth == 0:
                    if idx + 1 < len(self.tokens):
                        next_t = self.tokens[idx+1]
                        return next_t.type == TokenType.OPERATOR and next_t.value == '=>'
                    return False
            idx += 1
        return False

    def parse_function_def(self, is_export: bool, is_method: bool) -> FunctionDef:
        return_type = None
        if self.peek().value in PINE_TYPES:
            if self.current + 1 < len(self.tokens) and self.tokens[self.current+1].type == TokenType.IDENTIFIER:
                 return_type = self.advance().value
        
        name_tok = self.consume(TokenType.IDENTIFIER, "Expect function name.")
        self.consume(TokenType.LPAREN, "Expect '('.")
        
        params = []
        if not self.check(TokenType.RPAREN):
            while True:
                # Skip newlines/indents between params
                self.skip_newlines_only()
                while self.match(TokenType.INDENT): pass 
                
                qualifier = None
                if self.check(TokenType.IDENTIFIER) and self.peek().value in ["series", "simple", "const", "input"]:
                    qualifier = self.advance().value
                
                sig = self.parse_type_signature()
                
                p_type = None
                p_name = None
                
                if self.check(TokenType.IDENTIFIER):
                    p_type = sig
                    p_name = self.advance().value
                else:
                    p_name = sig
                
                if qualifier and p_type:
                    p_type = f"{qualifier} {p_type}"
                elif qualifier and not p_type:
                    p_type = qualifier
                
                default_val = None
                if self.match(TokenType.OPERATOR) and self.previous().value == '=':
                    default_val = self.parse_expression(Precedence.LOWEST, allow_newline=True)
                    
                params.append(ParamDef(name_tok.line, name_tok.column, name=p_name, type_name=p_type, default=default_val))
                
                self.skip_newlines_only()
                while self.match(TokenType.DEDENT): pass

                if not self.match(TokenType.COMMA):
                    break
        
        self.skip_newlines_only()
        while self.match(TokenType.DEDENT): pass
        self.consume(TokenType.RPAREN, "Expect ')'.")
        self.consume(TokenType.OPERATOR, "Expect '=>'.")
        if self.previous().value != '=>':
             raise self.error(self.previous(), "Expect '=>' definition.")
             
        if self.check(TokenType.NEWLINE) and self.tokens[self.current+1].type == TokenType.INDENT:
             body = self.parse_block()
        elif self.check(TokenType.INDENT):
             body = self.parse_block()
        else:
             if self.match(TokenType.NEWLINE):
                 body = self.parse_block()
             else:
                 body = self.parse_expression(Precedence.LOWEST)
                 
        return FunctionDef(name_tok.line, name_tok.column, name=name_tok.value, params=params, body=body, return_type=return_type, is_exported=is_export, is_method=is_method)

    def parse_script_decl(self, type_name: str) -> ScriptDecl:
        self.consume(TokenType.LPAREN, "Expect '(' after script declaration.")
        args = self.parse_arguments()
        self.consume(TokenType.RPAREN, "Expect ')' after arguments.")
        return ScriptDecl(
            self.previous().line,
            self.previous().column,
            script_type=type_name,
            args=args,
        )

    def parse_var_decl(self, qualifier: str) -> VarDecl:
        type_hint = None
        if self.peek().value in PINE_TYPES:
            type_hint = self.advance().value

        name = self.consume(TokenType.IDENTIFIER, "Expect variable name.").value

        return self.parse_var_init(name, type_hint, qualifier)

    def parse_var_init(
        self,
        name: str,
        type_hint: str = None,
        qualifier: str = None,
        is_reassignment: bool = False,
    ) -> VarDecl:
        if (
            not is_reassignment
            and self.check(TokenType.OPERATOR)
            and self.peek().value == "="
        ):
            self.advance()

        val = self.parse_expression(Precedence.LOWEST, allow_newline=True)
        return VarDecl(
            val.line,
            val.column,
            name=name,
            value=val,
            type_hint=type_hint,
            qualifier=qualifier,
        )

    def parse_block(self) -> Block:
        if self.match(TokenType.NEWLINE):
             pass
        elif self.check(TokenType.INDENT):
             pass 
        else:
             self.consume(TokenType.NEWLINE, "Expect newline before block.")

        self.consume(TokenType.INDENT, "Expect indentation for block.")

        stmts = []
        while not self.check(TokenType.DEDENT) and not self.is_at_end():
            if self.match(TokenType.NEWLINE):
                continue
            
            # Check for dedent again after newline
            if self.check(TokenType.DEDENT):
                break

            stmt = self.parse_statement()
            if stmt:
                stmts.append(stmt)

        self.consume(TokenType.DEDENT, "Expect end of block (dedent).")
        return Block(stmts[0].line if stmts else 0, 0, statements=stmts)

    # ==========================================================================
    # Expression Parsing (Pratt)
    # ==========================================================================

    def parse_expression(self, precedence: int, allow_newline: bool = False) -> Expression:
        start_level = self.indent_level
        
        # Prefix Indentation (Line continuation at start of expression)
        if self.check(TokenType.NEWLINE):
             # Check if followed by INDENT
             idx = 1
             has_indent = False
             while self.current + idx < len(self.tokens) and self.tokens[self.current+idx].type == TokenType.INDENT:
                 has_indent = True
                 idx += 1
             
             if has_indent:
                 self.advance() # Consume NL
                 while self.check(TokenType.INDENT):
                     self.indent_level += 1
                     self.advance()
             elif allow_newline:
                 self.advance() # Skip NL (continuation without indent? only if allowed)
        
        token = self.peek()
        
        handler = None
        if token.type in self.prefix_parse_fns:
            handler = self.prefix_parse_fns[token.type]
        
        if not handler:
            raise self.error(
                token, f"Expect expression. Found {token.type.name} '{token.value}'"
            )

        self.advance()
        left = handler()

        # Infix
        while True:
            # Determine if we should continue (must be same line or indented)
            lookahead = 0
            while self.peek_at(lookahead).type == TokenType.NEWLINE:
                lookahead += 1
            
            is_continuation = True
            if lookahead > 0:
                # We have newlines. Must be followed by INDENT to be a continuation.
                if self.peek_at(lookahead).type == TokenType.INDENT:
                    is_continuation = True
                else:
                    is_continuation = False
            
            if not is_continuation:
                break
            
            # Skip NLs and INDENTs to find the next meaningful token
            target_idx = lookahead
            while self.peek_at(target_idx).type in (TokenType.NEWLINE, TokenType.INDENT):
                target_idx += 1
            
            target = self.peek_at(target_idx)
            if target.type == TokenType.EOF: break
            
            # Special handling for Generic Function Call: ID < Type > (
            if target.type == TokenType.OPERATOR and target.value == '<':
                 t1 = self.peek_at(target_idx + 1)
                 t2 = self.peek_at(target_idx + 2)
                 t3 = self.peek_at(target_idx + 3)
                 
                 if t2.type == TokenType.OPERATOR and t2.value == '>' and t3.type == TokenType.LPAREN:
                      # Consume whitespace up to <
                      while self.peek() != target:
                          if self.check(TokenType.INDENT): self.indent_level += 1
                          if self.check(TokenType.DEDENT): self.indent_level -= 1
                          self.advance()
                      
                      self.advance() # <
                      self.advance() # Type
                      self.advance() # >
                      continue

            # Check Precedence of the target token
            if self.get_precedence(target) <= precedence:
                break
            
            # Check if target is a valid infix operator
            infix_handler = self.infix_parse_fns.get(target.type)
            if not infix_handler:
                break
                
            # It IS a continuation. Consume the whitespace we skipped.
            while self.peek() != target:
                if self.check(TokenType.INDENT): self.indent_level += 1
                if self.check(TokenType.DEDENT): self.indent_level -= 1
                self.advance()
            
            # Now consume the operator
            self.advance()
            left = infix_handler(left)
            
        # Cleanup Indents
        while self.indent_level > start_level:
            if self.check(TokenType.NEWLINE):
                self.advance()
                continue
            self.consume(TokenType.DEDENT, "Expect DEDENT")

        return left

    def get_precedence(self, token: Token) -> int:
        if token.type == TokenType.OPERATOR:
            return self.precedences.get(token.value, Precedence.LOWEST)
        if token.type == TokenType.LPAREN:
            return Precedence.CALL
        if token.type == TokenType.LBRACKET:
            return Precedence.CALL
        if token.type == TokenType.DOT:
            return Precedence.CALL
        if token.type == TokenType.QUESTION:
            return Precedence.TERNARY
        if token.type == TokenType.KEYWORD:
            return self.precedences.get(token.value, Precedence.LOWEST)
        return Precedence.LOWEST

    def parse_identifier(self) -> Expression:
        return Identifier(
            self.previous().line, self.previous().column, name=self.previous().value
        )

    def parse_literal(self) -> Expression:
        tok = self.previous()
        val = tok.value
        type_name = "string"

        if tok.type == TokenType.LITERAL_INTEGER:
            val = int(val)
            type_name = "int"
        elif tok.type == TokenType.LITERAL_FLOAT:
            val = float(val)
            type_name = "float"
        elif tok.type == TokenType.LITERAL_STRING:
            val = val[1:-1]
            type_name = "string"
        elif tok.type == TokenType.LITERAL_COLOR:
            type_name = "color"

        return Literal(tok.line, tok.column, value=val, type_name=type_name)

    def parse_keyword_prefix(self) -> Expression:
        tok = self.previous()
        if tok.value in ["true", "false"]:
            return Literal(
                tok.line, tok.column, value=(tok.value == "true"), type_name="bool"
            )
        if tok.value == "na":
            return Literal(tok.line, tok.column, value=None, type_name="na")
        if tok.value == "not":
            operand = self.parse_expression(Precedence.UNARY, allow_newline=True)
            return UnaryOp(tok.line, tok.column, operator="not", operand=operand)
        if tok.value == "if":
            return self.parse_if_statement()

        raise self.error(tok, f"Unexpected keyword prefix {tok.value}")

    def parse_unary(self) -> Expression:
        tok = self.previous()
        operand = self.parse_expression(Precedence.UNARY, allow_newline=True)
        return UnaryOp(tok.line, tok.column, operator=tok.value, operand=operand)

    def parse_grouping(self) -> Expression:
        expr = self.parse_expression(Precedence.LOWEST, allow_newline=True)
        self.skip_newlines_only()
        self.consume(TokenType.RPAREN, "Expect ')' after expression.")
        return expr

    def parse_array_literal(self) -> Expression:
        tok = self.previous() # [
        elements = []
        if not self.check(TokenType.RBRACKET):
             while True:
                 self.skip_newlines_only() 
                 elements.append(self.parse_expression(Precedence.LOWEST, allow_newline=True))
                 self.skip_newlines_only()
                 if not self.match(TokenType.COMMA):
                     break
        
        self.consume(TokenType.RBRACKET, "Expect ']' after array literal.")
        return ArrayLiteral(tok.line, tok.column, elements=elements)

    def parse_binary(self, left: Expression) -> Expression:
        tok = self.previous()
        precedence = self.precedences.get(tok.value, Precedence.LOWEST)
        right = self.parse_expression(precedence + 1, allow_newline=True)
        return BinaryOp(
            tok.line, tok.column, left=left, operator=tok.value, right=right
        )

    def parse_call(self, left: Expression) -> Expression:
        args = self.parse_arguments()
        self.consume(TokenType.RPAREN, "Expect ')' after arguments.")
        name = self._extract_dotted_name(left) or "unknown"
        return FunctionCall(left.line, left.column, name=name, args=args)

    def _extract_dotted_name(self, node: Expression) -> Optional[str]:
        if isinstance(node, Identifier):
            return node.name
        if isinstance(node, BinaryOp) and node.operator == '.':
            lhs = self._extract_dotted_name(node.left)
            rhs = self._extract_dotted_name(node.right)
            if lhs and rhs:
                return f"{lhs}.{rhs}"
        return None

    def parse_arguments(self) -> List[CallArgument]:
        args = []
        if not self.check(TokenType.RPAREN):
            while True:
                # Skip newlines before argument
                self.skip_newlines_only()
                if self.check(TokenType.RPAREN): break # Trailing comma support or just empty line
                
                # Consume indents if present (some weird formatting)
                while self.match(TokenType.INDENT): pass 

                expr = self.parse_expression(Precedence.LOWEST, allow_newline=True)

                if (
                    isinstance(expr, Identifier)
                    and self.match(TokenType.OPERATOR)
                    and self.previous().value == "="
                ):
                    val = self.parse_expression(Precedence.LOWEST, allow_newline=True)
                    args.append(
                        CallArgument(expr.line, expr.column, name=expr.name, value=val)
                    )
                else:
                    args.append(
                        CallArgument(expr.line, expr.column, value=expr, name=None)
                    )

                self.skip_newlines_only()
                while self.match(TokenType.DEDENT): pass

                if not self.match(TokenType.COMMA):
                    break
        
        self.skip_newlines_only()
        while self.match(TokenType.DEDENT): pass
        return args

    def parse_array_access(self, left: Expression) -> Expression:
        indices = []
        if not self.check(TokenType.RBRACKET):
            while True:
                indices.append(self.parse_expression(Precedence.LOWEST, allow_newline=True))
                if not self.match(TokenType.COMMA):
                    break
        self.consume(TokenType.RBRACKET, "Expect ']' after index.")
        return ArrayAccess(left.line, left.column, array=left, indices=indices)

    def parse_method_call(self, left: Expression) -> Expression:
        name_tok = self.consume(TokenType.IDENTIFIER, "Expect property name after '.'.")
        prop = Identifier(name_tok.line, name_tok.column, name=name_tok.value)
        return BinaryOp(left.line, left.column, left=left, operator=".", right=prop)

    def parse_ternary(self, left: Expression) -> Expression:
        true_expr = self.parse_expression(Precedence.LOWEST, allow_newline=True)
        self.skip_newlines_only()
        self.consume(TokenType.COLON, "Expect ':' in ternary operator.")
        false_expr = self.parse_expression(Precedence.TERNARY, allow_newline=True)
        
        return TernaryOp(left.line, left.column, condition=left, true_expr=true_expr, false_expr=false_expr)

    def parse_if_statement(self) -> IfStatement:
        tok = self.previous()
        cond = self.parse_expression(Precedence.LOWEST)

        then_block = self.parse_block()
        else_block = None

        if self.match(TokenType.NEWLINE):
            pass

        if self.check(TokenType.KEYWORD) and self.peek().value == "else":
            self.advance()
            if self.check(TokenType.KEYWORD) and self.peek().value == "if":
                # Handle 'else if' by parsing the if statement and wrapping it in a block
                else_block = Block(self.peek().line, self.peek().column, [self.parse_if_statement()])
            else:
                else_block = self.parse_block()

        return IfStatement(
            tok.line,
            tok.column,
            condition=cond,
            then_block=then_block,
            else_block=else_block,
        )

    def parse_for_statement(self) -> ForStatement:
        tok = self.previous()
        name = self.consume(TokenType.IDENTIFIER, "Expect loop variable.").value
        self.consume(TokenType.OPERATOR, "Expect '='.")
        if self.previous().value != "=":
            raise self.error(self.previous(), "Expect '=' in for loop.")

        start = self.parse_expression(Precedence.LOWEST)

        if self.check(TokenType.KEYWORD) and self.peek().value == "to":
            self.advance()
        else:
            found = self.peek()
            raise self.error(found, f"Expect 'to' in for loop. Found {found.type.name} '{found.value}'")

        end = self.parse_expression(Precedence.LOWEST)

        step = None
        if self.check(TokenType.KEYWORD) and self.peek().value == "by":
            self.advance()
            step = self.parse_expression(Precedence.LOWEST)

        body = self.parse_block()
        return ForStatement(
            tok.line,
            tok.column,
            var_name=name,
            start_expr=start,
            end_expr=end,
            body=body,
            step_expr=step,
        )

    def parse_while_statement(self) -> WhileStatement:
        tok = self.previous()
        cond = self.parse_expression(Precedence.LOWEST)
        body = self.parse_block()
        return WhileStatement(tok.line, tok.column, condition=cond, body=body)

    def parse_switch_statement(self) -> SwitchStatement:
        tok = self.previous()
        expr = None
        if not self.check(TokenType.NEWLINE):
            expr = self.parse_expression(Precedence.LOWEST)

        self.consume(TokenType.NEWLINE, "Expect newline before switch block.")
        self.consume(TokenType.INDENT, "Expect indentation.")

        cases = []
        while not self.check(TokenType.DEDENT) and not self.is_at_end():
            if self.match(TokenType.NEWLINE):
                continue

            case_expr = None
            if self.match(TokenType.OPERATOR) and self.previous().value == "=>":
                pass
            else:
                case_expr = self.parse_expression(Precedence.LOWEST)
                self.consume(TokenType.OPERATOR, "Expect '=>'.")

            if self.check(TokenType.NEWLINE) and self.peek_at(1).type == TokenType.INDENT:
                 block = self.parse_block()
            elif self.check(TokenType.INDENT):
                 block = self.parse_block()
            else:
                 stmt_expr = self.parse_expression(Precedence.LOWEST)
                 block = Block(stmt_expr.line, stmt_expr.column, [ExpressionStatement(stmt_expr.line, stmt_expr.column, stmt_expr)])
            
            cases.append((case_expr, block))

        self.consume(TokenType.DEDENT, "End switch")
        return SwitchStatement(tok.line, tok.column, expression=expr, cases=cases)

    def parse_type_def(self, is_export: bool) -> TypeDef:
        name_tok = self.consume(TokenType.IDENTIFIER, "Expect type name.")
        
        self.consume(TokenType.NEWLINE, "Expect newline before fields.")
        self.consume(TokenType.INDENT, "Expect indentation for fields.")
        
        fields = []
        while not self.check(TokenType.DEDENT) and not self.is_at_end():
            if self.match(TokenType.NEWLINE):
                continue
            
            type_sig = self.parse_type_signature()
            f_name = self.consume(TokenType.IDENTIFIER, "Expect field name.").value
            
            default_val = None
            if self.match(TokenType.OPERATOR) and self.previous().value == '=':
                default_val = self.parse_expression(Precedence.LOWEST)
            
            val_node = default_val if default_val else Literal(name_tok.line, name_tok.column, None, 'na')
            fields.append(VarDecl(name_tok.line, name_tok.column, name=f_name, type_hint=type_sig, value=val_node))
            
        self.consume(TokenType.DEDENT, "Expect end of type definition.")
        
        return TypeDef(name_tok.line, name_tok.column, name=name_tok.value, fields=fields, is_exported=is_export)

    def parse_import(self) -> ImportDecl:
        path_parts = []
        while not self.is_at_end() and not self.check(TokenType.NEWLINE):
            if self.check(TokenType.IDENTIFIER) and self.peek().value == 'as':
                break
            path_parts.append(self.advance().value)
            
        path = "".join(path_parts)
        alias = None
        if self.check(TokenType.IDENTIFIER) and self.peek().value == 'as':
            self.advance()
            alias = self.consume(TokenType.IDENTIFIER, "Expect alias.").value
            
        return ImportDecl(0, 0, path=path, alias=alias)
