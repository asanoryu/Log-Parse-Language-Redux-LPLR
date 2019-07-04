"""Abstract syntax tree definitions for LPLR."""
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class LPLRNode:
    """Base class for all AST Nodes."""

    pass


@dataclass
class LPLRStatement(LPLRNode):
    """Base class for all LPLR statements."""

    pass


@dataclass
class LPLRExpression(LPLRNode):
    """Base class for all LPLR expressions."""

    pass


@dataclass
class SelectExpr(LPLRExpression):
    """Expression containing all queried keywords.

    <select_expression>    ::=
        <value> [ { <comma> <value> }... ]
    """

    values: List = field(default_factory=list)

    def build(self, params: str):
        """Split params and populate self.values."""
        for val in params.split(","):
            self.values.append(val)


@dataclass
class FileRefExpr(LPLRExpression):
    """Reference to a single file.
    
    <file_reference> ::= [<path_reference>] <filename>
    """

    file_path: str


@dataclass
class FROMStatement(LPLRStatement):
    """Contains filestatements.
    
    <from_statement>    ::=   FROM <file_reference> [ { <comma> <file_reference>.. ]
    """

    file_reference: List[FileRefExpr] = field(default_factory=list)


@dataclass
class Email(LPLRExpression):
    """Email representation."""

    email: str


@dataclass
class SendStatement(LPLRStatement):
    """State if output should be sent and where.
    
    <send_statement> ::= SEND <email>
    """

    email: Email


@dataclass
class OutputStatement(LPLRStatement):
    """Optional statement for outputing the response of the query.
    
    <output_statement> ::= <file_reference> [ZIP] [<send_statement>]

    """

    fileref: Optional[FileRefExpr] = None
    zip_: bool = False
    send_statement: Optional[SendStatement] = None


@dataclass
class QueryStatement(LPLRStatement):
    """Main statement of LPLR.

    <query_statement>    ::=
        GET <select_expression> <from_statement> [<output_statement>]
    """

    select_expression: Optional[SelectExpr] = None
    from_statement: Optional[FROMStatement] = None
    output_statement: Optional[OutputStatement] = None
