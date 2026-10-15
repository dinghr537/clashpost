---
title: "部落冲突 coc 反击卡组升级数据"
navTitle: "反击卡组"
shownTitle: "反击卡组"
englishName: "Revenge Deck"
module: upgrade-home
imgFolder: home_heroes/07e5
wiki: https://clashofclans.fandom.com/wiki/Revenge_Deck
canonical: /upgrade/07e5-Revenge-Deck
dataSyncedOn: 2026-10-13
---

<script setup>
const tableExtraInfo0 = [
    {
        "column": 4,
        "type": "cost",
        "icon": "Shiny_Ore",
        "gpClass": "research",
        "noGoldPass": true
    },
    {
        "column": 5,
        "type": "cost",
        "icon": "Glowy_Ore",
        "gpClass": "research",
        "noGoldPass": true
    },
    {
        "column": 6,
        "type": "cost",
        "icon": "Starry_Ore",
        "gpClass": "research",
        "noGoldPass": true
    }
];
</script>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Revenge_Deck.png" :imgAlt="$frontmatter.navTitle" :isSmallImg="true" />

<SmallTitle>重要说明</SmallTitle>

1. 距离超过25格（来源带问号、尚不确定）的攻击可能不触发反击，例如足够远的天鹰火炮。

<SmallTitle>升级数据</SmallTitle>

<UnitTable :tableExtraInfo="tableExtraInfo0">

| 等级 | 技能<br>每次反击回血 | 技能<br>反击伤害 | 生命值<br>增加 | 升级费用 | 升级费用 | 升级费用 | 所需<br>铁匠铺等级 | 所需<br>大本等级 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 30 | 150 | 900 | \ | \ | \ | 1 | 8 |
| 2 | 30 | 150 | 988 | 120 | \ | \ | 1 | 8 |
| 3 | 32 | 155 | 1077 | 240 | 20 | \ | 1 | 8 |
| 4 | 32 | 155 | 1165 | 400 | \ | \ | 1 | 8 |
| 5 | 32 | 155 | 1254 | 600 | \ | \ | 1 | 8 |
| 6 | 35 | 160 | 1342 | 840 | 100 | \ | 1 | 8 |
| 7 | 35 | 160 | 1431 | 1120 | \ | \ | 1 | 8 |
| 8 | 35 | 160 | 1519 | 1440 | \ | \ | 1 | 8 |
| 9 | 39 | 165 | 1608 | 1800 | 200 | 10 | 1 | 8 |
| 10 | 39 | 165 | 1696 | 1900 | \ | \ | 1 | 8 |
| 11 | 39 | 165 | 1785 | 2000 | \ | \ | 1 | 8 |
| 12 | 43 | 175 | 1873 | 2100 | 400 | 20 | 1 | 8 |
| 13 | 43 | 175 | 1962 | 2200 | \ | \ | 3 | 10 |
| 14 | 43 | 175 | 2050 | 2300 | \ | \ | 3 | 10 |
| 15 | 46 | 185 | 2139 | 2400 | 600 | 30 | 3 | 10 |
| 16 | 46 | 185 | 2227 | 2500 | \ | \ | 5 | 12 |
| 17 | 46 | 185 | 2316 | 2600 | \ | \ | 5 | 12 |
| 18 | 49 | 195 | 2404 | 2700 | 600 | 50 | 5 | 12 |
| 19 | 49 | 195 | 2493 | 2800 | \ | \ | 7 | 14 |
| 20 | 49 | 195 | 2581 | 2900 | \ | \ | 7 | 14 |
| 21 | 52 | 205 | 2670 | 3000 | 600 | 100 | 7 | 14 |
| 22 | 52 | 205 | 2758 | 3100 | \ | \ | 8 | 15 |
| 23 | 52 | 205 | 2847 | 3200 | \ | \ | 8 | 15 |
| 24 | 55 | 215 | 2935 | 3300 | 600 | 120 | 8 | 15 |
| 25 | 55 | 215 | 3024 | 3400 | \ | \ | 9 | 16 |
| 26 | 55 | 215 | 3112 | 3500 | \ | \ | 9 | 16 |
| 27 | 60 | 225 | 3200 | 3600 | 600 | 150 | 9 | 16 |
</UnitTable>

<SmallTitle>属性</SmallTitle>

<UnitProperties>
    <UnitProperty pKey="最大反击范围" pValue="25格" />
    <UnitProperty pKey="反击冷却时间" pValue="0.8秒" />
</UnitProperties>

<SmallTitle>更新历史</SmallTitle>

<Timeline>
    <TimelineItem date="2026/08/12">
        <TimelineRow>反击卡组在神勇奖章活动中开放。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2026/07/14">
        <TimelineRow>调整全部等级的每次反击回血： 1-2级： 38 → 30 3-5级： 41 → 32 6-8级： 45 → 35 9-11级： 49 → 39 12-14级： 53 → 43 15-17级： 56 → 46 18-20级： 60 → 49 21-23级： 64 → 52 24-26级： 68 → 55 27级： 75 → 60 调整3至27级的反击伤害： 3-5级： 165 → 155 6-8级： 180 → 160 9-11级： 195 → 165 12-14级： 210 → 175 15-17级： 225 → 185 18-20级： 240 → 195 21-23级： 255 → 205 24-26级： 270 → 215 27级： 300 → 225 移除反击卡组的被动伤害加成。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2026/06/16">
        <TimelineRow>反击卡组已加入游戏文件。</TimelineRow>
    </TimelineItem>
</Timeline>


<p><small>数值核对：2026-10-13 · <a href="https://clashofclans.fandom.com/wiki/Revenge_Deck?oldid=625660" target="_blank" rel="noopener noreferrer">部落冲突维基</a>。</small></p>
