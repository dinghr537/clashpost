---
title: "部落冲突 coc 都城稻草屋数据"
navTitle: "稻草屋"
shownTitle: "稻草屋"
module: upgrade-capital
imgFolder: capital_buildings/2502
wiki: https://clashofclans.fandom.com/wiki/Houses
canonical: /upgrade/2502-Thatched-Hut
dataSyncedOn: 2026-10-13
description: "住着野蛮人。这简陋小屋建起来快，燃起来更快。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/2502-Thatched-Hut.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2022-05-02'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Thatched_Hut.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2022/05/02">
        <TimelineRow>稻草屋随着部落都城玩法一同推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
