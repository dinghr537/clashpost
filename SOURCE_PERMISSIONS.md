# 来源权限核查（2026-10-16）

本文件记录实际查阅的条款、收录范围和仍需确认的事项，不把来源链接、可访问的 API 或视觉检查当作授权。面向读者的署名与许可见 [NOTICE.md](NOTICE.md) 和 [来源与许可](docs/sources.md)。

## 2026-11-21 来源收口：统一仅采用四项来源

按用户要求，全站活跃数据与页面引用统一收口为 **4 项来源**：**部落驿站原资料**、**Supercell 官方资料**、**Clash of Clans Wiki**、**ClashKing Assets**。下文早期的第三方参考记录仅作为历史审计档案保留，不再作为当前数据或页面引用来源：

- **Clash Ninja**：2026 年 4 月法师塔已无引用；2026-10-20 调整的 10 种建筑超级充能均已在 19 本退役并从页面移除，本次一并清理 10 个单位 JSON 中过期的 `sync.balanceUpdate` 及对应页面前置元数据 `dataBalanceUpdatedOn`。
- **ClashFox**：2026-10-20 平衡调整涉及的 10 个单位均已逐一核对 **Clash of Clans Wiki** 当前表格一致（其中 8 个于 2026-11-17 核对，超级矿工与超级野猪骑士于 2026-11-21 核对），对应 JSON 的 `numericSourceUrl` 及小陨石戈仑派生表来源均已替换为 Wiki 页面地址。
- **1337Wiki**：活跃页面与脚本中已无任何引用，正式停用。
- **ClashPerk Wiki 与其他零星站点**（`9game.cn`、`clashdaddy.com`、`cocwarbase.com`、`clash-markets.com`、`blooing.com`、`gibiarena.com`、`goblinsfarm.com`、`reddit.com`）：
  - 移除毒药法术、急速法术及三座资源库 JSON 中残留的 `additionalSource`（ClashPerk）。
  - 毒药法术、亡灵王子、飞龙公爵、愤怒水母 4 页属性差异脚注改以**原站资料**与**部落冲突维基**对照说明。
  - `0301-Cannon.json`、`0489-Hero-Hall.json`、`200f-Super-Miner.json` 及 `scripts/reviewed-building-count-differences.json` 中的修正依据，按实际对应关系改记为**部落驿站原资料**、**Clash of Clans Wiki** 或 **Supercell 官方公告**。

## 2026-11-17 用户决定：采用 ClashKing 数据，允许访问 Fandom

用户决定：

