---
title: "部落冲突 coc 都城隐秘弓箭手训练营升级数据"
navTitle: "隐秘弓箭手训练营"
shownTitle: "隐秘弓箭手训练营"
module: upgrade-capital
imgFolder: capital_buildings/2341
wiki: https://clashofclans.fandom.com/wiki/Clan_Capital_Barracks#Sneaky_Archer_Barracks
canonical: /upgrade/2341-Sneaky-Archer-Barracks
dataSyncedOn: 2026-10-13
description: "隐秘弓箭手的训练场地。当心有锋利的东西猛地飞过来！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/2341-Sneaky-Archer-Barracks.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2022-05-02'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Sneaky_Archer_Barracks5.png" :imgAlt="$frontmatter.navTitle"
    :description="$frontmatter.description"
    :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2022/05/02">
        <TimelineRow>隐秘弓箭手训练营随着部落都城玩法一同推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
