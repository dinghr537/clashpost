---
title: "部落冲突 coc 圣水收集器升级数据"
navTitle: "圣水收集器"
shownTitle: "圣水收集器"
module: upgrade-home
imgFolder: home_buildings/0402
wiki: https://clashofclans.fandom.com/wiki/Elixir_Collector
canonical: /upgrade/0402-Elixir-Collector
dataSyncedOn: 2026-10-13
description: "圣水收集器可以从村庄地下的圣泉中收集圣水。升级您的圣水收集器以使圣水产量最大化。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0402-Elixir-Collector.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-11-17'">

<template #introduction>

- *如想查看夜世界的圣水收集器，请访问：[夜世界圣水收集器](/upgrade/1202-Elixir-Collector)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Elixir_Collector17.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

\* 采集器容量满后将停止工作，直到玩家收集采集器内的资源。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/11/17">
        <TimelineRow>新增 17 级圣水收集器，16 本可解锁。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/10/06">
        <TimelineRow>14 ~ 15 级圣水收集器的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/06/16">
        <TimelineRow>1 ~ 8 级圣水收集器的生命值减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>1 ~ 16 级圣水收集器的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/02/10">
        <TimelineRow>2 ~ 10 级圣水收集器的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>6、7、9 级圣水收集器的升级时间减少。</TimelineRow>
        <TimelineRow>11 ~ 12 级圣水收集器的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/09/09">
        <TimelineRow>超级充能推出，圣水收集器是第一批可以充能的建筑之一。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/02/27">
        <TimelineRow>新增 16 级圣水收集器，14 本可解锁。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>8、10 ~15 级圣水收集器的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/12/09">
        <TimelineRow>新增 15 级圣水收集器，12 级大本营可解锁。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/06/15">
        <TimelineRow>5 级圣水收集器的升级费用从 3500 减少到 3000，与 5 级金矿的升级费用相同（现在这两座建筑每一等级的升级费用都保持一致）</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>1 ~ 4 级的圣水收集器/金矿的容量加倍，3 小时不再能填满这些采集器。</TimelineRow>
        <TimelineRow>10 ~ 14 级圣水收集器的升级费用降低。</TimelineRow>
        <TimelineRow>3 ~ 6、12 ~ 14 级圣水收集器的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/03/30">
        <TimelineRow>新增 14 级圣水收集器，11 级大本营可解锁。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/04/02">
        <TimelineRow>包含大量降低发展成本和提高发展速度的调整，其中 7 ~ 13 级圣水收集器的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
