"""Parser for LPLR."""
from typing import Callable
from main.lplr_tokens.lplr_token import Token
from main.ast.lplr_ast import QueryStatement


class LPLRParser:
    """Parser class for LPLR."""

    def __init__(self, lex_generator: Callable):
        """Initialize with the provided Token generator."""
        self.lexer = lex_generator

    def parse(self, input_: str):
        """Parse the provided input."""
        query_stmt = QueryStatement()

        for tok in self.lexer(input_):
            print(tok)
        return query_stmt
