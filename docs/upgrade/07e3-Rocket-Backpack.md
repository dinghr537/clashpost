---
title: "部落冲突 coc 火箭背包装备升级数据"
navTitle: "火箭背包"
shownTitle: "火箭背包"
description: "火箭背包是飞龙公爵的第一件史诗装备。使用后，飞龙公爵会沿直线飞向基地中心并穿越整座基地，对路径上的目标造成伤害。除此之外，火箭背包还会提升飞龙公爵的每秒伤害、生命值和开启技能后的生命值恢复。"
module: upgrade-home
imgFolder: home_heroes/07e3
wiki: https://clashofclans.fandom.com/wiki/Rocket_Backpack
canonical: /upgrade/07e3-Rocket-Backpack
dataSyncedOn: 2026-10-13
---

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Rocket_Backpack_info.png" :imgAlt="$frontmatter.navTitle" description="让飞龙公爵沿直线穿越整个基地，同时对路径上的目标造成伤害。" />

<SmallTitle>说明</SmallTitle>

1. 火箭背包是 [飞龙公爵](/upgrade/0205-Dragon-Duke) 的第一件史诗装备，于 2026 年 4 月的冲突之声活动中开放获取。
2. 使用时，飞龙公爵会沿直线飞行，穿越整座基地，并对路径上的所有目标造成伤害。
3. 飞行期间，飞龙公爵不会被选为目标，也不会触发陷阱或部落城堡援军，但会触发特斯拉电磁塔。
4. 除了主动技能外，火箭背包还会提升飞龙公爵的每秒伤害、生命值，以及开启技能后的生命值恢复量。

<SmallTitle>属性</SmallTitle>

<UnitProperties>
    <UnitProperty pKey="技能类型" pValue="主动技能" />
    <UnitProperty pKey="装备稀有度" pValue="史诗" />
    <UnitProperty pKey="伤害半径" pValue="4 格" />
</UnitProperties>

<SmallTitle>升级数据</SmallTitle>

<script setup>
const tableExtraInfo = [
    {
        "column": 5,
        "type": "cost",
        "icon": "Shiny_Ore",
        "noGoldPass": true
    },
    {
        "column": 6,
        "type": "cost",
        "icon": "Glowy_Ore",
        "noGoldPass": true
    },
    {
        "column": 7,
        "type": "cost",
        "icon": "Starry_Ore",
        "noGoldPass": true
    }
];
</script>

<UnitTable :tableExtraInfo="tableExtraInfo">

| 等级 |主动技能<br>伤害|每秒伤害值<br>提升|生命值<br>增加|生命值<br>恢复量增加|闪亮矿石|璀璨矿石|星辉矿石|所需铁匠铺等级|
|  --- |     ---      |       ---       |      ---    |        ---        |   ---  |  ---  |  ---  |     ---     |
| 1 | 575 | 20 | 900 | 300 | \ | \ | \ | 1 |
| 2 | 575 | 23 | 988 | 380 | 120 | \ | \ | 1 |
| 3 | 750 | 26 | 1077 | 460 | 240 | 20 | \ | 1 |
| 4 | 750 | 29 | 1165 | 540 | 400 | \ | \ | 1 |
| 5 | 750 | 32 | 1254 | 620 | 600 | \ | \ | 1 |
| 6 | 950 | 35 | 1342 | 700 | 840 | 100 | \ | 1 |
| 7 | 950 | 38 | 1431 | 780 | 1120 | \ | \ | 1 |
| 8 | 950 | 41 | 1519 | 860 | 1440 | \ | \ | 1 |
| 9 | 1125 | 44 | 1608 | 940 | 1800 | 200 | 10 | 1 |
| 10 | 1125 | 47 | 1696 | 1020 | 1900 | \ | \ | 1 |
| 11 | 1125 | 50 | 1785 | 1100 | 2000 | \ | \ | 1 |
| 12 | 1325 | 53 | 1873 | 1180 | 2100 | 400 | 20 | 1 |
| 13 | 1325 | 56 | 1962 | 1260 | 2200 | \ | \ | 3 |
| 14 | 1325 | 59 | 2050 | 1340 | 2300 | \ | \ | 3 |
| 15 | 1500 | 62 | 2139 | 1420 | 2400 | 600 | 30 | 3 |
| 16 | 1500 | 64 | 2227 | 1500 | 2500 | \ | \ | 5 |
| 17 | 1500 | 66 | 2316 | 1580 | 2600 | \ | \ | 5 |
| 18 | 1700 | 68 | 2404 | 1660 | 2700 | 600 | 50 | 5 |
| 19 | 1700 | 70 | 2493 | 1740 | 2800 | \ | \ | 7 |
| 20 | 1700 | 72 | 2581 | 1800 | 2900 | \ | \ | 7 |
| 21 | 1875 | 74 | 2670 | 1860 | 3000 | 600 | 100 | 7 |
| 22 | 1875 | 76 | 2758 | 1910 | 3100 | \ | \ | 8 |
| 23 | 1875 | 78 | 2847 | 1950 | 3200 | \ | \ | 8 |
| 24 | 2050 | 80 | 2935 | 1975 | 3300 | 600 | 120 | 8 |
| 25 | 2050 | 82 | 3024 | 1990 | 3400 | \ | \ | 9 |
| 26 | 2050 | 84 | 3112 | 1995 | 3500 | \ | \ | 9 |
| 27 | 2150 | 86 | 3200 | 2000 | 3600 | 600 | 150 | 9 |
</UnitTable>

