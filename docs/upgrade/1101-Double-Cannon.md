---
title: "部落冲突 coc 夜世界双管加农炮升级数据"
navTitle: "双管加农炮"
shownTitle: "双管加农炮"
description: "双管加农炮，每管二连发。四倍炮弹，四倍火力！"
module: upgrade-bh
imgFolder: bh_buildings/1101
wiki: https://clashofclans.fandom.com/wiki/Double_Cannon
canonical: /upgrade/1101-Double-Cannon
dataSyncedOn: 2026-10-13
---

- *如想查看夜世界的加农炮，请访问：[夜世界加农炮](/upgrade/1100-Cannon)。*
- *如想查看夜世界的巨型加农炮，请访问：[夜世界巨型加农炮](/upgrade/110a-Giant-Cannon)。*
- *如想查看家乡改装后的加农炮，请访问该页面后切换为“连发模式”：[加农炮](/upgrade/0301-Cannon)。*
- *如想查看都城的多管加农炮，请访问：[都城多管加农炮](/upgrade/2204-Multi-Cannon)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Double_Cannon10.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

<SmallTitle>各等级图片</SmallTitle>

<Panel>
    <UnitImgGroup :folder="$frontmatter.imgFolder">
        <UnitImg imgTitle="1 级" imgSrc="Double_Cannon1.png" />
        <UnitImg imgTitle="2 级" imgSrc="Double_Cannon2.png" />
        <UnitImg imgTitle="3 级" imgSrc="Double_Cannon3.png" />
        <UnitImg imgTitle="4 级" imgSrc="Double_Cannon4.png" />
        <UnitImg imgTitle="5 级" imgSrc="Double_Cannon5.png" />
        <UnitImg imgTitle="6 级" imgSrc="Double_Cannon6.png" />
        <UnitImg imgTitle="7 级" imgSrc="Double_Cannon7.png" />
        <UnitImg imgTitle="8 级" imgSrc="Double_Cannon8.png" />
        <UnitImg imgTitle="9 级" imgSrc="Double_Cannon9.png" />
        <UnitImg imgTitle="10 级" imgSrc="Double_Cannon10.png" />
    </UnitImgGroup>
</Panel>

<SmallTitle>建筑数量对照表</SmallTitle>

<BuildingNum>
    <BuildingNumRow title="大本等级" num="1, 2 - 4, 5 - 7, 8 - 10" />
    <BuildingNumRow title="建筑数量" num="0,     1,     2,      3" />
</BuildingNum>

<SmallTitle>属性</SmallTitle>

<UnitProperties>
    <UnitProperty pKey="占地面积" pValue="3×3" />
    <UnitProperty pKey="判定面积" pValue="2×2" :isJudgeSquare="true" />
    <UnitProperty pKey="伤害类型" pValue="单体伤害" />
    <UnitProperty pKey="攻击的目标" pValue="仅地面目标" />
    <UnitProperty pKey="射程" pValue="7 格" />
    <UnitProperty pKey="攻速" pValue="约 2.4 秒/轮<sup>*</sup>" />
</UnitProperties>

\* 双管加农炮的攻击节奏是 0.192 秒一发，4 发后冷却 1.6 秒。

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

| 等级 |每秒伤害<sup>#</sup>| 每次伤害 | 生命值 | 升级费用 | 升级时间 |升级后可<br>获得的经验|所需夜世界<br>大本等级|
|  --- |        ---        |   ---   |  ---   |   ---   |    ---  |         ---         |         ---        |
| 1 | 91 | 50 | 600 | 20000 | 0,0,10,0 |  | 2 |
| 2 | 101 | 55 | 690 | 50000 | 0,1,0,0 |  | 3 |
| 3 | 112 | 61 | 800 | 80000 | 0,3,0,0 |  | 3 |
| 4 | 123 | 67 | 910 | 300000 | 0,12,0,0 |  | 4 |
| 5 | 136 | 74 | 1050 | 900000 | 1,0,0,0 |  | 5 |
| 6 | 148 | 81 | 1250 | 1400000 | 2,0,0,0 |  | 6 |
| 7 | 163 | 89 | 1450 | 2200000 | 4,0,0,0 |  | 7 |
| 8 | 180 | 98 | 1700 | 3200000 | 6,0,0,0 |  | 8 |
| 9 | 198 | 108 | 1950 | 4200000 | 8,0,0,0 |  | 9 |
| 10 | 220 | 120 | 2200 | 5200000 | 10,0,0,0 |  | 10 |

</UnitTable>

\# 这里的每秒伤害数据是游戏中显示的近似值，如果双管加农炮在攻击期间被打断，则实际的每秒伤害就会降低。

<SmallTitle>更新历史</SmallTitle>

<Timeline>
    <TimelineItem date="2023/05/15">
        <TimelineRow>夜世界重做，建筑的数值重新平衡，伤害、生命值等数据有变化。</TimelineRow>
        <TimelineRow>6 ~ 9 级双管加农炮的升级时间增加。</TimelineRow>
        <TimelineRow>夜世界 10 本推出，双管加农炮可升至 10 级。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/06/18">
        <TimelineRow>夜世界 9 本推出，双管加农炮可升至 9 级。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>
<p><small>数值核对：2026-10-13 · <a href="https://clashofclans.fandom.com/wiki/Double_Cannon?oldid=622502" target="_blank" rel="noopener noreferrer">部落冲突维基</a>。部分附加字段沿用原记录。</small></p>
