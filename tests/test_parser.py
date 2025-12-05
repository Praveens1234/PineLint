import unittest
from pinelint.lexer import Lexer
from pinelint.parser import Parser
from pinelint.ast_nodes import *

class TestParser(unittest.TestCase):
    def parse(self, source):
        lexer = Lexer(source)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        return parser.parse()

    def test_basic_assignment(self):
        source = "x = 10"
        script = self.parse(source)
        self.assertIsInstance(script.statements[0], Assignment)
        self.assertEqual(script.statements[0].target, "x")

    def test_function_call(self):
        source = "ta.sma(close, 14)"
        script = self.parse(source)
        stmt = script.statements[0]
        self.assertIsInstance(stmt, ExpressionStatement)
        call = stmt.expression
        self.assertIsInstance(call, FunctionCall)
        self.assertEqual(call.name, "ta.sma")
        self.assertEqual(len(call.args), 2)

    def test_block_parsing(self):
        source = """
if true
    x = 1
else
    x = 2
"""
        script = self.parse(source.strip())
        stmt = script.statements[0]
        self.assertIsInstance(stmt, IfStatement)
        self.assertIsInstance(stmt.then_block, Block)
        self.assertIsInstance(stmt.else_block, Block)
        self.assertEqual(len(stmt.then_block.statements), 1)

    def test_ternary_op(self):
        source = "a = cond ? 1 : 0"
        script = self.parse(source)
        stmt = script.statements[0]
        self.assertIsInstance(stmt.value, TernaryOp)

    def test_operator_precedence(self):
        source = "x = 1 + 2 * 3"
        script = self.parse(source)
        # Expected: 1 + (2 * 3) -> BinaryOp(1, +, BinaryOp(2, *, 3))
        expr = script.statements[0].value
        self.assertEqual(expr.operator, "+")
        self.assertEqual(expr.right.operator, "*")

    def test_untyped_var_decl(self):
        source = "var x = 1"
        script = self.parse(source)
        stmt = script.statements[0]
        self.assertIsInstance(stmt, VarDecl)
        self.assertEqual(stmt.name, "x")
        self.assertIsNone(stmt.type_hint)

    def test_typed_var_decl(self):
        source = "var int y = 2"
        script = self.parse(source)
        stmt = script.statements[0]
        self.assertIsInstance(stmt, VarDecl)
        self.assertEqual(stmt.name, "y")
        self.assertEqual(stmt.type_hint, "int")

if __name__ == '__main__':
    unittest.main()
