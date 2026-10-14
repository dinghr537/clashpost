---
title: "部落冲突 coc 根蔓骑士（棘木骑士、树根）升级数据"
navTitle: "根蔓骑士"
shownTitle: "根蔓骑士（棘木骑士、树根）"
module: upgrade-home
imgFolder: home_tech/0010
wiki: https://clashofclans.fandom.com/wiki/Root_Rider
canonical: /upgrade/0010-Root-Rider
dataSyncedOn: 2026-10-13
description: "这位大地战士与大自然融为一体，甚至不用自己走路，而是骑在坚硬无比的根蔓上作战。她的根蔓可摧毁城墙，将防御建筑夷为平地。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0010-Root-Rider.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-10-06'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Root_Rider_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

根蔓骑士可以将树根放在墙上，快速摧毁 [城墙](/upgrade/0300-Walls)。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/10/06">
        <TimelineRow>2 ~ 3 级根蔓骑士的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/27">
        <TimelineRow>部队的训练时间取消，但增加了捐赠费用。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>2 ~ 3 级根蔓骑士的升级时间减少。</TimelineRow>
        <TimelineRow>2 级根蔓骑士的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/02/10">
        <TimelineRow>根蔓骑士的训练时间由 3:40 改为 2:50</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>3 级根蔓骑士的升级时间减少。</TimelineRow>
        <TimelineRow>2 ~ 3 级根蔓骑士的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/03">
        <TimelineRow>所有等级根蔓骑士的每秒伤害降低（190/210/230 => 95/105/115）。</TimelineRow>
        <TimelineRow>所有等级根蔓骑士的生命值降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/03/26">
        <TimelineRow>所有等级根蔓骑士的每秒伤害降低，生命值减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/02/27">
        <TimelineRow>所有等级根蔓骑士的生命值减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>16 本推出，并在 15 本新增根蔓骑士，共设 3 个等级。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
