---
title: "部落冲突 coc 都城高山戈仑石场升级数据"
navTitle: "高山戈仑石场"
shownTitle: "高山戈仑石场"
description: "一个形似戈仑石人的巨坑，希望不是每次训练高山戈仑都要挖一个新坑。"
module: upgrade-capital
imgFolder: capital_buildings/234d
wiki: https://clashofclans.fandom.com/wiki/Clan_Capital_Barracks#Mountain_Golem_Quarry
canonical: /upgrade/234d-Mountain-Golem-Quarry
dataSyncedOn: 2026-10-13
---

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Mountain_Golem_Quarry5.png" :imgAlt="$frontmatter.navTitle"
    :description="$frontmatter.description"
    :isSmallImg="true" />

<SmallTitle>各等级图片</SmallTitle>

<Panel>
    <UnitImgGroup :folder="$frontmatter.imgFolder">
        <UnitImg imgTitle="废墟" imgSrc="Mountain_Golem_Quarry_Ruin.png" />
        <UnitImg imgTitle="1 级" imgSrc="Mountain_Golem_Quarry1.png" />
        <UnitImg imgTitle="2 级" imgSrc="Mountain_Golem_Quarry2.png" />
        <UnitImg imgTitle="3 级" imgSrc="Mountain_Golem_Quarry3.png" />
        <UnitImg imgTitle="4 级" imgSrc="Mountain_Golem_Quarry4.png" />
        <UnitImg imgTitle="5 级" imgSrc="Mountain_Golem_Quarry5.png" />
    </UnitImgGroup>
</Panel>

<SmallTitle>各子城的建筑数量</SmallTitle>

<DistrictTable>

|             |   1   |   2   |   3   |   4   |   5   |
|     ---     |  ---  |  ---  |  ---  |  ---  |  ---  |
|   戈仑石场   |   1   |   1   |   1   |   1   |   1   |

</DistrictTable>

<SmallTitle>属性</SmallTitle>

<UnitProperties>
    <UnitProperty pKey="占地面积" pValue="3×3" />
    <UnitProperty pKey="判定面积" pValue="2×2" />
    <UnitProperty pKey="可训练的兵种" pValue="<a href='/upgrade/200d-Mountain-Golem'>高山戈仑</a>" />
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
| 1 | 1500 | \ | 25 | 7 | 1 |
| 2 | 1750 | 50000 | 30 | 7 | 2 |
| 3 | 2000 | 150000 | 35 | 8 | 3 |
| 4 | 2250 | 300000 | 40 | 9 | 4 |
| 5 | 2500 | 600000 | 45 | 10 | 5 |
</UnitTable>

<SmallTitle>更新历史</SmallTitle>

<Timeline>
    <TimelineItem date="2022/05/02">
        <TimelineRow>高山戈仑石场随着部落都城玩法一同推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>
<p><small>数值核对：2026-10-13 · <a href="https://clashofclans.fandom.com/wiki/Clan_Capital_Barracks?oldid=616742" target="_blank" rel="noopener noreferrer">部落冲突维基</a>。部分附加字段沿用原记录。</small></p>
