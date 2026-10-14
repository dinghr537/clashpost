---
title: "部落冲突 coc 都城骷髅飞桶训练营升级数据"
navTitle: "骷髅飞桶训练营"
shownTitle: "骷髅飞桶训练营"
module: upgrade-capital
imgFolder: capital_buildings/2347
wiki: https://clashofclans.fandom.com/wiki/Clan_Capital_Barracks#Skeleton_Barrel_Barracks
canonical: /upgrade/2347-Skeleton-Barrel-Barracks
dataSyncedOn: 2026-10-13
description: "其实就是个建在墓地边的木桶厂，老板是个卖气球的。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/2347-Skeleton-Barrel-Barracks.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2022-05-02'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Skeleton_Barrel_Barracks5.png" :imgAlt="$frontmatter.navTitle"
    :description="$frontmatter.description"
    :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2022/05/02">
        <TimelineRow>骷髅飞桶训练营随着部落都城玩法一同推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
