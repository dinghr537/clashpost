# 部落驿站 · 升级数据查询

**在线访问：[cocpost.pages.dev](https://cocpost.pages.dev)**

本项目作为「部落驿站」的继承项目，基于 [lemonicy/clashpost](https://github.com/lemonicy/clashpost) 继续整理《部落冲突》的升级等级、费用、时间与前置条件。

当前本地版聚焦升级数据：提供家乡、夜世界与部落都城目录、本地单位搜索和月卡减免展示。安装包下载服务已关闭；文章不再随网站构建，网站仅提供数据查询。

2026-10-13 已同步 357 个单位的数据页，包含 17 个新增单位。常驻单位、今年两批精工防御及新增和回归的临时单位采用 Clash of Clans Wiki 固定修订的当前表格与可取得的 2026 年历史记录；其余 31 个往期活动单位保留历史数据并标注。数值来源中的未知项、同等级条件分支和不同模式原样保留。

同步前的版本进度、2026 年 2 月至 10 月更新范围与本次完成情况见 [更新核对清单](UPDATE_AUDIT_2026-10-13.md)。

页面、目录和搜索结果采用中文名称；同步的表头、能力参数和更新历史均有中文展示。英文名称支持搜索，来源原文保留在默认收起的核对区域。每次更新或准备发布时运行中文展示检查，补齐本次新增的翻译。

## 本地运行

需要 Node.js 22+。

```bash
npm ci
npm run docs:dev
```

访问 [http://127.0.0.1:5174](http://127.0.0.1:5174)。

## 构建与预览

```bash
npm run docs:build
npm run docs:preview
```

构建产物在 `docs/.vitepress/dist`。构建和本地预览不会发布网站。

## 更新与发布

当前由用户手动告诉 AI 要更新什么、准备哪次发布以及何时发布，不安排后台更新或自动发布。同步目标是正确采用指定数据网站的数值，并记录来源与同步日期。

- [维护方案](MAINTENANCE.md)
- [当前数据结构](UPGRADE_DATA_FORMAT.md)
- [来源、署名与许可](NOTICE.md)
- [来源权限核查与未决项](SOURCE_PERMISSIONS.md)

资料转载许可与自动访问权限分别核对。2026-10-16 的核查尚未确认本项目对 Fandom 批量自动获取的适用授权，因此暂不运行联网抓取和补图；已有本地快照的解析、页面维护与构建可以继续。图片不自动适用 Wiki 文本的 CC 许可。

试点差异检查与回归检查需要 Python 3，使用标准库，无额外依赖。将示例快照路径替换为已有、来源记录完整的本地 MediaWiki JSON 文件：

```bash
python3 scripts/check_upgrade_data.py --unit 0301-Cannon --snapshot /path/to/cannon-snapshot.json --output /tmp/cannon-diff.json
python3 -B scripts/check_synced_data.py
python3 -B -m unittest discover -s tests
node --disable-warning=MODULE_TYPELESS_PACKAGE_JSON --test tests/test_chinese_ui.mjs
node --disable-warning=MODULE_TYPELESS_PACKAGE_JSON scripts/check_chinese_ui.mjs
```

保留原数据资料的作者署名；被移除的文章可从原项目或 Git 历史中查阅。本项目与 Supercell 没有任何关联。
