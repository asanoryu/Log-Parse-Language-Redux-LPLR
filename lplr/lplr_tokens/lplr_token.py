import re
from typing import Pattern
from dataclasses import dataclass


@dataclass
class TokenDef:
    name: str
    pattern: Pattern[str]


@dataclass()
class Token:
    """ holds a token """

    name: str
    literal: str

    def to_dict(self):
        """returns a dict representation of the Token"""
        return {"token_name": self.name, "token_value": self.value}


"""Lexeme/token definitions"""
_tok_defs = [
    TokenDef("GET_KEYWORD", re.compile("get")),
    TokenDef("FROM_KEYWORD", re.compile("from")),
    TokenDef("SEND_KEYWORD", re.compile("send")),
    TokenDef("OUTPUT_KEYWORD", re.compile("output")),
    TokenDef("ZIP_KEYWORD", re.compile("zip")),
    TokenDef("LBRACKET", re.compile("\[")),
    TokenDef("RBRACKET", re.compile("\]")),
    # TokenDef('LPARENTESES',re.compile('\(')),
    # TokenDef('RPARENTESES',re.compile('\)')),
    TokenDef("WHITESPACE", re.compile("[ \t]+")),
    TokenDef("NEWLINE", re.compile("[\n]")),
    TokenDef("CLAUSE_PARAMETER", re.compile("\([\w\\\/@.]+\)")),
]
