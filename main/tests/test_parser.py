"""Test LPLR parser."""
import unittest
from main.parser import lplr_parser
from main.lexer import lexer
from main.ast.lplr_ast import QueryStatement, SelectExpr
from main.lplr_tokens.lplr_token import Token


class TestParser(unittest.TestCase):
    """Parser test cases."""

    # def test_parse_query_statement(self):
    #     """Parse a base query."""
    #     q = "get error,warning from /var/log/error.log"
    #     p = lplr_parser.LPLRParser(input_=q, lex_generator=lexer.lex)
    #     query = p.parse()

    #     self.assertIsNotNone(query)
    #     self.assertIsInstance(query, QueryStatement)

    #     self.assertIsNotNone(query.select_expression)
    #     self.assertEqual(query.select_expression.values, ["error", "warning"])

    #     self.assertIsNotNone(query.from_expression)
    #     self.assertEqual(len(query.from_statement.file_reference), 1)
    #     self.assertEqual(query.from_statement.file_reference[0], "/var/log/error.log")

    def test_parse_get_stmt(self):
        """Parse a simple get statement."""
        q = "get error"
        p = lplr_parser.LPLRParser(input_=q, lex_generator=lexer.lex)
        query = p.parse()
        print(f"query in test {query}")

        self.assertIsNotNone(query)
        self.assertIsInstance(query, QueryStatement)

        self.assertIsNotNone(query.select_expression)
        self.assertEqual(query.select_expression.values, ["error"])

    def test_parse_select_expression(self):
        """Test parsing of a select expression."""
        q = "error,warning"
        p = lplr_parser.LPLRParser(input_=q, lex_generator=lexer.lex)
        res = p.parse_get_stmt()

        self.assertIsNotNone(res)
        self.assertIsInstance(res, SelectExpr)

        self.assertEqual(res.values, ["error", "warning"])

    def test_parse_get_stmt_multiple(self):
        """Parse a simple get statement."""
        q = "get error,warning"
        p = lplr_parser.LPLRParser(input_=q, lex_generator=lexer.lex)
        query = p.parse()
        print(f"query in test {query}")

        self.assertIsNotNone(query)
        self.assertIsInstance(query, QueryStatement)

        self.assertIsNotNone(query.select_expression)
        self.assertEqual(query.select_expression.values, ["error", "warning"])

    def test_init(self):
        """Test advancement of tokens."""
        q = "get error"
        p = lplr_parser.LPLRParser(input_=q, lex_generator=lexer.lex)
        self.assertEqual(p.cur_token, Token("GET_KEYWORD", "get"))
        self.assertEqual(p.peek_token, Token("VALUE", "error"))
        self.assertEqual(p.cur_pos, 2)
