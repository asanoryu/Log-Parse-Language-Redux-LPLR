"""Abstract syntax tree definitions for LPLR."""
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List


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
class QueryStatement(LPLRStatement):
    """Main statement of LPLR.

    <query_statement>    ::=
        GET <select_expression> <from_statement> [<output_statement>]
    """

    select_expression: SelectExpr
    from_statement: FROMStatement
    output_statement: LPLRStatement


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
class FROMStatement(LPLRStatement):
    """Contains filestatements.
    
    <from_statement>    ::=   FROM <file_reference> [ { <comma> <file_reference>.. ]
    """

    file_reference: List[FileRefExpr] = field(default_factory=list)


@dataclass
class FileRefExpr(LPLRExpression):
    """Reference to a single file.
    
    <file_reference> ::= [<path_reference>] <filename>
    """

    file_path: str
