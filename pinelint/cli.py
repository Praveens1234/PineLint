"""
PineLint CLI.
"""

import argparse
import sys
import os
from typing import List

from .lexer import Lexer, LexerError
from .parser import Parser, ParseError
from .rules import RuleRunner
from .diagnostics import Report, Diagnostic, Severity


def check_file(filepath: str, format_type: str):
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}", file=sys.stderr)
        sys.exit(2)

    with open(filepath, "r") as f:
        source = f.read()

    report = Report()

    # 1. Lexer
    try:
        lexer = Lexer(source)
        tokens = lexer.tokenize()
    except LexerError as e:
        # We can't proceed to parse if lexer fails drastically, or we can try?
        # Assuming e has message.
        # LexerError might be simple exception.
        report.add(Diagnostic(Severity.ERROR, "E001", str(e), 1, 1, filepath))
        _print_report(report, format_type)
        sys.exit(1)

    # 2. Parser
    parser = Parser(tokens)
    ast_root = parser.parse()  # Returns List[Statement]

    # Collect parser errors
    for e in parser.errors:
        report.add(
            Diagnostic(Severity.ERROR, "E002", str(e), e.line, e.column, filepath)
        )

    # 3. Rule Engine
    if not parser.errors:  # Only run rules if parse succeeded (or try anyway?)
        runner = RuleRunner()
        rule_diagnostics = runner.run(source, ast_root, filepath)
        for d in rule_diagnostics:
            report.add(d)

    _print_report(report, format_type)

    if report.has_errors():
        sys.exit(1)
    else:
        sys.exit(0)


def _print_report(report: Report, format_type: str):
    if format_type == "json":
        print(report.to_json())
    else:
        print(report.to_text())


def main():
    parser = argparse.ArgumentParser(
        description="PineLint - Pine Script Static Analyzer"
    )
    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # Check command
    check_parser = subparsers.add_parser("check", help="Check a Pine Script file")
    check_parser.add_argument("file", help="Path to .pine file")
    check_parser.add_argument(
        "--format", choices=["text", "json"], default="text", help="Output format"
    )

    args = parser.parse_args()

    if args.command == "check":
        check_file(args.file, args.format)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
