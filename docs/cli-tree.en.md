# CLI Tree

`ChatLink` is currently a root-only CLI. This page must stay synchronized from the real `chatlink --tree` output and must not invent future commands.

```text
chatlink  # ChatArch link utilities entrypoint
├── --help  # show command help
├── --version  # show the installed package version
└── --tree  # show this CLI tree
```

## Current Status

| Entry | Status | Notes |
| --- | --- | --- |
| `chatlink --help` | Implemented | Shows root command help. |
| `chatlink --version` | Implemented | Shows the installed package version. |
| `chatlink --tree` | Implemented | Shows the current real CLI tree. |
| `chatlink hello` | Removed | Template scaffold command; not kept as public compatibility surface. |
| Link utility subcommands | Not implemented | Add them only after real link utility capability exists. |

## Update Rule

When real commands are added, update the Click registration and tests first, then run `chatlink --tree` to refresh README and this page.