注意：如果升级费用中有多种资源，则同时需要多种资源才能升级。

<SmallTitle>更新历史</SmallTitle>

<Timeline>
    <TimelineItem date="2026/08/31">
        <TimelineRow>修复冲刺缺少火焰效果或过早结束的问题；飞龙公爵会先完成冲刺再被击败，凤凰临时复活效果在冲刺途中结束也不会立即中断冲刺。 <a href="https://supercell.com/en/games/clashofclans/blog/release-notes/august-update-3/" target="_blank" rel="noopener noreferrer">官方公告</a>（08/30 发布；<a href="https://clashofclans.fandom.com/wiki/Diggy?oldid=625147#History" target="_blank" rel="noopener noreferrer">更新日期</a>）</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2026/07/14">
        <TimelineRow>为处理火箭背包有时无法触发的问题，暂时恢复助燃器沿火箭背包方向推动飞龙公爵的行为，等待后续版本正式修复。 <a href="https://supercell.com/en/games/clashofclans/blog/news/july-balance-update/" target="_blank" rel="noopener noreferrer">官方公告</a>（07/09 发布；<a href="https://clashofclans.fandom.com/wiki/Dragon_Rider?oldid=625318#History" target="_blank" rel="noopener noreferrer">更新日期</a>）</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2026/06/16">
        <TimelineRow>装备触发顺序改为由装备本身决定，不再取决于装备栏位置；同时携带助燃器与火箭背包时，先触发助燃器，再触发火箭背包。 <a href="https://supercell.com/en/games/clashofclans/blog/release-notes/the-anime-fury-update-is-here/" target="_blank" rel="noopener noreferrer">官方公告</a>（06/15 发布；<a href="https://clashofclans.fandom.com/wiki/X-Bow?oldid=596696#History" target="_blank" rel="noopener noreferrer">更新日期</a>）</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2026/05/26">
        <TimelineRow>调整21至27级的技能伤害： 21-23级： 1,925 → 1,875 27级： 2,200 → 2,150</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2026/04/27">
        <TimelineRow>修复火箭背包的多项技能问题。 <a href="https://supercell.com/en/games/clashofclans/blog/release-notes/the-sound-of-clash-update/" target="_blank" rel="noopener noreferrer">官方公告</a></TimelineRow>
    </TimelineItem>
    <TimelineItem date="2026/04/08">
        <TimelineRow>新装备：火箭背包。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2026/03/19">
        <TimelineRow>正式开放前调整技能伤害：24—26 级由 2125 降至 2050，27 级由 2325 降至 2200。 <a href="https://clashofclans.fandom.com/wiki/Rocket_Backpack#History" target="_blank" rel="noopener noreferrer">来源</a></TimelineRow>
    </TimelineItem>
    <TimelineItem date="2026/02/23">
        <TimelineRow>火箭背包已加入游戏文件。 <a href="https://clashofclans.fandom.com/wiki/Rocket_Backpack#History" target="_blank" rel="noopener noreferrer">来源</a></TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

<p><small>数值核对：2026-10-13 · <a href="https://clashofclans.fandom.com/wiki/Rocket_Backpack?oldid=623906" target="_blank" rel="noopener noreferrer">部落冲突维基</a>。部分附加字段沿用原记录。</small></p>
