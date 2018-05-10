'''
    lexer for the LPLR
    has a single callable generator returning a stream of token 
'''
from collections import namedtuple
import re
import sys

IGNORE_WHITESPACE = True

TokenDef = namedtuple('TokenDef' ,('name', 'pattern'))

class Token(namedtuple('Token',('name','value'))):
    '''Extending a named tuple repesenting a token/lexeme with its name and value'''
    def to_dict(self):
        '''returns a dict representation of the Token namedtuple'''
        return {'token_name' : self.name, 'token_value': self.value}

class LexingError(Exception):
    pass

'''Lexeme/token definitions'''
_tok_defs = [
    TokenDef('GET_KEYWORD',re.compile('get')),
    TokenDef('FROM_KEYWORD',re.compile('from')),
    TokenDef('SEND_KEYWORD',re.compile('send')),
    TokenDef('OUTPUT_KEYWORD',re.compile('output')),
    TokenDef('ZIP_KEYWORD',re.compile('zip')),
    TokenDef('LBRACKET',re.compile('\[')),
    TokenDef('LBRACKET',re.compile('\]')),
    # TokenDef('LPARENTESES',re.compile('\(')),
    # TokenDef('RPARENTESES',re.compile('\)')),
    TokenDef('WHITESPACE', re.compile('[ \t]+')),
    TokenDef('NEWLINE', re.compile('[\n]')),
    TokenDef('CLAUSE_PARAMETER',re.compile("\([\w\\\/@.]+\)"))
]

def lex(characters, token_exprs):
    '''checks for each token definition pattern in the provided string'''
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
                if token_name and token_name !='WHITESPACE' and IGNORE_WHITESPACE:
                    yield Token(token_name,text)
                break
        if not match:
           raise LexingError('Illegal character at possition :{} = {} '.format(pos, characters[pos]))
        else:
            pos = match.end(0)
    


if __name__ == '__main__':
    _file = 'test.lpl'
    with open(_file) as f:
        try:
            for token in lex( f.read(), _tok_defs):
                print(token.to_dict())
        except LexingError as lexErr:
            print('Lexing Error caugth: {}'.format(lexErr))