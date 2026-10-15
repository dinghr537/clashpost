---
title: "部落冲突 coc 都城超级电磁炮工坊升级数据"
navTitle: "超级电磁炮工坊"
shownTitle: "超级电磁炮工坊"
description: "闪电反复击中玻璃球，于是就有了这台超级电磁炮。这足以让经过的人毛发悚立。"
module: upgrade-capital
imgFolder: capital_buildings/2350
wiki: https://clashofclans.fandom.com/wiki/Clan_Capital_Barracks#Mega_Sparky_Workshop
canonical: /upgrade/2350-Mega-Sparky-Workshop
dataSyncedOn: 2026-10-13
---

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Mega_Sparky_Workshop4.png" :imgAlt="$frontmatter.navTitle"
    :description="$frontmatter.description"
    :isSmallImg="true" />

<SmallTitle>各等级图片</SmallTitle>

<Panel>
    <UnitImgGroup :folder="$frontmatter.imgFolder">
        <UnitImg imgTitle="废墟" imgSrc="Mega_Sparky_Workshop_Ruin.png" />
        <UnitImg imgTitle="1 级" imgSrc="Mega_Sparky_Workshop1.png" />
        <UnitImg imgTitle="2 级" imgSrc="Mega_Sparky_Workshop2.png" />
        <UnitImg imgTitle="3 级" imgSrc="Mega_Sparky_Workshop3.png" />
        <UnitImg imgTitle="4 级" imgSrc="Mega_Sparky_Workshop4.png" />
    </UnitImgGroup>
</Panel>

<SmallTitle>各子城的建筑数量</SmallTitle>

<DistrictTable>

|             |   1   |   2   |   3   |   4   |   5   |
|     ---     |  ---  |  ---  |  ---  |  ---  |  ---  |
|  哥布林矿井  |   0   |   1   |   1   |   1   |   \   |

</DistrictTable>

<SmallTitle>属性</SmallTitle>

<UnitProperties>
    <UnitProperty pKey="占地面积" pValue="3×3" />
    <UnitProperty pKey="判定面积" pValue="2×2" />
    <UnitProperty pKey="可训练的兵种" pValue="<a href='/upgrade/2010-Mega-Sparky'>超级电磁炮</a>" />
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
| 1 | 1500 | 37500 | 25 | 9 | 2 |
| 2 | 1750 | 75000 | 30 | 9 | 2 |
| 3 | 2000 | 200000 | 35 | 10 | 3 |
| 4 | 2250 | 400000 | 40 | 10 | 4 |
</UnitTable>

<SmallTitle>更新历史</SmallTitle>

<Timeline>
    <TimelineItem date="2023/10/09">
        <TimelineRow>新建筑：超级电磁炮工坊。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>
<p><small>数值核对：2026-10-13 · <a href="https://clashofclans.fandom.com/wiki/Clan_Capital_Barracks?oldid=616742" target="_blank" rel="noopener noreferrer">部落冲突维基</a>。部分附加字段沿用原记录。</small></p>
