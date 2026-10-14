---
title: "部落冲突 coc 都城哥布林小屋数据"
navTitle: "哥布林小屋"
shownTitle: "哥布林小屋"
module: upgrade-capital
imgFolder: capital_buildings/2508
wiki: https://clashofclans.fandom.com/wiki/Houses
canonical: /upgrade/2508-Goblin-Hut
dataSyncedOn: 2026-10-13
description: "一间空空如也的哥布林小屋，可能是要卖掉吧？"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/2508-Goblin-Hut.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-10-09'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Goblin_Hut.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/10/09">
        <TimelineRow>新建筑：哥布林小屋。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
