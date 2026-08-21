# CLI Tree

ChatLink uses the shared `chatstyle.add_tree_option()` integration to generate command trees from the real registered Click command surface:

- `chatlink --tree` includes parameter signatures for interface review.
- `chatlink --tree-brief` preserves the same nodes and descriptions without parameter signatures.

The CLI is currently root-only and has no business-command parameters, so the full and brief views are identical. This page must not invent future commands.

## Full Command Tree

```text
chatlink
├── --help  # Show this message and exit.
├── --version  # Show the version and exit.
├── --tree  # Print the registered CLI tree and exit.
└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.
```

## Brief Command Tree

```text
chatlink
├── --help  # Show this message and exit.
├── --version  # Show the version and exit.
├── --tree  # Print the registered CLI tree and exit.
└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.
```

## Current Status

| Entry | Status | Notes |
| --- | --- | --- |
| `chatlink --help` | Implemented | Shows root command help. |
| `chatlink --version` | Implemented | Shows the installed package version. |
| `chatlink --tree` | Implemented | Shows the registered tree with parameter signatures. |
| `chatlink --tree-brief` | Implemented | Shows the same registered tree without parameter signatures. |
| `chatlink hello` | Removed | Template scaffold command; not kept as public compatibility surface. |
| Link utility subcommands | Not implemented | Add them only after real link utility capability exists. |

## Update Rule

When real commands are added, update the Click registration and tests first, then run `chatlink --tree` and `chatlink --tree-brief` to refresh README and this page.
