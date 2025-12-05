from pinelint.lexer import Lexer, TokenType
with open("tests/repro.pine") as f:
    code = f.read()
lexer = Lexer(code)
tokens = lexer.tokenize()
for t in tokens:
    print(t)
