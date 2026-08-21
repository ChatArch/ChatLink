# Changelog

## 2026-08-21 - 0.1.1

### Added

- Added `chatlink --tree-brief`, which renders the same registered command surface without parameter signatures.
- Added full/brief tree contract tests and installed console-script CI readbacks.

### Changed

- Replaced the package-local tree renderer with ChatStyle `add_tree_option()` and required `chatstyle>=0.2.0,<0.3.0`.
- Made the public `chatlink` root name explicit and synchronized bilingual CLI tree documentation with runtime output.
- Bounded Click and MkDocs Material to the supported compatibility ranges.

## 2026-08-12 - 0.1.0

### Added

- Added real root-only `chatlink --tree` generated from the Click command surface.
- Added top-level `chatlink --version`.
- Added bilingual MkDocs home and CLI tree pages.
- Added CLI and workflow/docs contract tests.

### Changed

- Removed scaffold `hello` command from the public CLI surface.
- Reduced runtime dependencies to `click>=8.0` because no ChatStyle/ChatEnv command surface remains.
- Aligned documentation URL to `https://arch.gh.wzhecnu.cn/ChatLink/`.
- Hardened CI, Preview Docs, Deploy Docs, and tag-only OIDC publish workflows.
