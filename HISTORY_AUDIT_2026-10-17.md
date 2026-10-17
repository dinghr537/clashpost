# 更新历史与来源链接修复：2026-10-17

## 范围与原因

以 2026-10-13 已保存的 357 份单位数据及对应 Wiki 固定快照为范围，离线重读历史表，并对照前次更新核对清单中的二月、四月、五月、六月、七月、八月官方公告。未重新抓取 Wiki，也未把数据同步日期改为本次检查日期。31 个未同步的往期临时单位继续保留原来的历史数据标记。

原同步代码只接受 `Date` 表头，漏读了 `Patch`、`Patch / Type`、`Patch / Update` 形式。因此龙骑士五月、七月的削弱虽然在快照中，却没有导入。日期范围、问号日期也曾被忽略。新解析器保留日期范围与不确定性，遇到核对期内无法识别的日期会报错。

## 结果

- 从缓存补回 26 个单位的 30 条来源历史（含 3 条范围或不确定日期记录）。
- 复查所有已导入历史，补齐漏展示的事件，以及同一日期下遗漏的事实；保持原来的时间线组件、措辞及旧记录。
- 用官方公告补充 53 条单位历史，并单独保存公告发布日期和更新日期依据。
- 共修改 66 个单位页的历史区域；357 份数据现有 225 条历史全部通过逐条正文覆盖检查。
- 对照此前公告的 34 组最高等级缺口，页面均有对应更新历史。
- 全部 400 个构建页面共 436 个 Wiki 链接，均移除读者链接中的 oldid；章节锚点保留，源 Markdown、JSON 中的修订号与固定地址继续保留。

龙骑士新增：2026/05/26，6 级生命值 6200→6000、每秒伤害 520→510；2026/07/14，生命值 6000→5900、每秒伤害 510→490。数值采用已有修订 625318 的历史，未从当前属性反推日期。

## 验证与界限

- 与修改前提交逐文件比较，66 个页面的历史区域以外内容一致，表格的每一行不变；单位 JSON 除 history 外完全一致。
- 35 项 Python 测试、7 项 Node 测试通过，包含原页面结构回归、历史表头和日期解析。来源快照的 42,840 个数值单元格核对通过。
- 新增历史覆盖检查，不再以“日期存在”代替“每条变化都已展示”。已核对的原中文表述保存在 history-paraphrases.json；来源文本变化后旧核对不会自动复用。
- 补充历史保存于 supplemental-history.json，下次数据同步不会覆盖丢失。
- 覆盖目标是已采用来源的历史和所核对公告；不据此承诺来源本身记录了游戏的每一次修正。

浏览器在新启动的生产预览中验证龙骑士历史、月卡切换及时间/费用格式化正常，传送吊坠引用保留 `#Summary` 且不含 `oldid`；新预览没有控制台错误。旧预览在构建更新后出现过初始化错误，未作为发布验证依据。

## 本次修改的单位页

