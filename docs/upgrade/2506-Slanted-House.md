---
title: "部落冲突 coc 都城斜顶屋数据"
navTitle: "斜顶屋"
shownTitle: "斜顶屋"
module: upgrade-capital
imgFolder: capital_buildings/2506
wiki: https://clashofclans.fandom.com/wiki/Houses
canonical: /upgrade/2506-Slanted-House
dataSyncedOn: 2026-10-13
description: "屋顶可以有效防止积雪，但屋子里面装修起来就麻烦了。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/2506-Slanted-House.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2022-05-02'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Slanted_House.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2022/05/02">
        <TimelineRow>斜顶屋随着部落都城玩法一同推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
