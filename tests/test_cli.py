from click.testing import CliRunner

from chatlink import __version__
from chatlink.cli import main


def test_help_mentions_tree_and_no_scaffold_hello():
    result = CliRunner().invoke(main, ["--help"])

    assert result.exit_code == 0
    assert "--tree" in result.output
    assert "hello" not in result.output.lower()


def test_version_option_reports_package_version():
    result = CliRunner().invoke(main, ["--version"])

    assert result.exit_code == 0
    assert f"chatlink, version {__version__}" in result.output


def test_tree_reports_registered_root_only_surface():
    result = CliRunner().invoke(main, ["--tree"])

    assert result.exit_code == 0
    assert result.output == (
        "chatlink  # ChatArch link utilities entrypoint\n"
        "├── --help  # show command help\n"
        "├── --version  # show the installed package version\n"
        "└── --tree  # show this CLI tree\n"
    )
    assert "hello" not in result.output.lower()