- [气球兵](docs/upgrade/0005-Balloon.md)
- [飞龙](docs/upgrade/0008-Dragon.md)
- [掘地矿工](docs/upgrade/000b-Miner.md)
- [雷电飞龙](docs/upgrade/000c-Electro-Dragon.md)
- [大雪怪](docs/upgrade/000d-Yeti.md)
- [龙骑士](docs/upgrade/000e-Dragon-Rider.md)
- [根蔓骑士](docs/upgrade/0010-Root-Rider.md)
- [巨矛投手](docs/upgrade/0011-Thrower.md)
- [陨石戈仑](docs/upgrade/0012-Meteor-Golem.md)
- [瓦基丽武神](docs/upgrade/0082-Valkyrie.md)
- [戈仑石人](docs/upgrade/0083-Golem.md)
- [巨石投手](docs/upgrade/0086-Bowler.md)
- [英雄猎手](docs/upgrade/0088-Headhunter.md)
- [守护者学徒](docs/upgrade/0089-Apprentice-Warden.md)
- [烈焰熔炉](docs/upgrade/008b-Furnace.md)
- [狂暴法术](docs/upgrade/0102-Rage-Spell.md)
- [冰冻法术](docs/upgrade/0104-Freeze-Spell.md)
- [镜像法术](docs/upgrade/0105-Clone-Spell.md)
- [回溯法术](docs/upgrade/0107-Recall-Spell.md)
- [图腾法术](docs/upgrade/0109-Totem-Spell.md)
- [毒药法术](docs/upgrade/0180-Poison-Spell.md)
- [蔓生法术](docs/upgrade/0185-Overgrowth-Spell.md)
- [冰障法术](docs/upgrade/0186-Ice-Block-Spell.md)
- [愤怒法术](docs/upgrade/0187-Angry-Spell.md)
- [弓箭女皇](docs/upgrade/0201-Archer-Queen.md)
- [飞龙公爵](docs/upgrade/0205-Dragon-Duke.md)
- [攻城战车](docs/upgrade/0240-Wall-Wrecker.md)
- [攻城飞艇](docs/upgrade/0241-Battle-Blimp.md)
- [攻城气球](docs/upgrade/0242-Stone-Slammer.md)
- [攻城训练营](docs/upgrade/0243-Siege-Barracks.md)
- [攻城滚木车](docs/upgrade/0244-Log-Launcher.md)
- [攻城烈焰车](docs/upgrade/0245-Flame-Flinger.md)
- [攻城钻机](docs/upgrade/0246-Battle-Drill.md)
- [部队发射器](docs/upgrade/0247-Troop-Launcher.md)
- [空中战车](docs/upgrade/0248-Sky-Wagon.md)
- [大牦](docs/upgrade/0282-Mighty-Yak.md)
- [地兽](docs/upgrade/0285-Diggy.md)
- [凤凰](docs/upgrade/0287-Phoenix.md)
- [贪婪渡鸦](docs/upgrade/028b-Greedy-Raven.md)
- [城墙](docs/upgrade/0300-Walls.md)
- [迫击炮](docs/upgrade/0303-Mortar.md)
- [法术塔](docs/upgrade/0311-Spell-Tower.md)
- [火焰喷射器](docs/upgrade/0316-Firespitter.md)
- [空中炸弹](docs/upgrade/0382-Air-Bomb.md)
- [兵营](docs/upgrade/0480-Army-Camp.md)
- [暗黑训练营](docs/upgrade/0482-Dark-Barracks.md)
- [暗黑法术工厂](docs/upgrade/0485-Dark-Spell-Factory.md)
- [攻城机器工坊](docs/upgrade/0486-Workshop.md)
- [铁匠铺](docs/upgrade/0488-Blacksmith.md)
- [超级野蛮人](docs/upgrade/0600-Super-Barbarian.md)
- [火箭气球兵](docs/upgrade/060b-Rocket-Balloon.md)
- [超级飞龙](docs/upgrade/060d-Super-Dragon.md)
- [超级大雪怪](docs/upgrade/0610-Super-Yeti.md)
- [地震金靴](docs/upgrade/0702-Earthquake-Boots.md)
- [暗黑皇冠](docs/upgrade/0724-Dark-Crown.md)
- [擎天箭矢](docs/upgrade/0747-Monolith-Arrow.md)
- [生命宝石](docs/upgrade/0781-Life-Gem.md)
- [英雄火炬](docs/upgrade/0786-Heroic-Torch.md)
- [烈焰之心](docs/upgrade/07e0-Fire-Heart.md)
- [助燃器](docs/upgrade/07e1-Flame-Blower.md)
- [爆震器](docs/upgrade/07e2-Stun-Blaster.md)
- [火箭背包](docs/upgrade/07e3-Rocket-Backpack.md)
- [雷电獠牙](docs/upgrade/07e4-Electro-Fangs.md)
- [远袭者](docs/upgrade/0840-Longshot.md)
- [粉碎者](docs/upgrade/0841-Smasher.md)
- [滚木守卫](docs/upgrade/0842-Logger.md)
