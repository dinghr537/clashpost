---
title: "部落冲突 coc 金矿升级数据"
navTitle: "金矿"
shownTitle: "金矿"
module: upgrade-home
imgFolder: home_buildings/0401
wiki: https://clashofclans.fandom.com/wiki/Gold_Mine
canonical: /upgrade/0401-Gold-Mine
dataSyncedOn: 2026-10-13
description: "金矿生产金币。升级金矿提高金币产量和容量。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0401-Gold-Mine.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-11-17'">

<template #introduction>

- *如想查看夜世界的金矿，请访问：[夜世界金矿](/upgrade/1201-Gold-Mine)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Gold_Mine17.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

\* 采集器容量满后将停止工作，直到玩家收集采集器内的资源。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/11/17">
        <TimelineRow>新增 17 级金矿，16 本可解锁。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/10/06">
        <TimelineRow>14 ~ 15 级金矿的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/06/16">
        <TimelineRow>1 ~ 8 级金矿的生命值减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>1 ~ 16 级金矿的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/02/10">
        <TimelineRow>2 ~ 10 级金矿的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>6、7、9 级金矿的升级时间减少。</TimelineRow>
        <TimelineRow>11 ~ 12 级金矿的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/09/09">
        <TimelineRow>超级充能推出，金矿是第一批可以充能的建筑之一。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/02/27">
        <TimelineRow>新增 16 级金矿，14 本可解锁。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>8、10 ~15 级金矿的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/12/09">
        <TimelineRow>新增 15 级金矿，12 级大本营可解锁。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>1 ~ 4 级的圣水收集器/金矿的容量加倍，3 小时不再能填满这些采集器。</TimelineRow>
        <TimelineRow>10 ~ 14 级金矿的升级费用降低。</TimelineRow>
        <TimelineRow>3 ~ 6、12 ~ 14 级金矿的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/03/30">
        <TimelineRow>新增 14 级金矿，11 级大本营可解锁。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/04/02">
        <TimelineRow>包含大量降低发展成本和提高发展速度的调整，其中 7 ~ 13 级金矿的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
