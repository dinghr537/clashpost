---
title: "部落冲突 coc 都城冰霜法术工厂（霜冻法术工厂）升级数据"
navTitle: "冰霜法术工厂"
shownTitle: "冰霜法术工厂（霜冻法术工厂）"
description: "配制一桶桶冰霜法术。如果要来参观，最好穿暖和点！"
module: upgrade-capital
imgFolder: capital_buildings/2383
wiki: https://clashofclans.fandom.com/wiki/Clan_Capital_Spell_Factories#Frost_Spell_Factory
canonical: /upgrade/2383-Frost-Spell-Factory
dataSyncedOn: 2026-10-13
---

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Frost_Spell_Factory5.png" :imgAlt="$frontmatter.navTitle"
    :description="$frontmatter.description"
    :isSmallImg="true" />

<SmallTitle>各等级图片</SmallTitle>

<Panel>
    <UnitImgGroup :folder="$frontmatter.imgFolder">
        <UnitImg imgTitle="废墟" imgSrc="Spell_Factory_Ruin.png" />
        <UnitImg imgTitle="1 级" imgSrc="Frost_Spell_Factory1.png" />
        <UnitImg imgTitle="2 级" imgSrc="Frost_Spell_Factory2.png" />
        <UnitImg imgTitle="3 级" imgSrc="Frost_Spell_Factory3.png" />
        <UnitImg imgTitle="4 级" imgSrc="Frost_Spell_Factory4.png" />
        <UnitImg imgTitle="5 级" imgSrc="Frost_Spell_Factory5.png" />
    </UnitImgGroup>
</Panel>

<SmallTitle>各子城的建筑数量</SmallTitle>

<DistrictTable>

|             |   1   |   2   |   3   |   4   |   5   |
|     ---     |  ---  |  ---  |  ---  |  ---  |  ---  |
| 建筑工人工坊 |   0   |   0   |   1   |   1   |   1   |

</DistrictTable>

<SmallTitle>属性</SmallTitle>

<UnitProperties>
    <UnitProperty pKey="占地面积" pValue="3×3" />
    <UnitProperty pKey="判定面积" pValue="2×2" />
    <UnitProperty pKey="可配置的法术" pValue="<a href='/upgrade/2103-Frost-Spell'>冰霜法术</a>" />
</UnitProperties>

<SmallTitle>升级数据</SmallTitle>

<script setup>
const tableExtraInfo = [
    {
        "column": 2,
        "type": "cost",
        "icon": "Gold3",
        "noGoldPass": true
    },
    {
        "column": 3,
        "type": "number",
        "icon": "Gold3",
        "noGoldPass": true
    }
];
</script>

<UnitTable :tableExtraInfo="tableExtraInfo">

| 等级 | 生命值 | 升级费用 | 摧毁奖励 |所需都城<br>大本等级|所需子城<br>大本等级|
| ---- |   --- |    ---  |   ---    |        ---       |        ---        |
| 1 | 1000 | 15000 | 25 | 7 | 3 |
| 2 | 1150 | 30000 | 30 | 7 | 3 |
| 3 | 1300 | 60000 | 35 | 7 | 3 |
| 4 | 1450 | 120000 | 40 | 9 | 4 |
| 5 | 1600 | 250000 | 45 | 10 | 5 |
</UnitTable>

<SmallTitle>更新历史</SmallTitle>

<Timeline>
    <TimelineItem date="2022/05/02">
        <TimelineRow>冰霜法术工厂随着部落都城玩法一同推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>
<p><small>数值核对：2026-10-13 · <a href="https://clashofclans.fandom.com/wiki/Clan_Capital_Spell_Factories?oldid=621246" target="_blank" rel="noopener noreferrer">部落冲突维基</a>。部分附加字段沿用原记录。</small></p>
