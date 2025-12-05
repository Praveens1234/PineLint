from typing import List, Optional
from .rules import Rule, SemanticAnalyzer, Diagnostic, Severity
from .ast_nodes import ASTNode

class ExtendedRule(Rule):
    def check(self, source: str, ast_root: Optional[ASTNode], file_path: str) -> List[Diagnostic]:
        diagnostics = []
        if not ast_root: return []
        
        analyzer = SemanticAnalyzer()
        try:
            if isinstance(ast_root, list):
                for stmt in ast_root:
                    stmt.accept(analyzer)
            else:
                ast_root.accept(analyzer)
        except Exception: pass
        
        # W002: Unused variable
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
        
        # W001: Shadowing
        for w in analyzer.warnings:
            if "Shadowing" in str(w):
                diagnostics.append(Diagnostic(
                    Severity.WARNING, "W001", str(w), w.line, w.column, file_path
                ))
                
        return diagnostics
