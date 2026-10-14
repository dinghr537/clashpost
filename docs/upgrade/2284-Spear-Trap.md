---
title: "部落冲突 coc 都城投矛陷阱升级数据"
navTitle: "投矛陷阱"
shownTitle: "投矛陷阱"
module: upgrade-capital
imgFolder: capital_buildings/2284
wiki: https://clashofclans.fandom.com/wiki/Spear_Trap
canonical: /upgrade/2284-Spear-Trap
dataSyncedOn: 2026-10-13
description: "等待一群敌方单位经过，然后发射威力十足的尖矛，打他们个措手不及。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/2284-Spear-Trap.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-10-09'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Spear_Trap4.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/10/09">
        <TimelineRow>都城新陷阱：投矛陷阱。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
