---
title: "部落冲突 coc 都城哥布林前哨基地数据"
navTitle: "哥布林前哨基地"
shownTitle: "哥布林前哨基地"
module: upgrade-capital
imgFolder: capital_buildings/2507
wiki: https://clashofclans.fandom.com/wiki/Houses
canonical: /upgrade/2507-Goblin-Outpost
dataSyncedOn: 2026-10-13
description: "一个被遗弃的哥布林前哨基地，大家都去哪儿了？"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/2507-Goblin-Outpost.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-10-09'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Goblin_Outpost.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/10/09">
        <TimelineRow>新建筑：哥布林前哨基地。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
