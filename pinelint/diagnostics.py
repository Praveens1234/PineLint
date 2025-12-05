"""
Diagnostics and Reporting.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Any, Dict
import json


class Severity(Enum):
    ERROR = "error"
    WARNING = "warning"
    INFO = "info"
    HINT = "hint"


@dataclass
class Diagnostic:
    severity: Severity
    code: str
    message: str
    line: int
    column: int
    file_path: str = ""
    suggestion: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return {
            "severity": self.severity.value,
            "code": self.code,
            "message": self.message,
            "location": {
                "line": self.line,
                "column": self.column,
                "file": self.file_path,
            },
            "suggestion": self.suggestion,
        }

    def __str__(self):
        return f"{self.file_path}:{self.line}:{self.column}: {self.severity.value.upper()}[{self.code}]: {self.message}"


class Report:
    def __init__(self):
        self.diagnostics: List[Diagnostic] = []

    def add(self, diagnostic: Diagnostic):
        self.diagnostics.append(diagnostic)

    def has_errors(self) -> bool:
        return any(d.severity == Severity.ERROR for d in self.diagnostics)

    def to_json(self) -> str:
        return json.dumps(
            {
                "valid": not self.has_errors(),
                "error_count": sum(
                    1 for d in self.diagnostics if d.severity == Severity.ERROR
                ),
                "warning_count": sum(
                    1 for d in self.diagnostics if d.severity == Severity.WARNING
                ),
                "diagnostics": [d.to_dict() for d in self.diagnostics],
            },
            indent=2,
        )

    def to_text(self) -> str:
        lines = []
        for d in self.diagnostics:
            lines.append(str(d))

        summary = f"\nFound {sum(1 for d in self.diagnostics if d.severity == Severity.ERROR)} errors, {sum(1 for d in self.diagnostics if d.severity == Severity.WARNING)} warnings."
        lines.append(summary)
        return "\n".join(lines)
