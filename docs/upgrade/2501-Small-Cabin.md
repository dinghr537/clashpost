---
title: "部落冲突 coc 都城平顶屋（小棚屋）数据"
navTitle: "平顶屋"
shownTitle: "平顶屋"
module: upgrade-capital
imgFolder: capital_buildings/2501
wiki: https://clashofclans.fandom.com/wiki/Houses
canonical: /upgrade/2501-Small-Cabin
dataSyncedOn: 2026-10-13
description: "如果村民喜欢明亮方正的房子，那很适合住在这里。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/2501-Small-Cabin.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2022-05-02'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Small_Cabin.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2022/05/02">
        <TimelineRow>平顶屋随着部落都城玩法一同推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
