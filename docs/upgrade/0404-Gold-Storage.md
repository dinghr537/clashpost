---
title: "部落冲突 coc 储金罐升级数据"
navTitle: "储金罐"
shownTitle: "储金罐"
description: "您珍贵的金币都存在这里！不要让狡猾的哥布林有机可乘！升级储金罐，提高它们的容量和抗打击能力。"
module: upgrade-home
imgFolder: home_buildings/0404
wiki: https://clashofclans.fandom.com/wiki/Gold_Storage
canonical: /upgrade/0404-Gold-Storage
dataSyncedOn: 2026-10-13
---

- *如想查看夜世界的储金罐，请访问：[夜世界储金罐](/upgrade/1203-Gold-Storage)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Gold_Storage19.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

<SmallTitle>各等级图片</SmallTitle>

<Panel>
    <UnitImgGroup :folder="$frontmatter.imgFolder">
        <UnitImg imgTitle="1 级" imgSrc="Gold_Storage1.png" />
        <UnitImg imgTitle="2 级" imgSrc="Gold_Storage2.png" />
        <UnitImg imgTitle="3 级" imgSrc="Gold_Storage3.png" />
        <UnitImg imgTitle="4 级" imgSrc="Gold_Storage4.png" />
        <UnitImg imgTitle="5 级" imgSrc="Gold_Storage5.png" />
        <UnitImg imgTitle="6 级" imgSrc="Gold_Storage6.png" />
        <UnitImg imgTitle="7 级" imgSrc="Gold_Storage7.png" />
        <UnitImg imgTitle="8 级" imgSrc="Gold_Storage8.png" />
        <UnitImg imgTitle="9 级" imgSrc="Gold_Storage9.png" />
        <UnitImg imgTitle="10 级" imgSrc="Gold_Storage10.png" />
        <UnitImg imgTitle="11 级" imgSrc="Gold_Storage11.png" />
        <UnitImg imgTitle="12 级" imgSrc="Gold_Storage12.png" />
        <UnitImg imgTitle="13 级" imgSrc="Gold_Storage13.png" />
        <UnitImg imgTitle="14 级" imgSrc="Gold_Storage14.png" />
        <UnitImg imgTitle="15 级" imgSrc="Gold_Storage15.png" />
        <UnitImg imgTitle="16 级" imgSrc="Gold_Storage16.png" />
        <UnitImg imgTitle="17 级" imgSrc="Gold_Storage17.png" />
        <UnitImg imgTitle="18 级" imgSrc="Gold_Storage18.png" />
        <UnitImg imgTitle="19 级" imgSrc="Gold_Storage19.png" />
    </UnitImgGroup>
</Panel>

<SmallTitle>建筑数量对照表</SmallTitle>

<BuildingNum>
    <BuildingNumRow title="大本等级" num="1 - 2, 3 - 7, 8, 9 - 18" />
    <BuildingNumRow title="建筑数量" num="    1,     2, 3,      4" />
</BuildingNum>

<SmallTitle>重要说明</SmallTitle>

[雷电法术](/upgrade/0100-Lightning-Spell) 和 [地震法术](/upgrade/0181-Earthquake-Spell) 不能对资源仓库造成伤害。

<SmallTitle>属性</SmallTitle>

<UnitProperties>
    <UnitProperty pKey="占地面积" pValue="3×3" />
    <UnitProperty pKey="判定面积" pValue="2×2" :isJudgeSquare="true" />
    <UnitProperty pKey="掠夺比例" pValue="点击查看" />
</UnitProperties>

<SmallTitle>升级数据</SmallTitle>

