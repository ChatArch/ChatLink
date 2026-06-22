# Changelog

## 2026-06-23

### Added

### Changed

- 发布 workflow 改为显式 `v*` tag / `workflow_dispatch` 触发，使用 PyPI Trusted Publishing（`id-token: write` + `environment: pypi`），不再依赖仓库级 PyPI token secret。
- 准备 `0.0.2` 测试发版，用于验证 `develop` 分支上打 `v0.0.2` tag 后的 PyPI Trusted Publishing 流程。

### Fixed
