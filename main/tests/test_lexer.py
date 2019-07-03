"""Testcases for LPLR lexer."""
import unittest
from main.lexer.lexer import lex
from main.lplr_tokens.lplr_token import Token


class TestLexer(unittest.TestCase):
    """Lexer tests."""

    test_cases_single = {
        "get": Token("GET_KEYWORD", "get"),
        "from": Token("FROM_KEYWORD", "from"),
        "send": Token("SEND_KEYWORD", "send"),
        "output": Token("OUTPUT_KEYWORD", "output"),
        "zip": Token("ZIP_KEYWORD", "zip"),
        "[": Token("LBRACKET", "["),
        "]": Token("RBRACKET", "]"),
        "error": Token("IDENT", "error"),
        "/": Token("SLASH", "/"),
        "\\": Token("BSLASH", "\\"),
        ".": Token("DOT", "."),
        ",": Token("COMMA", ","),
    }

    test_cases_expr = {
        "get error from /var/log/messages": [
            Token("GET_KEYWORD", "get"),
            Token("IDENT", "error"),
            Token("FROM_KEYWORD", "from"),
            Token("SLASH", "/"),
            Token("IDENT", "var"),
            Token("SLASH", "/"),
            Token("IDENT", "log"),
            Token("SLASH", "/"),
            Token("IDENT", "messages"),
        ],
        "get error,warning from error.log": [
            Token("GET_KEYWORD", "get"),
            Token("IDENT", "error"),
            Token("COMMA", ","),
            Token("IDENT", "warning"),
            Token("FROM_KEYWORD", "from"),
            Token("IDENT", "error"),
            Token("DOT", "."),
            Token("IDENT", "log"),
        ],
    }

    def test_single_token(self):
        """Test single token generation."""
        for case, expected in self.test_cases_single.items():
            for token in lex(case):
                self.assertEqual(token, expected)

    def test_expression_lexing(self):
        """Test lexing a full a expression."""
        for case, expected in self.test_cases_expr.items():
            got = []
            for token in lex(case):
                got.append(token)
            self.assertEqual(expected, got)


if __name__ == "__main__":
    unittest.main()
