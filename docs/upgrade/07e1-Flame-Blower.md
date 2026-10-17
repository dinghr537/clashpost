---
title: "部落冲突 coc 助燃器装备升级数据"
navTitle: "助燃器"
shownTitle: "助燃器"
description: "助燃器是飞龙公爵的两件初始装备之一，另一件是烈焰之心。使用时，助燃器在飞龙公爵面前喷出锥形的火焰造成大量伤害。烈焰之心装备还可以增加飞龙公爵生命值以及技能状态下的生命值恢复量。"
module: upgrade-home
imgFolder: home_heroes/07e1
wiki: https://clashofclans.fandom.com/wiki/Flame_Blower
canonical: /upgrade/07e1-Flame-Blower
dataSyncedOn: 2026-10-13
---

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Flame_Blower_info.png" :imgAlt="$frontmatter.navTitle" description="吹出炽热烈焰，灼烧敌人和建筑。" />

<SmallTitle>说明</SmallTitle>

1. 助燃器是 [飞龙公爵](/upgrade/0205-Dragon-Duke) 的两件初始装备之一，另一件是 [烈焰之心](/upgrade/07e0-Fire-Heart)。
2. 开启技能后，飞龙公爵面前会喷出锥形火焰，可造成大量伤害。
3. 烈焰之心装备还可以增加飞龙公爵生命值以及技能状态下的生命值恢复量。

<SmallTitle>属性</SmallTitle>

<UnitProperties>
    <UnitProperty pKey="技能类型" pValue="主动技能" />
    <UnitProperty pKey="装备稀有度" pValue="普通" />
    <UnitProperty pKey="解锁条件" pValue="有飞龙公爵即可" />
    <UnitProperty pKey="火焰半径" pValue="12 格" />
</UnitProperties>

<SmallTitle>升级数据</SmallTitle>

<script setup>
const tableExtraInfo = [
    {
        "column": 4,
        "type": "cost",
        "icon": "Shiny_Ore",
        "noGoldPass": true
    },
    {
        "column": 5,
        "type": "cost",
        "icon": "Glowy_Ore",
        "noGoldPass": true
    }
];
</script>

<UnitTable :tableExtraInfo="tableExtraInfo">

| 等级 | 技能伤害 |英雄<br>生命值增加|开启技能后<br>生命值恢复量增加|升级费用|升级费用|所需<br>铁匠铺等级|所需<br>大本等级|
| ---- |    ---  |       ---      |            ---             |   ---  |  ---  |       ---       |       ---     |
| 1 | 1300 | 500 | 150 | \ | \ | \ | 15 |
| 2 | 1300 | 700 | 250 | 120 | \ | 1 | 8 |
| 3 | 1375 | 900 | 350 | 240 | 20 | 1 | 8 |
| 4 | 1375 | 1100 | 450 | 400 | \ | 1 | 8 |
| 5 | 1375 | 1300 | 550 | 600 | \ | 1 | 8 |
| 6 | 1500 | 1500 | 650 | 840 | 100 | 1 | 8 |
| 7 | 1500 | 1700 | 750 | 1120 | \ | 1 | 8 |
| 8 | 1500 | 1850 | 850 | 1440 | \ | 1 | 8 |
| 9 | 1750 | 2000 | 950 | 1800 | 200 | 1 | 8 |
| 10 | 1750 | 2150 | 1050 | 1900 | \ | 3 | 10 |
| 11 | 1750 | 2300 | 1150 | 2000 | \ | 3 | 10 |
| 12 | 2000 | 2450 | 1250 | 2100 | 400 | 3 | 10 |
| 13 | 2000 | 2600 | 1300 | 2200 | \ | 5 | 12 |
| 14 | 2000 | 2750 | 1350 | 2300 | \ | 5 | 12 |
| 15 | 2250 | 2900 | 1400 | 2400 | 600 | 5 | 12 |
| 16 | 2250 | 3000 | 1450 | 2500 | \ | 7 | 14 |
| 17 | 2250 | 3050 | 1500 | 2600 | \ | 7 | 14 |
| 18 | 2500 | 3100 | 1500 | 2700 | 600 | 7 | 14 |
</UnitTable>

注意：如果升级费用中有多种资源，则同时需要多种资源才能升级。<br>

<SmallTitle>更新历史</SmallTitle>

<Timeline>
    <TimelineItem date="2026/08/31">
        <TimelineRow>修复与火箭背包配合时的方向问题，助燃器现在沿飞龙公爵面朝的方向喷射。 <a href="https://supercell.com/en/games/clashofclans/blog/release-notes/august-update-3/" target="_blank" rel="noopener noreferrer">官方公告</a>（08/30 发布；<a href="https://clashofclans.fandom.com/wiki/Diggy?oldid=625147#History" target="_blank" rel="noopener noreferrer">更新日期</a>）</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2026/07/14">
        <TimelineRow>为处理火箭背包有时无法触发的问题，暂时恢复助燃器沿火箭背包方向推动飞龙公爵的行为，等待后续版本正式修复。 <a href="https://supercell.com/en/games/clashofclans/blog/news/july-balance-update/" target="_blank" rel="noopener noreferrer">官方公告</a>（07/09 发布；<a href="https://clashofclans.fandom.com/wiki/Dragon_Rider?oldid=625318#History" target="_blank" rel="noopener noreferrer">更新日期</a>）</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2026/06/16">
        <TimelineRow>装备触发顺序改为由装备本身决定，不再取决于装备栏位置；同时携带助燃器与火箭背包时，先触发助燃器，再触发火箭背包。 <a href="https://supercell.com/en/games/clashofclans/blog/release-notes/the-anime-fury-update-is-here/" target="_blank" rel="noopener noreferrer">官方公告</a>（06/15 发布；<a href="https://clashofclans.fandom.com/wiki/X-Bow?oldid=596696#History" target="_blank" rel="noopener noreferrer">更新日期</a>）</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2026/02/27">
        <TimelineRow>公布助燃器的技能机制。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2026/02/23">
        <TimelineRow>新装备：助燃器。</TimelineRow>
        <TimelineRow>此时仅加入游戏，飞龙公爵仍被囚禁，装备暂时无法获取。 <a href="https://clashofclans.fandom.com/wiki/Flame_Blower#History" target="_blank" rel="noopener noreferrer">来源</a></TimelineRow>
    </TimelineItem>
    <TimelineItem date="2026/02/22">
        <TimelineRow>飞龙公爵公布时展示助燃器。 <a href="https://clashofclans.fandom.com/wiki/Flame_Blower#History" target="_blank" rel="noopener noreferrer">来源</a></TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>
<p><small>数值核对：2026-10-13 · <a href="https://clashofclans.fandom.com/wiki/Flame_Blower?oldid=624519" target="_blank" rel="noopener noreferrer">部落冲突维基</a>。部分附加字段沿用原记录。</small></p>
