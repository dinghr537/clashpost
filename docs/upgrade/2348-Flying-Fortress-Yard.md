---
title: "部落冲突 coc 都城飞行堡垒工坊（空中堡垒工坊）升级数据"
navTitle: "飞行堡垒工坊"
shownTitle: "飞行堡垒工坊（空中堡垒工坊）"
description: "制造飞行堡垒的地方，之所以建在高山上，也许是因为建筑工人怕它飞不起来。"
module: upgrade-capital
imgFolder: capital_buildings/2348
wiki: https://clashofclans.fandom.com/wiki/Clan_Capital_Barracks#Flying_Fortress_Yard
canonical: /upgrade/2348-Flying-Fortress-Yard
dataSyncedOn: 2026-10-13
---

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Flying_Fortress_Yard5.png" :imgAlt="$frontmatter.navTitle"
    :description="$frontmatter.description"
    :isSmallImg="true" />

<SmallTitle>各等级图片</SmallTitle>

<Panel>
    <UnitImgGroup :folder="$frontmatter.imgFolder">
        <UnitImg imgTitle="废墟" imgSrc="Flying_Fortress_Yard_Ruin.png" />
        <UnitImg imgTitle="1 级" imgSrc="Flying_Fortress_Yard1.png" />
        <UnitImg imgTitle="2 级" imgSrc="Flying_Fortress_Yard2.png" />
        <UnitImg imgTitle="3 级" imgSrc="Flying_Fortress_Yard3.png" />
        <UnitImg imgTitle="4 级" imgSrc="Flying_Fortress_Yard4.png" />
        <UnitImg imgTitle="5 级" imgSrc="Flying_Fortress_Yard5.png" />
    </UnitImgGroup>
</Panel>

<SmallTitle>各子城的建筑数量</SmallTitle>

<DistrictTable>

|             |   1   |   2   |   3   |   4   |   5   |
|     ---     |  ---  |  ---  |  ---  |  ---  |  ---  |
|   气球环礁   |   0   |   1   |   1   |   1   |   1   |

</DistrictTable>

<SmallTitle>属性</SmallTitle>

<UnitProperties>
    <UnitProperty pKey="占地面积" pValue="3×3" />
    <UnitProperty pKey="判定面积" pValue="2×2" />
    <UnitProperty pKey="可训练的兵种" pValue="<a href='/upgrade/2008-Flying-Fortress'>空中堡垒</a>" />
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
| 1 | 1500 | 25000 | 25 | 5 | 2 |
| 2 | 1750 | 50000 | 30 | 5 | 2 |
| 3 | 2000 | 150000 | 35 | 7 | 3 |
| 4 | 2250 | 300000 | 40 | 8 | 4 |
| 5 | 2500 | 600000 | 45 | 10 | 5 |
</UnitTable>

<SmallTitle>更新历史</SmallTitle>

<Timeline>
    <TimelineItem date="2022/05/02">
        <TimelineRow>飞行堡垒工坊（空中堡垒工坊）随着部落都城玩法一同推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>
<p><small>数值核对：2026-10-13 · <a href="https://clashofclans.fandom.com/wiki/Clan_Capital_Barracks?oldid=616742" target="_blank" rel="noopener noreferrer">部落冲突维基</a>。部分附加字段沿用原记录。</small></p>
