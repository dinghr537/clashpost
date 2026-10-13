# 部落驿站 · 升级数据查询

本项目作为「部落驿站」的继承项目，基于 [lemonicy/clashpost](https://github.com/lemonicy/clashpost) 继续整理《部落冲突》的升级等级、费用、时间与前置条件。

当前本地版聚焦升级数据：提供家乡、夜世界与部落都城目录、本地单位搜索和月卡减免展示。安装包下载服务已关闭；文章不再随网站构建，网站仅提供数据查询。

2026-10-13 已同步 357 个单位的数据页，包含 17 个新增单位。常驻单位、今年两批精工防御及新增和回归的临时单位采用 Clash of Clans Wiki 固定修订的当前表格与可取得的 2026 年历史记录；其余 31 个往期活动单位保留历史数据并标注。数值来源中的未知项、同等级条件分支和不同模式原样保留。

同步前的版本进度、2026 年 2 月至 10 月更新范围与本次完成情况见 [更新核对清单](UPDATE_AUDIT_2026-10-13.md)。

## 本地运行

需要 Node.js 22+：

```bash
npm ci
npm run docs:dev
```

打开 http://127.0.0.1:5174 。默认仅监听本机，固定使用 5174 端口；端口被占用时会报错。需要其他端口时可运行 `npm run docs:dev -- --port 5175`。

首页、搜索和升级图片均从本地加载。原站图片文件位于 `docs/public/images/original`，映射位于 `docs/.vitepress/theme/assets/original-image-manifest.json`，来源记录在 `docs/public/images/original-sources.json`。

已通过浏览器下载 2,515 个原站图片文件，保留村庄与单位目录，包含分类缩略图、单位图、各等级图及资源图标。原站页面使用的 WebP 图片直接保存，不重新生成，优先继续使用原图。新增单位、等级及缺失图片的补充图下载到 `docs/public/images/wiki`，来源及 Wiki 修订链接保存在 `docs/public/images/wiki-sources.json`。

当前仍有 3 个主图引用无法取得：都城攻城槌爆出的野蛮人、12 级龙宝宝和 14 级亡灵；原站页面的对应 WebP 也加载失败。这些原图缺项保留在清单中；同步后的图集仅展示已取得的图片，当前页面引用已全部解析为本地文件。具体路径见 `docs/public/images/missing-original-images.json`。未用于当前显示的可选高清 PNG 不属于此次图片导出范围。

补图仍由 AI 手动操作：在原站打开相关页面、展开折叠区域并加载图片后，通过浏览器导出，再用 `scripts/import_original_image_bundles.py` 导入工具生成的图片清单。检查本地文件和主图引用：

```bash
python3 scripts/check_local_images.py
```

以上操作不会创建后台任务或发布网站。

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

试点差异检查与回归检查需要 Python 3，使用标准库，无额外依赖：

```bash
python3 scripts/check_upgrade_data.py --unit 0301-Cannon --output /tmp/cannon-diff.json
python3 -B scripts/check_synced_data.py
python3 -B -m unittest discover -s tests
```

保留原数据资料的作者署名；被移除的文章可从原项目或 Git 历史中查阅。本项目与 Supercell 没有任何关联。
