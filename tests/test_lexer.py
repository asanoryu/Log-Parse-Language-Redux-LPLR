import unittest
from .lplr.lexer.lexer import lex
from .lplr.lplr_tokens.lplr_token import Token


class TestLexer(unittest.TestCase):
    test_cases = {
        "get": Token("GET_KEYWORD", "GET"),
        "from": Token("FROM_KEYWORD", "from"),
        "send": Token("SEND_KEYWORD", "send"),
        "output": Token("OUTPUT_KEYWORD", "output"),
        "zip": Token("ZIP_KEYWORD", "zip"),
        "[": Token("LBRACKET", "["),
        "]": Token("RBRACKET", "]"),
        "/var/log/messages": Token("CLAUSE_PARAMETER", "/var/log/messages"),
    }

    def TestSingleToken(self):
        for case, expected in self.test_cases.items():
            print(f"Checking {case}")
            got = lex(case)
            print(f"Result {got}")
