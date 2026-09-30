# 安装与卸载

[English overview](../README.en.md#install)

需要一款能读取本地自定义宠物目录的 Codex 桌面客户端。资源文件与文件复制流程已通过检查；作者于 2026-10-01 反馈在自己的 Codex 客户端实测正常。具体客户端版本未记录，不代表所有版本与系统都已验证。

## 用脚本安装

在仓库根目录运行；脚本需要 Python 3.9 或更高版本，无需额外依赖：

```sh
python3 scripts/install.py all
python3 scripts/install.py super-lahm-classic super-nono
```

Windows 可以使用：

```powershell
py -3 scripts/install.py all
```

默认安装到 `$CODEX_HOME/pets`；未设置 `CODEX_HOME` 时使用用户主目录下的 `.codex/pets`。指定另一位置时，`--target` 指的是 **pets 目录本身**：

```sh
python3 scripts/install.py all --target /path/to/codex-data/pets
```

脚本先检查所选 manifest、哈希及目录冲突，再复制。任何所选同名目录已存在（包括符号链接）时，整批安装会拒绝继续，不替你覆盖或删除旧版本。请先自行备份并移走要替换的目录，再重试。

脚本不会修改配置、重启应用、切换活动宠物或连接网络。它验证的是已验收资源的完整性，不是应用运行行为。磁盘或权限错误可能留下本次新建的不完整目录，修正问题并检查该目录后再重试。

## 手动安装

把所选目录整个复制过去。例如：

```text
.codex/pets/
└── lahm-classic-orange/
    ├── pet.json
    └── spritesheet.webp
```

不要只复制精灵图，也不要更改目录 ID 或 manifest 的相对路径。下载或 clone 仓库本身不会自动安装。

## 在应用里使用

打开客户端的宠物选择入口，选择“经典普通拉姆”“经典超级拉姆”或“超能 NONO”。如果没有出现，可以重启应用刷新。遇到识别问题时，请记录客户端版本、系统和所选宠物，便于复现。

## 卸载

先取消选择要卸载的宠物，再将对应的整个目录移到回收站。只处理自己选中的宠物 ID，不删除整个 `pets` 目录或其他宠物。
