# PineLint Knowledge Base

This document serves as the comprehensive specification and rule definition for the PineLint static analysis engine. It covers the 14-point architecture required for validating complex Pine Script (v5/v6) strategies.

## 1. Lexical Rules
*   **Tokenizer:** Custom regex-based lexer (`lexer.py`) supporting Pine Script syntax.
*   **Indentation:** Python-style indentation tracking (Stack-based `INDENT`/`DEDENT` emission).
*   **Comments:** Support for `//` (single-line) and `/* ... */` (multi-line).
*   **Literals:** Support for Integers, Floats, Strings, Booleans, Colors (hex), and `na`.

## 2. Grammar & Syntax
*   **Parser:** Recursive Descent Parser (`parser.py`) with Pratt Parsing for expressions.
*   **Statements:** Control flow (`if`, `for`, `while`, `switch`), Variable Declarations (`var`, `varip`), Assignments (`=`, `:=`).
*   **Advanced Syntax:**
    *   **Tuple Assignments:** `[a, b] = func()` supported.
    *   **Switch Statements:** Full expression and case condition analysis.
    *   **User-Defined Types (UDTs):** `type` keyword and object instantiation (`new`).
    *   **Method Calls:** `obj.method()` resolution to namespace calls (`ta.method(obj)`).

## 3. Type System
*   **Types:** `int`, `float`, `bool`, `string`, `color`, `line`, `label`, `box`, `table`, `array<T>`, `matrix<T>`, `map<K,V>`, `void`, `na`.
*   **User-Defined Types:** Structs defined via `type` are registered types.
*   **Tuples:** Support for Tuple return types (e.g., from `ta.macd`).

## 4. Series vs Simple Rules
*   **Qualifier Hierarchy:** `const` < `input` < `simple` < `series`.
*   **Promotion Rule:** A type with a lower qualifier can always be cast to a higher qualifier (e.g., `const int` -> `series int`).
*   **Strict Validation:** Passing a `series` value to a parameter requiring `simple`, `input`, or `const` triggers **E302 Type Mismatch**.

## 5. Built-in Functions
*   **Database:** `pine_spec.py` contains signatures for 50+ built-in functions including `ta.*`, `strategy.*`, `math.*`, `array.*`, `request.*`.
*   **Namespace Resolution:** Automatic resolution of `ta`, `math`, `array`, etc. namespaces from method calls.

## 6. Built-in Variables
*   **Database:** `pine_spec.py` defines standard variables (`open`, `close`, `high`, `low`, `volume`, `time`, `bar_index`, etc.) with correct types (`series float`, `series int`).
*   **Constants:** `barmerge.*`, `format.*`, `plot.*` constants defined.

## 7. Indicator vs Strategy Rules
*   **ContextRule (E401):** Validates that `strategy.*` functions are **only** used in scripts declared with `strategy()`.
*   Usage in `indicator()` or `library()` triggers an error.

## 8. Scope & Mutability
*   **Scope:** Nested block scoping supported (Global -> Script -> Local -> Block).
*   **Shadowing:** Variables can shadow outer scopes (currently allowed with warning W001 in future).
*   **Mutability:** Reassignment (`:=`) checked against declaration. (Phase 2 implementation partial).

## 9. Security & MTF Rules
*   **RepaintingRule (W005):** Detects `request.security` usage with `lookahead=barmerge.lookahead_on` or `lookahead=true`. This is flagged as a repainting risk.
*   **SecurityRule (SEC01-03):** Scans for malicious Python injection patterns (`exec`, `eval`, `import os`) in identifiers and strings.

## 10. Runtime Constraints
*   **Plot Limits:** `PlotLimitRule` (R004) warns if `plot()` calls exceed 64 (TradingView limit).
*   **Loop/Array:** Parsing supports loops/arrays, semantic validation checks types.

## 11. Error Codes
*   **E1xx:** Lexical/Indentation Errors.
*   **E2xx:** Parsing/Syntax Errors (e.g., E206 Tuple Assignment format).
*   **E3xx:** Semantic Errors (E302 Type Mismatch, E303 Undefined Var, E308 Arg Count).
*   **E4xx:** Context Errors (E401 Strategy in Indicator).
*   **Wxxx:** Warnings (W005 Repainting).
*   **SECxx:** Security Violations.

## 12. Execution Model
*   The analyzer assumes standard Pine Script execution model (initialization block vs per-bar block).
*   `var` declarations are treated as persistent.

## 13. Repainting Analysis
*   Static analysis of `request.security` parameters to identify lookahead bias.

## 14. Structural Templates
*   Supported via standard Pine Script syntax structure:
    1. Version Declaration (`//@version=5`)
    2. Script Declaration (`indicator`/`strategy`)
    3. Global Constants/Inputs
    4. Calculations
    5. Plots/Strategy Calls
