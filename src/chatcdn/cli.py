"""CLI entrypoint for chatcdn."""

from __future__ import annotations

import click
from chatstyle import add_tree_option

from chatcdn import __version__


@click.group(
    name="chatcdn",
    context_settings={"help_option_names": ["-h", "--help"]},
    invoke_without_command=True,
    no_args_is_help=True,
)
@click.version_option(__version__, prog_name="chatcdn")
@add_tree_option(renderer_options={"root_name": "chatcdn"})
def main() -> None:
    """ChatCDN command-line interface."""


if __name__ == "__main__":
    main()
