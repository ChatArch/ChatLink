# Changelog

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
