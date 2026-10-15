---
title: "部落冲突 coc 夜世界防空火炮升级数据"
navTitle: "防空火炮"
shownTitle: "防空火炮"
description: "发射一连串的小型火箭来驱赶“飞虫”！就像灭虫器一样，但它的造型更加美观。"
module: upgrade-bh
imgFolder: bh_buildings/1104
wiki: https://clashofclans.fandom.com/wiki/Firecrackers
canonical: /upgrade/1104-Firecrackers
dataSyncedOn: 2026-10-13
---

- *如想查看家乡的防空火箭，请访问：[防空火箭](/upgrade/0304-Air-Defense)。*
- *如想查看都城的防空火箭，请访问：[都城防空火箭](/upgrade/2203-Air-Defense)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Firecrackers10.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

<SmallTitle>各等级图片</SmallTitle>

<Panel>
    <UnitImgGroup :folder="$frontmatter.imgFolder">
        <UnitImg imgTitle="1 级" imgSrc="Firecrackers1.png" />
        <UnitImg imgTitle="2 级" imgSrc="Firecrackers2.png" />
        <UnitImg imgTitle="3 级" imgSrc="Firecrackers3.png" />
        <UnitImg imgTitle="4 级" imgSrc="Firecrackers4.png" />
        <UnitImg imgTitle="5 级" imgSrc="Firecrackers5.png" />
        <UnitImg imgTitle="6 级" imgSrc="Firecrackers6.png" />
        <UnitImg imgTitle="7 级" imgSrc="Firecrackers7.png" />
        <UnitImg imgTitle="8 级" imgSrc="Firecrackers8.png" />
        <UnitImg imgTitle="9 级" imgSrc="Firecrackers9.png" />
        <UnitImg imgTitle="10 级" imgSrc="Firecrackers10.png" />
    </UnitImgGroup>
</Panel>

<SmallTitle>建筑数量对照表</SmallTitle>

<BuildingNum>
    <BuildingNumRow title="大本等级" num="1 - 2, 3 - 4, 5 - 6, 7, 8, 9 - 10" />
    <BuildingNumRow title="建筑数量" num="    0,     1,     2, 3, 4,      5" />
</BuildingNum>

<SmallTitle>属性</SmallTitle>

<UnitProperties>
    <UnitProperty pKey="占地面积" pValue="2×2" />
    <UnitProperty pKey="判定面积" pValue="2×2" :isJudgeSquare="true" />
    <UnitProperty pKey="伤害类型" pValue="单体伤害" />
    <UnitProperty pKey="攻击的目标" pValue="仅空中目标" />
    <UnitProperty pKey="射程" pValue="9 格" />
    <UnitProperty pKey="攻速" pValue="约 1 秒/轮*" />
</UnitProperties>

\* 防空火炮的攻击节奏是 0.064 秒一发，4 发后冷却 0.8 秒。

<SmallTitle>升级数据</SmallTitle>

<script setup>
const tableExtraInfo = [
    {
        "column": 4,
        "type": "cost",
        "gpClass": "building",
        "icon": "Gold2"
    },
    {
        "column": 5,
        "type": "time",
        "gpClass": "building"
    },
    {
        "column": 6,
        "type": "exp",
        "icon": "Exp"
    }
];
</script>

<UnitTable :tableExtraInfo="tableExtraInfo">

| 等级 | 每秒伤害 | 每次伤害 | 生命值 | 升级费用 | 升级时间 |升级后可<br>获得的经验|所需夜世界<br>大本等级|
|  --- |   ---   |   ---   |  ---   |   ---   |    ---  |         ---         |         ---        |
| 1 | 59 | 19 | 400 | 40000 | 0,0,15,0 |  | 3 |
| 2 | 65 | 21 | 460 | 80000 | 0,2,0,0 |  | 3 |
| 3 | 71 | 23 | 530 | 120000 | 0,4,0,0 |  | 3 |
| 4 | 78 | 25 | 610 | 300000 | 0,12,0,0 |  | 4 |
| 5 | 84 | 27 | 700 | 800000 | 1,0,0,0 |  | 5 |
| 6 | 93 | 30 | 850 | 1200000 | 2,0,0,0 |  | 6 |
| 7 | 103 | 33 | 1000 | 2000000 | 4,0,0,0 |  | 7 |
| 8 | 112 | 36 | 1150 | 3000000 | 6,0,0,0 |  | 8 |
| 9 | 125 | 40 | 1300 | 4000000 | 8,0,0,0 |  | 9 |
| 10 | 137 | 44 | 1500 | 5000000 | 9,0,0,0 |  | 10 |

</UnitTable>

<SmallTitle>更新历史</SmallTitle>

<Timeline>
    <TimelineItem date="2023/05/15">
        <TimelineRow>夜世界重做，建筑的数值重新平衡，伤害、生命值等数据有变化。</TimelineRow>
        <TimelineRow>6 ~ 9 级防空火炮的升级时间增加。</TimelineRow>
        <TimelineRow>夜世界 10 本推出，防空火炮可升至 10 级。</TimelineRow>
        <TimelineRow>为配合更小的地图，防空火炮的射程由 10 格降低到 9 格。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/06/18">
        <TimelineRow>夜世界 9 本推出，防空火炮可升至 9 级。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>
<p><small>数值核对：2026-10-13 · <a href="https://clashofclans.fandom.com/wiki/Firecrackers?oldid=621755" target="_blank" rel="noopener noreferrer">部落冲突维基</a>。部分附加字段沿用原记录。</small></p>
