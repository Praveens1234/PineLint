"""
Rule Engine.
"""

from abc import ABC, abstractmethod
from typing import List, Optional
import re

from .ast_nodes import ASTNode
from .diagnostics import Diagnostic, Severity
from .semantic import SemanticAnalyzer, SemanticError


class Rule(ABC):
    @abstractmethod
    def check(
        self, source: str, ast_root: Optional[ASTNode], file_path: str
    ) -> List[Diagnostic]:
        pass


class VersionCheckRule(Rule):
    """
    R001: Script must have exactly one //@version directive.
    R003: Version number must be 4, 5, or 6.
    """

    def check(
        self, source: str, ast_root: Optional[ASTNode], file_path: str
    ) -> List[Diagnostic]:
        diagnostics = []
        # Regex search for //@version
        # Note: Lexer stripped comments, so we search raw source.
        # Assuming simple grep style
        matches = list(re.finditer(r"^//@version=(\d+)", source, re.MULTILINE))

        if not matches:
            diagnostics.append(
                Diagnostic(
                    Severity.ERROR,
                    "R001",
                    "Missing //@version directive.",
                    1,
                    1,
                    file_path,
                )
            )
        elif len(matches) > 1:
            diagnostics.append(
                Diagnostic(
                    Severity.ERROR,
                    "R001",
                    "Multiple //@version directives.",
                    1,
                    1,
                    file_path,
                )
            )
        else:
            v_str = matches[0].group(1)
            v_num = int(v_str)
            if v_num not in [4, 5, 6]:
                line_num = source[: matches[0].start()].count("\n") + 1
                diagnostics.append(
                    Diagnostic(
                        Severity.ERROR,
                        "R003",
                        f"Unsupported Pine Script version: {v_num}. Expected 4, 5, or 6.",
                        line_num,
                        1,
                        file_path,
                    )
                )

        return diagnostics


class SecurityRule(Rule):
    """
    SEC01: Scan for malicious Python keywords or patterns.
    """
    def check(self, source: str, ast_root: Optional[ASTNode], file_path: str) -> List[Diagnostic]:
        diagnostics = []
        suspicious = ['import os', 'import sys', 'exec(', 'eval(', '__import__']
        lines = source.split('\n')
        for i, line in enumerate(lines):
            for s in suspicious:
                if s in line:
                    diagnostics.append(Diagnostic(
                        Severity.WARNING, "SEC01", 
                        f"Suspicious pattern found: '{s}'. Verify this is intended Pine Script.", 
                        i + 1, 1, file_path))
        return diagnostics

class SemanticCheckRule(Rule):
    """
    Runs the Semantic Analyzer.
    """

    def check(
        self, source: str, ast_root: Optional[ASTNode], file_path: str
    ) -> List[Diagnostic]:
        if not ast_root:
            return []  # Can't check

        analyzer = SemanticAnalyzer()
        # Run visitor
        # AST is a list of statements from Parser.parse() which returns List[Statement], not single ASTNode.
        # Wait, Parser.parse() returns List[Statement].
        # SemanticAnalyzer.visit_block expects Block.
        # I should wrap statements in a pseudo-Block?

        # Helper to run on list
        diagnostics = []

        try:
            # We treat the list of statements as a top-level block body
            # But we don't have a Block node.
            # SemanticAnalyzer has `visit_script_decl`, etc.
            # I'll iterate.
            if isinstance(ast_root, list):
                for stmt in ast_root:
                    stmt.accept(analyzer)
            elif isinstance(ast_root, ASTNode):
                ast_root.accept(analyzer)

        except Exception as e:
            # Should catch internal errors
            import traceback

            traceback.print_exc()
            diagnostics.append(
                Diagnostic(
                    Severity.ERROR,
                    "E999",
                    f"Internal Analyzer Error: {str(e)}",
                    1,
                    1,
                    file_path,
                )
            )

        # Collect errors from analyzer
        for err in analyzer.errors:
            # Mapping SemanticError to Diagnostic
            # Code? We need to categorize.
            code = "R200"  # General semantic
            if "Undefined" in str(err):
                code = "R201"
            elif "Type mismatch" in str(err):
                code = "R202"

            diagnostics.append(
                Diagnostic(
                    Severity.ERROR, code, str(err), err.line, err.column, file_path
                )
            )
            
        # Collect warnings
        for w in analyzer.warnings:
            diagnostics.append(Diagnostic(Severity.WARNING, "W001", str(w), w.line, w.column, file_path))
            
        # Unused Variables
        for scope in analyzer.all_scopes:
            for name, sym in scope.symbols.items():
                if sym.is_mutable and sym.declared_at is not None and sym.usage_count == 0:
                    if name.startswith('_'): continue
                    
                    line = sym.declared_at.line
                    diagnostics.append(Diagnostic(
                        Severity.WARNING, "W002",
                        f"Variable '{name}' is declared but never used.",
                        line, 1, file_path,
                        suggestion=f"Remove '{name}' or prefix with '_'."
                    ))

        return diagnostics


class RuleRunner:
    def __init__(self):
        self.rules: List[Rule] = [
            VersionCheckRule(),
            SecurityRule(),
            SemanticCheckRule(),
        ]

    def run(
        self, source: str, ast_root: Optional[ASTNode], file_path: str
    ) -> List[Diagnostic]:
        results = []
        for rule in self.rules:
            results.extend(rule.check(source, ast_root, file_path))
        return results
