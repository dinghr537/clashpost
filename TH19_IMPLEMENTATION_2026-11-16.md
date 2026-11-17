# 19 本版本实施与待核对（2026-11-16）

本分支供本地预览，不代表所有数据已核实。原 Wiki 同步修订日期继续保留；本次另行补充的数据在各页面和 JSON 的 `sync.th19Update` 中标注来源。

## 已处理

- 新增 12 种小队、小队训练营、尖刺塔、烟花炮手塔、守卫神殿和英雄法术，接入家乡目录和搜索。技能和组成依据 [Supercell 更新公告](https://supercell.com/en/games/clashofclans/blog/release-notes/the-clash-of-titans-update-is-rolling-out/)及 [COC Wiki 19 本指南](https://cocwiki.com/guides/town-hall-19)，遵照后者要求同时注明 [Clash of Clans Wiki](https://clashofclans.fandom.com/)及许可。
- 在既有升级表中补充本次新等级，以及旧等级的价格、时间变化。另将用户提供原文的[玩家整理](https://mp.weixin.qq.com/s/1C8VxevkSERrS2x1vJd8aA)全部 410 条逐项对照本站表格及 [ClashKing Assets 固定修订](https://github.com/ClashKingInc/ClashKingAssets/blob/fa40345986d5c862480e6fa34aa5100ab8eee345/assets/static_data.json)，所列新值均与该快照一致；修正遗漏值，并同步相关数据记录。不能据此宣称所有数据均由 Wiki 核实。英雄、研究和守卫数据的升级费用按前一级记录读取，建筑、陷阱按目标等级读取。
- 补充大本营自身储量、建筑及陷阱数量表的 19 本数据，并按小队训练营和现有建筑数量修正大本营建筑总数；19 本精制台按用户确认的一座计入总数。六张宝库表的 19 本容量暂列待更新。
- 根据 Wiki 补全 15 级部落城堡的法术、攻城机器容量、10 级法术工厂容量和 9 级小雪怪；同时检查召唤物与不同模式的表格，来源未提供的数值标为待更新。
- 按用户提供的信息补充 13 级英雄殿堂（4 个栏位、不解锁新英雄）、14 级隐形弹簧（弹飞上限 18 人口）以及三项精工防御的 19 本可用数量（各 1）；粉碎者 2–5 级费用按官方公告修正。
- 将用户提供的截图作为非权威参考，逐项对照 140 条可辨认的升级费用和时间。137 条与本站一致，3 条不同：截图将黑油钻井 1250 万、6 天 12 小时标为 10→11 级，[官方公告](https://supercell.com/en/games/clashofclans/blog/release-notes/the-clash-of-titans-update-is-rolling-out/)列出的新增等级是 12 级，[ClashPerk](https://wiki.clashperk.com/resources/dark-elixir-drill) 和本站也将该费用、时间列于 12 级；截图中巨矛投手 5 级为 12 天 12 小时、英雄法术 4 级为 15 天，本站及 [巨矛投手](https://wiki.clashperk.com/troops/thrower)、[英雄法术](https://wiki.clashperk.com/spells/heroic-spell)资料分别为 13 天、15 天 12 小时。这些差异仍可用游戏内数据核对，未仅凭截图改动。
- 依据官方公告补充 19 本驻军、10 类建筑旧充能的移除、17 本地狱火炮改为满威力单等级、部分平衡调整与冷冽冰晶伤害加成。历史充能数据保留并注明已退役。
- 某些数值按页面已有规则推算，例如飞龙宝宝狂暴、哥布林资源伤害、炸弹人对城墙伤害、跳弹加农炮弹射和疗伤法术总治疗；相关页面注明计算。

## 尚未解决

- 直接查看的 [储金罐](https://clashofclans.fandom.com/wiki/Gold_Storage)、[暗黑重油钻井](https://clashofclans.fandom.com/wiki/Dark_Elixir_Drill)及[冷冽冰晶](https://clashofclans.fandom.com/wiki/Frost_Flake) Wiki 页面截至核查仍未更新本次新增等级或伤害加成；其他页面的更新进度不一致。不能把所有数据称为 Wiki 已核实。
- 17 种超级兵的候选数据在不同快照中重新编号，与现有 Wiki 的“与原兵种同级”编号存在差异。本次分别用 6 至 12 组既有等级的相同生命值和秒伤建立对应，并验证与原兵种新增等级一致，再以旧 Wiki 编号补入部分新等级属性；每页注明映射方式。不同来源的编号与部分特殊技能仍需游戏内确认。官方公布的等级可在 [Supercell 公告](https://supercell.com/en/games/clashofclans/blog/release-notes/the-clash-of-titans-update-is-rolling-out/)核对。
- 粉碎者 2–5 级费用：此前查阅的 Wiki 为 1,300/1,600/1,900/2,150 万圣水，官方公告为 1,500/1,800/2,100/2,300 万；按用户要求现使用官方数值。大守护者 76–80 级费用现按用户提供的玩家整理和 ClashKing 快照中一致的数值填写。2026-11-16 查看的 Wiki 表格仍只列到 85 级，76–80 级为 2,350/2,450/2,550/2,650/2,750 万，既不同于本站新值，也与玩家整理中的调整前数值不完全一致，差异原因仍需核实。
- 部分新等级的技能、容量或治疗参数尚未找到可核实的数值，页面显示“待更新”。主要包括采集器的产量和容量、骷髅陷阱和召唤物数量、部分兵种技能、法术效果和愤怒水母技能时间。小戈仑 7–11 级生命值已确认发生调整，但具体值仍待更新。部分中文名称为暂译。
- 已为 17 种新增单位及 19 级大本营补充本地图片，来源及逐图记录见 [图片清单](docs/public/images/th19-sources.json)。ClashKing 仓库声明 GPL-3.0；数据集合、素材及上游权利的适用范围尚未取得进一步授权或法律确认。正式发布前应结合本站许可完成判断。没有对 Fandom 执行批量自动抓取。

## 新等级中仍标为待更新的字段

- [0402-Elixir-Collector](docs/upgrade/0402-Elixir-Collector.md) 18 级：每小时产量、采集器容量*、出现收集标志时的储量、每个采集器提速所需宝石。
- [0401-Gold-Mine](docs/upgrade/0401-Gold-Mine.md) 18 级：每小时产量、采集器容量*、出现收集标志时的储量、每个采集器提速所需宝石。
- [0407-Clan-Castle](docs/upgrade/0407-Clan-Castle.md) 19 本宝库容量：各部落等级对应的金币、圣水和暗黑重油上限。
- [0403-Dark-Elixir-Drill](docs/upgrade/0403-Dark-Elixir-Drill.md) 12 级：每小时产量、采集器容量*、出现收集标志时的储量、每个采集器提速所需宝石。
- [0385-Skeleton-Trap](docs/upgrade/0385-Skeleton-Trap.md) 6 级：骷髅数量、骷髅等级。
- [0083-Golem](docs/upgrade/0083-Golem.md) 16 级：死亡后分裂的小石头人数量。
- [0083-Golem](docs/upgrade/0083-Golem.md) 16 级：每秒伤害、每次伤害、死亡溅射伤害、生命值。
- [0084-Witch](docs/upgrade/0084-Witch.md) 9 级：每次召唤数量*、召唤的骷髅等级、最大召唤数量。
- [0085-Lava-Hound](docs/upgrade/0085-Lava-Hound.md) 9 级：死后分裂的小狗数量 (进攻/防守)。
- [008a-Druid](docs/upgrade/008a-Druid.md) 7 级：巨熊形态伤害、生命值。
- [0012-Meteor-Golem](docs/upgrade/0012-Meteor-Golem.md) 4 级：小陨石戈仑伤害；生命值为满血母体分裂时的推算值。
- [000c-Electro-Dragon](docs/upgrade/000c-Electro-Dragon.md) 10 级：死亡后闪电伤害。
- [0088-Headhunter](docs/upgrade/0088-Headhunter.md) 5 级：毒药法术效果*。
- [0245-Flame-Flinger](docs/upgrade/0245-Flame-Flinger.md) 6 级：熔岩的最大伤害④、最大存活时间⑤。
- [000f-Electro-Titan](docs/upgrade/000f-Electro-Titan.md) 6 级：光环伤害(每秒/每次)。
- [0013-Ruin-Witch](docs/upgrade/0013-Ruin-Witch.md) 5 级：召唤骑士等级、最多召唤骑士数。
- [0010-Root-Rider](docs/upgrade/0010-Root-Rider.md) 5 级：对墙伤害(每秒/每次)。
- [0109-Totem-Spell](docs/upgrade/0109-Totem-Spell.md) 5 级：图腾生命值。
- [0289-Angry-Jelly](docs/upgrade/0289-Angry-Jelly.md) 11 级：技能持续时间 (秒)。
- [0289-Angry-Jelly](docs/upgrade/0289-Angry-Jelly.md) 12 级：技能持续时间 (秒)。
- [0289-Angry-Jelly](docs/upgrade/0289-Angry-Jelly.md) 13 级：技能持续时间 (秒)。
- [0289-Angry-Jelly](docs/upgrade/0289-Angry-Jelly.md) 14 级：技能持续时间 (秒)。
- [0289-Angry-Jelly](docs/upgrade/0289-Angry-Jelly.md) 15 级：技能持续时间 (秒)。

## 超级兵新增等级尚缺的字段

- [0604-Inferno-Dragon](docs/upgrade/0604-Inferno-Dragon.md) 13 级：初始秒伤、1.7 秒后秒伤、3.2 秒后秒伤。
- [060a-Ice-Hound](docs/upgrade/060a-Ice-Hound.md) 9 级：死亡后冰冻时间、死亡后分裂的迷你寒冰猎犬数量 (进攻/防守)。
- [060d-Super-Dragon](docs/upgrade/060d-Super-Dragon.md) 14 级：平均每秒伤害、每次伤害。
- [060e-Super-Miner](docs/upgrade/060e-Super-Miner.md) 13 级：1.5 秒后秒伤、3 秒后秒伤。
- [0610-Super-Yeti](docs/upgrade/0610-Super-Yeti.md) 9 级：分裂的雷电小雪怪数量。
- [0610-Super-Yeti](docs/upgrade/0610-Super-Yeti.md) 9 级：雷电小雪怪伤害和生命值。
- [060f-Super-Hog-Rider](docs/upgrade/060f-Super-Hog-Rider.md) 16 级：分裂后的超级野猪与超级骑士属性。

## 超级兵等级编号核对

下表比较更新前后数据集中生命值和秒伤均相同的旧等级，并以原兵种的新等级作交叉检查；这是编号推算，尚需游戏内核验。

| 单位 | 候选数据新编号 | 本站沿用的编号 | 一致的旧等级组数 |
| --- | --- | --- | --- |
| 0600-Super-Barbarian | 10 | 14 | 9 |
| 0601-Sneaky-Goblin | 7 | 11 | 6 |
| 0602-Super-Giant | 11 | 15 | 10 |
| 0603-Super-Wall-Breaker | 11 | 15 | 10 |
| 0604-Inferno-Dragon | 13 | 13 | 12 |
| 0605-Super-Witch | 9 | 9 | 8 |
| 0606-Super-Archer | 11 | 15 | 10 |
| 0607-Super-Valkyrie | 13 | 13 | 12 |
| 0608-Super-Minion | 12 | 15 | 11 |
| 0609-Super-Wizard | 11 | 15 | 10 |
| 060a-Ice-Hound | 9 | 9 | 8 |
| 060b-Rocket-Balloon | 10 | 14 | 9 |
| 060c-Super-Bowler | 11 | 11 | 10 |
| 060d-Super-Dragon | 12 | 14 | 11 |
| 060e-Super-Miner | 13 | 13 | 12 |
| 060f-Super-Hog-Rider | 13 | 16 | 12 |
| 0610-Super-Yeti | 9 | 9 | 8 |
