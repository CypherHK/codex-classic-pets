# Codex Classic Pets

中文（默认） · [English](README.en.md)

把《摩尔庄园》的拉姆和《赛尔号》的超能 NONO 带到 Codex 桌面。

这里有三款完整动画宠物：会眨眼、打招呼、跳跃，也有工作中、等待输入和查看结果的表情。下载后可以直接安装，不需要运行图片生成工具。

## 先看看它们

| 经典普通拉姆 | 经典超级拉姆 · 柔化版 | 超能 NONO |
| --- | --- | --- |
| ![橙色经典普通拉姆的完整状态动画](previews/lahm-classic-orange/all-states.gif) | ![经典超级拉姆柔化版的完整状态动画](previews/super-lahm-classic/all-states.gif) | ![超能 NONO 的完整状态动画](previews/super-nono/all-states.gif) |
| 橙色圆团子、两片软软的绿叶。 | 黄色身体、三片柔曲金叶，保留经典超拉的样子。 | 蓝白色悬浮机器人、浅蓝电子表情。 |

GIF 展示完整状态序列。每只还有单状态预览、[跳跃衔接和十六方向预览](previews/README.md)，以及 MP4。

## 安装

下载仓库 ZIP 并解压，或 clone 仓库，然后在仓库目录运行：

```sh
python3 scripts/install.py all
```

只想安装其中一只：

```sh
python3 scripts/install.py lahm-classic-orange
```

安装工具只使用 Python 标准库，会检查文件哈希，默认**不覆盖已有宠物**。它不会改动 Codex 配置、切换当前宠物或联网下载其他内容。

不想运行脚本也可以：把 `pets/` 中所选宠物的整个目录复制到 `~/.codex/pets/`。自定义数据目录、Windows 和已有同名宠物的处理方式见 [安装说明](docs/installation.md)。

安装后，在 Codex 的宠物选择入口中选择相应名称。若新条目未出现，可以重启应用刷新。具体入口和动画触发方式取决于客户端版本。

## 现在验证到了哪里？

三款发行精灵图均通过文件结构与资源质量检查；每款包含九组标准动画和十六个观察方向。安装工具在隔离目录测试，不会拿你正在使用的宠物做覆盖实验。

**尚未完成 Codex 应用内的菜单识别、激活及全部状态触发实测**，目前不承诺某个客户端版本已完全兼容。检查范围、保留的评审警告和 NONO 的打包修正见 [验收说明](docs/validation.md)。

## 仓库里有什么？

- `pets/`：安装所需的 `pet.json` 和透明 `spritesheet.webp`。
- `previews/`：从本次发行精灵图生成的 GIF、MP4、联系表和关键帧。
- `source-art/`：两款拉姆的高清基准图，不是安装依赖。
- `qa/`：去除个人路径后的检查记录；`checksums.json` 记录运行文件哈希。

## 关于角色和许可

这是非官方的角色重绘与动画资源包，不代表原游戏或 OpenAI。角色来自《摩尔庄园》和《赛尔号》，AI 辅助重绘并不意味着我们拥有原角色的权利。

代码许可证和角色素材的公开再分发依据仍待确认；目前不要把整个包当作 MIT、CC0 或可自由商用的素材。详见 [角色来源](CREDITS.md) 和 [素材权利说明](ASSET_RIGHTS.md)。

当前仓库已准备本地安装资源，尚未公开发布。[发布准备状态](docs/release-checklist.md)
