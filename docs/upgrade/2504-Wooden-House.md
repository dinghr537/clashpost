---
title: "部落冲突 coc 都城木屋数据"
navTitle: "木屋"
shownTitle: "木屋"
module: upgrade-capital
imgFolder: capital_buildings/2504
wiki: https://clashofclans.fandom.com/wiki/Houses
canonical: /upgrade/2504-Wooden-House
dataSyncedOn: 2026-10-13
description: "建造和设计都很不错，温馨舒适，让人有家的感觉。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/2504-Wooden-House.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2022-05-02'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Wooden_House.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2022/05/02">
        <TimelineRow>木屋随着部落都城玩法一同推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
