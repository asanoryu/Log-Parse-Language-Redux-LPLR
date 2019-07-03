"""Main LPLR application.

Uses a click cli
"""
import click
import unittest

VERSION_NUMBER = {"LPLR": 0.1, "REPL": 0.1}


@click.group()
def cli():
    """Start cli for LPLR.
        
    has the following commands:
        test - runs all unittests from main/tests
        repl - starts the LPLR REPL
    """
    pass


@click.command()
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover("main/tests", pattern="test*.py")
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


@click.command()
def repl():
    """Start LPLR REPL."""
    click.echo(f"LPLR version {VERSION_NUMBER}")


cli.add_command(test)
cli.add_command(repl)


if __name__ == "__main__":
    cli()