- **采用 ClashKing 游戏数据。** Wiki 尚未更新的 19 本数值，改用 [ClashKing Assets](https://github.com/ClashKingInc/ClashKingAssets) 发布的 `static_data.json`（下载地址 `https://assets.clashk.ing/static_data.json`，2026-11-17 下载）。该仓库的 `update_static.py` 从游戏安装包提取数据表格后生成此文件。README 欢迎他人使用其托管文件并请求署名，仓库采用 GPL-3.0。本站只把所需的单个数值填入自有表格，并在单位页注明 ClashKing，不复制其数据文件。
  - 采用前已与 Wiki 及官方核实过的数值比对：19 本新增和调整的 482 个重叠数值中有 479 个一致。不一致的 3 个中，2 个是 Wiki 的笔误或取整，1 个是多人箭塔 5 级生命值（Wiki 5,400，ClashKing 5,900）。1–4 级生命值依次为 5,000、5,200、5,400、5,500，Wiki 的 5 级值与 3 级相同，且低于 4 级，经用户决定采用 ClashKing 的 5,900。
  - 等级对应规则：兵种、法术、英雄、战宠的升级费用和时间取 ClashKing 前一级的记录，建筑和陷阱取同一级的记录。每个单位的每一列，须先与本站已核实数值完全一致才会填入；没有通过比对的列不填，并保留原状。
- **Fandom 可以访问，可以使用其数据。** 下文《Fandom 获取方式：待确认》一节中“不再执行批量联网抓取和补图”的限制，按用户本次决定不再适用。2026-11-17 已经通过公开 API 刷新 Wiki 快照，并下载了新等级图片；图片来源记录在 `scripts/image-sources/wiki-sources.json`。

## 2026-11-16 来源收缩：当前执行方式

以下各节保留此前真实的查找、对照和使用记录；它们不是对当前仍使用所有候选数值的声明。按用户要求，当前版本优先使用 Supercell 官方、Clash of Clans Wiki、原部落驿站资料，以及用户或其他玩家核实的事实。用户亲自查看游戏提供的信息也统一标为“玩家提供”。此前来自小站或第三方整理、尚未通过这些来源确认的候选数值不再作为当前表格数值，相关字段标为“待更新”。用户提供的第三方文章和截图不自动等于玩家亲自核实。

本轮人工查看 Wiki，确认 12 种小队的研究表、小队训练营 1–12 级、尖刺塔和烟花炮手塔 1–2 级、英雄法术、野蛮人、弓箭手、巨人，以及大本营和部落城堡已核对字段，可使用对应 Wiki 页面；粉碎者 2–5 级费用仍以官方公告为准。Wiki 的实验室升级总表仍有旧值。储金罐、圣水瓶、暗黑重油罐和骷髅陷阱所查看的 Wiki 页面尚未列出各自新增等级；19 本宝库基础容量亦未在已查看的 Wiki 表中找到。其他标为待更新的字段中有的尚未逐页核查，不能由此断言 Wiki 没有，详见 [待更新数据核对清单](docs/verification.md)。

19 本图片仍使用本文件下文列出的 33 张 ClashKing 素材及一张官方素材，图片出处与数据来源分开记录，并没有因为精简游戏数值来源而移除图片署名。

2026-11-17 复查 [Wiki 宝库](https://clashofclans.fandom.com/wiki/Treasury)、[储金罐](https://clashofclans.fandom.com/wiki/Gold_Storage)和[骷髅陷阱](https://clashofclans.fandom.com/wiki/Skeleton_Trap)页面，相关表格仍分别只列至 18 本、19 级和 5 级。圣水瓶、暗黑重油罐的最后一次人工检查是 11 月 16 日，不能套用 11 月 17 日的复查日期。

同日逐行核对 [实验室](https://clashofclans.fandom.com/wiki/Laboratory)、[防空火箭](https://clashofclans.fandom.com/wiki/Air_Defense)、[特斯拉电磁塔](https://clashofclans.fandom.com/wiki/Hidden_Tesla)、[建筑工人小屋](https://clashofclans.fandom.com/wiki/Builder%27s_Hut)的部分旧等级和新增等级，及 [X 连弩](https://clashofclans.fandom.com/wiki/X-Bow)的历史充能费用和时间；已将这些与 Wiki 一致的字段补回。Wiki 的英雄殿堂和隐形弹簧页面仍未列出新增等级，旧等级也有未跟上此次调整的数值，不能用整页替换。升级经验由已确认的升级秒数开平方取整计算，修正了九处本地数据中的旧经验值。

同日还核对了 [哥布林](https://clashofclans.fandom.com/wiki/Goblin)、[法师](https://clashofclans.fandom.com/wiki/Wizard)、[天使](https://clashofclans.fandom.com/wiki/Healer)、[掘地矿工](https://clashofclans.fandom.com/wiki/Miner)的升级表，以及 [大雪怪](https://clashofclans.fandom.com/wiki/Yeti)更新历史中的旧等级减免，补回页面中直接列出的数值。又核对了[金矿](https://clashofclans.fandom.com/wiki/Gold_Mine)、[圣水收集器](https://clashofclans.fandom.com/wiki/Elixir_Collector)、[暗黑重油钻井](https://clashofclans.fandom.com/wiki/Dark_Elixir_Drill)的历史充能费用和部分时间；金矿、圣水收集器第 3 次充能时间与此前候选记录不一致，暂不采用；回本时间没有照搬其他来源。

同日进一步核对了[野蛮人之王](https://clashofclans.fandom.com/wiki/Barbarian_King)、[弓箭女皇](https://clashofclans.fandom.com/wiki/Archer_Queen)、[炸弹人](https://clashofclans.fandom.com/wiki/Wall_Breaker)、[气球兵](https://clashofclans.fandom.com/wiki/Balloon)、[飞龙](https://clashofclans.fandom.com/wiki/Dragon)和[皮卡超人](https://clashofclans.fandom.com/wiki/P.E.K.K.A)的升级表。炸弹人 15 级死亡后对墙伤害仍未在表中列出，保留待更新；[大守护者](https://clashofclans.fandom.com/wiki/Grand_Warden)、[飞盾战神](https://clashofclans.fandom.com/wiki/Royal_Champion)、[亡灵王子](https://clashofclans.fandom.com/wiki/Minion_Prince)和[飞龙公爵](https://clashofclans.fandom.com/wiki/Dragon_Duke)的表仍是此次更新前的等级与费用。

同日核对了[飞龙宝宝](https://clashofclans.fandom.com/wiki/Baby_Dragon)、[雷电飞龙](https://clashofclans.fandom.com/wiki/Electro_Dragon)、[龙骑士](https://clashofclans.fandom.com/wiki/Dragon_Rider)、[雷霆泰坦](https://clashofclans.fandom.com/wiki/Electro_Titan)、[根蔓骑士](https://clashofclans.fandom.com/wiki/Root_Rider)、[巨矛投手](https://clashofclans.fandom.com/wiki/Thrower)、[陨石戈仑](https://clashofclans.fandom.com/wiki/Meteor_Golem)和[瓦基丽武神](https://clashofclans.fandom.com/wiki/Valkyrie)的部分等级。瓦基丽武神的旧等级减免见更新历史，升级表尚未同步；雷电飞龙 5 级表格亦仍是旧值，因此没有用其覆盖待更新项。

同日核对了多种法术及防御建筑的 Wiki 升级表和 11 月更新历史，补回其中直接列出的费用、时间和已确认属性。多人箭塔 5 级生命值在 Wiki 表中为 5,400，而此前候选记录为 5,900；因为存在差异，当前保留待更新，等待玩家从游戏核实。所有随时间变化的升级经验均由已核对的升级时间重新计算。

同日逐级核对了 [冷冽冰晶](https://clashofclans.fandom.com/wiki/Frost_Flake)、[传送吊坠](https://clashofclans.fandom.com/wiki/Portal_Pendant)、[冰封箭矢](https://clashofclans.fandom.com/wiki/Frozen_Arrow)、[烈焰之心](https://clashofclans.fandom.com/wiki/Fire_Heart)和[废墟骑士](https://clashofclans.fandom.com/wiki/Ruin_Witch/Ruin_Knight)的当前 Wiki 数据及更新历史，补回对应字段。攻城战车、飞艇、气球、训练营、滚木车、烈焰车和钻机的相关等级表仍显示调整前的费用与时间，已在核对清单列出。

## 已确认的内容许可

| 来源 | 依据 | 本项目处理 |
| --- | --- | --- |
| 部落驿站 | [用户须知](https://clashpost.com/p/260)第 1 节：游戏数据、文章默认 CC BY-SA 4.0；[README](https://github.com/lemonicy/clashpost#readme)允许继续整理、维护、迁移历史资料，并要求说明继承关系 | 保留原作者和继承关系；为数据资料补充 CC 许可；不把该说明扩大为所有代码、界面和图片的许可 |
| Clash of Clans Wiki | [版权说明](https://clashofclans.fandom.com/wiki/Clash_of_Clans_Wiki:Copyrights)、[Fandom Licensing](https://www.fandom.com/licensing)、[署名说明](https://community.fandom.com/wiki/Help:Licensing)：文本默认 CC BY-SA 3.0，链接原文章可满足其贡献者署名方式 | 保留单位原页、修订与日期；改编用 CC BY-SA 4.0，未改编原文保留 3.0；不将图片一并声明为 CC |
| Supercell | [玩家内容政策](https://supercell.com/en/fan-content-policy/)允许符合条件的线上玩家资料与素材展示 | 保留非官方声明；不收费解锁查询，不暗示官方认可；第三方加工素材仍需单独判断 |
| Clash Ninja | [使用条款](https://www.clash.ninja/terms-of-use)第 3 节要求复制内容前取得书面许可 | 不作为批量导入来源；仅保留少量明确标注用途的事实参考，不能将其标记为已获转载许可 |

CC BY-SA 3.0 的 [4(b) 条](https://creativecommons.org/licenses/by-sa/3.0/legalcode.en#s4b)允许改编采用后续同要素版本；这不改变未改编原文的原许可，也不覆盖第三方图片和游戏资产。

## 2026-11-18 19 本资料来源复核

大本营、12 种小队、小队训练营、英勇法术、尖刺塔、烟花炮手塔和守卫神殿共 18 页，现按[Supercell 更新公告](https://supercell.com/en/games/clashofclans/blog/release-notes/the-clash-of-titans-update-is-rolling-out/)与 Fandom 原条目整理。单位页的 Markdown 保存各自的固定修订链接。43 条有升级费用和时间的研究或建筑记录已逐行比对 Fandom 表格。19 级大本营的生命值、升级费用和时间另与 [ClashKing 数据快照](https://github.com/ClashKingInc/ClashKingAssets/blob/fa40345986d5c862480e6fa34aa5100ab8eee345/assets/static_data.json)交叉核对。Fandom 文字、表格的署名和改编许可见[来源与许可](docs/sources.md)。

早期版本所用来源及当时的许可核查保存在[迁移前的记录](https://github.com/dinghr537/clashpost/blob/626b6db7a26597c35a9581b6df9c98e19cd3a9bf/SOURCE_PERMISSIONS.md)。

## ClashKing Assets：2026-11-16 核查

[仓库 README](https://github.com/ClashKingInc/ClashKingAssets/blob/fa40345986d5c862480e6fa34aa5100ab8eee345/README.md)声明仓库采用 GPL-3.0，并欢迎在署名的情况下使用其托管素材。仓库包含游戏资料与素材，该声明不能自动解决上游权利、本站资料许可与批量转载的适配问题；尤其不能将 Supercell 游戏图片直接标为 GPL 或 CC 授权。比较两个公开修订后，本站针对本次版本新增等级及部分旧等级费用、时间引用了有限范围的游戏数值，按本站原有表格结构整理，并在单位页注明；没有复制该仓库的说明文字或原始数据结构。结果及尚未核实的字段见 [19 本逐等级核查](TH19_LEVEL_COVERAGE_2026-11-16.md)和 [19 本实施记录](TH19_IMPLEMENTATION_2026-11-16.md)。

随后为本地预览补充了 33 张该仓库固定修订中的游戏图片，并从 [Supercell 官方帮助中心](https://sc-clashofclans.zendesk.com/hc/en-us/articles/49529107397403-Guardians)补充守卫神殿图片。每张图的精确地址、画面说明、核对日期和权利依据见 [19 本图片记录](scripts/image-sources/th19-sources.json)；图片不按文字的 CC 许可处理。Supercell 的[玩家内容政策](https://supercell.com/en/fan-content-policy/)及 ClashKing 仓库声明与本站发布形式、许可的适配仍需在正式发布前确认。

## Fandom 获取方式：待确认（2026-11-17 已由用户决定，见上文）

2026-10-16 已通过浏览器读取[当前使用条款](https://www.fandom.com/terms-of-use)，页面修订日期为 **2025-12-19**。`User conduct` 包含自动抓取/提取限制、未经书面许可使用自动工具访问的限制，以及未经书面同意将内容用于软件开发（包括训练 AI）的限制。本文不自行断定这些条款与社区 CC 许可的法律适用关系，也不将 AI 整理资料等同于训练模型。

当前条款中没有确认到适用于本项目批量 MediaWiki API 读取的例外。2026-10-13 的 357 页同步使用了公开 API，但接口能访问不构成许可证明。因此，**在取得适用的明确 API 条款或书面许可前，不再执行对 Fandom 的批量联网抓取和补图**。手动要求 AI 运行脚本仍是自动访问，不是例外。

已有本地快照的解析、翻译校正、来源记录补充及页面构建可以继续进行；这不代表已追认此前的获取方式。后续若使用平台正式提供的导出文件，也须核对下载途径与用途条款，不能把更换接口当作绕过限制的方法。

未取得新的第三方书面授权。若需联系网站，应先由用户明确授权发送具体询问信息。

## Clash Ninja 引用核对

四月更新中，法师塔单位页、其 JSON 和同步脚本的补充历史，以及旧更新核对文档引用了 Ninja 的四月公告，没有导入其整套表格或文章。十月充能调整的引用范围见下文。

- **17 级升级时间旧值 8 天 12 小时**：已在本地保存的 [Wiki 修订 625327 的 2025-11-17 历史](https://clashofclans.fandom.com/wiki/Wizard_Tower?oldid=625327#History)核实。
- **当前值 5 天 12 小时**：已在同一固定修订的 17 级升级表核实，页面与 JSON 的数值来源改为该 Wiki 修订。
- **2026-04-27 生效日期**：该 Wiki 修订没有对应历史条目；[官方公告](https://supercell.com/en/games/clashofclans/blog/release-notes/the-sound-of-clash-update/)仅笼统说明缩减费用和时间，没有法师塔的这一行。日期仍注明来自 [Ninja 当日公告](https://www.clash.ninja/blog/april-2026-update-is-live)，未伪装成官方或 Wiki 已确认的日期。若找到可支持同一日期和变更的开放来源，再替换日期引用。

保留这个事实参考不等于认定 Ninja 授予了转载许可。原始发现过程保留在旧核对文档中。

### 2026-10-20 充能费用与时间调整

根据用户提供的 [Clash Ninja 当日公开动态](https://x.com/ClashDotNinja/status/2112523574984446061)，记录 10 种建筑、23 个充能等级的费用和时间，逐页附来源。仅提取此次变更的游戏数值，以本站原有表格和自行整理的中文变更说明呈现；不转载配图、原文或整套数据库，也不将其视为获准批量同步的来源。原 Wiki 快照日期保留，后续定向修正另记在 `sync.balanceUpdate`。

经验按升级秒数的平方根向下取整；采集器 JSON 中的回本时间沿用停产损失除以新增产量的计算方式，按新充能时间重算。派生值注明计算依据，未冒充动态直接提供的数值。

## 2026-10-20 平衡调整的补充事实参考

本次调整范围采用 [Supercell 10 月 17 日公告](https://supercell.com/en/games/clashofclans/blog/news/balance-changes-incoming-october-2026/)。公告没有完整等级数字，具体数值参考 [ClashFox 的同次调整整理](https://clashfox.com/blog/balance-changes-before-town-hall-19-fire-heart-and-ruin-witch-nerfed-hogs-and-p-e-k-k-a-bu)，仅记录涉及的游戏数值，未复制其文章、评论、图表图片或站点素材，也未批量导入其资料库。

已查阅 [ClashFox 条款](https://clashfox.com/terms)（页面标注 2024 年 12 月更新），其中限制自动访问及未经许可复制其原创内容；没有取得新的书面转载或自动获取授权，不将其列为获准批量同步来源。此处记录有限事实引用的实际来源，不宣称该站整篇内容已获授权或属于本站 CC 许可。来源把骑士数值误标为女巫，本次根据官方公告和游戏内核对将其归入废墟骑士。

生效日期依据 10 月 20 日 UTC 的[官方维护完成消息](https://x.com/ClashofClans/status/2112450159326179560)，并在维护后核对游戏内调整后的数值；该维护消息本身只确认维护结束。1 级废墟骑士已确认为 2900 生命、240 秒伤、18 人口、游戏内移动速度 14。没有将 10 月 17 日的预告日期当作生效日期。

## 图片来源检查与限制

现有来源清单有 **2,641 个原站文件**（`static.clashpost.com`，含 2026-11-03 补充的 126 张原图）和 **210 个 Wiki 补图文件**（`static.wikia.nocookie.net`）。本次核对了清单覆盖和来源域名，为 Wiki 文件补充了可回查许可的文件说明页地址。先前 `reviewed-wiki-images.json` 的审核只代表图与单位、等级相符，**不代表版权审核通过**。

游戏原始美术适用 Supercell 玩家内容政策；Wiki 文件说明页若写 fair use，并不等于向本站授予 CC 许可。作者自制图解、截图加工、站点图标及其他独立作品需核对实际权利与授权。本次未逐一确认全部图片的文件许可，故不把这些图片统一标记为“已授权”或 CC BY-SA。

新增图片时应记录来源文件页、作者/权利人、许可或玩家内容政策适用依据及核对日期。已有来源不明的图片保留待核查记录，不靠批量删除来掩盖缺项。正式发布前需完成实际使用图片中第三方独立作品的权利判断；尚未完成时如实列入发布说明。

## 本次落实与剩余事项

已落实：全站页脚许可入口、资料许可范围与贡献者署名、改编说明、Wiki 图片文件页回查地址、Ninja 数值引用替换、维护流程中的来源权限要求。

未解决：Fandom 批量自动获取的明确授权；图片逐项权利判断；上游代码和界面公开部署的授权范围（README 的资料继承说明与旧网站其他内容限制并存）；法师塔更新日期的替代来源。上述未决项不会因补了一个声明页面而自动消失。

## 2026-11-03 数据与原图定向核查

- 超级巨人岗哨、都城地雷、滚木陷阱及火箭气球兵训练营的子城数量或名称，依据各页已有的 Wiki 固定修订核对，并定向查看 1337Wiki 对应子城资料；引用链接已放在各表旁。只采用相关游戏数值，没有复制该站文章、图片或整套数据；两个站的数据是否独立采集没有确认。
- 夜世界隐形弹簧的触发半径按已有 Wiki 修订与 1337Wiki 对应页面核对；巨型地狱之塔 2024 年 6 月历史的 13 本标记及攻城机器的人口说明依据页面内 Supercell 链接核对。都城超级矿工 3 级生命值来源已替换成 Supercell 官方 2024 年 2 月公告。
- 用户提供的 12 级超级亡灵游戏截图显示“范围：2.5 格”，截图未标注游戏版本；本站记录该显示值，不据此推断与其他来源 3.5 格、4 格之间的换算关系，也不转载截图。
- 逐项检查原页面声明但未保存在本地的 127 个原图地址：126 个返回 PNG、1 个（`Miner12_hd.png`）返回 404。126 个中有 123 个比对应本地缩略图分辨率更大，另 3 个尺寸相同。根据用户要求和用户提供的[上游历史资料维护说明](https://github.com/lemonicy/clashpost#readme)，126 个原图已原样保存，并逐一核对与页面等级图片的视觉对应关系；每个文件的来源页、原始 URL、尺寸、SHA-256、导入时间及权利参考保存在 `scripts/image-sources/original-sources.json`。上游说明允许维护和迁移历史资料，未明确对每张图片的第三方加工权利作统一许可；游戏资产仍按 [Supercell 玩家内容政策](https://supercell.com/en/fan-content-policy/)处理，逐项权利判断未完成，不将图片统一标为 CC 授权。
- 木屋子城名称、超级亡灵及其他射程来源冲突仍待确认；多来源相同并不自动证明数据分别来自独立测量。

## ClashPerk Wiki：2026-11-16 定向参考

[急速法术页面](https://wiki.clashperk.com/spells/haste-spell)显示 8 级的加速、持续时间和半径；另参考[毒药法术页面](https://wiki.clashperk.com/spells/poison-spell)的 13 级减速数据，以及[储金罐](https://wiki.clashperk.com/resources/gold-storage)、[圣水瓶](https://wiki.clashperk.com/resources/elixir-storage)和[暗黑重油罐](https://wiki.clashperk.com/resources/dark-elixir-storage)的新增等级容量。本站仅引用这些相关游戏数值并注明来源，没有复制其文字、图片或整套数据。[其条款页](https://clashperk.com/terms)描述 Discord 机器人服务，不足以证明 Wiki 内容的转载许可；不把其页面统一标为开放许可。
