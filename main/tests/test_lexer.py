"""Testcases for LPLR lexer."""
import unittest
from main.lexer.lexer import lex
from main.lplr_tokens.lplr_token import Token


class TestLexer(unittest.TestCase):
    """Lexer tests."""

    test_cases = {
        "get": Token("GET_KEYWORD", "get"),
        "from": Token("FROM_KEYWORD", "from"),
        "send": Token("SEND_KEYWORD", "send"),
        "output": Token("OUTPUT_KEYWORD", "output"),
        "zip": Token("ZIP_KEYWORD", "zip"),
        "[": Token("LBRACKET", "["),
        "]": Token("RBRACKET", "]"),
        "error": Token("IDENT", "error"),
        "/var/log/messages": Token("PATH", "/var/log/messages"),
    }

    def test_single_token(self):
        """Test single token generation."""
        for case, expected in self.test_cases.items():
            print(f"Checking {case}: ", end="")
            for token in lex(case):
                print(f" result {token} : ", end="")
                self.assertEqual(token, expected)
                print("PASS")


if __name__ == "__main__":
    unittest.main()
