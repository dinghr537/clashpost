---
title: "部落冲突 coc 都城小屋数据"
navTitle: "小屋"
shownTitle: "小屋"
module: upgrade-capital
imgFolder: capital_buildings/2503
wiki: https://clashofclans.fandom.com/wiki/Houses
canonical: /upgrade/2503-Small-Hut
dataSyncedOn: 2026-10-13
description: "别致小巧，不适合高个子住。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/2503-Small-Hut.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2022-05-02'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Small_Hut.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2022/05/02">
        <TimelineRow>小屋随着部落都城玩法一同推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
