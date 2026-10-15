---
title: "部落冲突 coc 夜世界熔岩火炮升级数据"
navTitle: "熔岩火炮"
shownTitle: "熔岩火炮"
description: "用滚烫的岩浆给敌军洗个澡！地面部队和空中部队都将会感受到这个灼热！"
module: upgrade-bh
imgFolder: bh_buildings/1109
wiki: https://clashofclans.fandom.com/wiki/Roaster
canonical: /upgrade/1109-Roaster
dataSyncedOn: 2026-10-13
---

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Roaster10.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

<SmallTitle>各等级图片</SmallTitle>

<Panel>
    <UnitImgGroup :folder="$frontmatter.imgFolder">
        <UnitImg imgTitle="1 级" imgSrc="Roaster1.png" />
        <UnitImg imgTitle="2 级" imgSrc="Roaster2.png" />
        <UnitImg imgTitle="3 级" imgSrc="Roaster3.png" />
        <UnitImg imgTitle="4 级" imgSrc="Roaster4.png" />
        <UnitImg imgTitle="5 级" imgSrc="Roaster5.png" />
        <UnitImg imgTitle="6 级" imgSrc="Roaster6.png" />
        <UnitImg imgTitle="7 级" imgSrc="Roaster7.png" />
        <UnitImg imgTitle="8 级" imgSrc="Roaster8.png" />
        <UnitImg imgTitle="9 级" imgSrc="Roaster9.png" />
        <UnitImg imgTitle="10 级" imgSrc="Roaster10.png" />
    </UnitImgGroup>
</Panel>

<SmallTitle>建筑数量对照表</SmallTitle>

<BuildingNum>
    <BuildingNumRow title="大本等级" num="1 - 5, 6 - 10" />
    <BuildingNumRow title="建筑数量" num="    0,      1" />
</BuildingNum>

<SmallTitle>属性</SmallTitle>

<UnitProperties>
    <UnitProperty pKey="占地面积" pValue="3×3" />
    <UnitProperty pKey="判定面积" pValue="2×2" :isJudgeSquare="true" />
    <UnitProperty pKey="伤害类型" pValue="范围伤害" />
    <UnitProperty pKey="伤害半径" pValue="1.2 格" />
    <UnitProperty pKey="攻击的目标" pValue="地面和空中目标" />
    <UnitProperty pKey="射程" pValue="7 格" />
    <UnitProperty pKey="攻速" pValue="3.76 秒/轮<sup>*</sup>" />
</UnitProperties>

\* 熔岩火炮的攻击节奏是：0.14 秒一发，15 发之后冷却 1.8 秒。

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

| 等级 | 每秒伤害# | 每次伤害 | 生命值 | 升级费用 | 升级时间 |升级后可<br>获得的经验|所需夜世界<br>大本等级|
|  --- |   ---   |   ---    |   ---  |    ---  |   ---   |         ---        |         ---         |
| 1 | 59 | 15 | 800 | 1000000 | 1,0,0,0 |  | 6 |
| 2 | 67 | 17 | 950 | 1200000 | 2,0,0,0 |  | 6 |
| 3 | 75 | 19 | 1100 | 1400000 | 3,0,0,0 |  | 6 |
| 4 | 83 | 21 | 1300 | 1500000 | 4,0,0,0 |  | 6 |
| 5 | 91 | 23 | 1500 | 1600000 | 5,0,0,0 |  | 6 |
| 6 | 99 | 25 | 1700 | 1700000 | 6,0,0,0 |  | 6 |
| 7 | 107 | 27 | 1900 | 2600000 | 8,0,0,0 |  | 7 |
| 8 | 119 | 30 | 2100 | 3600000 | 10,0,0,0 |  | 8 |
| 9 | 131 | 33 | 2350 | 4600000 | 11,0,0,0 |  | 9 |
| 10 | 143 | 36 | 2600 | 5600000 | 12,0,0,0 |  | 10 |

</UnitTable>

\# 这里的每秒伤害数据是游戏中显示的近似值，如果熔岩火炮在攻击期间被打断，则实际的每秒伤害就会降低。

<SmallTitle>更新历史</SmallTitle>

<Timeline>
    <TimelineItem date="2023/05/15">
        <TimelineRow>夜世界重做，建筑的数值重新平衡，伤害、生命值等数据有变化。</TimelineRow>
        <TimelineRow>所有等级熔岩火炮的升级时间增加。</TimelineRow>
        <TimelineRow>夜世界 10 本推出，熔岩火炮可升至 10 级。</TimelineRow>
    </TimelineItem>
        <TimelineItem date="2019/12/09">
        <TimelineRow>所有等级熔岩火炮的每秒伤害减少（更新公告里没有这个，但是确实削了）。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/06/18">
        <TimelineRow>夜世界 9 本推出，熔岩火炮可升至 9 级。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>
<p><small>数值核对：2026-10-13 · <a href="https://clashofclans.fandom.com/wiki/Roaster?oldid=622474" target="_blank" rel="noopener noreferrer">部落冲突维基</a>。部分附加字段沿用原记录。</small></p>
