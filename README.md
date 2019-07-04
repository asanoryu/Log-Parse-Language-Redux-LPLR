
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

    <query_specification>    ::=
        GET <select_list> <from_expression> [<output_expression>]

    <select_list>    ::=
        <value> [ { <comma> <value> }... ]

    <from_expression>    ::=   FROM <file_reference> [ { <comma> <file_reference>.. ]

    <output_expression> ::= <file_reference> [ZIP] [<send_expression>]

    <send_expression> ::= SEND <email_expression>

    <file_reference> ::= [<path_reference>] <filename>

    <path_reference> ::= (<slash><value>)*

    <filename> ::= <value>[<dot><value>]

    <email_expression> ::= <value><at><value><dot><value>

    <slash> ::= /

    <dot> ::= .

    <comma> ::= ,

    <at> ::= @

    <value> ::=  <letter> { <letter> | <digit> }

    <letter> ::= 	["a"-"z","A"-"Z"] | ["\u0153"-"\ufffd"]

    <digit> ::= ["0"-"9"]
