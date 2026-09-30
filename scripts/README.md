# 安装工具 / Installer

`install.py` 只依赖 Python 3.9+ 标准库。选择单只、多只或 `all`，默认复制到 `$CODEX_HOME/pets`（未设置时为 `~/.codex/pets`）。支持 `--target` 指定 pets 目录。

复制前检查所选资源、manifest、SHA-256 和目录冲突；拒绝覆盖已有目录或符号链接。没有覆盖开关、卸载命令、网络请求、配置修改或自动激活行为。

`python3 -m unittest discover -s tests -v` 运行隔离测试，不写入实际 Codex 数据目录。
