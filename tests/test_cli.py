import click
from click.testing import CliRunner

from chatcdn import __version__
from chatcdn.cli import main


def test_version_option_reports_package_version():
    result = CliRunner().invoke(main, ["--version"])

    assert result.exit_code == 0
    assert f"chatcdn, version {__version__}" in result.output


def test_help_mentions_tree_option():
    result = CliRunner().invoke(main, ["--help"])

    assert result.exit_code == 0, result.output
    assert "--tree" in result.output
    assert "--tree-brief" in result.output
    assert "Print the registered CLI tree" in result.output


def test_tree_shows_registered_top_level_surface_with_purposes():
    result = CliRunner().invoke(main, ["--tree"])

    assert result.exit_code == 0, result.output
    assert result.output.splitlines() == [
        "chatcdn",
        "├── --help  # Show this message and exit.",
        "├── --version  # Show the version and exit.",
        "├── --tree  # Print the registered CLI tree and exit.",
        "└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.",
    ]


def test_tree_defaults_to_signatures_and_brief_omits_them():
    @click.command("probe")
    @click.argument("source")
    @click.option("--target")
    def probe(source: str, target: str | None) -> None:
        """Probe a parameterized command."""

    main.add_command(probe)
    try:
        detailed = CliRunner().invoke(main, ["--tree"])
        brief = CliRunner().invoke(main, ["--tree-brief"])
    finally:
        main.commands.pop("probe")

    assert detailed.exit_code == 0, detailed.output
    assert brief.exit_code == 0, brief.output
    assert "└── probe <SOURCE> [--target TARGET]  # Probe a parameterized command." in detailed.output
    assert "└── probe  # Probe a parameterized command." in brief.output
    assert "<SOURCE>" not in brief.output
    assert "[--target TARGET]" not in brief.output


def test_template_hello_command_is_not_registered():
    result = CliRunner().invoke(main, ["hello"])

    assert result.exit_code != 0
    assert "No such command" in result.output
