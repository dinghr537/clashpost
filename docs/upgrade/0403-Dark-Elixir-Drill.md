---
title: "部落冲突 coc 暗黑重油钻井（黑水采集器）升级数据"
navTitle: "暗黑重油钻井"
shownTitle: "暗黑重油钻井（黑水采集器）"
module: upgrade-home
imgFolder: home_buildings/0403
wiki: https://clashofclans.fandom.com/wiki/Dark_Elixir_Drill
canonical: /upgrade/0403-Dark-Elixir-Drill
dataSyncedOn: 2026-10-13
description: "建筑工人们终于找到了提炼纯净暗黑重油的方法，这是一种非常稀有的魔法物质。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0403-Dark-Elixir-Drill.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-11-17'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Dark_Elixir_Drill11.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

\* 采集器容量满后将停止工作，直到玩家收集采集器内的资源。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/11/17">
        <TimelineRow>新增 11 级暗黑重油钻井，16 本可解锁。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/10/06">
        <TimelineRow>9 ~ 10 级暗黑重油钻井的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>1 ~ 5、7 ~ 10 级暗黑重油钻井的升级费用降低。</TimelineRow>
        <TimelineRow>7 ~ 10 级暗黑重油钻井的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>1 ~ 6、9 级暗黑重油钻井的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/09/09">
        <TimelineRow>超级充能推出，暗黑重油钻井是第一批可以充能的建筑之一。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/02/27">
        <TimelineRow>新增 10 级暗黑重油钻井，14 本可解锁。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/12/09">
        <TimelineRow>新增 9 级暗黑重油钻井，12 本可解锁。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>所有等级暗黑重油钻井的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/03/30">
        <TimelineRow>新增 8 级暗黑重油钻井，11 本可解锁。</TimelineRow>
        <TimelineRow>9 本（之前是 10 本）即可建造第 3 个暗黑重油钻井。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/04/02">
        <TimelineRow>2 ~ 7 级暗黑重油钻井的升级费用降低。</TimelineRow>
        <TimelineRow>所有等级暗黑重油钻井的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
