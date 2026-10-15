# 升级数据维护方案

本项目拟作为「部落驿站」的继承项目继续维护升级数据。原仓库包含 2026 年 2 月更新与少量 4 月内容，各单位、各字段的收录进度不同，不能视为统一月份的完整快照。同步范围与日期按实际完成情况记录；历史缺口见 [2026 年更新核对清单](UPDATE_AUDIT_2026-10-13.md)。

维护范围是升级等级、费用、时间和前置条件。当前阶段由用户手动告诉 AI 要更新什么、准备哪次发布以及何时发布。

数据同步沿用原站的简洁中文表头、必要换行和资源图标。来源网站的分组名称保存在源数据中，不能直接拼成长表头。更新数据时保持既有展示习惯，页面布局或样式的调整须有用户明确要求。

单位页的简介、机制说明、注意事项、关联单位链接和更新历史属于数据查询内容，不能因为移除攻略文章而一并删除。Markdown 正文由人工维护；同步脚本只更新数据 JSON 和同步元信息，不得用通用模板覆盖已有正文。数值变化涉及说明时，应逐条修改相关句子，保留其余说明。

原有表格的列顺序、表头换行和单元格链接也属于页面内容。`SourceUnitTable` 可按页面明确列出的来源字段读取新数值，同时保留原表结构；来源字段缺失或匹配到多张表时会报错，须核对后再更新字段对应关系。

大部分页面继续使用原来的 `UnitTable`。`scripts/authored-table-mappings.json` 为每张表明确记录来源表编号、完整表头与列对应关系；`update_authored_data.py` 只回填单元格，不生成或替换正文。来源表结构变化时停止更新，先人工核对映射。不同模式、召唤物、获取方式和历史迁移表分别保留，不能拿主单位的表覆盖。来源没有提供的原字段沿用原记录，新增等级的缺失字段显示「未知」。

## 手动指示维护

无需定时监控、后台任务或自动发布。用户可以这样发出指示：

- 「按 Wiki 更新家乡英雄的升级数据。」AI 获取对应来源、比较差异、修改数据，并报告更新范围与未解决的缺项。
- 「准备发布这一版。」AI 检查数据和页面、运行构建、整理变更摘要与发布所需文件，并指出会影响本次发布的问题。
- 「发布这一版。」这是本次发布的授权。AI 按项目部署方式发布已准备的版本，验证上线结果；若部署方式或凭据尚未配置，先说明具体缺项。

更新数据与准备发布本身不包含发布动作。已有明确发布授权时继续执行，不重复请求确认。

## 来源与准确性目标

