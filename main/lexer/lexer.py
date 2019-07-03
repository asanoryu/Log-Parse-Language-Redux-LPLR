"""Lexer for the LPLR.

has a single callable generator returning a stream of tokens. 
"""
from main.lplr_tokens.lplr_token import _tok_defs
from main.utils.lplr_errors import LexingError


def lex(characters):
    """Check for each token definition pattern in the provided string."""
    pos = 0
    while pos < len(characters):
        match = None
        for token_name, pattern in _tok_defs:
            try:
                match = pattern.match(characters, pos)
            except Exception as e:
                raise MatchingError(str(e))
            if match:
                text = match.group(0)
                if token_name and token_name != "WHITESPACE" and IGNORE_WHITESPACE:
                    yield Token(token_name, text)
                break
        if not match:
            raise LexingError(
                f"Illegal character at possition :{pos} = {characters[pos]}"
            )
        else:
            pos = match.end(0)
