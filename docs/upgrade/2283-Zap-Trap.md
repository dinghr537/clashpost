---
title: "部落冲突 coc 都城电击陷阱升级数据"
navTitle: "电击陷阱"
shownTitle: "电击陷阱"
module: upgrade-capital
imgFolder: capital_buildings/2283
wiki: https://clashofclans.fandom.com/wiki/Zap_Trap
canonical: /upgrade/2283-Zap-Trap
dataSyncedOn: 2026-10-13
description: "如果附近有个电击陷阱，路过的部队一定会被电得惊慌失措。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/2283-Zap-Trap.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2022-06-27'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Zap_Trap5.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2022/06/27">
        <TimelineRow>电击陷阱的触发距离提升 2 倍，与空中炸弹和搜空地雷一致（官方说一致，实际上并不一致）。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/05/02">
        <TimelineRow>电击陷阱随着部落都城玩法一同推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
