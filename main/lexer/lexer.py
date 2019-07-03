"""Lexer for the LPLR.

has a single callable generator returning a stream of tokens. 
"""
from main.lplr_tokens.lplr_token import _tok_defs, Token
from main.utils.lplr_errors import LexingError
from main.utils import config


def lex(characters):
    """Check for each token definition pattern in the provided string."""
    pos = 0
    while pos < len(characters):
        match = None
        for token_def in _tok_defs:
            try:
                match = token_def.pattern.match(characters, pos)
            except Exception as e:
                raise MatchingError(str(e))
            if match:
                text = match.group(0)

                if (
                    token_def.name
                    and token_def.name != "WHITESPACE"
                    and config.IGNORE_WHITESPACE
                ):
                    yield Token(token_def.name, text)
                break
        if not match:
            raise LexingError(
                f"Illegal character at position :{pos} = {characters[pos]}"
            )
        else:
            pos = match.end(0)
