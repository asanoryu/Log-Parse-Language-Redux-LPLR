"""Test LPLR parser."""
import unittest
from main.parser import lplr_parser
from main.lexer import lexer
from main.ast.lplr_ast import QueryStatement


class TestParser(unittest.TestCase):
    """Parser test cases."""

    def test_parse_query_statement(self):
        """Parse a base query."""
        q = "get error,warning from /var/log/error.log"
        p = lplr_parser.LPLRParser(lex_generator=lexer.lex)
        query = p.parse(q)

        self.assertIsNotNone(query)
        self.assertIsInstance(query, QueryStatement)

        self.assertIsNotNone(query.select_expression)
        self.assertEqual(query.select_expression.values, ["error", "warning"])

        self.assertIsNotNone(query.from_expression)
        self.assertEqual(len(query.from_statement.file_reference), 1)
        self.assertEqual(query.from_statement.file_reference[0], "/var/log/error.log")
