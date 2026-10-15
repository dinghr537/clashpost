---
title: "部落冲突 coc 滚木守卫升级数据"
navTitle: "滚木守卫"
shownTitle: "滚木守卫"
module: upgrade-home
imgFolder: home_heroes/0842
wiki: https://clashofclans.fandom.com/wiki/Logger
canonical: /upgrade/0842-Logger
dataSyncedOn: 2026-10-13
---

<script setup>
const tableExtraInfo0 = [
    {
        "column": 5,
        "type": "cost",
        "icon": "Elixir",
        "gpClass": "building",
        "noGoldPass": false
    },
    {
        "column": 6,
        "type": "time",
        "gpClass": "building",
        "noGoldPass": false
    }
];
</script>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Logger1.png" :imgAlt="$frontmatter.navTitle" :isSmallImg="true" />

<SmallTitle>重要说明</SmallTitle>

1. 解锁条件：18级大本营。

<SmallTitle>属性</SmallTitle>

<UnitProperties>
    <UnitProperty pKey="目标" pValue="地面和空中" />
    <UnitProperty pKey="攻击方式" pValue="范围伤害" />
    <UnitProperty pKey="移动速度" pValue="1 格/秒" />
    <UnitProperty pKey="攻击间隔" pValue="2.5秒" />
    <UnitProperty pKey="射程" pValue="7格" />
    <UnitProperty pKey="巡逻半径" pValue="14格" />
    <UnitProperty pKey="触发半径" pValue="15格" />
    <UnitProperty pKey="伤害半径" pValue="??" />
    <UnitProperty pKey="击退范围" pValue="1.5格" />
</UnitProperties>

<SmallTitle>升级数据</SmallTitle>

<UnitTable :tableExtraInfo="tableExtraInfo0">

| 等级 | 每秒伤害 | 每次伤害 | 生命值 | 命中后穿透距离（格） | 升级费用 | 升级时间 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 230 | 575 | 8000 | 5格 | \ | \ |
| 2 | 260 | 650 | 9000 | 5格 | 18000000 | 7,0,0,0 |
| 3 | 290 | 725 | 10000 | 5格 | 22000000 | 9,0,0,0 |
| 4 | 320 | 800 | 11000 | 6格 | 26000000 | 11,0,0,0 |
| 5 | 350 | 875 | 12000 | 6格 | 28000000 | 13,0,0,0 |
</UnitTable>

<SmallTitle>更新历史</SmallTitle>

<Timeline>
    <TimelineItem date="2026/07/14">
        <TimelineRow>滚木守卫击退距离1格→1.5格；命中后穿透距离：1至3级7格→5格，4至5级8格→6格。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2026/04/27">
        <TimelineRow>新增滚木守卫。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2026/04/26">
        <TimelineRow>公布滚木守卫，共5级。</TimelineRow>
    </TimelineItem>
</Timeline>


<p><small>数值核对：2026-10-13 · <a href="https://clashofclans.fandom.com/wiki/Logger?oldid=625039" target="_blank" rel="noopener noreferrer">部落冲突维基</a>。</small></p>
