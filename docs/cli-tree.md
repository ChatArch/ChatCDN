# CLI 能力地图

这篇文档是 `ChatCDN` CLI 的简明能力地图，用来校对哪些命令已经是一等入口、哪些仍然只是边界或规划。文档中的命令树应与 `chatcdn --tree` 的运行结果保持一致；不要把未实现命令写成已可用操作。

可导入 Python 函数映射见 [接口树](interface-tree.md)。当前包能力边界见 [能力地图](capability-map.md)。

## 顶层命令

```text
chatcdn  # ChatCDN command-line interface.
├── --help  # Show this help message.
├── --version  # Show the installed package version.
└── --tree  # Print the registered command tree.
```

## 基础入口

```text
chatcdn --help           # 验证命令已安装，并查看帮助
chatcdn --version        # 验证当前安装版本
chatcdn --tree           # 从真实 Click 注册树输出命令树
```

当前 `ChatCDN` 还没有业务子命令。新增业务命令后，应像 ChatTea 的 CLI 树一样，把命令组单独展开，并给每个命令写一行注释。

## 业务命令槽位

这里是占位槽位，不是未来能力承诺。只有当命令、Python 函数和测试都存在时，才把它写成已实现入口。

## 状态约定

| 状态 | 含义 |
| --- | --- |
| 已实现 | 命令、函数和测试已经存在 |
| 已验证 | 已通过 CI、本地 smoke 或真实服务实践 |
| 规划 / checkpoint | 只保留边界说明；实现前不要写操作教程 |

## 实现合约

- 每个已实现命令都要能追到 Python 函数、类或 service 层。
- 如果命令会写远端状态，文档必须说明凭据、权限、dry-run/checkpoint 或确认边界。
- 新增命令时，同步更新 README、接口树、能力地图、测试和相关 Flow 页面。
