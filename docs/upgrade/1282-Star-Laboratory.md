---
title: "部落冲突 coc 夜世界星空实验室升级数据"
navTitle: "星空实验室"
shownTitle: "星空实验室"
description: "星空实验室通过探索宇宙的奥秘来发掘兵种的全部潜能。可以提升兵种的生命值和伤害、减少兵种所需空间，还可以增强兵种的特殊技能！"
module: upgrade-bh
imgFolder: bh_buildings/1282
wiki: https://clashofclans.fandom.com/wiki/Star_Laboratory
canonical: /upgrade/1282-Star-Laboratory
dataSyncedOn: 2026-10-13
---

- 如想查看家乡的实验室，请访问：[实验室](/upgrade/0483-Laboratory)。

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Star_Laboratory10.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

<SmallTitle>各等级图片</SmallTitle>

<Panel>
    <UnitImgGroup :folder="$frontmatter.imgFolder">
        <UnitImg imgTitle="废墟" imgSrc="Star_Laboratory_Ruin.png"/>
        <UnitImg imgTitle="1 级" imgSrc="Star_Laboratory1.png"/>
        <UnitImg imgTitle="2 级" imgSrc="Star_Laboratory2.png"/>
        <UnitImg imgTitle="3 级" imgSrc="Star_Laboratory3.png"/>
        <UnitImg imgTitle="4 级" imgSrc="Star_Laboratory4.png"/>
        <UnitImg imgTitle="5 级" imgSrc="Star_Laboratory5.png"/>
        <UnitImg imgTitle="6 级" imgSrc="Star_Laboratory6.png"/>
        <UnitImg imgTitle="7 级" imgSrc="Star_Laboratory7.png"/>
        <UnitImg imgTitle="8 级" imgSrc="Star_Laboratory8.png"/>
        <UnitImg imgTitle="9 级" imgSrc="Star_Laboratory9.png"/>
        <UnitImg imgTitle="10 级" imgSrc="Star_Laboratory10.png"/>
    </UnitImgGroup>
</Panel>

<SmallTitle>建筑数量对照表</SmallTitle>

<BuildingNum>
    <BuildingNumRow title="大本等级" num="1 - 5, 6 - 10" />
    <BuildingNumRow title="合计" num="1, 1" />
    <BuildingNumRow title="第一区域的建筑数量上限" num="\, 1" />
    <BuildingNumRow title="第二区域的建筑数量上限" num="\, 0" />
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
        "column": 2,
        "type": "cost",
        "gpClass": "building",
        "icon": "Elixir2"
    },
    {
        "column": 3,
        "type": "time",
        "gpClass": "building"
    },
    {
        "column": 4,
        "type": "exp",
        "icon": "Exp"
    }
];
</script>

<UnitTable :tableExtraInfo="tableExtraInfo">

| 等级 |  生命值 | 升级费用 | 升级时间 | 升级后可<br>获得的经验| 所需夜世界<br>大本营等级 |
|  --- |   ---  |    ---  |   ---   |         ---          |          ---           |
| 1 | 650 | 1000 | \ |  | 2 |
| 2 | 800 | 15000 | 0,0,10,0 |  | 2 |
| 3 | 975 | 50000 | 0,0,30,0 |  | 3 |
| 4 | 1150 | 300000 | 0,8,0,0 |  | 4 |
| 5 | 1350 | 700000 | 0,12,0,0 |  | 5 |
| 6 | 1600 | 1000000 | 2,0,0,0 |  | 6 |
| 7 | 1850 | 2000000 | 4,0,0,0 |  | 7 |
| 8 | 2150 | 3000000 | 6,0,0,0 |  | 8 |
| 9 | 2450 | 4000000 | 8,0,0,0 |  | 9 |
| 10 | 2750 | 5000000 | 10,0,0,0 |  | 10 |
</UnitTable>

<SmallTitle>更新历史</SmallTitle>

<Timeline>
    <TimelineItem date="2023/05/15">
        <TimelineRow>夜世界重做，建筑的数值重新平衡，伤害、生命值等数据有变化。</TimelineRow>
        <TimelineRow>6 ~ 9 级星空实验室的升级费用增加。</TimelineRow>
        <TimelineRow>夜世界 10 本推出，星空实验室可升至 10 级。</TimelineRow>
    </TimelineItem>
     <TimelineItem date="2019/06/18">
        <TimelineRow>夜世界 9 本推出，星空实验室可升至 9 级。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>
<p><small>数值核对：2026-10-13 · <a href="https://clashofclans.fandom.com/wiki/Star_Laboratory?oldid=620172" target="_blank" rel="noopener noreferrer">部落冲突维基</a>。部分附加字段沿用原记录。</small></p>
