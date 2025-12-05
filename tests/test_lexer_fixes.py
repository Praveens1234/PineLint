import unittest
from pinelint.lexer import Lexer, TokenType

class TestLexerFixes(unittest.TestCase):
    def test_word_boundary_operators(self):
        # 'order' contains 'or', should be IDENTIFIER
        source = "strategy.order"
        lexer = Lexer(source)
        tokens = lexer.tokenize()
        
        # Expected: strategy (ID), . (DOT), order (ID)
        # Not: strategy, ., or, der
        
        self.assertEqual(tokens[0].type, TokenType.KEYWORD)
        self.assertEqual(tokens[0].value, "strategy")
        
        self.assertEqual(tokens[1].type, TokenType.DOT)
        
        self.assertEqual(tokens[2].type, TokenType.IDENTIFIER)
        self.assertEqual(tokens[2].value, "order") # Should be full word
        
    def test_comment_in_string(self):
        source = 'url = "http://example.com"'
        lexer = Lexer(source)
        tokens = lexer.tokenize()
        
        # Should contain STRING token with full value
        # Tokens: url, =, "...", NEWLINE, EOF
        
        str_token = tokens[2]
        self.assertEqual(str_token.type, TokenType.STRING)
        # Lexer preserves quotes in value? No, my lexer usually keeps value raw match
        # Let's check lexer impl: `value = m.group(0)` -> yes keeps quotes
        self.assertIn("//", str_token.value)
        self.assertIn("http:", str_token.value)

    def test_real_comment(self):
        source = 'x = 1 // This is a comment'
        lexer = Lexer(source)
        tokens = lexer.tokenize()
        
        # Should stop after 1
        # Tokens: x, =, 1, NEWLINE, EOF
        self.assertEqual(len(tokens), 5)
        self.assertEqual(tokens[2].value, "1")

if __name__ == '__main__':
    unittest.main()
