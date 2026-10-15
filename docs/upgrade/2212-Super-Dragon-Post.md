---
title: "部落冲突 coc 都城超级飞龙岗哨升级数据"
navTitle: "超级飞龙岗哨"
shownTitle: "超级飞龙岗哨"
description: "超级飞龙领地意识极强，任何来犯之敌都逃不过它们的龙息炙烤。"
module: upgrade-capital
imgFolder: capital_buildings/2212
wiki: https://clashofclans.fandom.com/wiki/Super_Dragon_Post
canonical: /upgrade/2212-Super-Dragon-Post
dataSyncedOn: 2026-10-13
---

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Super_Dragon_Post4.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

<SmallTitle>各等级图片</SmallTitle>

<Panel>
    <UnitImgGroup :folder="$frontmatter.imgFolder">
        <UnitImg imgTitle="废墟" imgSrc="Guard_Post_Ruin.png" />
        <UnitImg imgTitle="1 级" imgSrc="Super_Dragon_Post1.png" />
        <UnitImg imgTitle="2 级" imgSrc="Super_Dragon_Post2.png" />
        <UnitImg imgTitle="3 级" imgSrc="Super_Dragon_Post3.png" />
        <UnitImg imgTitle="4 - 5 级" imgSrc="Super_Dragon_Post4.png" />
    </UnitImgGroup>
</Panel>

<SmallTitle>建筑数量对照表</SmallTitle>

<BuildingNum>
    <BuildingNumRow title="大本等级" num="1 - 9, 10" />
    <BuildingNumRow title="建筑数量" num="0, 1" />
</BuildingNum>

<SmallTitle>各子城的建筑数量</SmallTitle>

<DistrictTable>

|             |   1   |   2   |   3   |   4   |   5   |
|     ---     |  ---  |  ---  |  ---  |  ---  |  ---  |
|   飞龙悬崖   |   2   |   3   |   4   |   5   |   6   |

</DistrictTable>

<SmallTitle>属性</SmallTitle>

<UnitProperties>
    <UnitProperty pKey="占地面积" pValue="3×3" />
    <UnitProperty pKey="判定面积" pValue="2×2" :isJudgeSquare="true" />
    <UnitProperty pKey="守家兵种" pValue="<a href='/upgrade/200c-Super-Dragon'>超级飞龙</a>" />
    <UnitProperty pKey="兵种数量" pValue="1" />
</UnitProperties>

<SmallTitle>升级数据</SmallTitle>

<script setup>
const tableExtraInfo = [
    {
        "column": 3,
        "type": "cost",
        "icon": "Gold3",
        "noGoldPass": true
    },
    {
        "column": 4,
        "type": "number",
        "icon": "Gold3",
        "noGoldPass": true
    }
];
</script>

<UnitTable :tableExtraInfo="tableExtraInfo">

| 等级 | 兵种等级 | 建筑生命值 | 升级费用 | 摧毁奖励 | 所需都城<br>大本等级 | 所需子城<br>大本等级 |
| ---- |   ---   |    ---    |   ---   |    ---   |         ---         |         ---        |
| 1 | 1 | 800 | 12000 | 320 | 10 | 1 |
| 2 | 2 | 920 | 24000 | 380 | 10 | 2 |
| 3 | 3 | 1065 | 48000 | 440 | 10 | 3 |
| 4 | 4 | 1225 | 75000 | 500 | 10 | 4 |
| 5 | 5 | 1400 | 125000 | 560 | 10 | 5 |
</UnitTable>

<SmallTitle>更新历史</SmallTitle>

<Timeline>
    <TimelineItem date="2022/05/02">
        <TimelineRow>超级飞龙岗哨随着部落都城玩法一同推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>
<p><small>数值核对：2026-10-13 · <a href="https://clashofclans.fandom.com/wiki/Super_Dragon_Post?oldid=609246" target="_blank" rel="noopener noreferrer">部落冲突维基</a>。部分附加字段沿用原记录。</small></p>