| 来源 | 用途 | 当前状态 |
| --- | --- | --- |
| [Supercell 官网](https://supercell.com/en/games/clashofclans/blog/) | 查看更新范围，采用官方公开数值 | 已读取公开公告；部分公告有费用和时间表 |
| [Clash of Clans Wiki](https://clashofclans.fandom.com/wiki/Clash_of_Clans_Wiki) | 获取各等级的完整表格和更新历史 | 公开 MediaWiki API 已完成本次 357 页的固定修订同步 |
| [Clash Ninja](https://www.clash.ninja/upgrade-tracker/overview) | 获取或补充升级数据、参考更新范围 | 已采用四月公告中的法师塔升级时间变更补充历史 |
| 其他数据网站 | 用户指定来源、填补缺项 | 使用时记录对应页面与同步范围 |

目标是正确同步选定数据网站的内容，不承诺独立验证游戏中的每一个数值，也不要求每次多站交叉验证或进入游戏核实。来源网站的原始错误可以继承；本站应避免采集、转换、漏行、错列或折扣计算造成的新错误。

每批数据至少记录来源 URL、同步日期与覆盖范围；可取得版本或 Wiki 修订号时一并保留。同步日期表示本站采用来源的时间，不表示数值在游戏中生效的日期。未知游戏版本不猜测。

先确认正在取的表格属于目标服务器、村庄和模式，使用基础费用与时间，页面另算月卡。若用户指定了来源，优先按该来源同步；没有指定时，完整等级表默认取 Wiki，其他站补缺。站点之间数值不一致时记录采用哪一方，不进行无止境的追溯。缺失值或条件歧义不凭空补齐。

## AI 在准备发布时检查

每次准备发布均执行以下检查，检查程序由 AI 当次运行：

1. 检查本次更新范围与来源表一致，未误取其他村庄、模式、活动或月卡数值。
2. 检查等级与条件组合不重复；新增等级没有漏行，费用、时间、资源种类及预期前置列没有漏掉。
3. 区分已知数值、不适用和未知；对缺项、条件变体及来源差异，在发布摘要中说明。
4. 检查受影响的页面与月卡展示，运行 `npm run docs:build`；发生提取、转换、缺列、页面或构建错误时先修复。
5. 运行中文展示检查，补译新增名称、表头、属性、能力说明、图片说明和更新历史；目录与搜索结果采用中文名称。优先使用官方中文名，保留英文别名用于搜索，不能把来源英文直接作为默认页面内容。
6. 整理更新范围、采用来源、同步日期、仍沿用历史数据的范围和部署所需产物。

已如实标注的来源未知项不要求全部解决后才能发布。检查目标是避免本站引入错误，并让用户知道本次同步覆盖了哪里。

首次以「只提供升级数据」的定位上线前，还应关闭实际安装包下载行为，移除首页和导航中的下载、攻略服务入口，以及相关维护承诺；同步公告和 README。文章不随网站构建，只保留数据查询。本地版已完成这些入口与承诺的调整；首次正式发布时仍需核对部署产物与线上结果。

## 手动同步工具

本次已迁移 357 个数据页到独立 JSON 文件，新增 17 个单位；原 34 组最高等级缺口已补齐。其余 31 个往期活动单位保留旧数据并在页面标注。所有工具只在手动执行时运行，没有后台任务或自动发布。

```bash
python3 -B scripts/fetch_wiki_snapshots.py --cache /tmp/clashpost-next-sync
python3 -B scripts/sync_wiki_data.py --cache /tmp/clashpost-next-sync --date YYYY-MM-DD
python3 -B scripts/download_wiki_images.py --preview /tmp/clashpost-next-sync/records-preview.json
python3 -B scripts/sync_wiki_data.py --cache /tmp/clashpost-next-sync --date YYYY-MM-DD --apply
python3 -B scripts/update_authored_data.py --output /tmp/clashpost-next-sync/authored-preview.json
# 核对预览与字段映射后，回填原表：
python3 -B scripts/update_authored_data.py --apply --output /tmp/clashpost-next-sync/authored-applied.json
python3 -B scripts/check_synced_data.py --cache /tmp/clashpost-next-sync
python3 -B scripts/check_local_images.py
python3 -B -m unittest discover -s tests
node --disable-warning=MODULE_TYPELESS_PACKAGE_JSON --test tests/test_chinese_ui.mjs
node --disable-warning=MODULE_TYPELESS_PACKAGE_JSON scripts/check_chinese_ui.mjs
npm run docs:build
```

每批使用新的缓存目录，避免复用上一次修订。先查看预览报告与来源，再导入；新增内容还需手动检查目录、活动可用时间和来源中的单位模式。Wiki 缓存包含完整 HTML，仅放在临时目录；仓库保存数据表、修订号、图片及来源记录。

新单位须先参照同类页面建立中文正文、原站组件和字段映射。同步脚本拒绝为不存在的页面自动套用通用模板，来源记录仍会留在预览文件中。完成数值回填后，再按来源日期补充历史、核对受影响的说明和属性，更新页尾来源记录；同步表格不代表全部说明均已重新核对。

全站结构回归测试以 `9e77a85` 为更新前基线，检查原页面、属性、表头顺序、表格链接、模式分组、公式折叠区、高清图入口和历史日期。检查需要包含该提交的 Git 历史。页面仍须在浏览器中检查模式切换、月卡计算和图片显示。

图片检查分别报告普通图片和 `imgHd` 原图。普通图片缺失会阻止检查通过；高清文件缺项在 `missingHd` 中单独列出，不得把已有缩略图登记成高清原图。当前普通图片已齐，127 个高清原文件仍未能从原站保存到本地，原页面的高清地址声明继续保留。

补图必须先查看实际图片，再将对应单位、准确来源 URL 和中文说明登记到 `docs/.vitepress/theme/assets/reviewed-wiki-images.json`，随后导入。文件名含有单位名或数字不代表它是等级图；范围示意图、攻略截图、旧模型及其他单位的图片不能混入图集。图片说明采用已核对的中文含义，不根据文件名自动编造「外观」编号。原有已确认图片继续保留。

中文展示词典位于 `docs/.vitepress/theme/assets/i18n/zh-CN.json`。导入新修订后，给新增原文补齐中文译文或数据摘要；检查程序发现未翻译展示文本时会报错。原始文本与数值保存在单位 JSON 中，页面通过来源修订链接提供核对入口。

## 差异工具

`scripts/check_upgrade_data.py` 只比较家乡加农炮、蛮王和法师的主升级表，不覆盖页面：

```bash
python3 scripts/check_upgrade_data.py --unit 0301-Cannon --output /tmp/cannon-diff.json
python3 scripts/check_upgrade_data.py --unit 0200-Barbarian-King --output /tmp/king-diff.json
python3 scripts/check_upgrade_data.py --unit 0006-Wizard --output /tmp/wizard-diff.json
```

工具使用 Python 3 标准库。`--snapshot` 可复核已保存的 MediaWiki JSON 响应；报告日期是比较执行时间。网络失败会报错。

报告分别列出数值变化、适用性差异、未知值、新增等级、缺失等级、条件歧义和双向缺列。原 Markdown 预期前置列丢失时直接报错；迁移后的 JSON 比较对应来源表，并把同等级的不同前置条件分别比较。Wiki 的 `N/A` 记为不适用；本地空白、反斜杠等历史占位符记为未知，原始文本保留。蛮王一级的条件变体单独列出；新版数据按 Wiki 原行保留，不能仅按等级合并。

回归检查：

```bash
python3 -B -m unittest discover -s tests -p 'test_upgrade_data.py'
```

## 当前数据结构

已同步部分使用独立数据文件，以原页面单位 ID 为主键。数值通过显式映射回填原 Markdown 表格；战宠小屋使用保留原列定义的 `SourceUnitTable` 读取来源。页面说明、表格布局和样式由原组件保留。数据约定见 [UPGRADE_DATA_FORMAT.md](UPGRADE_DATA_FORMAT.md)：支持多资源费用、时间不适用、同等级的条件变体，以及字段状态。

本次已完成上述数据同步与本地页面更新。网站发布仍需用户单独指示。
