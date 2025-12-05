# PineLint

A static analysis tool for TradingView Pine Script (v5/v6).

## Features

- **Lexer/Parser:** Custom recursive descent parser with indentation support.
- **Semantic Analysis:** Symbol table, scope resolution, and type checking.
- **Rules:**
  - Structural checks (Version directive).
  - Semantic checks (Undefined variables, Type mismatches).
  - Function signature validation.
- **CLI:** JSON and Text reporting.

## Usage

```bash
# Install
pip install .

# Check a file
pinelint check my_script.pine

# JSON output
pinelint check my_script.pine --format json
```

## Architecture

- `pinelint/pine_spec.py`: Language specification (generated).
- `pinelint/lexer.py`: Tokenizer.
- `pinelint/ast_nodes.py`: AST definitions.
- `pinelint/parser.py`: Parser.
- `pinelint/semantic.py`: Semantic Analysis.
- `pinelint/rules.py`: Rule Engine.
- `pinelint/diagnostics.py`: Reporting.
- `pinelint/cli.py`: Command Line Interface.
