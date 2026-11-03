# 单位页面历史与当前展示核查（2026-11-02）

> **后续修复：**以下清单保留修复前的检查结果。分支 `codex/fix-history-display-gaps` 已补入三座建筑各模式的充能、五个派生单位表的缺行，修正已确认的正文及历史错误，并补上只写在历史中的相关规则；尚未发布。仍无法确定的活动版本、派生单位等级及其他来源差异继续保留说明。

修复时对主要冲突的判断：

- 迫击炮充能需要 18 本。多管来源表写 17，但充能对应的 18 级本体和同一建筑标准模式表都要求 18 本；不同模式的伤害仍各自采用原表。
- 回溯法术优先召回英雄；[官方公告](https://supercell.com/en/games/clashofclans/blog/release-notes/the-sound-of-clash-update/)没有给出其他单位的完整排序，因此不继续声称该顺序已核实。
- 图腾在暗黑皇冠和擎天箭矢的人口计算中计为 1；[官方八月公告](https://supercell.com/en/games/clashofclans/blog/release-notes/august-update-3/)明确修正了此前的 20。隐形弹簧的行为单独参照其来源，不能由计数直接推断。
- 18 级生命宝石的生命加成是 120%、上限 1,200；袋装小冰怪 11 级当前表为 17，但 2023 年的 16 是当时的历史值，后续调整日期尚未确认。
- 扫帚女巫精灵的 1～13 级采用对应[维基子单位表](https://clashofclans.fandom.com/wiki/Broom_Witch/Witch_Spirit)；临时活动数值可能因返场而变化。
- 临时熔岩气球在 2025 年活动时为 35 人口，而保存的维基来源表为 21；后续活动版本是否改动尚不能确定。女巫戈仑 12、13 级召唤的大宝宝等级、夜世界储存建筑数量及超级亡灵普通射程仍待进一步核实。

本次应用户要求检查“更新历史写了变化，但上方数据或说明没有跟上”。以下记录的是核查时的仓库内容，不等同于游戏内实时核验；核查当时没有修改单位页或发布。

## 覆盖范围与边界

- 扫描全部 **388** 个 `docs/upgrade/*.md` 单位页；其中 **383** 页有可识别的带日期时间线，合计 **3,321** 条历史行（含仅说明来源的行）。仓库 `docs` 目录里其余页面没有带日期的 `TimelineItem`。对所有单位页生成下方覆盖清单；没有时间线的页面也保留在清单里。
- 对这 388 个线上页面逐页发起只读请求，将服务器返回的 `<main>` 文字与工作区现有构建的对应页面比较：去除标签并规范空白后 **388 页全部一致**。此项检查不比较 HTML 结构、客户端交互或运行时动态变化。
- 有 **357** 份本地来源记录；**31** 个页面（包括旧活动和精工防御页面）没有本地来源记录。数据主要采用 2026-10-13 的 Wiki 固定修订，部分有随后定向修正。保存来源不代表独立验证了游戏内数值，也不代表后来没有变更。
- 对 356 页的既有映射计划执行回填预览和一致性检查：其中 340 页有可回填表、2 页只有保留表、14 页的计划为空；战宠小屋另核对来源表动态渲染。来源有而未映射的等级/充能表也单独列出，并按不同单位和形态核对。数量表检查比较了 **110 页、122 张表、1,885 个单元格**；结果包括已登记的来源分歧，部分页面和单元格未匹配到来源。
- 在全部历史中识别数字形式的新增等级并核对显示的等级行，共识别 **657** 处候选等级表达；另检查全部相关的充能来源表、多模式和派生单位保留表、2026 年的可明确辨认变化，以及可匹配的固定属性。这些是可复核的检查项，**不是对全部自然语言、每种模式和每个历史数字完成语义证明**。
- 自动比较不会保证自行发现所有新写法、条件组合、历史变更后再次变化的情况。原始 Wiki HTML 快照不在仓库，无法逐条对照所有历史时期；某些特定子单位表和字段没有本地来源，不能确认数值。下文将已确认的遗漏、只在历史出现的说明、来源分歧分开列出。

## 已确认：页面数据缺行或前后矛盾

### 本地已有来源，但页面缺充能

1. [迫击炮](docs/upgrade/0303-Mortar.md)：历史明确 18 级有两级超级充能；标准模式和改装快速模式都缺充能行。本地来源表 10、11 各有两行，没有接入页面映射。
2. [地狱之塔](docs/upgrade/030a-Inferno-Tower.md)：历史明确单一目标与多重目标均可充能；两种模式都缺充能行。本地来源表 9、10 未映射。
3. [复仇之塔](docs/upgrade/0319-Revenge-Tower.md)：休眠和三个攻击阶段均缺两级充能；本地来源表 15–18 未映射。

依据：[Supercell 四月更新公告](https://supercell.com/en/games/clashofclans/blog/release-notes/the-sound-of-clash-update/)及仓库保存的各单位来源记录。迫击炮保存的快速模式充能表所需大本等级写 17，标准模式表写 18，与 18 级适用条件有疑点，修复时应先核对，不能静默选一个。

### 本体已经更新，派生单位表未跟上

1. [大雪怪](docs/upgrade/000d-Yeti.md)：本体和历史已有 8 级，但小雪怪表只有 1–7 级；[Wiki 小雪怪表](https://clashofclans.fandom.com/wiki/Yeti/Yetimite)列出第 8 级。
2. [超级大雪怪](docs/upgrade/0610-Super-Yeti.md)：本体和历史已有 8 级，但雷电小雪怪表只有 1–7 级；[Wiki 雷电小雪怪表](https://clashofclans.fandom.com/wiki/Super_Yeti/Electromite)列出第 8 级。
3. [戈仑石人](docs/upgrade/0083-Golem.md)：本体和历史已有 15 级，但小戈仑石人表只有 1–14 级；[Wiki 小戈仑石人表](https://clashofclans.fandom.com/wiki/Golem/Golemite)列出第 15 级。
4. [临时熔岩气球](docs/upgrade/0e0b-Lavaloon.md)：本体表有 12、13 级，但迷你熔岩气球犬表只有 1–11 级；[Wiki 派生单位表](https://clashofclans.fandom.com/wiki/Lavaloon/Lavaloon_Pup)列出 12、13 级。注意此处是临时兵种；装备召唤物是另一套本体数据。
5. [扫帚女巫](docs/upgrade/0e13-Broom-Witch.md)：本体表有 13 级，但女巫精灵表只有 1–12 级；[Wiki 女巫精灵表](https://clashofclans.fandom.com/wiki/Broom_Witch/Witch_Spirit)列出第 13 级。此外历史写低本女巫精灵已增强，上方 1 级仍为伤害 7、生命 300；该 Wiki 当前表为伤害 10、生命 330，来源及活动版本需核对后更新。

这里引用的子单位 Wiki 是供核对的当前公开条目，并非原父单位快照的固定修订；本次未将数值写入项目。

### 页面内部的矛盾

1. [回溯法术](docs/upgrade/0107-Recall-Spell.md)：正文第 9 条写“大单位先被召回”，历史写“优先选择英雄”；应说明英雄优先及其他单位的排序，避免绝对表述冲突。
2. [图腾法术](docs/upgrade/0109-Totem-Spell.md)：正文第 6 条仍称图腾按 20 人口计算暗黑皇冠，历史称改为 1。[Supercell 八月公告](https://supercell.com/en/games/clashofclans/blog/release-notes/august-update-3/)明确涉及暗黑皇冠与擎天箭矢的计数；弹簧陷阱的其他判断不应未经验证直接推断。
3. [生命宝石](docs/upgrade/0781-Life-Gem.md)：18 级的说明例子仍写 100%、上限 725；同页升级表为 120%、上限 1,200，历史也写了比例和上限提升。
4. [女巫戈仑](docs/upgrade/0e0c-Witch-Golem.md)：12、13 级的“每次召唤”一列分别已写“最高 36 / 38”，邻列“最大召唤数量”却写“未知”，同一行表达不一致。
5. [袋装小冰怪](docs/upgrade/0e82-Bag-of-Frostmites.md)：前三行等级全写成 3，对应 6、7、8 本；[Wiki 当前表](https://clashofclans.fandom.com/wiki/Bag_of_Frostmites)对应等级为 1、2、3。该页没有本地来源快照，这是单页额外查到的证据。

## 已确认：当前机制只出现在历史中

以下是实际核对到的具体规则；“正文未写”不等于页面内完全找不到，它们仍出现在更新历史中。

- [复苏法术](docs/upgrade/0108-Revive-Spell.md)：上方只解释范围内选择最近英雄，没有说明点击阵亡英雄图标精确复苏的新增操作。
- [巨型箭矢](docs/upgrade/0742-Giant-Arrow.md)：上方说明和升级表未提对防空火箭的 2 倍伤害。
- [擎天箭矢](docs/upgrade/0747-Monolith-Arrow.md)：上方没有写取消 460 人口上限及图腾人口计数修正；[暗黑皇冠](docs/upgrade/0724-Dark-Crown.md)上方也没有写图腾计数修正。
- [毒药法术](docs/upgrade/0180-Poison-Spell.md)、[远袭者](docs/upgrade/0840-Longshot.md)和[粉碎者](docs/upgrade/0841-Smasher.md)：对守卫造成正常值 30% 毒药伤害的规则只写历史；前两名守卫及[滚木守卫](docs/upgrade/0842-Logger.md)被冻结时不能激活的规则也只写历史。
- [守护者学徒](docs/upgrade/0089-Apprentice-Warden.md)、[生命宝石](docs/upgrade/0781-Life-Gem.md)上方未写光环不再影响攻城机器；[英雄火炬](docs/upgrade/0786-Heroic-Torch.md)上方未写不再影响图腾。
- [天使](docs/upgrade/0007-Healer.md)上方未说明防守天使的溅射治疗不再给防御建筑加血；[搜空地雷](docs/upgrade/0384-Seeking-Air-Mine.md)上方未写最大追踪半径为触发半径的两倍；[夜世界弹射陷阱](docs/upgrade/1180-Push-Trap.md)上方未说明其可弹射跳跃单位。这三项分别记录在 2021、2020 和 2023 年的历史中。
- 九种攻城机器的页面：[攻城战车](docs/upgrade/0240-Wall-Wrecker.md)、[攻城飞艇](docs/upgrade/0241-Battle-Blimp.md)、[攻城气球](docs/upgrade/0242-Stone-Slammer.md)、[攻城训练营](docs/upgrade/0243-Siege-Barracks.md)、[攻城滚木车](docs/upgrade/0244-Log-Launcher.md)、[攻城烈焰车](docs/upgrade/0245-Flame-Flinger.md)、[攻城钻机](docs/upgrade/0246-Battle-Drill.md)、[部队发射器](docs/upgrade/0247-Troop-Launcher.md)、[空中战车](docs/upgrade/0248-Sky-Wagon.md)，上方均未说明小火灵火焰、大本营毒药及光环的更新后关系。原有“进攻方施放的法术无效”与这些具体例外需要分别表述。
- [迫击炮](docs/upgrade/0303-Mortar.md)改装模式的首次连发延迟、[火热蜡烛](docs/upgrade/090b-Hot-Candle.md)衰减开始时机，以及[助燃器](docs/upgrade/07e1-Flame-Blower.md)和[火箭背包](docs/upgrade/07e3-Rocket-Backpack.md)共同装备时的触发顺序，上方均未写明。

机制是否值得在正文展开可按页面定位决定；这里将与用户关注点直接相关的遗漏列为可审阅项目，不声称所有历史中的修复都必须重复放在正文。

## 另外发现：历史本身有误

- [兵营（Army Camp）](docs/upgrade/0480-Army-Camp.md)：2021 年历史声称新增 15 级；页面后来的记录说 2022 年新增 12 级，当前最高也只有 14 级。[2021 官方公告](https://supercell.com/en/games/clashofclans/blog/release-notes/full-patch-notes-th14-update/)与[单位历史](https://clashofclans.fandom.com/wiki/Army_Camp)不支持该新增 15 级记录。
- [暗黑重油罐](docs/upgrade/0406-Dark-Elixir-Storage.md)：2023 年写新增 10 级、16 本解锁，与该页 2022 年 15 本新增 10 级及当前表相矛盾；[官方 16 本公告](https://supercell.com/en/games/clashofclans/blog/game-updates/december-2023-town-hall-16)列的是 11 级。2019 年又写“新增 14 级、8 本可解锁”，[官方 13 本公告](https://supercell.com/en/games/clashofclans/blog/news/december-update-patch-notes/)列的是 8 级暗黑重油罐。
- [骷髅陷阱](docs/upgrade/0385-Skeleton-Trap.md)：2019 年两条历史写成了“搜空地雷”，应核对是否误粘贴；不能直接把其他单位的历史当成骷髅陷阱的更新。

## 待确认，不能直接当成遗漏

- [女巫戈仑](docs/upgrade/0e0c-Witch-Golem.md)本体 1–13 级，大宝宝表 1–11 级；[当前 Wiki 大宝宝条目](https://clashofclans.fandom.com/wiki/Witch_Golem/Big_Boy)也只列 1–11 级。需要确认高等级是否沿用上限，不能仅凭本体等级补造两行。
- [临时熔岩气球](docs/upgrade/0e0b-Lavaloon.md)正文和 2025 年历史写占 35 人口；2026-10-13 保存的来源表写 21。装备召唤物的 21 人口是另一版本，需确认临时兵种的活动版本后处理。
- [袋装小冰怪](docs/upgrade/0e82-Bag-of-Frostmites.md)2023 历史写 11 级降至 16 个，当前表和公开 Wiki 表均写 17；2025 年曾返场，可能有后续调整，不能只凭旧历史覆盖当前表。
- 没有本地来源的页面中，[铁臂终结者](docs/upgrade/0e19-The-Disarmer.md)的 1–12 级伤害及生命值与[当前公开条目](https://clashofclans.fandom.com/wiki/The_Disarmer)相符；这次单页比对不能代替对其他无来源页面的验证。
- 夜世界储金罐、圣水瓶的 12 个数量单元格有已记录来源分歧；超级亡灵普通射程也已记录分歧。建筑数量检查另有 7 个未比较项（包括 4 个无来源活动陷阱、都城特殊表和部落城堡特殊标记）。
- 30 页共 34 张映射表明确保留原始内容；73 页至少有一个字段沿用旧值而没有来源映射。它们不等同于错误，但不能因常规映射检查通过就说已逐值核对。
- 固定属性的机械比较产生 38 条差异候选；攻击范围的计量口径、不同子单位或多发周期可能不同，**不能据此直接判错**。原始候选见下方附录，供逐项复核。

## 逐页覆盖清单

“已映射”只表示现有映射参加了数值预览；“保留/沿用”说明存在未由该映射独立核对的表或列。没有标记的页面不代表人工逐条证明了所有历史和所有正文一致。

| 页面 | 历史行数 | 本地来源 | 升级表检查状态 | 本次发现 |
| --- | ---: | --- | --- | --- |
| [野蛮人](docs/upgrade/0000-Barbarian.md) | 30 | 有 | 已映射 1 张 | — |
| [弓箭手](docs/upgrade/0001-Archer.md) | 28 | 有 | 已映射 1 张 | — |
| [巨人](docs/upgrade/0002-Giant.md) | 30 | 有 | 已映射 1 张 | — |
| [哥布林](docs/upgrade/0003-Goblin.md) | 23 | 有 | 已映射 1 张 | — |
| [炸弹人](docs/upgrade/0004-Wall-Breaker.md) | 32 | 有 | 已映射 1 张 | — |
| [气球兵](docs/upgrade/0005-Balloon.md) | 24 | 有 | 已映射 1 张 | — |
| [法师](docs/upgrade/0006-Wizard.md) | 24 | 有 | 已映射 1 张 | — |
| [天使](docs/upgrade/0007-Healer.md) | 36 | 有 | 已映射 1 张 | 防守天使不能治疗防御建筑只写历史 |
| [飞龙](docs/upgrade/0008-Dragon.md) | 28 | 有 | 已映射 1 张 | — |
| [皮卡超人](docs/upgrade/0009-P.E.K.K.A.md) | 30 | 有 | 已映射 1 张 | — |
| [飞龙宝宝](docs/upgrade/000a-Baby-Dragon.md) | 27 | 有 | 已映射 1 张 | — |
| [掘地矿工](docs/upgrade/000b-Miner.md) | 31 | 有 | 已映射 1 张 | — |
| [雷电飞龙](docs/upgrade/000c-Electro-Dragon.md) | 26 | 有 | 已映射 1 张 | — |
| [大雪怪](docs/upgrade/000d-Yeti.md) | 24 | 有 | 已映射 1 张；保留 1 张 | 确认：小雪怪表缺大雪怪8级 |
| [龙骑士](docs/upgrade/000e-Dragon-Rider.md) | 20 | 有 | 已映射 1 张 | — |
| [雷霆泰坦](docs/upgrade/000f-Electro-Titan.md) | 12 | 有 | 已映射 1 张 | — |
| [根蔓骑士](docs/upgrade/0010-Root-Rider.md) | 13 | 有 | 已映射 1 张 | — |
| [巨矛投手](docs/upgrade/0011-Thrower.md) | 14 | 有 | 已映射 1 张 | — |
| [陨石戈仑](docs/upgrade/0012-Meteor-Golem.md) | 9 | 有 | 已映射 2 张 | — |
| [废墟女巫](docs/upgrade/0013-Ruin-Witch.md) | 5 | 有 | 已映射 1 张 | — |
| [废墟骑士](docs/upgrade/0014-Ruin-Knight.md) | 5 | 有 | 已映射 1 张 | — |
| [亡灵](docs/upgrade/0080-Minion.md) | 28 | 有 | 已映射 1 张 | — |
| [野猪骑士](docs/upgrade/0081-Hog-Rider.md) | 33 | 有 | 已映射 1 张 | — |
| [瓦基丽武神](docs/upgrade/0082-Valkyrie.md) | 29 | 有 | 已映射 1 张 | — |
| [戈仑石人](docs/upgrade/0083-Golem.md) | 34 | 有 | 已映射 1 张；保留 1 张 | 确认：小戈仑石人表缺15级 |
| [女巫](docs/upgrade/0084-Witch.md) | 23 | 有 | 已映射 1 张；保留 1 张 | — |
| [熔岩猎犬](docs/upgrade/0085-Lava-Hound.md) | 23 | 有 | 已映射 1 张 | — |
| [巨石投手](docs/upgrade/0086-Bowler.md) | 27 | 有 | 已映射 1 张 | — |
| [戈仑冰人](docs/upgrade/0087-Ice-Golem.md) | 25 | 有 | 已映射 1 张 | — |
| [英雄猎手](docs/upgrade/0088-Headhunter.md) | 10 | 有 | 已映射 1 张 | — |
| [守护者学徒](docs/upgrade/0089-Apprentice-Warden.md) | 11 | 有 | 已映射 1 张 | 攻城机器例外只写历史 |
| [德鲁伊](docs/upgrade/008a-Druid.md) | 20 | 有 | 已映射 1 张；保留 1 张 | — |
| [烈焰熔炉](docs/upgrade/008b-Furnace.md) | 3 | 有 | 已映射 1 张；保留 1 张 | — |
| [雷电法术](docs/upgrade/0100-Lightning-Spell.md) | 30 | 有 | 已映射 1 张 | — |
| [疗伤法术](docs/upgrade/0101-Healing-Spell.md) | 23 | 有 | 已映射 1 张 | — |
| [狂暴法术](docs/upgrade/0102-Rage-Spell.md) | 13 | 有 | 已映射 1 张 | — |
| [弹跳法术](docs/upgrade/0103-Jump-Spell.md) | 13 | 有 | 已映射 1 张；1 张含沿用列 | — |
| [冰冻法术](docs/upgrade/0104-Freeze-Spell.md) | 14 | 有 | 已映射 1 张 | — |
| [镜像法术](docs/upgrade/0105-Clone-Spell.md) | 18 | 有 | 已映射 1 张 | — |
| [隐形法术](docs/upgrade/0106-Invisibility-Spell.md) | 10 | 有 | 已映射 1 张 | — |
| [回溯法术](docs/upgrade/0107-Recall-Spell.md) | 17 | 有 | 已映射 1 张 | 确认：正文大单位优先与历史英雄优先冲突 |
| [复苏法术](docs/upgrade/0108-Revive-Spell.md) | 6 | 有 | 已映射 1 张 | 复苏英雄的新增操作只写历史 |
| [图腾法术](docs/upgrade/0109-Totem-Spell.md) | 7 | 有 | 已映射 1 张 | 确认：正文暗黑皇冠计数20与历史改为1冲突 |
| [毒药法术](docs/upgrade/0180-Poison-Spell.md) | 26 | 有 | 已映射 1 张 | 对守卫生效的规则只写历史 |
| [地震法术](docs/upgrade/0181-Earthquake-Spell.md) | 13 | 有 | 已映射 1 张 | — |
| [急速法术](docs/upgrade/0182-Haste-Spell.md) | 15 | 有 | 已映射 1 张 | — |
| [骷髅法术](docs/upgrade/0183-Skeleton-Spell.md) | 22 | 有 | 已映射 1 张 | — |
| [蝙蝠法术](docs/upgrade/0184-Bat-Spell.md) | 17 | 有 | 已映射 1 张 | — |
| [蔓生法术](docs/upgrade/0185-Overgrowth-Spell.md) | 9 | 有 | 已映射 1 张 | — |
| [冰障法术](docs/upgrade/0186-Ice-Block-Spell.md) | 2 | 有 | 已映射 1 张 | — |
| [愤怒法术](docs/upgrade/0187-Angry-Spell.md) | 3 | 有 | 已映射 1 张 | — |
| [野蛮人之王](docs/upgrade/0200-Barbarian-King.md) | 41 | 有 | 已映射 1 张 | — |
| [弓箭女皇](docs/upgrade/0201-Archer-Queen.md) | 39 | 有 | 已映射 1 张 | — |
| [大守护者](docs/upgrade/0202-Grand-Warden.md) | 49 | 有 | 已映射 1 张 | — |
| [飞盾战神](docs/upgrade/0203-Royal-Champion.md) | 31 | 有 | 已映射 1 张 | — |
| [亡灵王子](docs/upgrade/0204-Minion-Prince.md) | 7 | 有 | 已映射 1 张 | — |
| [飞龙公爵](docs/upgrade/0205-Dragon-Duke.md) | 10 | 有 | 已映射 1 张 | — |
| [攻城战车](docs/upgrade/0240-Wall-Wrecker.md) | 13 | 有 | 已映射 1 张 | 攻城机器与火焰、毒药和光环的变化只写历史 |
| [攻城飞艇](docs/upgrade/0241-Battle-Blimp.md) | 14 | 有 | 已映射 1 张 | 攻城机器与火焰、毒药和光环的变化只写历史 |
| [攻城气球](docs/upgrade/0242-Stone-Slammer.md) | 11 | 有 | 已映射 1 张；1 张含沿用列 | 攻城机器与火焰、毒药和光环的变化只写历史 |
| [攻城训练营](docs/upgrade/0243-Siege-Barracks.md) | 11 | 有 | 已映射 1 张 | 攻城机器与火焰、毒药和光环的变化只写历史 |
| [攻城滚木车](docs/upgrade/0244-Log-Launcher.md) | 9 | 有 | 已映射 1 张 | 攻城机器与火焰、毒药和光环的变化只写历史 |
| [攻城烈焰车](docs/upgrade/0245-Flame-Flinger.md) | 18 | 有 | 已映射 1 张 | 攻城机器与火焰、毒药和光环的变化只写历史 |
| [攻城钻机](docs/upgrade/0246-Battle-Drill.md) | 10 | 有 | 已映射 1 张 | 攻城机器与火焰、毒药和光环的变化只写历史 |
| [部队发射器](docs/upgrade/0247-Troop-Launcher.md) | 4 | 有 | 已映射 1 张 | 攻城机器与火焰、毒药和光环的变化只写历史 |
| [空中战车](docs/upgrade/0248-Sky-Wagon.md) | 4 | 有 | 已映射 2 张 | 攻城机器与火焰、毒药和光环的变化只写历史 |
| [莱希](docs/upgrade/0280-L.A.S.S.I.md) | 9 | 有 | 已映射 1 张 | — |
| [闪枭](docs/upgrade/0281-Electro-Owl.md) | 9 | 有 | 已映射 1 张 | — |
| [大牦](docs/upgrade/0282-Mighty-Yak.md) | 10 | 有 | 已映射 1 张 | — |
| [独角](docs/upgrade/0283-Unicorn.md) | 8 | 有 | 已映射 1 张 | — |
| [冰牙](docs/upgrade/0284-Frosty.md) | 8 | 有 | 已映射 1 张 | — |
| [地兽](docs/upgrade/0285-Diggy.md) | 8 | 有 | 已映射 1 张 | — |
| [猛蜥](docs/upgrade/0286-Poison-Lizard.md) | 9 | 有 | 已映射 1 张 | — |
| [凤凰](docs/upgrade/0287-Phoenix.md) | 7 | 有 | 已映射 1 张 | — |
| [灵狐](docs/upgrade/0288-Spirit-Fox.md) | 5 | 有 | 已映射 1 张 | — |
| [愤怒水母](docs/upgrade/0289-Angry-Jelly.md) | 3 | 有 | 已映射 1 张 | — |
| [阿啾](docs/upgrade/028a-Sneezy.md) | 2 | 有 | 已映射 1 张；保留 1 张 | — |
| [贪婪渡鸦](docs/upgrade/028b-Greedy-Raven.md) | 2 | 有 | 已映射 1 张 | — |
| [城墙](docs/upgrade/0300-Walls.md) | 39 | 有 | 已映射 1 张 | — |
| [加农炮](docs/upgrade/0301-Cannon.md) | 32 | 有 | 已映射 2 张 | — |
| [箭塔](docs/upgrade/0302-Archer-Tower.md) | 34 | 有 | 已映射 2 张 | — |
| [迫击炮](docs/upgrade/0303-Mortar.md) | 37 | 有 | 已映射 2 张 | 确认：两种模式缺充能行；首轮延迟只写历史 |
| [防空火箭](docs/upgrade/0304-Air-Defense.md) | 33 | 有 | 已映射 1 张；1 张含沿用列 | — |
| [法师塔](docs/upgrade/0305-Wizard-Tower.md) | 30 | 有 | 已映射 1 张 | — |
| [空气炮](docs/upgrade/0306-Air-Sweeper.md) | 7 | 有 | 已映射 1 张 | — |
| [特斯拉电磁塔](docs/upgrade/0307-Hidden-Tesla.md) | 33 | 有 | 已映射 1 张 | — |
| [炸弹塔](docs/upgrade/0308-Bomb-Tower.md) | 30 | 有 | 已映射 1 张；1 张含沿用列 | — |
| [X连弩（十字连弩）](docs/upgrade/0309-X-Bow.md) | 42 | 有 | 已映射 1 张 | — |
| [地狱之塔](docs/upgrade/030a-Inferno-Tower.md) | 36 | 有 | 已映射 2 张 | 确认：两种模式缺充能行 |
| [天鹰火炮](docs/upgrade/030b-Eagle-Artillery.md) | 21 | 有 | 已映射 1 张 | — |
| [巨型特斯拉电磁塔](docs/upgrade/030c-Giga-Tesla.md) | 8 | 有 | 未建立常规映射，须单独核对 | — |
| [巨型地狱之塔](docs/upgrade/030d-Giga-Inferno.md) | 28 | 有 | 未建立常规映射，须单独核对 | — |
| [投石炮](docs/upgrade/030e-Scattershot.md) | 29 | 有 | 已映射 1 张 | — |
| [法术塔](docs/upgrade/0311-Spell-Tower.md) | 14 | 有 | 已映射 1 张 | — |
| [巨石碑](docs/upgrade/0312-Monolith.md) | 14 | 有 | 已映射 1 张 | — |
| [跳弹加农炮](docs/upgrade/0313-Ricochet-Cannon.md) | 14 | 有 | 已映射 1 张 | — |
| [多人箭塔](docs/upgrade/0314-Multi-Archer-Tower.md) | 14 | 有 | 已映射 1 张 | — |
| [地狱火炮](docs/upgrade/0315-Inferno-Artillery.md) | 3 | 有 | 已映射 1 张 | — |
| [火焰喷射器](docs/upgrade/0316-Firespitter.md) | 8 | 有 | 已映射 1 张 | — |
| [复合机械塔](docs/upgrade/0317-Multi-Gear-Tower.md) | 9 | 有 | 已映射 2 张 | — |
| [超级法师塔](docs/upgrade/0318-Super-Wizard-Tower.md) | 1 | 有 | 已映射 1 张 | — |
| [复仇之塔](docs/upgrade/0319-Revenge-Tower.md) | 6 | 有 | 已映射 4 张 | 确认：四种状态缺充能行 |
| [隐形炸弹](docs/upgrade/0380-Bomb.md) | 26 | 有 | 已映射 1 张 | — |
| [隐形弹簧](docs/upgrade/0381-Spring-Trap.md) | 16 | 有 | 已映射 1 张 | — |
| [空中炸弹](docs/upgrade/0382-Air-Bomb.md) | 28 | 有 | 已映射 1 张 | — |
| [巨型炸弹](docs/upgrade/0383-Giant-Bomb.md) | 26 | 有 | 已映射 1 张 | — |
| [搜空地雷](docs/upgrade/0384-Seeking-Air-Mine.md) | 27 | 有 | 已映射 1 张 | 最大追踪半径只写历史 |
| [骷髅陷阱](docs/upgrade/0385-Skeleton-Trap.md) | 13 | 有 | 已映射 2 张 | 确认：2019历史误写搜空地雷 |
| [飓风陷阱](docs/upgrade/0386-Tornado-Trap.md) | 4 | 有 | 已映射 1 张 | — |
| [终极炸弹](docs/upgrade/0387-Giga-Bomb.md) | 3 | 有 | 已映射 1 张 | — |
| [大本营](docs/upgrade/0400-Town-Hall.md) | 28 | 有 | 已映射 2 张 | — |
| [金矿](docs/upgrade/0401-Gold-Mine.md) | 20 | 有 | 已映射 1 张；1 张含沿用列 | — |
| [圣水收集器](docs/upgrade/0402-Elixir-Collector.md) | 21 | 有 | 已映射 1 张；1 张含沿用列 | — |
| [暗黑重油钻井](docs/upgrade/0403-Dark-Elixir-Drill.md) | 17 | 有 | 已映射 1 张；1 张含沿用列 | — |
| [储金罐](docs/upgrade/0404-Gold-Storage.md) | 23 | 有 | 已映射 1 张 | — |
| [圣水瓶](docs/upgrade/0405-Elixir-Storage.md) | 24 | 有 | 已映射 1 张 | — |
| [暗黑重油罐](docs/upgrade/0406-Dark-Elixir-Storage.md) | 23 | 有 | 已映射 1 张 | 确认：2019及2023历史等级写错 |
| [部落城堡](docs/upgrade/0407-Clan-Castle.md) | 27 | 有 | 已映射 1 张 | — |
| [兵营](docs/upgrade/0480-Army-Camp.md) | 22 | 有 | 已映射 1 张 | 确认：2021历史的15级记录有误 |
| [训练营](docs/upgrade/0481-Barracks.md) | 25 | 有 | 已映射 1 张 | — |
| [暗黑训练营](docs/upgrade/0482-Dark-Barracks.md) | 23 | 有 | 已映射 1 张 | — |
| [实验室](docs/upgrade/0483-Laboratory.md) | 20 | 有 | 已映射 1 张 | — |
| [法术工厂](docs/upgrade/0484-Spell-Factory.md) | 14 | 有 | 已映射 1 张 | — |
| [暗黑法术工厂](docs/upgrade/0485-Dark-Spell-Factory.md) | 14 | 有 | 已映射 1 张 | — |
| [攻城机器工坊](docs/upgrade/0486-Workshop.md) | 21 | 有 | 已映射 1 张 | — |
| [战宠小屋](docs/upgrade/0487-Pet-House.md) | 16 | 有 | 来源表动态渲染 | — |
| [铁匠铺](docs/upgrade/0488-Blacksmith.md) | 10 | 有 | 已映射 1 张 | — |
| [英雄殿堂](docs/upgrade/0489-Hero-Hall.md) | 9 | 有 | 已映射 1 张 | — |
| [精制台](docs/upgrade/048a-Crafting-Station.md) | 6 | 有 | 未建立常规映射，须单独核对 | — |
| [建筑工人小屋](docs/upgrade/0500-Builders-Hut.md) | 25 | 有 | 已映射 1 张 | — |
| [小博木屋](docs/upgrade/0501-B.O.Bs-Hut.md) | 1 | 有 | 未建立常规映射，须单独核对 | — |
| [帮手小屋](docs/upgrade/0502-Helper-Hut.md) | 4 | 有 | 已映射 1 张 | — |
| [超级野蛮人](docs/upgrade/0600-Super-Barbarian.md) | 11 | 有 | 已映射 1 张 | — |
| [隐秘哥布林](docs/upgrade/0601-Sneaky-Goblin.md) | 7 | 有 | 已映射 1 张 | — |
| [超级巨人](docs/upgrade/0602-Super-Giant.md) | 11 | 有 | 已映射 1 张；1 张含沿用列 | — |
| [超级炸弹人](docs/upgrade/0603-Super-Wall-Breaker.md) | 11 | 有 | 已映射 1 张 | — |
| [地狱飞龙](docs/upgrade/0604-Inferno-Dragon.md) | 17 | 有 | 已映射 1 张；1 张含沿用列 | — |
| [超级女巫](docs/upgrade/0605-Super-Witch.md) | 12 | 有 | 已映射 1 张 | — |
| [超级弓箭手](docs/upgrade/0606-Super-Archer.md) | 13 | 有 | 已映射 1 张；1 张含沿用列 | — |
| [超级瓦基丽武神](docs/upgrade/0607-Super-Valkyrie.md) | 13 | 有 | 已映射 1 张 | — |
| [超级亡灵](docs/upgrade/0608-Super-Minion.md) | 20 | 有 | 已映射 1 张 | — |
| [超级法师](docs/upgrade/0609-Super-Wizard.md) | 9 | 有 | 已映射 1 张；1 张含沿用列 | — |
| [寒冰猎犬](docs/upgrade/060a-Ice-Hound.md) | 10 | 有 | 已映射 1 张 | — |
| [火箭气球兵](docs/upgrade/060b-Rocket-Balloon.md) | 8 | 有 | 已映射 1 张 | — |
| [超级巨石投手](docs/upgrade/060c-Super-Bowler.md) | 10 | 有 | 已映射 1 张；1 张含沿用列 | — |
| [超级飞龙](docs/upgrade/060d-Super-Dragon.md) | 11 | 有 | 已映射 1 张 | — |
| [超级矿工](docs/upgrade/060e-Super-Miner.md) | 10 | 有 | 已映射 1 张；1 张含沿用列 | — |
| [超级野猪骑士](docs/upgrade/060f-Super-Hog-Rider.md) | 9 | 有 | 已映射 1 张；保留 2 张；1 张含沿用列 | — |
| [超级大雪怪](docs/upgrade/0610-Super-Yeti.md) | 5 | 有 | 已映射 1 张；保留 1 张 | 确认：雷电小雪怪表缺8级 |
| [野蛮人木偶](docs/upgrade/0700-Barbarian-Puppet.md) | 4 | 有 | 已映射 1 张 | — |
| [狂暴药水瓶](docs/upgrade/0701-Rage-Vial.md) | 1 | 有 | 已映射 1 张 | — |
| [地震金靴](docs/upgrade/0702-Earthquake-Boots.md) | 7 | 有 | 已映射 1 张 | — |
| [嗜血胡须](docs/upgrade/0703-Vampstache.md) | 2 | 有 | 已映射 1 张 | — |
| [巨型手套](docs/upgrade/0704-Giant-Gauntlet.md) | 6 | 有 | 已映射 1 张；保留 1 张 | — |
| [尖刺足球](docs/upgrade/0705-Spiky-Ball.md) | 2 | 有 | 已映射 1 张；保留 1 张 | — |
| [灵蛇手镯](docs/upgrade/0706-Snake-Bracelet.md) | 1 | 有 | 已映射 1 张；保留 2 张 | — |
| [木棍马驹](docs/upgrade/0707-Stick-Horse.md) | 2 | 有 | 已映射 1 张；保留 1 张 | — |
| [护卫玩偶](docs/upgrade/0720-Henchmen-Puppet.md) | 2 | 有 | 已映射 1 张；保留 1 张 | — |
| [暗黑魔球](docs/upgrade/0721-Dark-Orb.md) | 2 | 有 | 已映射 1 张 | — |
| [铁甲短裤](docs/upgrade/0722-Metal-Pants.md) | 2 | 有 | 已映射 1 张 | — |
| [贵族哑铃](docs/upgrade/0723-Noble-Iron.md) | 4 | 有 | 已映射 1 张 | — |
| [暗黑皇冠](docs/upgrade/0724-Dark-Crown.md) | 3 | 有 | 已映射 1 张；保留 1 张 | 图腾计数修正只写历史 |
| [陨石法杖](docs/upgrade/0725-Meteor-Staff.md) | 2 | 有 | 已映射 1 张；保留 1 张 | — |
| [传送吊坠](docs/upgrade/0726-Portal-Pendant.md) | 5 | 有 | 已映射 1 张 | — |
| [弓箭手木偶](docs/upgrade/0740-Archer-Puppet.md) | 4 | 有 | 已映射 1 张 | — |
| [隐形药水瓶](docs/upgrade/0741-Invisibility-Vial.md) | 2 | 有 | 已映射 1 张 | — |
| [巨型箭矢](docs/upgrade/0742-Giant-Arrow.md) | 3 | 有 | 已映射 1 张 | 对防空火箭2倍伤害只写历史 |
| [天使木偶](docs/upgrade/0743-Healer-Puppet.md) | 1 | 有 | 已映射 1 张 | — |
| [冰封箭矢](docs/upgrade/0744-Frozen-Arrow.md) | 6 | 有 | 已映射 1 张；保留 1 张 | — |
| [克隆魔镜](docs/upgrade/0745-Magic-Mirror.md) | 2 | 有 | 已映射 1 张；保留 1 张 | — |
| [动作人偶](docs/upgrade/0746-Action-Figure.md) | 1 | 有 | 已映射 1 张；保留 1 张 | — |
| [擎天箭矢](docs/upgrade/0747-Monolith-Arrow.md) | 3 | 有 | 已映射 1 张 | 460人口限制取消、图腾计数修正只写历史 |
| [永恒书卷](docs/upgrade/0780-Eternal-Tome.md) | 5 | 有 | 已映射 1 张 | — |
| [生命宝石](docs/upgrade/0781-Life-Gem.md) | 6 | 有 | 已映射 1 张 | 确认：18级例子与表格冲突；攻城机器例外仅在历史 |
| [狂暴宝石](docs/upgrade/0782-Rage-Gem.md) | 2 | 有 | 已映射 1 张 | — |
| [治疗书卷](docs/upgrade/0783-Healing-Tome.md) | 2 | 有 | 已映射 1 张 | — |
| [巨大火球](docs/upgrade/0784-Fireball.md) | 2 | 有 | 已映射 1 张；保留 1 张 | — |
| [熔岩气球玩偶](docs/upgrade/0785-Lavaloon-Puppet.md) | 3 | 有 | 已映射 1 张；保留 3 张 | — |
| [英雄火炬](docs/upgrade/0786-Heroic-Torch.md) | 4 | 有 | 已映射 1 张 | 图腾例外只写历史 |
| [寻踪飞盾](docs/upgrade/07c0-Seeking-Shield.md) | 1 | 有 | 已映射 1 张 | — |
| [皇家宝石](docs/upgrade/07c1-Royal-Gem.md) | 1 | 有 | 已映射 1 张 | — |
| [野猪骑士木偶](docs/upgrade/07c2-Hog-Rider-Puppet.md) | 3 | 有 | 已映射 1 张 | — |
| [急速药水瓶](docs/upgrade/07c3-Haste-Vial.md) | 3 | 有 | 已映射 1 张 | — |
| [火箭飞矛](docs/upgrade/07c4-Rocket-Spear.md) | 2 | 有 | 已映射 1 张；保留 1 张 | — |
| [雷电战靴](docs/upgrade/07c5-Electro-Boots.md) | 3 | 有 | 已映射 1 张；保留 1 张 | — |
| [冷冽冰晶](docs/upgrade/07c6-Frost-Flake.md) | 1 | 有 | 已映射 1 张；保留 1 张 | — |
| [烈焰之心](docs/upgrade/07e0-Fire-Heart.md) | 8 | 有 | 已映射 1 张 | — |
| [助燃器](docs/upgrade/07e1-Flame-Blower.md) | 7 | 有 | 已映射 1 张 | 与火箭背包的触发顺序只写历史 |
| [爆震器](docs/upgrade/07e2-Stun-Blaster.md) | 4 | 有 | 已映射 1 张 | — |
| [火箭背包](docs/upgrade/07e3-Rocket-Backpack.md) | 8 | 有 | 已映射 1 张 | 与助燃器的触发顺序只写历史 |
| [雷电獠牙](docs/upgrade/07e4-Electro-Fangs.md) | 2 | 有 | 已映射 1 张 | — |
| [反击卡组](docs/upgrade/07e5-Revenge-Deck.md) | 3 | 有 | 已映射 1 张 | — |
| [实验助手](docs/upgrade/0800-Lab-Assistant.md) | 1 | 有 | 已映射 1 张；1 张含沿用列 | — |
| [建筑工人学徒](docs/upgrade/0801-Builder's-Apprentice.md) | 2 | 有 | 已映射 1 张；1 张含沿用列 | — |
| [炼金术士](docs/upgrade/0802-Alchemist.md) | 1 | 有 | 已映射 1 张 | — |
| [探矿者](docs/upgrade/0803-Prospector.md) | 4 | 有 | 已映射 1 张 | — |
| [远袭者](docs/upgrade/0840-Longshot.md) | 9 | 有 | 已映射 1 张；1 张含沿用列 | 冰冻激活、毒药规则只写历史 |
| [粉碎者](docs/upgrade/0841-Smasher.md) | 6 | 有 | 已映射 1 张；1 张含沿用列 | 冰冻激活、毒药规则只写历史 |
| [滚木守卫](docs/upgrade/0842-Logger.md) | 4 | 有 | 已映射 1 张 | 冰冻激活规则只写历史 |
| [钩索塔](docs/upgrade/0900-Hook-Tower.md) | 2 | 无 | 无本地来源，不能逐值核验 | — |
| [旋转喷火器](docs/upgrade/0901-Flame-Spinner.md) | 2 | 无 | 无本地来源，不能逐值核验 | — |
| [碎岩迫击炮](docs/upgrade/0902-Crusher-Mortar.md) | 2 | 无 | 无本地来源，不能逐值核验 | — |
| [英雄警钟](docs/upgrade/0903-Hero-Bell.md) | 1 | 无 | 无本地来源，不能逐值核验 | — |
| [炸弹蜂巢](docs/upgrade/0904-Bomb-Hive.md) | 1 | 无 | 无本地来源，不能逐值核验 | — |
| [圣光灯塔](docs/upgrade/0905-Light-Beam.md) | 1 | 无 | 无本地来源，不能逐值核验 | — |
| [精工空中炸弹发射器](docs/upgrade/0906-Crafted-Air-Bombs.md) | 6 | 有 | 已映射 3 张 | — |
| [精工熔岩发射器](docs/upgrade/0907-Crafted-Lava-Launcher.md) | 6 | 有 | 已映射 3 张 | — |
| [精工炙热熔炉](docs/upgrade/0908-Crafted-Roaster.md) | 6 | 有 | 已映射 3 张 | — |
| [蛋糕投掷器](docs/upgrade/0909-Cake-A-Pult.md) | 3 | 有 | 已映射 3 张 | — |
| [英雄猎台](docs/upgrade/090a-Hero-Hunter.md) | 3 | 有 | 已映射 3 张 | — |
| [火热蜡烛](docs/upgrade/090b-Hot-Candle.md) | 5 | 有 | 已映射 3 张 | 衰减开始时机只写历史 |
| [寒冰法师](docs/upgrade/0e00-Ice-Wizard.md) | 8 | 无 | 无本地来源，不能逐值核验 | — |
| [野蛮人攻城槌](docs/upgrade/0e01-Battle-Ram.md) | 6 | 无 | 无本地来源，不能逐值核验 | — |
| [南瓜野蛮人](docs/upgrade/0e02-Pumpkin-Barbarian.md) | 2 | 无 | 无本地来源，不能逐值核验 | — |
| [骷髅巨人](docs/upgrade/0e03-Giant-Skeleton.md) | 4 | 有 | 已映射 1 张 | — |
| [骷髅飞桶](docs/upgrade/0e04-Skeleton-Barrel.md) | 2 | 无 | 无本地来源，不能逐值核验 | — |
| [艾尔普里莫](docs/upgrade/0e05-El-Primo.md) | 1 | 无 | 无本地来源，不能逐值核验 | — |
| [派对法师](docs/upgrade/0e06-Party-Wizard.md) | 4 | 有 | 已映射 1 张 | — |
| [皇家幽灵](docs/upgrade/0e07-Royal-Ghost.md) | 3 | 有 | 已映射 1 张 | — |
| [蛮羊骑士](docs/upgrade/0e08-Ram-Rider.md) | 6 | 无 | 无本地来源，不能逐值核验 | — |
| [野蛮箭手](docs/upgrade/0e09-Barcher.md) | 6 | 无 | 无本地来源，不能逐值核验 | — |
| [野猪法师](docs/upgrade/0e0a-Hog-Wizard.md) | 4 | 无 | 无本地来源，不能逐值核验 | — |
| [熔岩气球](docs/upgrade/0e0b-Lavaloon.md) | 7 | 有 | 已映射 1 张；保留 1 张 | 确认：迷你熔岩气球犬表缺12、13级；人口来源不一致 |
| [女巫戈仑](docs/upgrade/0e0c-Witch-Golem.md) | 4 | 有 | 已映射 1 张；保留 1 张；1 张含沿用列 | 确认：12、13级召唤上限与同一行最高值冲突；派生单位等级上限待核实 |
| [饼干皮卡](docs/upgrade/0e0d-C.O.O.K.I.E.md) | 3 | 无 | 无本地来源，不能逐值核验 | — |
| [烟花炮手](docs/upgrade/0e0e-Firecracker.md) | 7 | 无 | 无本地来源，不能逐值核验 | — |
| [驭水青龙](docs/upgrade/0e0f-Azure-Dragon.md) | 4 | 无 | 无本地来源，不能逐值核验 | — |
| [任意球野蛮人](docs/upgrade/0e10-Barbarian-Kicker.md) | 4 | 无 | 无本地来源，不能逐值核验 | — |
| [边线球巨人](docs/upgrade/0e11-Giant-Thrower.md) | 1 | 无 | 无本地来源，不能逐值核验 | — |
| [机甲超人](docs/upgrade/0e12-M.E.C.H.A.md) | 3 | 有 | 已映射 1 张 | — |
| [扫帚女巫](docs/upgrade/0e13-Broom-Witch.md) | 4 | 有 | 已映射 1 张；保留 1 张 | 确认：女巫精灵表缺13级；旧值与当前Wiki不一致 |
| [寒冰亡灵](docs/upgrade/0e14-Ice-Minion.md) | 5 | 无 | 无本地来源，不能逐值核验 | — |
| [灵蛇飞桶](docs/upgrade/0e15-Snake-Barrel.md) | 1 | 无 | 无本地来源，不能逐值核验 | — |
| [战吼狂人](docs/upgrade/0e16-YEETer.md) | 1 | 有 | 已映射 2 张 | — |
| [霸天巨人](docs/upgrade/0e17-Giant-Giant.md) | 4 | 有 | 已映射 1 张 | — |
| [皮卡凯恩](docs/upgrade/0e18-K.A.N.E.md) | 2 | 有 | 已映射 2 张 | — |
| [铁臂终结者](docs/upgrade/0e19-The-Disarmer.md) | 6 | 无 | 无本地来源；另核对了伤害和生命值 | — |
| [收债哥布林](docs/upgrade/0e1a-Debt-Collector.md) | 1 | 无 | 无本地来源，不能逐值核验 | — |
| [陨石戈仑](docs/upgrade/0e1b-Meteor-Golem.md) | 2 | 无 | 无本地来源，不能逐值核验 | — |
| [送葬者大雪怪](docs/upgrade/0e1c-Yeti-Undertaker.md) | 0 | 有 | 已映射 2 张 | — |
| [图腾投手](docs/upgrade/0e1d-Totem-Thrower.md) | 3 | 有 | 已映射 2 张 | — |
| [大象骑士](docs/upgrade/0e1e-Elephant-Rider.md) | 0 | 有 | 已映射 1 张 | — |
| [圣诞奇袭](docs/upgrade/0e80-Santas-Surprise.md) | 7 | 无 | 无本地来源，不能逐值核验 | — |
| [生日大爆炸](docs/upgrade/0e81-Birthday-Boom.md) | 1 | 有 | 已映射 0 张；保留 1 张 | — |
| [袋装小冰怪](docs/upgrade/0e82-Bag-of-Frostmites.md) | 6 | 无 | 无本地来源，不能逐值核验 | 确认：前两行等级误写为3；历史与11级数量需核对版本 |
| [黄牌法术](docs/upgrade/0e83-Yellow-Card.md) | 1 | 无 | 无本地来源，不能逐值核验 | — |
| [南瓜炸弹](docs/upgrade/0f00-Pumpkin-Bomb.md) | 2 | 无 | 无本地来源，不能逐值核验 | — |
| [圣诞陷阱](docs/upgrade/0f01-Santa-Strike.md) | 2 | 无 | 无本地来源，不能逐值核验 | — |
| [冰冻陷阱](docs/upgrade/0f02-Freeze-Trap.md) | 1 | 无 | 无本地来源，不能逐值核验 | — |
| [玲珑陷阱](docs/upgrade/0f03-Shrink-Trap.md) | 1 | 无 | 无本地来源，不能逐值核验 | — |
| [狂暴野蛮人](docs/upgrade/1000-Raged-Barbarian.md) | 8 | 有 | 已映射 1 张 | — |
| [隐秘弓箭手](docs/upgrade/1001-Sneaky-Archer.md) | 7 | 有 | 已映射 1 张 | — |
| [巨人拳击手](docs/upgrade/1002-Boxer-Giant.md) | 8 | 有 | 已映射 1 张 | — |
| [异变亡灵](docs/upgrade/1003-Beta-Minion.md) | 7 | 有 | 已映射 1 张 | — |
| [炸弹兵](docs/upgrade/1004-Bomber.md) | 7 | 有 | 已映射 1 张 | — |
| [飞龙宝宝](docs/upgrade/1005-Baby-Dragon.md) | 7 | 有 | 已映射 1 张 | — |
| [加农炮战车](docs/upgrade/1006-Cannon-Cart.md) | 8 | 有 | 已映射 2 张 | — |
| [暗夜女巫](docs/upgrade/1007-Night-Witch.md) | 11 | 有 | 已映射 1 张 | — |
| [骷髅气球](docs/upgrade/1008-Drop-Ship.md) | 12 | 有 | 已映射 1 张 | — |
| [雷霆皮卡](docs/upgrade/1009-Power-P.E.K.K.A.md) | 8 | 有 | 已映射 1 张 | — |
| [野猪飞骑](docs/upgrade/100a-Hog-Glider.md) | 6 | 有 | 已映射 1 张 | — |
| [电火法师](docs/upgrade/100b-Electrofire-Wizard.md) | 1 | 有 | 已映射 2 张 | — |
| [战争机器](docs/upgrade/10f0-Battle-Machine.md) | 12 | 有 | 已映射 1 张 | — |
| [战斗直升机](docs/upgrade/10f1-Battle-Copter.md) | 0 | 有 | 已映射 1 张 | — |
| [加农炮](docs/upgrade/1100-Cannon.md) | 5 | 有 | 已映射 1 张 | — |
| [双管加农炮](docs/upgrade/1101-Double-Cannon.md) | 4 | 有 | 已映射 1 张 | — |
| [箭塔](docs/upgrade/1102-Archer-Tower.md) | 5 | 有 | 已映射 2 张 | — |
| [特斯拉电磁塔](docs/upgrade/1103-Hidden-Tesla.md) | 5 | 有 | 已映射 1 张 | — |
| [防空火炮](docs/upgrade/1104-Firecrackers.md) | 5 | 有 | 已映射 1 张 | — |
| [撼地巨石](docs/upgrade/1105-Crusher.md) | 5 | 有 | 已映射 1 张 | — |
| [守卫岗哨](docs/upgrade/1106-Guard-Post.md) | 4 | 有 | 已映射 1 张 | — |
| [空中炸弹发射器](docs/upgrade/1107-Air-Bombs.md) | 5 | 有 | 已映射 1 张 | — |
| [多管迫击炮](docs/upgrade/1108-Multi-Mortar.md) | 5 | 有 | 已映射 1 张 | — |
| [熔岩火炮](docs/upgrade/1109-Roaster.md) | 5 | 有 | 已映射 1 张 | — |
| [巨型加农炮](docs/upgrade/110a-Giant-Cannon.md) | 6 | 有 | 已映射 1 张 | — |
| [超级特斯拉电磁塔](docs/upgrade/110b-Mega-Tesla.md) | 4 | 有 | 已映射 1 张 | — |
| [城墙](docs/upgrade/110c-Walls.md) | 7 | 有 | 已映射 1 张 | — |
| [熔岩发射器](docs/upgrade/110d-Lava-Launcher.md) | 6 | 有 | 已映射 1 张 | — |
| [X连弩](docs/upgrade/110e-X-Bow.md) | 1 | 有 | 已映射 1 张 | — |
| [弹射陷阱](docs/upgrade/1180-Push-Trap.md) | 7 | 有 | 已映射 1 张 | 可弹射跳跃单位只写历史 |
| [隐形弹簧](docs/upgrade/1181-Spring-Trap.md) | 7 | 有 | 已映射 1 张 | — |
| [地雷](docs/upgrade/1182-Mine.md) | 8 | 有 | 已映射 1 张 | — |
| [巨型地雷](docs/upgrade/1183-Mega-Mine.md) | 8 | 有 | 已映射 1 张 | — |
| [建筑大师大本营](docs/upgrade/1200-Builder-Hall.md) | 4 | 有 | 已映射 1 张；1 张含沿用列 | — |
| [金矿](docs/upgrade/1201-Gold-Mine.md) | 5 | 有 | 已映射 1 张；1 张含沿用列 | — |
| [圣水收集器](docs/upgrade/1202-Elixir-Collector.md) | 5 | 有 | 已映射 1 张；1 张含沿用列 | — |
| [储金罐](docs/upgrade/1203-Gold-Storage.md) | 4 | 有 | 已映射 1 张 | — |
| [圣水瓶](docs/upgrade/1204-Elixir-Storage.md) | 4 | 有 | 已映射 1 张 | — |
| [宝石矿井](docs/upgrade/1205-Gem-Mine.md) | 4 | 有 | 已映射 1 张 | — |
| [奥仔哨站](docs/upgrade/1240-O.T.T.O's-Outpost.md) | 1 | 有 | 已映射 1 张 | — |
| [电击车](docs/upgrade/1241-Zappy.md) | 1 | 有 | 已映射 1 张；1 张含沿用列 | — |
| [建筑大师训练营](docs/upgrade/1280-Builder-Barracks.md) | 5 | 有 | 已映射 1 张；1 张含沿用列 | — |
| [兵营](docs/upgrade/1281-Army-Camp.md) | 1 | 有 | 已映射 1 张 | — |
| [星空实验室](docs/upgrade/1282-Star-Laboratory.md) | 4 | 有 | 已映射 1 张 | — |
| [时光钟楼](docs/upgrade/1283-Clock-Tower.md) | 9 | 有 | 已映射 1 张 | — |
| [小博控制室](docs/upgrade/1284-B.O.B-Control.md) | 2 | 有 | 已映射 0 张；保留 1 张 | — |
| [预备营](docs/upgrade/1285-Reinforcement-Camp.md) | 1 | 有 | 已映射 1 张 | — |
| [治疗小屋](docs/upgrade/1286-Healing-Hut.md) | 1 | 有 | 已映射 1 张 | — |
| [超级野蛮人](docs/upgrade/2000-Super-Barbarian.md) | 2 | 有 | 已映射 1 张 | — |
| [隐秘弓箭手](docs/upgrade/2001-Sneaky-Archer.md) | 2 | 有 | 已映射 1 张 | — |
| [超级巨人](docs/upgrade/2002-Super-Giant.md) | 2 | 有 | 已映射 1 张 | — |
| [野蛮人攻城槌](docs/upgrade/2003-Battle-Ram.md) | 6 | 有 | 已映射 1 张 | — |
| [亡灵大军](docs/upgrade/2004-Minion-Horde.md) | 2 | 有 | 已映射 1 张 | — |
| [超级法师](docs/upgrade/2005-Super-Wizard.md) | 2 | 有 | 已映射 1 张 | — |
| [火箭气球兵](docs/upgrade/2006-Rocket-Balloon.md) | 1 | 有 | 已映射 1 张 | — |
| [骷髅飞桶](docs/upgrade/2007-Skeleton-Barrel.md) | 2 | 有 | 已映射 1 张 | — |
| [飞行堡垒](docs/upgrade/2008-Flying-Fortress.md) | 3 | 有 | 已映射 1 张；保留 1 张 | — |
| [突袭炮车](docs/upgrade/2009-Raid-Cart.md) | 4 | 有 | 已映射 1 张 | — |
| [雷霆皮卡](docs/upgrade/200a-Power-P.E.K.K.A.md) | 3 | 有 | 已映射 1 张 | — |
| [野猪突袭队](docs/upgrade/200b-Hog-Raiders.md) | 1 | 有 | 已映射 2 张 | — |
| [超级飞龙](docs/upgrade/200c-Super-Dragon.md) | 4 | 有 | 已映射 1 张 | — |
| [高山戈仑](docs/upgrade/200d-Mountain-Golem.md) | 5 | 有 | 已映射 1 张 | — |
| [地狱飞龙](docs/upgrade/200e-Inferno-Dragon.md) | 2 | 有 | 已映射 1 张 | — |
| [超级矿工](docs/upgrade/200f-Super-Miner.md) | 7 | 有 | 已映射 1 张 | — |
| [超级电磁炮](docs/upgrade/2010-Mega-Sparky.md) | 1 | 有 | 已映射 1 张 | — |
| [野蛮人](docs/upgrade/20c0-Barbarian.md) | 1 | 有 | 已映射 1 张 | — |
| [骷髅](docs/upgrade/20c1-Skeleton.md) | 0 | 有（无固定修订） | 未建立常规映射，须单独核对 | — |
| [疗伤法术](docs/upgrade/2100-Healing-Spell.md) | 4 | 有 | 已映射 1 张 | — |
| [弹跳法术](docs/upgrade/2101-Jump-Spell.md) | 2 | 有 | 已映射 1 张 | — |
| [雷电法术](docs/upgrade/2102-Lightning-Spell.md) | 2 | 有 | 已映射 1 张 | — |
| [冰霜法术](docs/upgrade/2103-Frost-Spell.md) | 2 | 有 | 已映射 1 张 | — |
| [狂暴法术](docs/upgrade/2104-Rage-Spell.md) | 2 | 有 | 已映射 1 张 | — |
| [骷髅召唤法术](docs/upgrade/2105-Graveyard-Spell.md) | 5 | 有 | 已映射 1 张 | — |
| [永恒急速法术](docs/upgrade/2106-Endless-Haste-Spell.md) | 1 | 有 | 已映射 1 张 | — |
| [城墙](docs/upgrade/2200-Walls.md) | 1 | 有 | 已映射 1 张 | — |
| [加农炮](docs/upgrade/2201-Cannon.md) | 2 | 有 | 已映射 1 张；1 张含沿用列 | — |
| [投矛器](docs/upgrade/2202-Spear-Thrower.md) | 2 | 有 | 已映射 1 张；1 张含沿用列 | — |
| [防空火箭](docs/upgrade/2203-Air-Defense.md) | 3 | 有 | 已映射 1 张；1 张含沿用列 | — |
| [多管加农炮](docs/upgrade/2204-Multi-Cannon.md) | 1 | 有 | 已映射 1 张；1 张含沿用列 | — |
| [炸弹塔](docs/upgrade/2205-Bomb-Tower.md) | 2 | 有 | 已映射 1 张；1 张含沿用列 | — |
| [多管迫击炮](docs/upgrade/2206-Multi-Mortar.md) | 2 | 有 | 已映射 1 张；1 张含沿用列 | — |
| [超级法师塔](docs/upgrade/2207-Super-Wizard-Tower.md) | 1 | 有 | 已映射 1 张；1 张含沿用列 | — |
| [空中炸弹发射器](docs/upgrade/2208-Air-Bombs.md) | 1 | 有 | 已映射 1 张；1 张含沿用列 | — |
| [疾速火箭](docs/upgrade/2209-Rapid-Rockets.md) | 2 | 有 | 已映射 1 张；1 张含沿用列 | — |
| [撼地巨石](docs/upgrade/220a-Crusher.md) | 1 | 有 | 已映射 1 张；1 张含沿用列 | — |
| [超级特斯拉电磁塔](docs/upgrade/220b-Hidden-Mega-Tesla.md) | 1 | 有 | 已映射 1 张；1 张含沿用列 | — |
| [巨型加农炮](docs/upgrade/220c-Giant-Cannon.md) | 1 | 有 | 已映射 1 张；1 张含沿用列 | — |
| [火箭炮](docs/upgrade/220d-Rocket-Artillery.md) | 3 | 有 | 已映射 1 张；1 张含沿用列 | — |
| [地狱之塔](docs/upgrade/220e-Inferno-Tower.md) | 2 | 有 | 已映射 1 张；1 张含沿用列 | — |
| [爆炸强弩](docs/upgrade/220f-Blast-Bow.md) | 2 | 有 | 已映射 1 张；1 张含沿用列 | — |
| [超级巨人岗哨](docs/upgrade/2210-Super-Giant-Post.md) | 1 | 有 | 已映射 1 张；1 张含沿用列 | — |
| [突袭炮车岗哨](docs/upgrade/2211-Raid-Cart-Post.md) | 1 | 有 | 已映射 1 张；1 张含沿用列 | — |
| [超级飞龙岗哨](docs/upgrade/2212-Super-Dragon-Post.md) | 1 | 有 | 已映射 1 张；1 张含沿用列 | — |
| [迷你亡灵巢](docs/upgrade/2213-Mini-Minion-Hive.md) | 1 | 有 | 已映射 1 张；1 张含沿用列 | — |
| [反弹机](docs/upgrade/2214-Reflector.md) | 1 | 有 | 已映射 1 张；1 张含沿用列 | — |
| [哥布林发射器](docs/upgrade/2215-Goblin-Thrower.md) | 1 | 有 | 已映射 1 张；保留 1 张；1 张含沿用列 | — |
| [地雷](docs/upgrade/2280-Mine.md) | 1 | 有 | 已映射 1 张 | — |
| [巨型地雷](docs/upgrade/2281-Mega-Mine.md) | 1 | 有 | 已映射 1 张 | — |
| [滚木陷阱](docs/upgrade/2282-Log-Trap.md) | 1 | 有 | 已映射 1 张 | — |
| [电击陷阱](docs/upgrade/2283-Zap-Trap.md) | 2 | 有 | 已映射 1 张 | — |
| [投矛陷阱](docs/upgrade/2284-Spear-Trap.md) | 1 | 有 | 已映射 1 张 | — |
| [兵营](docs/upgrade/2300-Army-Camp.md) | 2 | 有 | 已映射 1 张；1 张含沿用列 | — |
| [法术仓库](docs/upgrade/2301-Spell-Storage.md) | 0 | 有 | 已映射 1 张；1 张含沿用列 | — |
| [超级野蛮人训练营](docs/upgrade/2340-Super-Barbarian-Barracks.md) | 1 | 有 | 已映射 1 张；1 张含沿用列 | — |
| [隐秘弓箭手训练营](docs/upgrade/2341-Sneaky-Archer-Barracks.md) | 1 | 有 | 已映射 1 张；1 张含沿用列 | — |
| [超级巨人训练营](docs/upgrade/2342-Super-Giant-Barracks.md) | 1 | 有 | 已映射 1 张；1 张含沿用列 | — |
| [野蛮人攻城槌训练营](docs/upgrade/2343-Battle-Ram-Barracks.md) | 1 | 有 | 已映射 1 张；1 张含沿用列 | — |
| [亡灵训练营](docs/upgrade/2344-Minion-Barracks.md) | 1 | 有 | 已映射 1 张；1 张含沿用列 | — |
| [超级法师训练营](docs/upgrade/2345-Super-Wizard-Barracks.md) | 1 | 有 | 已映射 1 张；1 张含沿用列 | — |
| [火箭气球兵训练营](docs/upgrade/2346-Rocket-Balloon-Barracks.md) | 1 | 有 | 已映射 1 张；1 张含沿用列 | — |
| [骷髅飞桶训练营](docs/upgrade/2347-Skeleton-Barrel-Barracks.md) | 1 | 有 | 已映射 1 张；1 张含沿用列 | — |
| [飞行堡垒工坊](docs/upgrade/2348-Flying-Fortress-Yard.md) | 1 | 有 | 已映射 1 张；1 张含沿用列 | — |
| [突袭炮车训练营](docs/upgrade/2349-Raid-Cart-Barracks.md) | 1 | 有 | 已映射 1 张；1 张含沿用列 | — |
| [雷霆皮卡训练营](docs/upgrade/234a-Power-P.E.K.K.A-Barracks.md) | 1 | 有 | 已映射 1 张；1 张含沿用列 | — |
| [野猪突袭队训练营](docs/upgrade/234b-Hog-Raider-Barracks.md) | 1 | 有 | 已映射 1 张；1 张含沿用列 | — |
| [超级飞龙训练营](docs/upgrade/234c-Super-Dragon-Barracks.md) | 1 | 有 | 已映射 1 张；1 张含沿用列 | — |
| [高山戈仑石场](docs/upgrade/234d-Mountain-Golem-Quarry.md) | 1 | 有 | 已映射 1 张；1 张含沿用列 | — |
| [地狱飞龙训练营](docs/upgrade/234e-Inferno-Dragon-Barracks.md) | 1 | 有 | 已映射 1 张；1 张含沿用列 | — |
| [超级矿工训练营](docs/upgrade/234f-Super-Miner-Barracks.md) | 1 | 有 | 已映射 1 张；1 张含沿用列 | — |
| [超级电磁炮工坊](docs/upgrade/2350-Mega-Sparky-Workshop.md) | 1 | 有 | 已映射 1 张；1 张含沿用列 | — |
| [疗伤法术工厂](docs/upgrade/2380-Heal-Spell-Factory.md) | 1 | 有 | 已映射 1 张；1 张含沿用列 | — |
| [弹跳法术工厂](docs/upgrade/2381-Jump-Spell-Factory.md) | 1 | 有 | 已映射 1 张；1 张含沿用列 | — |
| [雷电法术工厂](docs/upgrade/2382-Lightning-Spell-Factory.md) | 1 | 有 | 已映射 1 张；1 张含沿用列 | — |
| [冰霜法术工厂](docs/upgrade/2383-Frost-Spell-Factory.md) | 1 | 有 | 已映射 1 张；1 张含沿用列 | — |
| [狂暴法术工厂](docs/upgrade/2384-Rage-Spell-Factory.md) | 1 | 有 | 已映射 1 张；1 张含沿用列 | — |
| [骷髅召唤法术工厂](docs/upgrade/2385-Graveyard-Spell-Factory.md) | 1 | 有 | 已映射 1 张；1 张含沿用列 | — |
| [永恒急速法术工厂](docs/upgrade/2386-Endless-Haste-Spell-Factory.md) | 1 | 有 | 已映射 1 张；1 张含沿用列 | — |
| [都城大本营](docs/upgrade/2400-Capital-Hall.md) | 1 | 有 | 已映射 1 张；1 张含沿用列 | — |
| [子城大本营](docs/upgrade/2401-District-Hall.md) | 1 | 有 | 已映射 1 张；1 张含沿用列 | — |
| [平顶屋](docs/upgrade/2501-Small-Cabin.md) | 1 | 有 | 未建立常规映射，须单独核对 | — |
| [稻草屋](docs/upgrade/2502-Thatched-Hut.md) | 1 | 有 | 未建立常规映射，须单独核对 | — |
| [小屋](docs/upgrade/2503-Small-Hut.md) | 1 | 有 | 未建立常规映射，须单独核对 | — |
| [木屋](docs/upgrade/2504-Wooden-House.md) | 1 | 有 | 未建立常规映射，须单独核对 | — |
| [平顶木屋](docs/upgrade/2505-Wooden-Cabin.md) | 1 | 有 | 未建立常规映射，须单独核对 | — |
| [斜顶屋](docs/upgrade/2506-Slanted-House.md) | 1 | 有 | 未建立常规映射，须单独核对 | — |
| [哥布林前哨基地](docs/upgrade/2507-Goblin-Outpost.md) | 1 | 有 | 未建立常规映射，须单独核对 | — |
| [哥布林小屋](docs/upgrade/2508-Goblin-Hut.md) | 1 | 有 | 未建立常规映射，须单独核对 | — |
| [哥布林大本营](docs/upgrade/2509-Goblin-Hall.md) | 1 | 有 | 未建立常规映射，须单独核对 | — |

## 附录：固定属性数值差异候选

这些候选仅表示机械提取的数字不同；标题相同也可能来自不同形态，攻击距离、攻速或人口可能采用不同口径。已经解释为不同对象的项不应视作本站错误。

| 页面 | 来源字段 | 本地来源原文（表编号） | 页面值 |
| --- | --- | --- | --- |
| [0005-Balloon](docs/upgrade/0005-Balloon.md) | Range | 0.5 tiles（2） | 攻击距离：0 格 (建筑头顶) |
| [0008-Dragon](docs/upgrade/0008-Dragon.md) | Range | 3 tiles（2） | 攻击距离：2.5 格 |
| [000a-Baby-Dragon](docs/upgrade/000a-Baby-Dragon.md) | Range | 2.75 tiles（2） | 攻击距离：2.25 格 |
| [000c-Electro-Dragon](docs/upgrade/000c-Electro-Dragon.md) | Range | 3 tiles（2） | 攻击距离：2.5 格 |
| [000e-Dragon-Rider](docs/upgrade/000e-Dragon-Rider.md) | Range | 4 tiles（2） | 攻击距离：3.5 格 |
| [0012-Meteor-Golem](docs/upgrade/0012-Meteor-Golem.md) | Range | 5 tiles（2） | 攻击距离：0.8 格 |
| [0012-Meteor-Golem](docs/upgrade/0012-Meteor-Golem.md) | Attack Speed | 1s（2） | 攻击速度：1.5 秒/次 |
| [0080-Minion](docs/upgrade/0080-Minion.md) | Range | 2.75 tiles（2） | 攻击距离：2.25 格 |
| [008a-Druid](docs/upgrade/008a-Druid.md) | Range | 5 tiles（2） | 攻击距离：0.6 格 |
| [0180-Poison-Spell](docs/upgrade/0180-Poison-Spell.md) | Radius | 4 tiles（1） | 作用半径：3.5 格 |
| [0183-Skeleton-Spell](docs/upgrade/0183-Skeleton-Spell.md) | Radius | 3.5 tiles（2） | 作用半径：2.25 格 |
| [0184-Bat-Spell](docs/upgrade/0184-Bat-Spell.md) | Radius | 3.5 tiles（2） | 作用半径：2.25 格 |
| [0204-Minion-Prince](docs/upgrade/0204-Minion-Prince.md) | Range | 3.5 tiles（2） | 攻击距离：4.5 格 |
| [0205-Dragon-Duke](docs/upgrade/0205-Dragon-Duke.md) | Range | 0.3 tiles（2） | 攻击距离：1.25 格 |
| [0240-Wall-Wrecker](docs/upgrade/0240-Wall-Wrecker.md) | Housing Space | 1（2） | 占据人口：30 |
| [0243-Siege-Barracks](docs/upgrade/0243-Siege-Barracks.md) | Housing Space | 1（2） | 占据人口：30 |
| [0244-Log-Launcher](docs/upgrade/0244-Log-Launcher.md) | Movement Speed | 5（2） | 移动速度：0.7 格/秒 |
| [0244-Log-Launcher](docs/upgrade/0244-Log-Launcher.md) | Housing Space | 1（2） | 占据人口：30 |
| [0245-Flame-Flinger](docs/upgrade/0245-Flame-Flinger.md) | Housing Space | 1（2） | 占据人口：30 |
| [0246-Battle-Drill](docs/upgrade/0246-Battle-Drill.md) | Housing Space | 1（2） | 占据人口：30 |
| [0247-Troop-Launcher](docs/upgrade/0247-Troop-Launcher.md) | Housing Space | 1（2） | 占据人口：30 |
| [0281-Electro-Owl](docs/upgrade/0281-Electro-Owl.md) | Range | 6 tiles（3） | 攻击距离：5.5 格 |
| [0289-Angry-Jelly](docs/upgrade/0289-Angry-Jelly.md) | Range | 1.5 tiles（2） | 攻击距离：5 格 |
| [030b-Eagle-Artillery](docs/upgrade/030b-Eagle-Artillery.md) | Attack Speed | 0.75s（5） | 攻速：11.53 秒一轮<sup>②</sup> |
| [0604-Inferno-Dragon](docs/upgrade/0604-Inferno-Dragon.md) | Range | 4 tiles（1） | 攻击距离：3.5 格 |
| [0607-Super-Valkyrie](docs/upgrade/0607-Super-Valkyrie.md) | Range | 0.6 tiles（1） | 攻击距离：0.5 格 |
| [0608-Super-Minion](docs/upgrade/0608-Super-Minion.md) | Range | 4 tiles (Normal) 10.25 tiles (Long Shot)（1） | 普攻攻击距离：3.5 格<sup>①</sup> |
| [0609-Super-Wizard](docs/upgrade/0609-Super-Wizard.md) | Range | 3 tiles（1） | 攻击距离：3.5 格 |
| [060b-Rocket-Balloon](docs/upgrade/060b-Rocket-Balloon.md) | Range | 0.5 tiles（1） | 攻击距离：0 (建筑头顶) |
| [1003-Beta-Minion](docs/upgrade/1003-Beta-Minion.md) | Range | 4 tiles（1） | 攻击距离：3.5 格 |
| [1005-Baby-Dragon](docs/upgrade/1005-Baby-Dragon.md) | Range | 2.5 tiles（1） | 攻击距离：2 格 |
| [10f1-Battle-Copter](docs/upgrade/10f1-Battle-Copter.md) | Range | 7 tiles（1） | 攻击距离：6.5 格 |
| [1108-Multi-Mortar](docs/upgrade/1108-Multi-Mortar.md) | Attack Speed | 0.5s（4） | 攻速：7 秒/轮<sup>*</sup> |
| [1181-Spring-Trap](docs/upgrade/1181-Spring-Trap.md) | Trigger Radius | 0.7 tiles（4） | 触发半径：1 格 |
| [2005-Super-Wizard](docs/upgrade/2005-Super-Wizard.md) | Range | 3 tiles（3） | 攻击距离：2.5 格 |
| [200c-Super-Dragon](docs/upgrade/200c-Super-Dragon.md) | Range | 3 tiles（3） | 攻击距离：2.25 格 |
| [200f-Super-Miner](docs/upgrade/200f-Super-Miner.md) | Range | 0.6 tiles（3） | 攻击距离：0.45 格 |
| [2206-Multi-Mortar](docs/upgrade/2206-Multi-Mortar.md) | Attack Speed | 0.5s（6） | 攻速：7 秒/轮<sup>*</sup> |

检查工具原始输出包括 `scripts/check_synced_data.py` 和只读预览 `scripts/update_authored_data.py`；历史表达与属性候选是本次临时脚本结果。页面来源冲突与无本地来源的区域仍需独立核验。
