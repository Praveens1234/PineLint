"""
Pine Script Lexer.
"""

import re
from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Optional, Generator, Tuple

from .pine_spec import PINE_KEYWORDS


class TokenType(Enum):
    # Structural
    EOF = auto()
    NEWLINE = auto()
    INDENT = auto()
    DEDENT = auto()

    # Identifiers & Keywords
    IDENTIFIER = auto()
    KEYWORD = auto()

    # Literals
    LITERAL_INTEGER = auto()
    LITERAL_FLOAT = auto()
    LITERAL_STRING = auto()
    LITERAL_COLOR = auto()

    # Operators & Delimiters
    OPERATOR = auto()
    LPAREN = auto()  # (
    RPAREN = auto()  # )
    LBRACKET = auto()  # [
    RBRACKET = auto()  # ]
    LBRACE = auto()  # {
    RBRACE = auto()  # }
    COMMA = auto()  # ,
    DOT = auto()  # .
    COLON = auto()       # :
    QUESTION = auto()    # ?

    # Comments (Internal use, usually filtered out)
    COMMENT = auto()
    WHITESPACE = auto()

    # Error
    ERROR = auto()


@dataclass
class Token:
    type: TokenType
    value: str
    line: int
    column: int
    position: int  # Absolute position in source


class LexerError(Exception):
    pass


