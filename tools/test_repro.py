from pinelint.lexer import Lexer
from pinelint.parser import Parser

with open("tests/repro.pine") as f:
    code = f.read()
    
lexer = Lexer(code)
tokens = lexer.tokenize()
parser = Parser(tokens)
parser.parse()

if parser.errors:
    for e in parser.errors:
        print(e)
else:
    print("Success")
