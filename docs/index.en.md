# ChatLink Documentation

ChatLink is the ChatArch link utilities package entrypoint. These docs record the implemented CLI and future extension boundary.

<div class="grid cards" markdown>

-   :material-console-line: **CLI Tree**

    ---

    Run `chatlink --tree` for the full registered tree or `chatlink --tree-brief` for the compact view, then review the root-only boundary and update rule.

    [View CLI Tree](cli-tree.md)

-   :material-link-variant: **Link Utility Boundary**

    ---

    The package currently stays as an installable, testable, releasable link utilities shell; real link subcommands are not exposed yet.

</div>

## Local Preview

```bash
pip install -e ".[docs]"
mkdocs serve
```
