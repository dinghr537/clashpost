---
title: "部落冲突 coc 都城平顶木屋（木棚屋）数据"
navTitle: "平顶木屋"
shownTitle: "平顶木屋"
module: upgrade-capital
imgFolder: capital_buildings/2505
wiki: https://clashofclans.fandom.com/wiki/Houses
canonical: /upgrade/2505-Wooden-Cabin
dataSyncedOn: 2026-10-13
description: "如果村民喜欢明亮方正的房子，而且要比邻居家大，那这里很适合。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/2505-Wooden-Cabin.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2022-05-02'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Wooden_Cabin.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2022/05/02">
        <TimelineRow>平顶木屋随着部落都城玩法一同推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
