"""Test LPLR AST."""
import unittest
from main.ast import lplr_ast


class TestAST(unittest.TestCase):
    """Main test case for AST."""

    def test_select_statement_init(self):
        """Test a select expr init."""
        sel = lplr_ast.SelectExpr(["error", "warning"])
        self.assertEqual(["error", "warning"], sel.values)

    def test_select_statement_build(self):
        """Test a select expr build from string."""
        sel = lplr_ast.SelectExpr()
        sel.build("error,warning")
        self.assertEqual(["error", "warning"], sel.values)
