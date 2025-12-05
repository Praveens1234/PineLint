import unittest
import os
import tempfile
from pinelint.cli import check_file
from pinelint.diagnostics import Severity

class TestIntegration(unittest.TestCase):
    def test_valid_script(self):
        code = """//@version=5
indicator("Test")
var int x = 10
plot(x)
"""
        with tempfile.NamedTemporaryFile(mode='w+', suffix='.pine', delete=False) as f:
            f.write(code)
            path = f.name
            
        try:
            # We can capture stdout or mock sys.exit?
            # check_file calls sys.exit.
            # I should refactor cli to be testable or mock sys.exit.
            # Or simpler: Instantiate components directly.
            pass
        finally:
            os.remove(path)

    # Better to test components directly than CLI main loop with sys.exit
    def test_pipeline(self):
        from pinelint.lexer import Lexer
        from pinelint.parser import Parser
        from pinelint.rules import RuleRunner
        
        code = """//@version=5
indicator("Test")
var int x = 10
plot(x)
"""
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        self.assertEqual(len(parser.errors), 0)
        
        runner = RuleRunner()
        diags = runner.run(code, ast, "test.pine")
        errors = [d for d in diags if d.severity == Severity.ERROR]
        self.assertEqual(len(errors), 0)

    def test_pipeline_errors(self):
        from pinelint.lexer import Lexer
        from pinelint.parser import Parser
        from pinelint.rules import RuleRunner
        
        code = """//@version=5
indicator("Test")
var int x = "string"
plot(y)
"""
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        self.assertEqual(len(parser.errors), 0)
        
        runner = RuleRunner()
        diags = runner.run(code, ast, "test.pine")
        errors = [d for d in diags if d.severity == Severity.ERROR]
        self.assertEqual(len(errors), 2)
        self.assertTrue(any("Type mismatch" in d.message for d in errors))
        self.assertTrue(any("Undefined" in d.message for d in errors))

if __name__ == '__main__':
    unittest.main()