<script setup>
const tableExtraInfo = [
    {
        "column": 1,
        "type": "number",
        "icon": "Gold",
        "noGoldPass": true
    },
    {
        "column": 3,
        "type": "cost",
        "gpClass": "building",
        "icon": "Elixir"
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

| 等级 | 最大储量 | 生命值 | 升级费用 |   升级时间   | 升级后可获<br>得的经验 | 所需<br>大本等级 |
| ---- |  ----   |  ---- |    ---   |     ---     |         ---          |       ---       |
| 1 | 1500 | 150 | 300 | 0,0,0,10 |  | 1 |
| 2 | 3000 | 300 | 750 | 0,0,2,0 |  | 2 |
| 3 | 6000 | 450 | 1500 | 0,0,5,0 |  | 2 |
| 4 | 12000 | 600 | 3000 | 0,0,15,0 |  | 3 |
| 5 | 25000 | 800 | 6000 | 0,0,30,0 |  | 3 |
| 6 | 45000 | 1000 | 12000 | 0,1,0,0 |  | 3 |
| 7 | 100000 | 1250 | 25000 | 0,2,0,0 |  | 4 |
| 8 | 225000 | 1500 | 50000 | 0,3,0,0 |  | 4 |
| 9 | 450000 | 1700 | 100000 | 0,4,0,0 |  | 5 |
| 10 | 850000 | 1900 | 250000 | 0,5,0,0 |  | 6 |
| 11 | 1750000 | 2100 | 500000 | 0,6,0,0 |  | 7 |
| 12 | 2000000 | 2500 | 1000000 | 0,12,0,0 |  | 11 |
| 13 | 3000000 | 2900 | 1800000 | 0,18,0,0 |  | 12 |
| 14 | 4000000 | 3300 | 2800000 | 1,0,0,0 |  | 13 |
| 15 | 4500000 | 3700 | 3000000 | 2,0,0,0 |  | 14 |
| 16 | 5000000 | 3900 | 4000000 | 3,0,0,0 |  | 15 |
| 17 | 5500000 | 4050 | 5500000 | 4,0,0,0 |  | 16 |
| 18 | 6000000 | 4200 | 10000000 | 5,0,0,0 |  | 17 |
| 19 | 6500000 | 4300 | 18000000 | 12,12,0,0 |  | 18 |
</UnitTable>

<SmallTitle>更新历史</SmallTitle>

<Timeline>
    <TimelineItem date="2025/11/17">
        <TimelineRow>18 本推出，并在 18 本新增 19 级储金罐。</TimelineRow>
        <TimelineRow>18 级储金罐的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/06/16">
        <TimelineRow>1 ~ 9 级储金罐的生命值减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>3 ~ 6、8 ~ 17 级储金罐的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/02/10">
        <TimelineRow>17 ~ 18 级储金罐的资源储量增加。</TimelineRow>
        <TimelineRow>2 ~ 8 级储金罐的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>17 本推出，并在 17 本新增 18 级储金罐。</TimelineRow>
        <TimelineRow>15 ~ 17 级储金罐的升级费用降低。</TimelineRow>
        <TimelineRow>17 级储金罐的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/18">
        <TimelineRow>12 ~ 16 级储金罐的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>新增 17 级储金罐，16 级大本营可解锁。</TimelineRow>
        <TimelineRow>15 级储金罐的升级费由 550 万降低到 450 万。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>13 ~ 14 级储金罐的升级时间减少。</TimelineRow>
        <TimelineRow>13 ~ 14 级储金罐的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>15 本推出，并在 15 本新增 16 级储金罐。</TimelineRow>
        <TimelineRow>12 ~ 15 级储金罐的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>14 本推出，并在 14 本新增 15 级储金罐。</TimelineRow>
        <TimelineRow>2 ~ 3 级储金罐的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/12/09">
        <TimelineRow>新增 14 级储金罐，13 级大本营可解锁。</TimelineRow>
        <TimelineRow>13 级储金罐的容量增加 50 万。</TimelineRow>
        <TimelineRow>12 级大本营可掠夺的金币增加至 50 万（不含采集器和城堡）。</TimelineRow>
    </TimelineItem>
        <TimelineItem date="2019/04/02">
        <TimelineRow>10 ~ 13 级储金罐的升级时间减少。</TimelineRow>
        <TimelineRow>12 ~ 13 级储金罐的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>
<p><small>数值核对：2026-10-13 · <a href="https://clashofclans.fandom.com/wiki/Gold_Storage?oldid=611745" target="_blank" rel="noopener noreferrer">部落冲突维基</a>。部分附加字段沿用原记录。</small></p>
