"""
    lexer for the LPLR
    has a single callable generator returning a stream of tokens 
"""
from token.token import _tok_defs
from lplp.utils.lplr_errors import LexingError


def lex(characters):
    """checks for each token definition pattern in the provided string"""
    pos = 0
    while pos < len(characters):
        match = None
        for token_name, pattern in token_exprs:
            try:
                match = pattern.match(characters, pos)
            except Exception as e:
                raise LexingError(str(e))
            if match:
                text = match.group(0)
                if token_name and token_name != "WHITESPACE" and IGNORE_WHITESPACE:
                    yield Token(token_name, text)
                break
        if not match:
            raise LexingError(
                "Illegal character at possition :{} = {} ".format(pos, characters[pos])
            )
        else:
            pos = match.end(0)


if __name__ == "__main__":
    _file = "test.lpl"
    with open(_file) as f:
        try:
            for token in lex(f.read()):
                print(token.to_dict())
        except LexingError as lexErr:
            print("Lexing Error caugth: {}".format(lexErr))