class Lexer:
    """
    Stateful tokenizer for Pine Script.
    """

    def __init__(self, source_code: str):
        self.source = source_code
        self.tokens: List[Token] = []
        self.indent_stack: List[int] = [0]
        self.line_num = 1

        # Regex Patterns
        # Note: Order matters!
        self.rules = [
            # Comments: We handle them separately or as a high priority rule
            (r"//[^\n]*", TokenType.COMMENT),
            (r"/\*[\s\S]*?\*/", TokenType.COMMENT),
            # Strings
            (r"'([^'\\]|\\.)*'", TokenType.LITERAL_STRING),
            (r'"([^"\\]|\\.)*"', TokenType.LITERAL_STRING),
            # Colors (Hex)
            (r"#[0-9A-Fa-f]{6}([0-9A-Fa-f]{2})?", TokenType.LITERAL_COLOR),
            # Numbers
            (r"\d+\.\d+([eE][+-]?\d+)?", TokenType.LITERAL_FLOAT),
            (r"\.\d+([eE][+-]?\d+)?", TokenType.LITERAL_FLOAT),
            (r"\d+[eE][+-]?\d+", TokenType.LITERAL_FLOAT),
            (r"\d+", TokenType.LITERAL_INTEGER),
            
            # Operators (Multi-char first)
            (r"==|!=|<=|>=|:=|=>", TokenType.OPERATOR),
            (r"\+|-|\*|/|%", TokenType.OPERATOR), # Removed ? from here
            (r"!=", TokenType.OPERATOR),
            (r"<|>", TokenType.OPERATOR),
            (r"=", TokenType.OPERATOR),
            (r"\?", TokenType.QUESTION), # Explicit ?
            (r":", TokenType.COLON),     # Explicit :
            
            # Delimiters
            (r"\(", TokenType.LPAREN),
            (r"\)", TokenType.RPAREN),
            (r"\[", TokenType.LBRACKET),
            (r"\]", TokenType.RBRACKET),
            (r"\{", TokenType.LBRACE),
            (r"\}", TokenType.RBRACE),
            (r",", TokenType.COMMA),
            # Dot is tricky. It's a delimiter/access operator.
            (r"\.", TokenType.DOT),
            # Identifiers (and keywords)
            (r"[a-zA-Z_][a-zA-Z0-9_]*", TokenType.IDENTIFIER),
            # Newline (we handle indentation on newlines)
            (r"\n", TokenType.NEWLINE),
            # Whitespace (skip)
            (r"[ \t]+", TokenType.WHITESPACE),
        ]

    def tokenize(self) -> List[Token]:
        """
        Main entry point.
        """
        raw_tokens = self._generate_raw_tokens()
        processed_tokens = self._process_indentation_and_comments(raw_tokens)
        self.tokens = processed_tokens
        return self.tokens

    def _generate_raw_tokens(self) -> List[Token]:
        tokens = []
        pos = 0
        line = 1
        col = 1

        regex_parts = []
        for idx, (pattern, type_) in enumerate(self.rules):
            group_name = f"GROUP_{idx}"
            regex_parts.append(f"(?P<{group_name}>{pattern})")

        master_pattern = re.compile("|".join(regex_parts))

        while pos < len(self.source):
            match = master_pattern.match(self.source, pos)
            if not match:
                raise LexerError(
                    f"Unexpected character at line {line}, column {col}: {self.source[pos]}"
                )

            # Find which group matched
            kind = match.lastgroup
            value = match.group(kind)
            idx = int(kind.split("_")[1])
            token_type = self.rules[idx][1]

            # Calculate token position data
            token = Token(token_type, value, line, col, pos)
            tokens.append(token)

            newlines = value.count("\n")
            if newlines > 0:
                line += newlines
                last_newline_idx = value.rfind("\n")
                col = len(value) - last_newline_idx
            else:
                col += len(value)

            pos += len(value)

        return tokens

    def _process_indentation_and_comments(self, raw_tokens: List[Token]) -> List[Token]:
        final_tokens = []
        clean_tokens = []
        for t in raw_tokens:
            if t.type == TokenType.COMMENT:
                if "\n" in t.value:
                    clean_tokens.append(
                        Token(TokenType.NEWLINE, "\n", t.line, t.column, t.position)
                    )
                continue
            clean_tokens.append(t)

        current_line_tokens = []
        lines_of_tokens = []

        for t in clean_tokens:
            if t.type == TokenType.NEWLINE:
                lines_of_tokens.append(current_line_tokens)
                current_line_tokens = []
            else:
                current_line_tokens.append(t)

        if current_line_tokens:
            lines_of_tokens.append(current_line_tokens)

        final_output = []

        for line_tokens in lines_of_tokens:
            if not line_tokens:
                continue

            indent_level = 0
            content_start_idx = 0

            for i, t in enumerate(line_tokens):
                if t.type == TokenType.WHITESPACE:
                    # Treat tabs as 4 spaces
                    expanded = t.value.replace("\t", "    ")
                    indent_level += len(expanded)
                else:
                    content_start_idx = i
                    break
            else:
                continue

            current_indent = self.indent_stack[-1]

            if indent_level > current_indent:
                self.indent_stack.append(indent_level)
                first_tok = line_tokens[content_start_idx]
                final_output.append(
                    Token(TokenType.INDENT, "", first_tok.line, 1, first_tok.position)
                )

            elif indent_level < current_indent:
                while indent_level < self.indent_stack[-1]:
                    self.indent_stack.pop()
                    first_tok = line_tokens[content_start_idx]
                    final_output.append(
                        Token(
                            TokenType.DEDENT, "", first_tok.line, 1, first_tok.position
                        )
                    )

                if indent_level != self.indent_stack[-1]:
                    raise LexerError(
                        f"Indentation error at line {line_tokens[content_start_idx].line}"
                    )

            for t in line_tokens[content_start_idx:]:
                if t.type == TokenType.WHITESPACE:
                    continue

                if t.type == TokenType.IDENTIFIER:
                    if t.value in PINE_KEYWORDS or t.value in ["and", "or", "not"]:
                        t.type = TokenType.KEYWORD

                final_output.append(t)

            last_tok = line_tokens[-1]
            final_output.append(
                Token(
                    TokenType.NEWLINE,
                    "\n",
                    last_tok.line,
                    last_tok.column,
                    last_tok.position,
                )
            )

        pos = final_output[-1].position if final_output else 0
        line = final_output[-1].line if final_output else 1

        while len(self.indent_stack) > 1:
            self.indent_stack.pop()
            final_output.append(Token(TokenType.DEDENT, "", line, 1, pos))

        final_output.append(Token(TokenType.EOF, "", line, 1, pos))

        return final_output
