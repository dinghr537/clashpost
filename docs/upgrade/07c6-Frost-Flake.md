---
title: "部落冲突 coc 冷冽冰晶装备升级数据"
navTitle: "冷冽冰晶"
shownTitle: "冷冽冰晶"
description: "冷冽冰晶是飞盾战神的第三件史诗装备，它在 2025 年 12 月的熔岩危机活动中首次开放购买。当飞盾战神装备冷冽冰晶时，开启技能时，能攻击距离飞盾战神最近的建筑并冻结它们几秒。除此之外，冷冽冰晶还可以提升飞盾战神的生命值。"
module: upgrade-home
imgFolder: home_heroes/07c6
wiki: https://clashofclans.fandom.com/wiki/Frost_Flake
canonical: /upgrade/07c6-Frost-Flake
dataSyncedOn: 2026-10-13
---

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Frost_Flake_info.png" :imgAlt="$frontmatter.navTitle" description="向距离最近的防御建筑投掷冰晶，将其冻住。" :isSmallImg="true" />

<SmallTitle>说明</SmallTitle>

1. 冷冽冰晶是 [飞盾战神](/upgrade/0203-Royal-Champion) 的第三件史诗装备，它在 2025 年 12 月的熔岩危机活动中首次开放购买。
2. 开启技能时，冷冽冰晶能同时发射一定数量的冰晶，攻击距离飞盾战神最近的建筑，造成少量伤害并冻结几秒。
3. 除此之外，冷冽冰晶还可以提升飞盾战神的生命值。

<SmallTitle>属性</SmallTitle>

<UnitProperties>
    <UnitProperty pKey="技能类型" pValue="主动技能" />
    <UnitProperty pKey="装备稀有度" pValue="史诗" />
    <UnitProperty pKey="减速比例" pValue="100%" />
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

| 等级 |冰晶伤害|减速<br>持续时间|目标数量|英雄<br>生命值增加|升级费用|升级费用|升级费用|所需<br>铁匠铺等级|所需<br>大本等级|
| ---- |  ---  |      ---      |  ---  |       ---       |  ---  |  ---  |   ---  |       ---      |       ---      |
| 1 | 105 | 5.2秒 | 4 | 50 | \ | \ | \ | 1 | 8 |
| 2 | 105 | 5.2秒 | 4 | 75 | 120 | \ | \ | 1 | 8 |
| 3 | 126 | 5.4秒 | 4 | 100 | 240 | 20 | \ | 1 | 8 |
| 4 | 126 | 5.4秒 | 4 | 125 | 400 | \ | \ | 1 | 8 |
| 5 | 126 | 5.4秒 | 4 | 150 | 600 | \ | \ | 1 | 8 |
| 6 | 147 | 5.6秒 | 4 | 175 | 840 | 100 | \ | 1 | 8 |
| 7 | 147 | 5.6秒 | 4 | 200 | 1120 | \ | \ | 1 | 8 |
| 8 | 147 | 5.6秒 | 4 | 225 | 1440 | \ | \ | 1 | 8 |
| 9 | 168 | 5.8秒 | 5 | 250 | 1800 | 200 | 10 | 1 | 8 |
| 10 | 168 | 5.8秒 | 5 | 275 | 1900 | \ | \ | 1 | 8 |
| 11 | 168 | 5.8秒 | 5 | 300 | 2000 | \ | \ | 1 | 8 |
| 12 | 189 | 6秒 | 5 | 325 | 2100 | 400 | 20 | 1 | 8 |
| 13 | 189 | 6秒 | 5 | 350 | 2200 | \ | \ | 3 | 10 |
| 14 | 189 | 6秒 | 5 | 375 | 2300 | \ | \ | 3 | 10 |
| 15 | 210 | 6.2秒 | 5 | 400 | 2400 | 600 | 30 | 3 | 10 |
| 16 | 210 | 6.2 | 5 | 425 | 2500 | \ | \ | 5 | 12 |
| 17 | 210 | 6.2秒 | 5 | 450 | 2600 | \ | \ | 5 | 12 |
| 18 | 231 | 6.4秒 | 6 | 475 | 2700 | 600 | 50 | 5 | 12 |
| 19 | 231 | 6.4秒 | 6 | 500 | 2800 | \ | \ | 7 | 14 |
| 20 | 231 | 6.4秒 | 6 | 525 | 2900 | \ | \ | 7 | 14 |
| 21 | 252 | 6.6秒 | 6 | 550 | 3000 | 600 | 100 | 7 | 14 |
| 22 | 252 | 6.6秒 | 6 | 575 | 3100 | \ | \ | 8 | 15 |
| 23 | 252 | 6.6秒 | 6 | 600 | 3200 | \ | \ | 8 | 15 |
| 24 | 273 | 6.8秒 | 6 | 625 | 3300 | 600 | 120 | 8 | 15 |
| 25 | 273 | 6.8秒 | 6 | 650 | 3400 | \ | \ | 9 | 16 |
| 26 | 273 | 6.8秒 | 6 | 675 | 3500 | \ | \ | 9 | 16 |
| 27 | 294 | 7秒 | 7 | 700 | 3600 | 600 | 150 | 9 | 16 |
</UnitTable>

注意：如果升级费用中有多种资源，则同时需要多种资源才能升级。

<SmallTitle>推出记录</SmallTitle>

<UnitTable>

| 推出时间 | 活动名称  |     价格       | 购买渠道 |
|   ---   |    ---    |      ---      |    ---   |
| 2025/12 |  熔岩危机  | 3 100 火苗奖章 |   商人   |
</UnitTable>

<SmallTitle>更新历史</SmallTitle>

<Timeline>
    <TimelineItem date="2025/12/08">
        <TimelineRow>新装备：冷冽冰晶。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>
<p><small>数值核对：2026-10-13 · <a href="https://clashofclans.fandom.com/wiki/Frost_Flake?oldid=621307" target="_blank" rel="noopener noreferrer">部落冲突维基</a>。部分附加字段沿用原记录。</small></p>
