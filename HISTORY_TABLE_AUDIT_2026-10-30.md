# 更新历史与页面数据核查（2026-10-30）

## 范围和方法

- 复查 2026-10-17 补历史时的处理方式：该次变更保留历史区域以外的页面内容，没有把历史变化逐项反馈到建筑数量表和属性。数量表也没有纳入 `UnitTable` 映射。
- 利用仓库保存的 357 份单位数据，重新检查映射过的升级表；新增数量表检查，展开 110 个页面的 122 张数量表，共比较 1,885 个大本等级或区域单元格。合并建筑使用合并后的数量。数字相同也不代表已独立验证来源正确。
- 检查 2026 年历史中可明确识别的新增等级及 23 条 2026-10-20 充能费用、时间调整；战宠小屋通过其来源表渲染。定向复核带具体数值的射程、速度和半径等属性，以及相关说明。
- 四个往期活动陷阱没有本地来源数据，未做来源比较；超级飞龙岗哨的都城大本数量表另对照维基，子城大本营需求表另对照保存的来源表。部落城堡 1 本来源单元格含特殊标记，也未由数量检查器自动解释。
- 旧 Wiki 完整 HTML 快照不在仓库内，本次未进行逐格历史快照比对，也不能据此保证所有文字说明、全部旧版历史或来源自身无误。

## 已修正的页面

| 页面 | 修正 |
| --- | --- |
| [跳弹加农炮](docs/upgrade/0313-Ricochet-Cannon.md) | 17 本数量由 2 改为 3，与页面更新历史和[17 本更新记录](https://www.clash.ninja/blog/town-hall-17-is-here)一致。 |
| [英雄殿堂](docs/upgrade/0489-Hero-Hall.md) | 数量表改为 4 本起可建；升级表和历史已经写了 4 本。保存的 Wiki 修订数量行仍为 7 本起，现按[游戏文件数据](https://www.gibiarena.com/en/clash-of-clans/upgrades/hero-hall)修正并保存原值。 |
| [精制台](docs/upgrade/048a-Crafting-Station.md) | 第四批开放期间改为 11 本起可用，并移除正文中「目前 17 本」的过时说明。[官方赛季安排](https://supercell.com/en/games/clashofclans/blog/news/the-awesome-quest-is-here/)确认本批从 11 本开放。 |
| [箭塔](docs/upgrade/0302-Archer-Tower.md) | 改装后快速模式射程由 7 改为 8 格，与保存的来源属性和更新历史一致。 |
| [粉碎者](docs/upgrade/0841-Smasher.md) | 修正写反的半径：警戒 14 格、巡逻 12 格，与来源和更新历史一致。 |
| [飞龙公爵](docs/upgrade/0205-Dragon-Duke.md) | 将简介中过时的陷阱伤害减半改为落单时减免 20%，并补到属性；更新历史已记载 2026 年两次调整。 |
| [建筑工人小屋](docs/upgrade/0500-Builders-Hut.md) | 1 本数量上限由 2 改为 5，与正文、来源和属性一致；修正移动速度单位为格/秒。 |
| [小博控制室](docs/upgrade/1284-B.O.B-Control.md) | 6～8 本数量由 1 改为 0，9 本起为 1，与本页建造条件和[来源](https://www.clash.ninja/guides/unlocking-the-6th-builder-b.o.b)一致。 |
| [夜世界箭塔](docs/upgrade/1102-Archer-Tower.md) | 两种模式的数量表均改为 2～3 本 1 座、4～5 本 2 座。 |
| [炸弹塔](docs/upgrade/0308-Bomb-Tower.md) | 数量表补上遗漏的 10 本：10 本起可建 2 座。 |
| [部落城堡](docs/upgrade/0407-Clan-Castle.md) | 数量表改为 2 本起可修复，并说明低本圣水容量限制。 |
| [远袭者](docs/upgrade/0840-Longshot.md) | 将二月更新中范围伤害只作用于同类型目标的规则补到当前说明。 |
| [夜世界储金罐](docs/upgrade/1203-Gold-Storage.md)、[夜世界圣水瓶](docs/upgrade/1204-Elixir-Storage.md) | 1～2 本数量改为 0，与建造条件一致；其他来源分歧在页面标明。 |

家乡加农炮的保存维基数量行写作 1 本 2 座，与[游戏文件数据](https://www.gibiarena.com/en/clash-of-clans/upgrades/cannon)及本站原表的 1 座不符；已在来源记录保存原值和修正依据。英雄殿堂与加农炮的修正均有同步保护，旧来源不能静默覆盖。

## 待确认的分歧

- 夜世界储金罐和圣水瓶：维基列 5 本各 2 个、6～10 本第一区域上限各 2 个；[官方 2.0 说明](https://supercell.com/en/games/clashofclans/blog/news/new-battle-copter-and-troop-abilities/)明确 6 本的两个储罐须分置两区，另有玩家反馈 5 本只有一个。两页保留原来的 5 本和分区数字并标注分歧，等待游戏内确认；登记的 12 个单元格会在数量检查结果中继续列出。
- [超级亡灵](docs/upgrade/0608-Super-Minion.md)的普通攻击射程：旧资料为 3.5 格，保存的维基数据为 4 格，页面已标注，等待游戏内确认；不影响远程狙杀射程的核对。

## 防止再次遗漏

`scripts/check_building_counts.py` 已接入 `check_synced_data.py`，检查数量与来源的差异以及一级解锁条件，遇到未登记或数值发生变化的分歧会报错。手工审定的来源冲突保存在 `scripts/reviewed-building-count-differences.json`，检查结果仍显示这些项目；未匹配到来源的数量表不会被算作已核对。
