# 升级页面核查记录（2026-10-29）

## 覆盖范围

- 共 388 个单位页面：生产预览中逐页检查页面标题、主要渲染、已加载图片及占位状态。四个分类目录涵盖 387 个地址，废墟骑士页面单独检查。
- 4,949 个普通图片引用均解析到本地文件；本地 2,727 个位图文件均完成解码。31 个页面的 127 个高清引用没有独立文件，当前普通图可显示。德鲁伊巨熊 6 级外观图尚未补齐。
- 357 个单位数据文件、42,864 个单元格通过结构、转换及已映射页面表格一致性检查；其中都城骷髅属于人工核对的基础属性，没有固定修订。31 个往期活动页面继续保留历史数据。
- 离线对照 [clash-of-clans-data 0.19.0](https://www.npmjs.com/package/clash-of-clans-data/v/0.19.0)：匹配到 284 个单位名称，其中 267 个页面至少有一项可对应的数值，共做 14,846 次字段比较。比较涵盖部分等级、生命、伤害、费用、时间、矿石或前置条件，并非逐字核对全部表格与说明。
- 外部数据包自身存在旧值、不同形态及字段口径差异；它仅用于提示疑点，不能据此自动覆盖本站数据。结果中的差异包括不同模式、召唤物、旧版本和计算口径，并不等同于本站错误。
- 仓库内未找到 2026-10-13 的完整 Wiki HTML 快照，项目也尚未确认对 Fandom 的批量自动获取授权。因此本次不能逐项确认所有字段、每条说明都与当前游戏或 Wiki 一致。

## 本次修正

- 都城超级矿工 3 级生命值由 3.7 改为 3,700；原 Wiki 表格写作 `3.700`，游戏数据参考见[来源](https://goblinsfarm.com/wiki/clan-capital/troops/super-miner.html)。已记录修正和同步保护。
- 都城骷髅此前误关联野蛮人的来源；已改为[骷髅来源](https://clashofclans.fandom.com/wiki/Skeleton/Clan_Capital)，移除错误的来源数据，并标记未取得固定修订。
- 修正德鲁伊治疗目标、英雄治疗说明、巨熊 6 级数据和两项历史记录；修正野蛮人、巨矛投手、大牦、高山戈仑的属性或历史说明，以及英雄猎手的毒药说明。
- 根据用户提供的游戏内数值，英雄猎手和大牦的移动速度均改为 24；此前 Wiki 快照分别记为 32 和 20，原值保留在修正记录中。灵狐 9 级每次伤害在不同来源之间存在冲突，已在页面标记，等待进一步核实。

## 数据包比较的差异候选

以下是离线比较产生的全部 49 个页面级候选，按字段统计。它们包含已在上文处理的来源争议及多模式、不同对象、旧版本和经验计算差异；不能当作已确认错误。后续需按具体来源和模式逐项复核。

| 页面 | 有差异的字段（比较次数） |
| --- | --- |
| [雷电飞龙](docs/upgrade/000c-Electro-Dragon.md) | 生命值 2 |
| [龙骑士](docs/upgrade/000e-Dragon-Rider.md) | 每秒伤害 1、生命值 1 |
| [陨石戈仑](docs/upgrade/0012-Meteor-Golem.md) | 生命值 6、所需大本 3、每秒伤害 3 |
| [废墟骑士](docs/upgrade/0014-Ruin-Knight.md) | 每秒伤害 4、生命值 4 |
| [巨石投手](docs/upgrade/0086-Bowler.md) | 每秒伤害 1、生命值 1 |
| [德鲁伊](docs/upgrade/008a-Druid.md) | 每秒治疗 1、每次治疗 1、英雄治疗 1 |
| [野蛮人之王](docs/upgrade/0200-Barbarian-King.md) | 每秒伤害 2、每次伤害 2、生命值 2 |
| [部队发射器](docs/upgrade/0247-Troop-Launcher.md) | 研究时间 1 |
| [灵狐](docs/upgrade/0288-Spirit-Fox.md) | 每次伤害 1 |
| [城墙](docs/upgrade/0300-Walls.md) | 费用 18 |
| [加农炮](docs/upgrade/0301-Cannon.md) | 生命值 6、建造费用 1、每秒伤害 15 |
| [箭塔](docs/upgrade/0302-Archer-Tower.md) | 每秒伤害 12、每发伤害 9 |
| [迫击炮](docs/upgrade/0303-Mortar.md) | 经验 2、每秒伤害 11、每发伤害 11 |
| [防空火箭](docs/upgrade/0304-Air-Defense.md) | 经验 1 |
| [法师塔](docs/upgrade/0305-Wizard-Tower.md) | 经验 1 |
| [特斯拉电磁塔](docs/upgrade/0307-Hidden-Tesla.md) | 经验 1 |
| [炸弹塔](docs/upgrade/0308-Bomb-Tower.md) | 经验 4 |
| [地狱之塔](docs/upgrade/030a-Inferno-Tower.md) | 经验 2 |
| [法术塔](docs/upgrade/0311-Spell-Tower.md) | 经验 1 |
| [巨石碑](docs/upgrade/0312-Monolith.md) | 经验 1 |
| [跳弹加农炮](docs/upgrade/0313-Ricochet-Cannon.md) | 经验 1 |
| [多人箭塔](docs/upgrade/0314-Multi-Archer-Tower.md) | 经验 1 |
| [地狱火炮](docs/upgrade/0315-Inferno-Artillery.md) | 费用 4、建造时间 4、经验 4 |
| [复合机械塔](docs/upgrade/0317-Multi-Gear-Tower.md) | 每秒伤害 1 |
| [隐形炸弹](docs/upgrade/0380-Bomb.md) | 经验 10 |
| [隐形弹簧](docs/upgrade/0381-Spring-Trap.md) | 经验 11 |
| [空中炸弹](docs/upgrade/0382-Air-Bomb.md) | 经验 5 |
| [巨型炸弹](docs/upgrade/0383-Giant-Bomb.md) | 经验 3 |
| [搜空地雷](docs/upgrade/0384-Seeking-Air-Mine.md) | 经验 4 |
| [终极炸弹](docs/upgrade/0387-Giga-Bomb.md) | 经验 2 |
| [金矿](docs/upgrade/0401-Gold-Mine.md) | 经验 9 |
| [圣水收集器](docs/upgrade/0402-Elixir-Collector.md) | 经验 9 |
| [储金罐](docs/upgrade/0404-Gold-Storage.md) | 经验 6 |
| [圣水瓶](docs/upgrade/0405-Elixir-Storage.md) | 经验 6 |
| [暗黑重油罐](docs/upgrade/0406-Dark-Elixir-Storage.md) | 经验 1 |
| [部落城堡](docs/upgrade/0407-Clan-Castle.md) | 所需大本 1、经验 1 |
| [训练营](docs/upgrade/0481-Barracks.md) | 经验 1 |
| [法术工厂](docs/upgrade/0484-Spell-Factory.md) | 经验 1 |
| [战宠小屋](docs/upgrade/0487-Pet-House.md) | 经验 1 |
| [英雄殿堂](docs/upgrade/0489-Hero-Hall.md) | 生命值 3、建造费用 1、建造时间 1、经验 2、所需大本 1 |
| [建筑工人小屋](docs/upgrade/0500-Builders-Hut.md) | 经验 1 |
| [野猪飞骑](docs/upgrade/100a-Hog-Glider.md) | 生命值 6 |
| [箭塔](docs/upgrade/1102-Archer-Tower.md) | 每秒伤害 10 |
| [城墙](docs/upgrade/110c-Walls.md) | 费用 9 |
| [电击车](docs/upgrade/1241-Zappy.md) | 生命值 10 |
| [建筑大师训练营](docs/upgrade/1280-Builder-Barracks.md) | 建造费用 1、所需夜世界大本 1 |
| [星空实验室](docs/upgrade/1282-Star-Laboratory.md) | 建造费用 1、所需夜世界大本 1 |
| [突袭炮车](docs/upgrade/2009-Raid-Cart.md) | 每秒伤害 5、生命值 5 |
| [野猪突袭队](docs/upgrade/200b-Hog-Raiders.md) | 生命值 5 |

## 未由该数据包做逐格比较的页面

共 121 页；此处表示未能从该数据包匹配字段，不表示这些页面没有做本地结构或图片检查，也不排除个别页面已做定向来源核对。

[巨型特斯拉电磁塔](docs/upgrade/030c-Giga-Tesla.md)、[巨型地狱之塔](docs/upgrade/030d-Giga-Inferno.md)、[超级法师塔](docs/upgrade/0318-Super-Wizard-Tower.md)、[复仇之塔](docs/upgrade/0319-Revenge-Tower.md)、[大本营](docs/upgrade/0400-Town-Hall.md)、[精制台](docs/upgrade/048a-Crafting-Station.md)
[小博木屋](docs/upgrade/0501-B.O.Bs-Hut.md)、[帮手小屋](docs/upgrade/0502-Helper-Hut.md)、[超级野蛮人](docs/upgrade/0600-Super-Barbarian.md)、[隐秘哥布林](docs/upgrade/0601-Sneaky-Goblin.md)、[超级巨人](docs/upgrade/0602-Super-Giant.md)、[超级炸弹人](docs/upgrade/0603-Super-Wall-Breaker.md)
[地狱飞龙](docs/upgrade/0604-Inferno-Dragon.md)、[超级女巫](docs/upgrade/0605-Super-Witch.md)、[超级弓箭手](docs/upgrade/0606-Super-Archer.md)、[超级瓦基丽武神](docs/upgrade/0607-Super-Valkyrie.md)、[超级亡灵](docs/upgrade/0608-Super-Minion.md)、[超级法师](docs/upgrade/0609-Super-Wizard.md)
[寒冰猎犬](docs/upgrade/060a-Ice-Hound.md)、[火箭气球兵](docs/upgrade/060b-Rocket-Balloon.md)、[超级巨石投手](docs/upgrade/060c-Super-Bowler.md)、[超级飞龙](docs/upgrade/060d-Super-Dragon.md)、[超级矿工](docs/upgrade/060e-Super-Miner.md)、[超级野猪骑士](docs/upgrade/060f-Super-Hog-Rider.md)
[超级大雪怪](docs/upgrade/0610-Super-Yeti.md)、[钩索塔](docs/upgrade/0900-Hook-Tower.md)、[旋转喷火器](docs/upgrade/0901-Flame-Spinner.md)、[碎岩迫击炮](docs/upgrade/0902-Crusher-Mortar.md)、[英雄警钟](docs/upgrade/0903-Hero-Bell.md)、[炸弹蜂巢](docs/upgrade/0904-Bomb-Hive.md)
[圣光灯塔](docs/upgrade/0905-Light-Beam.md)、[精工空中炸弹发射器](docs/upgrade/0906-Crafted-Air-Bombs.md)、[精工熔岩发射器](docs/upgrade/0907-Crafted-Lava-Launcher.md)、[精工炙热熔炉](docs/upgrade/0908-Crafted-Roaster.md)、[蛋糕投掷器](docs/upgrade/0909-Cake-A-Pult.md)、[英雄猎台](docs/upgrade/090a-Hero-Hunter.md)
[火热蜡烛](docs/upgrade/090b-Hot-Candle.md)、[寒冰法师](docs/upgrade/0e00-Ice-Wizard.md)、[野蛮人攻城槌](docs/upgrade/0e01-Battle-Ram.md)、[南瓜野蛮人](docs/upgrade/0e02-Pumpkin-Barbarian.md)、[骷髅巨人](docs/upgrade/0e03-Giant-Skeleton.md)、[骷髅飞桶](docs/upgrade/0e04-Skeleton-Barrel.md)
[艾尔普里莫](docs/upgrade/0e05-El-Primo.md)、[派对法师](docs/upgrade/0e06-Party-Wizard.md)、[皇家幽灵](docs/upgrade/0e07-Royal-Ghost.md)、[蛮羊骑士](docs/upgrade/0e08-Ram-Rider.md)、[野蛮箭手](docs/upgrade/0e09-Barcher.md)、[野猪法师](docs/upgrade/0e0a-Hog-Wizard.md)
[熔岩气球](docs/upgrade/0e0b-Lavaloon.md)、[女巫戈仑](docs/upgrade/0e0c-Witch-Golem.md)、[饼干皮卡](docs/upgrade/0e0d-C.O.O.K.I.E.md)、[烟花炮手](docs/upgrade/0e0e-Firecracker.md)、[驭水青龙](docs/upgrade/0e0f-Azure-Dragon.md)、[任意球野蛮人](docs/upgrade/0e10-Barbarian-Kicker.md)
[边线球巨人](docs/upgrade/0e11-Giant-Thrower.md)、[机甲超人](docs/upgrade/0e12-M.E.C.H.A.md)、[扫帚女巫](docs/upgrade/0e13-Broom-Witch.md)、[寒冰亡灵](docs/upgrade/0e14-Ice-Minion.md)、[灵蛇飞桶](docs/upgrade/0e15-Snake-Barrel.md)、[战吼狂人](docs/upgrade/0e16-YEETer.md)
[霸天巨人](docs/upgrade/0e17-Giant-Giant.md)、[皮卡凯恩](docs/upgrade/0e18-K.A.N.E.md)、[铁臂终结者](docs/upgrade/0e19-The-Disarmer.md)、[收债哥布林](docs/upgrade/0e1a-Debt-Collector.md)、[陨石戈仑](docs/upgrade/0e1b-Meteor-Golem.md)、[送葬者大雪怪](docs/upgrade/0e1c-Yeti-Undertaker.md)
[图腾投手](docs/upgrade/0e1d-Totem-Thrower.md)、[大象骑士](docs/upgrade/0e1e-Elephant-Rider.md)、[圣诞奇袭](docs/upgrade/0e80-Santas-Surprise.md)、[生日大爆炸](docs/upgrade/0e81-Birthday-Boom.md)、[袋装小冰怪](docs/upgrade/0e82-Bag-of-Frostmites.md)、[黄牌法术](docs/upgrade/0e83-Yellow-Card.md)
[南瓜炸弹](docs/upgrade/0f00-Pumpkin-Bomb.md)、[圣诞陷阱](docs/upgrade/0f01-Santa-Strike.md)、[冰冻陷阱](docs/upgrade/0f02-Freeze-Trap.md)、[玲珑陷阱](docs/upgrade/0f03-Shrink-Trap.md)、[兵营](docs/upgrade/1281-Army-Camp.md)、[小博控制室](docs/upgrade/1284-B.O.B-Control.md)
[预备营](docs/upgrade/1285-Reinforcement-Camp.md)、[骷髅飞桶](docs/upgrade/2007-Skeleton-Barrel.md)、[野蛮人](docs/upgrade/20c0-Barbarian.md)、[骷髅](docs/upgrade/20c1-Skeleton.md)、[弹跳法术](docs/upgrade/2101-Jump-Spell.md)、[雷电法术](docs/upgrade/2102-Lightning-Spell.md)
[冰霜法术](docs/upgrade/2103-Frost-Spell.md)、[狂暴法术](docs/upgrade/2104-Rage-Spell.md)、[骷髅召唤法术](docs/upgrade/2105-Graveyard-Spell.md)、[永恒急速法术](docs/upgrade/2106-Endless-Haste-Spell.md)、[超级野蛮人训练营](docs/upgrade/2340-Super-Barbarian-Barracks.md)、[隐秘弓箭手训练营](docs/upgrade/2341-Sneaky-Archer-Barracks.md)
[超级巨人训练营](docs/upgrade/2342-Super-Giant-Barracks.md)、[野蛮人攻城槌训练营](docs/upgrade/2343-Battle-Ram-Barracks.md)、[亡灵训练营](docs/upgrade/2344-Minion-Barracks.md)、[超级法师训练营](docs/upgrade/2345-Super-Wizard-Barracks.md)、[火箭气球兵训练营](docs/upgrade/2346-Rocket-Balloon-Barracks.md)、[骷髅飞桶训练营](docs/upgrade/2347-Skeleton-Barrel-Barracks.md)
[飞行堡垒工坊](docs/upgrade/2348-Flying-Fortress-Yard.md)、[突袭炮车训练营](docs/upgrade/2349-Raid-Cart-Barracks.md)、[雷霆皮卡训练营](docs/upgrade/234a-Power-P.E.K.K.A-Barracks.md)、[野猪突袭队训练营](docs/upgrade/234b-Hog-Raider-Barracks.md)、[超级飞龙训练营](docs/upgrade/234c-Super-Dragon-Barracks.md)、[高山戈仑石场](docs/upgrade/234d-Mountain-Golem-Quarry.md)
[地狱飞龙训练营](docs/upgrade/234e-Inferno-Dragon-Barracks.md)、[超级矿工训练营](docs/upgrade/234f-Super-Miner-Barracks.md)、[超级电磁炮工坊](docs/upgrade/2350-Mega-Sparky-Workshop.md)、[疗伤法术工厂](docs/upgrade/2380-Heal-Spell-Factory.md)、[弹跳法术工厂](docs/upgrade/2381-Jump-Spell-Factory.md)、[雷电法术工厂](docs/upgrade/2382-Lightning-Spell-Factory.md)
[冰霜法术工厂](docs/upgrade/2383-Frost-Spell-Factory.md)、[狂暴法术工厂](docs/upgrade/2384-Rage-Spell-Factory.md)、[骷髅召唤法术工厂](docs/upgrade/2385-Graveyard-Spell-Factory.md)、[永恒急速法术工厂](docs/upgrade/2386-Endless-Haste-Spell-Factory.md)、[平顶屋](docs/upgrade/2501-Small-Cabin.md)、[稻草屋](docs/upgrade/2502-Thatched-Hut.md)
[小屋](docs/upgrade/2503-Small-Hut.md)、[木屋](docs/upgrade/2504-Wooden-House.md)、[平顶木屋](docs/upgrade/2505-Wooden-Cabin.md)、[斜顶屋](docs/upgrade/2506-Slanted-House.md)、[哥布林前哨基地](docs/upgrade/2507-Goblin-Outpost.md)、[哥布林小屋](docs/upgrade/2508-Goblin-Hut.md)
[哥布林大本营](docs/upgrade/2509-Goblin-Hall.md)

## 后续需要

取得覆盖相应页面、允许本项目使用且带日期和修订信息的来源快照或游戏数据后，按村庄、单位形态、等级及前置条件逐字段比对，并复核正文说明。不要把本次页面打开、文件解码或内部一致性通过视为游戏内准确性的证明。
