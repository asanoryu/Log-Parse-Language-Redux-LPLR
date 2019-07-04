"""Parser for LPLR."""
from typing import Callable, Optional, List, Type
from main.lplr_tokens.lplr_token import Token
from main.ast.lplr_ast import QueryStatement, LPLRNode, SelectExpr


class LPLRParser:
    """Parser class for LPLR.
    
    “top down operator precedence” parser, sometimes called “Pratt parser”
    https://en.wikipedia.org/wiki/Pratt_parser
    """

    def __init__(self, input_: str, lex_generator: Callable):
        """Initialize with the provided Token generator."""
        self.lexer = lex_generator
        self.cur_token: Optional[Token] = None
        self.peek_token: Optional[Token] = None
        self.cur_pos: int = 0
        self.tokens: List[Token] = self.lexer(input_)
        # init current and peek tokens
        self.next_token()
        self.next_token()

    def next_token(self):
        """Advance current and peek_token positions."""
        self.cur_token = self.peek_token
        self.peek_token = self.tokens[self.cur_pos]
        self.cur_pos += 1

    def parse(self) -> QueryStatement:
        """Parse the provided input."""
        query_stmt = QueryStatement()
        print(self.tokens)
        while self.cur_pos + 1 <= len(self.tokens):
            stmt = self.parse_stmt()
            if stmt is not None:
                if isinstance(stmt, SelectExpr):
                    query_stmt.select_expression = stmt

            self.next_token()

        print(f"query in parse {query_stmt}")
        return query_stmt

    def parse_stmt(self) -> Optional[Type[LPLRNode]]:
        """Parse a single statement."""
        if self.cur_token.name == "GET_KEYWORD":
            return self.parse_get_stmt()
        else:
            return None

    def parse_get_stmt(self) -> Optional[SelectExpr]:
        """Parse a get statement."""
        ret = SelectExpr()
        ret.build(self.peek_token.literal)
        return ret
