import unittest
from pinelint.lexer import Lexer, TokenType

class TestLexer(unittest.TestCase):
    def test_basic_tokens(self):
        source = "a = 1 + 2"
        lexer = Lexer(source)
        tokens = lexer.tokenize()
        
        types = [t.type for t in tokens]
        expected = [
            TokenType.IDENTIFIER, TokenType.ASSIGN, TokenType.INTEGER, 
            TokenType.OPERATOR, TokenType.INTEGER, TokenType.NEWLINE, TokenType.EOF
        ]
        self.assertEqual(types, expected)

    def test_indentation(self):
        source = """
if true
    x = 1
    y = 2
z = 3
"""
        lexer = Lexer(source.strip())
        tokens = lexer.tokenize()
        
        # Expected sequence:
        # IF, TRUE, NEWLINE,
        # INDENT, x, =, 1, NEWLINE,
        # y, =, 2, NEWLINE,
        # DEDENT, z, =, 3, NEWLINE, EOF
        
        types = [t.type for t in tokens]
        self.assertIn(TokenType.INDENT, types)
        self.assertIn(TokenType.DEDENT, types)
        
        # Verify counts
        self.assertEqual(types.count(TokenType.INDENT), 1)
        self.assertEqual(types.count(TokenType.DEDENT), 1)

    def test_nested_indentation(self):
        source = """
if true
    if false
        x = 1
    y = 2
"""
        lexer = Lexer(source.strip())
        tokens = lexer.tokenize()
        
        types = [t.type for t in tokens]
        self.assertEqual(types.count(TokenType.INDENT), 2)
        # We expect 2 DEDENTS: one after x=1 (to get back to y=2 level), 
        # and one after y=2 (implicit at EOF to close the first if)
        self.assertEqual(types.count(TokenType.DEDENT), 2)

    def test_version_directive(self):
        source = "//@version=5\nindicator('test')"
        lexer = Lexer(source)
        tokens = lexer.tokenize()
        
        self.assertEqual(tokens[0].type, TokenType.VERSION_DIRECTIVE)
        self.assertEqual(tokens[0].value, "5")

if __name__ == '__main__':
    unittest.main()
