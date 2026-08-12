<div align="center">
    <a href="https://pypi.python.org/pypi/ChatLink">
        <img src="https://img.shields.io/pypi/v/ChatLink.svg" alt="PyPI version" />
    </a>
    <a href="https://github.com/ChatArch/ChatLink/actions/workflows/ci.yml">
        <img src="https://github.com/ChatArch/ChatLink/actions/workflows/ci.yml/badge.svg" alt="Tests" />
    </a>
    <a href="https://arch.gh.wzhecnu.cn/ChatLink/">
        <img src="https://img.shields.io/badge/docs-mkdocs-blue.svg" alt="Documentation" />
    </a>
</div>

<div align="center">

[English](README.en.md) | [简体中文](README.md)
</div>

# ChatLink

ChatLink is the ChatArch link utilities package entrypoint. The package currently keeps a minimal root-only CLI: the public scaffold `hello` command has been removed, and real link subcommands are not exposed yet.

## Quick Start

```bash
pip install ChatLink
chatlink --help
chatlink --version
chatlink --tree
```

## Current CLI Tree

```text
chatlink  # ChatArch link utilities entrypoint
├── --help  # show command help
├── --version  # show the installed package version
└── --tree  # show this CLI tree
```

## CLI Boundary

- The current CLI only exposes root options and has no business subcommands.
- The template leftover `hello` command has been removed; scaffold/demo commands should not be kept as public compatibility surface.
- `--tree` is generated from the real Click command registration and is used to align README, docs, and tests.
- When real link utility commands are added later, update the Click registration first and then sync docs from the real `chatlink --tree` output.

## Layout

- `src/`: package source code
- `tests/code-tests/`: code tests and migrated historical tests
- `tests/cli-tests/`: real CLI tests, doc-first
- `tests/mock-cli-tests/`: mock/fake CLI tests, doc-first
- `docs/`: long-lived project docs built by MkDocs

## Development Notes

See `DEVELOP.md` and `AGENTS.md` before expanding the scaffold.
