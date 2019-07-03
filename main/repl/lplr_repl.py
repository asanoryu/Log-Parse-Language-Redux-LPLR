"""REPL for LPLR."""
import sys
import pprint
from main.lexer import lexer
from main.utils import lplr_errors


def run():
    """Run REPL."""
    pp = pprint.PrettyPrinter(indent=4)
    while True:
        inp = input("LPLP >>")
        if inp == "quit":
            sys.exit()
        print(f"Executing {inp}")
        token_str = []
        try:
            for token in lexer.lex(inp):
                token_str.append(token)
        except lplr_errors.LexingError as e:
            print(f"Error {e}")

        print("lexer output:")
        pp.pprint(token_str)
