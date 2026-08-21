"""CLI entrypoint for chatlink."""

from __future__ import annotations

import click
from chatstyle import add_tree_option

from chatlink import __version__


@click.group(name="chatlink", invoke_without_command=True)
@click.version_option(__version__, prog_name="chatlink")
@add_tree_option(renderer_options={"root_name": "chatlink"})
@click.pass_context
def main(ctx: click.Context) -> None:
    """ChatArch link utilities entrypoint."""
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())


if __name__ == "__main__":
    main()
