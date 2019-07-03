
# Log-Parse-Language-Redux-LPLR

> Simple toy DSL for filtering and parsing files

Basic expression

    get <keyworddef> from <filenamedef>

Installation

    pip install -r requirements.txt

Commands

    python lplr.py repl - start the REPL
    python lplr.py test - run tests


Grammar

    get_expession : GET_KEYWORD keyword_list FROM_KEYWORD filepath
    keyword_list :  VALUE (',' VALUE)*
    filepath : [dir]*filename
    dir : SLASH VALUE
    filename:VALUE DOT VALUE
