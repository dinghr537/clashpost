---
title: "部落冲突 coc 夜世界治疗小屋升级数据"
navTitle: "治疗小屋"
shownTitle: "治疗小屋"
description: "按照建筑大师祖母的秘方，熬制一大锅丰盛又美味的汤。在进攻下一区域前，部队喝些汤可恢复部分生命值。"
module: upgrade-bh
imgFolder: bh_buildings/1286
wiki: https://clashofclans.fandom.com/wiki/Healing_Hut
canonical: /upgrade/1286-Healing-Hut
dataSyncedOn: 2026-10-13
---

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Healing_Hut6.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

<SmallTitle>各等级图片</SmallTitle>

<Panel>
    <UnitImgGroup :folder="$frontmatter.imgFolder">
        <UnitImg imgTitle="1 级" imgSrc="Healing_Hut1.png"/>
        <UnitImg imgTitle="2 级" imgSrc="Healing_Hut2.png"/>
        <UnitImg imgTitle="3 级" imgSrc="Healing_Hut3.png"/>
        <UnitImg imgTitle="4 级" imgSrc="Healing_Hut4.png"/>
        <UnitImg imgTitle="5 级" imgSrc="Healing_Hut5.png"/>
        <UnitImg imgTitle="6 级" imgSrc="Healing_Hut6.png"/>
    </UnitImgGroup>
</Panel>

<SmallTitle>建筑数量对照表</SmallTitle>

<BuildingNum>
    <BuildingNumRow title="大本等级" num="1 - 5, 6 - 10" />
    <BuildingNumRow title="合计" num="0, 1" />
    <BuildingNumRow title="第一区域的建筑数量上限" num="\, 0" />
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

| 等级 | 血量恢复比例 | 生命值 | 升级费用 | 升级时间 | 升级后可<br>获得的经验 | 所需夜世界<br>大本营等级 |
|  --- |     ---    |   ---  |    ---  |   ---   |          ---          |          ---           |
| 1 | 4% | 600 | 1500000 | 1,6,0,0 |  | 6 |
| 2 | 8% | 690 | 2000000 | 2,0,0,0 |  | 6 |
| 3 | 12% | 800 | 2500000 | 3,0,0,0 |  | 7 |
| 4 | 16% | 910 | 3250000 | 4,0,0,0 |  | 8 |
| 5 | 20% | 1050 | 4000000 | 5,0,0,0 |  | 9 |
| 6 | 24% | 1250 | 5000000 | 6,0,0,0 |  | 10 |
</UnitTable>

<SmallTitle>更新历史</SmallTitle>

<Timeline>
    <TimelineItem date="2023/05/15">
        <TimelineRow>夜世界重做，现在 6 本可解锁新建筑：治疗小屋。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>
<p><small>数值核对：2026-10-13 · <a href="https://clashofclans.fandom.com/wiki/Healing_Hut?oldid=623215" target="_blank" rel="noopener noreferrer">部落冲突维基</a>。部分附加字段沿用原记录。</small></p>
