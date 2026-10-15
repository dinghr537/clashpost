---
title: "部落冲突 coc 皇家宝石装备升级数据"
navTitle: "皇家宝石"
shownTitle: "皇家宝石"
description: "皇家宝石是飞盾战神的两件初始装备之一。皇家宝石可以使飞盾战神在使用技能时恢复大量生命值，这个属性可以与英雄本身的回血属性叠加。另外，皇家宝石可以增加飞盾战神的每秒伤害和生命值。"
module: upgrade-home
imgFolder: home_heroes/07c1
wiki: https://clashofclans.fandom.com/wiki/Royal_Gem
canonical: /upgrade/07c1-Royal-Gem
dataSyncedOn: 2026-10-13
---

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Royal_Gem_info.png" :imgAlt="$frontmatter.navTitle" description="为飞盾战神提供大量额外治疗。" />

<SmallTitle>说明</SmallTitle>

1. 皇家宝石是 [飞盾战神](/upgrade/0203-Royal-Champion) 的两件初始装备之一，另一件是 [寻踪飞盾](/upgrade/07c0-Seeking-Shield)。
2. 皇家宝石可以使飞盾战神在使用技能时恢复大量生命值，这个属性可以与英雄本身的回血属性叠加。
3. 另外，皇家宝石可以增加飞盾战神日常状态下的每秒伤害和生命值。

<SmallTitle>属性</SmallTitle>

<UnitProperties>
    <UnitProperty pKey="技能类型" pValue="主动技能" />
    <UnitProperty pKey="装备稀有度" pValue="普通" />
    <UnitProperty pKey="解锁条件" pValue="有飞盾战神即可" />
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

| 等级 |使用技能时的<br>回血属性加成|英雄每秒<br>伤害增加|英雄生命值<br>增加| 升级费用|升级费用|所需<br>铁匠铺等级|所需<br>大本等级|
| ---- |           ---           |        ---        |        ---      |   ---  |  ---  |       ---       |       ---     |
| 1 | 1200 | 35 | 60 | \ | \ | 1 | 13 |
| 2 | 1200 | 40 | 90 | 120 | \ | 1 | 8 |
| 3 | 1450 | 45 | 120 | 240 | 20 | 1 | 8 |
| 4 | 1450 | 50 | 150 | 400 | \ | 1 | 8 |
| 5 | 1450 | 55 | 180 | 600 | \ | 1 | 8 |
| 6 | 1600 | 60 | 210 | 840 | 100 | 1 | 8 |
| 7 | 1600 | 65 | 240 | 1120 | \ | 1 | 8 |
| 8 | 1600 | 70 | 270 | 1440 | \ | 1 | 8 |
| 9 | 1800 | 75 | 300 | 1800 | 200 | 1 | 8 |
| 10 | 1800 | 80 | 330 | 1900 | \ | 3 | 10 |
| 11 | 1800 | 85 | 360 | 2000 | \ | 3 | 10 |
| 12 | 2000 | 90 | 390 | 2100 | 400 | 3 | 10 |
| 13 | 2000 | 95 | 420 | 2200 | \ | 5 | 12 |
| 14 | 2000 | 100 | 450 | 2300 | \ | 5 | 12 |
| 15 | 2200 | 105 | 480 | 2400 | 600 | 5 | 12 |
| 16 | 2200 | 110 | 510 | 2500 | \ | 7 | 14 |
| 17 | 2200 | 115 | 540 | 2600 | \ | 7 | 14 |
| 18 | 2400 | 120 | 570 | 2700 | 600 | 7 | 14 |
</UnitTable>

注意：

1. 如果升级费用中有多种资源，则同时需要多种资源才能升级。<br>
2. 如果玩家升级到了 13 本并解锁了飞盾战神，即使玩家没有马上升 [铁匠铺](/upgrade/0488-Blacksmith) 也可以升级皇家宝石装备。

<SmallTitle>装备的初始等级</SmallTitle>

在 2023 年 12 月装备系统发布时，已解锁飞盾战神的玩家会有一个初始的装备等级，并且不需要解锁铁匠铺。装备等级与玩家的英雄等级相关，具体如下表。

<Table maxWidth="25rem">

| 飞盾战神等级 | 皇家宝石等级 |
|     ---     |     ---     |
|    1 - 2    |      1      |
|      3      |      2      |
|      4      |      3      |
|      5      |      4      |
|    6 - 7    |      5      |
|    8 - 9    |      6      |
|   10 - 11   |      7      |
|   12 - 14   |      8      |
|   15 - 17   |      9      |
|     18      |     10      |
|     19      |     11      |
|   20 - 24   |     12      |
|   25 - 26   |     13      |
|   27 - 29   |     14      |
|   30 - 40   |     15      |
</Table>

<SmallTitle>更新历史</SmallTitle>

<Timeline>
    <TimelineItem date="2023/12/12">
        <TimelineRow>游戏新增装备系统，皇家宝石是第一批推出的装备。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>
<p><small>数值核对：2026-10-13 · <a href="https://clashofclans.fandom.com/wiki/Royal_Gem?oldid=621038" target="_blank" rel="noopener noreferrer">部落冲突维基</a>。部分附加字段沿用原记录。</small></p>
