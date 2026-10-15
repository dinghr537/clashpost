---
title: "部落冲突 coc 都城骷髅召唤法术工厂升级数据"
navTitle: "骷髅召唤法术工厂"
shownTitle: "骷髅召唤法术工厂"
description: "配制一桶桶骷髅召唤法术。是不是会有骨头咔嗒作响，你就当没听到吧。"
module: upgrade-capital
imgFolder: capital_buildings/2385
wiki: https://clashofclans.fandom.com/wiki/Clan_Capital_Spell_Factories#Graveyard_Spell_Factory
canonical: /upgrade/2385-Graveyard-Spell-Factory
dataSyncedOn: 2026-10-13
---

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Graveyard_Spell_Factory4.png" :imgAlt="$frontmatter.navTitle"
    :description="$frontmatter.description"
    :isSmallImg="true" />

<SmallTitle>各等级图片</SmallTitle>

<Panel>
    <UnitImgGroup :folder="$frontmatter.imgFolder">
        <UnitImg imgTitle="废墟" imgSrc="Spell_Factory_Ruin.png" />
        <UnitImg imgTitle="1 级" imgSrc="Graveyard_Spell_Factory1.png" />
        <UnitImg imgTitle="2 级" imgSrc="Graveyard_Spell_Factory2.png" />
        <UnitImg imgTitle="3 级" imgSrc="Graveyard_Spell_Factory3.png" />
        <UnitImg imgTitle="4 级" imgSrc="Graveyard_Spell_Factory4.png" />
    </UnitImgGroup>
</Panel>

<SmallTitle>各子城的建筑数量</SmallTitle>

<DistrictTable>

|             |   1   |   2   |   3   |   4   |   5   |
|     ---     |  ---  |  ---  |  ---  |  ---  |  ---  |
|   骷髅公园   |   0   |   1   |   1   |   1   |   \   |

</DistrictTable>

<SmallTitle>属性</SmallTitle>

<UnitProperties>
    <UnitProperty pKey="占地面积" pValue="3×3" />
    <UnitProperty pKey="判定面积" pValue="2×2" />
    <UnitProperty pKey="可配置的法术" pValue="<a href='/upgrade/2105-Graveyard-Spell'>骷髅召唤法术</a>" />
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
| ---- |   --- |   ---   |   ---    |        ---       |        ---        |
| 1 | 1000 | 20000 | 25 | 8 | 2 |
| 2 | 1150 | 40000 | 30 | 8 | 2 |
| 3 | 1300 | 75000 | 35 | 9 | 3 |
| 4 | 1450 | 150000 | 40 | 10 | 4 |
</UnitTable>

<SmallTitle>更新历史</SmallTitle>

<Timeline>
    <TimelineItem date="2022/12/12">
        <TimelineRow>新建筑：骷髅召唤法术工厂。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>
<p><small>数值核对：2026-10-13 · <a href="https://clashofclans.fandom.com/wiki/Clan_Capital_Spell_Factories?oldid=621246" target="_blank" rel="noopener noreferrer">部落冲突维基</a>。部分附加字段沿用原记录。</small></p>
