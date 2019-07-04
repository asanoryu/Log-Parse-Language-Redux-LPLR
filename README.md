
# Log-Parse-Language-Redux-LPLR

> Simple toy DSL for filtering and parsing files

Basic expression

    get <keyworddef> from <filenamedef>

Examples

    get error from /var/log/apache/error.log
    get error,warning from /var/log/messages output /tmp/parsed_messages

Installation

    pip install -r requirements.txt

Commands

    python lplr.py repl - start the REPL
    python lplr.py test - run tests


Grammar

    <query_statement>    ::=
        GET <select_expression> <from_statement> [<output_statement>]

    <select_expression>    ::=
        <value> [ { <comma> <value> }... ]

    <from_statement>    ::=   FROM <file_reference> [ { <comma> <file_reference>.. ]

    <output_statement> ::= <file_reference> [ZIP] [<send_statement>]

    <send_statement> ::= SEND <email>

    <file_reference> ::= [<path_reference>] <filename>

    <path_reference> ::= (<slash><value>)*

    <filename> ::= <value>[<dot><value>]

    <email> ::= <value><at><value><dot><value>

    <slash> ::= /

    <dot> ::= .

    <comma> ::= ,

    <at> ::= @

    <value> ::=  <letter> { <letter> | <digit> }

    <letter> ::= 	["a"-"z","A"-"Z"] | ["\u0153"-"\ufffd"]

    <digit> ::= ["0"-"9"]
