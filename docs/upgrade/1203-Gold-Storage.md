---
title: "部落冲突 coc 夜世界储金罐升级数据"
navTitle: "储金罐"
shownTitle: "储金罐"
description: "您珍贵的金币都存在这里！不要让狡猾的哥布林有机可乘！升级储金罐，提高它们的容量和抗打击能力。"
module: upgrade-bh
imgFolder: bh_buildings/1203
wiki: https://clashofclans.fandom.com/wiki/Gold_Storage/Builder_Base
canonical: /upgrade/1203-Gold-Storage
dataSyncedOn: 2026-10-13
---

- *如想查看家乡的储金罐，请访问：[储金罐](/upgrade/0404-Gold-Storage)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Gold_Storage10.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

<SmallTitle>各等级图片</SmallTitle>

<Panel>
    <UnitImgGroup :folder="$frontmatter.imgFolder">
        <UnitImg imgTitle="1 级" imgSrc="Gold_Storage1.png"/>
        <UnitImg imgTitle="2 级" imgSrc="Gold_Storage2.png"/>
        <UnitImg imgTitle="3 级" imgSrc="Gold_Storage3.png"/>
        <UnitImg imgTitle="4 级" imgSrc="Gold_Storage4.png"/>
        <UnitImg imgTitle="5 级" imgSrc="Gold_Storage5.png"/>
        <UnitImg imgTitle="6 级" imgSrc="Gold_Storage6.png"/>
        <UnitImg imgTitle="7 级" imgSrc="Gold_Storage7.png"/>
        <UnitImg imgTitle="8 级" imgSrc="Gold_Storage8.png"/>
        <UnitImg imgTitle="9 级" imgSrc="Gold_Storage9.png"/>
        <UnitImg imgTitle="10 级" imgSrc="Gold_Storage10.png"/>
            <UnitImg imgTitle="10 级" imgSrc="Gold_Storage10B.png" />
</UnitImgGroup>
</Panel>

<SmallTitle>建筑数量对照表</SmallTitle>

<BuildingNum>
    <BuildingNumRow title="大本等级" num="1 - 5, 6 - 10" />
    <BuildingNumRow title="合计" num="1, 2" />
    <BuildingNumRow title="第一区域的建筑数量上限" num="\, 1" />
    <BuildingNumRow title="第二区域的建筑数量上限" num="\, 1" />
</BuildingNum>

<SmallTitle>属性</SmallTitle>

<UnitProperties>
    <UnitProperty pKey="占地面积" pValue="3×3" />
    <UnitProperty pKey="判定面积" pValue="2×2" :isJudgeSquare="true" />
</UnitProperties>

<SmallTitle>升级数据</SmallTitle>

<script setup>
const tableExtraInfo = [
    {
        "column": 1,
        "type": "number",
        "icon": "Gold2",
        "noGoldPass": true
    },
    {
        "column": 3,
        "type": "cost",
        "gpClass": "building",
        "icon": "Elixir2"
    },
    {
        "column": 4,
        "type": "time",
        "gpClass": "building"
    },
    {
        "column": 5,
        "type": "exp",
        "icon": "Exp"
    }
];
</script>

<UnitTable :tableExtraInfo="tableExtraInfo">

| 等级 | 最大储量 | 生命值 | 升级费用 | 升级时间 | 升级后可<br>获得的经验 | 所需夜世界<br>大本营等级 |
|  --- |   ---   |   ---  |    ---  |   ---   |         ---         |         ---          |
| 1 | 70000 | 650 | 20000 | 0,0,30,0 |  | 3 |
| 2 | 150000 | 800 | 80000 | 0,1,0,0 |  | 3 |
| 3 | 250000 | 975 | 200000 | 0,3,0,0 |  | 3 |
| 4 | 350000 | 1150 | 300000 | 0,6,0,0 |  | 4 |
| 5 | 600000 | 1350 | 600000 | 0,12,0,0 |  | 5 |
| 6 | 800000 | 1600 | 1000000 | 1,0,0,0 |  | 6 |
| 7 | 1200000 | 1850 | 1500000 | 2,0,0,0 |  | 7 |
| 8 | 1600000 | 2150 | 2000000 | 3,0,0,0 |  | 8 |
| 9 | 2000000 | 2450 | 2500000 | 4,0,0,0 |  | 9 |
| 10 | 2500000 | 2750 | 3200000 | 5,0,0,0 |  | 10 |
</UnitTable>

<SmallTitle>更新历史</SmallTitle>

<Timeline>
    <TimelineItem date="2023/05/15">
        <TimelineRow>夜世界重做，建筑的数值重新平衡，伤害、生命值等数据有变化。</TimelineRow>
        <TimelineRow>5 ~ 9 级储金罐的升级费用增加。</TimelineRow>
        <TimelineRow>夜世界 10 本推出，储金罐可升至 10 级。</TimelineRow>
    </TimelineItem>
     <TimelineItem date="2019/06/18">
        <TimelineRow>夜世界 9 本推出，储金罐可升至 9 级。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>
<p><small>数值核对：2026-10-13 · <a href="https://clashofclans.fandom.com/wiki/Gold_Storage/Builder_Base?oldid=608985" target="_blank" rel="noopener noreferrer">部落冲突维基</a>。部分附加字段沿用原记录。</small></p>
