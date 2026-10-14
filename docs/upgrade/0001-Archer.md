---
title: "部落冲突 coc 弓箭手升级数据"
navTitle: "弓箭手"
shownTitle: "弓箭手"
module: upgrade-home
imgFolder: home_tech/0001
wiki: https://clashofclans.fandom.com/wiki/Archer
canonical: /upgrade/0001-Archer
dataSyncedOn: 2026-10-13
description: "这些神箭手在战场上总是能够百步穿杨，一箭封喉。她们觉得没有什么比一箭打爆对手更爽的了。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0001-Archer.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2026-02-23'">

<template #introduction>

- *如想查看以弓箭手为原型的英雄，请访问：[弓箭女皇（女王）](/upgrade/0201-Archer-Queen)。*
- *如想查看该兵种的强化版本，请访问：[超级弓箭手](/upgrade/0606-Super-Archer)。*
- *如想查看夜世界的隐秘弓箭手，请访问：[夜世界隐秘弓箭手](/upgrade/1001-Sneaky-Archer)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Archer_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

\# 根据安装包解析的结果，玩家可以在 1 本把训练营升到 2 级以解锁弓箭手，但这仅仅是理论上的，实际上新手教程会直接引导玩家升到 2 本，根本没有在 1 本升级训练营的机会。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2026/02/23">
        <TimelineRow>在 18 本新增 14 级弓箭手。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/11/17">
        <TimelineRow>13 级弓箭手的升级时间和升级费用减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/10/06">
        <TimelineRow>9、11、12 级弓箭手的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/06/16">
        <TimelineRow>1 ~ 3 级弓箭手的生命值提升。</TimelineRow>
        <TimelineRow>1 ~ 3 级弓箭手的每秒伤害值提升。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/27">
        <TimelineRow>部队的训练时间取消，但增加了捐赠费用。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>2 ~ 6、8 ~ 12 级弓箭手的升级时间减少。</TimelineRow>
        <TimelineRow>2、4 ~ 9、11 ~ 12 级弓箭手的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/02/10">
        <TimelineRow>17 本新增 13 级弓箭手。</TimelineRow>
        <TimelineRow>2 级弓箭手的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/18">
        <TimelineRow>3 ~ 7、10 ~ 12 级弓箭手的升级时间减少。</TimelineRow>
        <TimelineRow>9 ~ 12 级弓箭手的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>16 本推出，同时在 16 本新增 12 级弓箭手。</TimelineRow>
        <TimelineRow>7 ~ 11 级弓箭手的升级时间减少。</TimelineRow>
        <TimelineRow>10 级弓箭手的升级花费降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>9 级弓箭手的升级时间减少。</TimelineRow>
        <TimelineRow>9 级弓箭手的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>15 本推出，并在 15 本新增 11 级弓箭手。</TimelineRow>
        <TimelineRow>7 ~ 10 级弓箭手的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/12/09">
        <TimelineRow>2 ~ 9 级弓箭手的升级费用降低。</TimelineRow>
        <TimelineRow>2 ~ 9 级弓箭手的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>14 本新增 10 级弓箭手。</TimelineRow>
        <TimelineRow>1 ~ 2 级弓箭手的训练费用：50/80 圣水→ 30/60 圣水</TimelineRow>
        <TimelineRow>2 ~ 9 级的弓箭手的升级费用降低。</TimelineRow>
        <TimelineRow>4 ~ 8 级弓箭手的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/06/22">
        <TimelineRow>12 本新增 9 级弓箭手。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/03/30">
        <TimelineRow>5 ~ 8 级弓箭手的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/04/02">
        <TimelineRow>包含大量降低发展成本和提高发展速度的调整，其中 5 ~ 8 级弓箭手的升级时间下调。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
