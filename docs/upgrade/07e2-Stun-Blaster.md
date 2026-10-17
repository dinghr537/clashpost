---
title: "部落冲突 coc 爆震器装备升级数据"
navTitle: "爆震器"
shownTitle: "爆震器"
description: "释放冲击波，对周围的敌人和建筑造成伤害并附带击晕/瘫痪效果。"
module: upgrade-home
imgFolder: home_heroes/07e2
wiki: https://clashofclans.fandom.com/wiki/Stun_Blaster
canonical: /upgrade/07e2-Stun-Blaster
dataSyncedOn: 2026-10-13
---

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Stun_Blaster_info.png" :imgAlt="$frontmatter.navTitle" description="释放冲击波，对周围的敌人和建筑造成伤害并附带击晕/瘫痪效果。" />

<SmallTitle>说明</SmallTitle>

1. 爆震器是 [飞龙公爵](/upgrade/0205-Dragon-Duke) 的一件普通装备。在铁匠铺 9 级时解锁，需要 16 本。
2. 使用时，爆震器创造冲击波，对周边防御部队和建筑造成伤害和击晕效果。
3. 爆震器装备还可以增加飞龙公爵的每秒伤害和生命值。

<SmallTitle>属性</SmallTitle>

<UnitProperties>
    <UnitProperty pKey="技能类型" pValue="主动技能" />
    <UnitProperty pKey="装备稀有度" pValue="普通" />
    <UnitProperty pKey="所需铁匠铺等级" pValue="9" />
    <UnitProperty pKey="所需大本等级" pValue="16" />
    <UnitProperty pKey="伤害和眩晕半径" pValue="8 格" />
    <UnitProperty pKey="眩晕时长" pValue="4.5 秒" />
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
    }
];
</script>

<UnitTable :tableExtraInfo="tableExtraInfo">

| 等级 | 技能伤害 | 晕眩时间 |英雄每秒<br>伤害提升|英雄<br>生命值提升|升级费用|升级费用|所需<br>铁匠铺等级|所需<br>大本等级|
|  --- |   ---   |   ---   |        ---        |         ---    |   ---  | ---   |        ---      |      ---      |
| 1 | 150 | 4.5秒 | 40 | 450 | \ | \ | \ | 16 |
| 2 | 150 | 4.5秒 | 43 | 650 | 120 | \ | 9 | 16 |
| 3 | 200 | 5秒 | 46 | 850 | 240 | 20 | 9 | 16 |
| 4 | 200 | 5秒 | 49 | 1000 | 400 | \ | 9 | 16 |
| 5 | 200 | 5秒 | 52 | 1150 | 600 | \ | 9 | 16 |
| 6 | 250 | 5.5秒 | 55 | 1300 | 940 | 100 | 9 | 16 |
| 7 | 250 | 5.5秒 | 58 | 1450 | 1120 | \ | 9 | 16 |
| 8 | 250 | 5.5秒 | 61 | 1600 | 1440 | \ | 9 | 16 |
| 9 | 300 | 6秒 | 64 | 1750 | 1800 | 200 | 9 | 16 |
| 10 | 300 | 6秒 | 67 | 1900 | 1900 | \ | 9 | 16 |
| 11 | 300 | 6秒 | 70 | 2000 | 2000 | \ | 9 | 16 |
| 12 | 350 | 6.5秒 | 73 | 2100 | 2100 | 400 | 9 | 16 |
| 13 | 350 | 6.5秒 | 76 | 2200 | 2200 | \ | 9 | 16 |
| 14 | 350 | 6.5秒 | 79 | 2275 | 2300 | \ | 9 | 16 |
| 15 | 375 | 7秒 | 82 | 2325 | 2400 | 600 | 9 | 16 |
| 16 | 375 | 7秒 | 85 | 2375 | 2500 | \ | 9 | 16 |
| 17 | 375 | 7秒 | 88 | 2400 | 2600 | \ | 9 | 16 |
| 18 | 400 | 7.5秒 | 90 | 2400 | 2700 | 600 | 9 | 16 |
</UnitTable>

注意：如果升级费用中有多种资源，则同时需要多种资源才能升级。

<SmallTitle>更新历史</SmallTitle>

<Timeline>
    <TimelineItem date="2026/02/27">
        <TimelineRow>公布爆震器的技能机制。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2026/02/23">
        <TimelineRow>新装备：爆震器。</TimelineRow>
        <TimelineRow>此时仅加入游戏，飞龙公爵仍被囚禁，装备暂时无法获取。 <a href="https://clashofclans.fandom.com/wiki/Stun_Blaster#History" target="_blank" rel="noopener noreferrer">来源</a></TimelineRow>
    </TimelineItem>
    <TimelineItem date="2026/02/22">
        <TimelineRow>飞龙公爵公布时展示爆震器。 <a href="https://clashofclans.fandom.com/wiki/Stun_Blaster#History" target="_blank" rel="noopener noreferrer">来源</a></TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>
<p><small>数值核对：2026-10-13 · <a href="https://clashofclans.fandom.com/wiki/Stun_Blaster?oldid=624501" target="_blank" rel="noopener noreferrer">部落冲突维基</a>。部分附加字段沿用原记录。</small></p>
