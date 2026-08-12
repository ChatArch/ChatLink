# CLI 树

`ChatLink` 当前是 root-only CLI。这个页面必须从真实 `chatlink --tree` 输出同步，不能手写未来命令。

```text
chatlink  # ChatArch link utilities entrypoint
├── --help  # show command help
├── --version  # show the installed package version
└── --tree  # show this CLI tree
```

## 当前状态

| 入口 | 状态 | 说明 |
| --- | --- | --- |
| `chatlink --help` | 已实现 | 显示根命令帮助。 |
| `chatlink --version` | 已实现 | 显示已安装包版本。 |
| `chatlink --tree` | 已实现 | 显示当前真实 CLI 树。 |
| `chatlink hello` | 已移除 | 模板 scaffold 命令，不作为公开兼容面保留。 |
| Link utility 子命令 | 尚未实现 | 未来有真实 link utilities 能力后再加入 CLI。 |

## 更新规则

新增真实命令时，先更新 Click 注册面和测试，再运行 `chatlink --tree` 回填 README 与本页。
