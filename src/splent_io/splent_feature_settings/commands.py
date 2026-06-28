"""
CLI commands contributed by splent_feature_settings.

These commands are auto-discovered by the framework and exposed in the
SPLENT CLI under the ``feature:settings`` group.

Usage::

    splent feature:settings hello
"""

import click


@click.command("hello")
def hello():
    """Example command — replace with your own."""
    click.echo("  Hello from splent_feature_settings!")


cli_commands = [hello]
