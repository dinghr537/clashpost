---
title: "部落冲突 coc 都城超级巨人训练营升级数据"
navTitle: "超级巨人训练营"
shownTitle: "超级巨人训练营"
module: upgrade-capital
imgFolder: capital_buildings/2342
wiki: https://clashofclans.fandom.com/wiki/Clan_Capital_Barracks#Super_Giant_Barracks
canonical: /upgrade/2342-Super-Giant-Barracks
dataSyncedOn: 2026-10-13
description: "超级巨人的家。到处都散落着他们的训练器材！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/2342-Super-Giant-Barracks.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2022-05-02'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Super_Giant_Barracks5.png" :imgAlt="$frontmatter.navTitle"
    :description="$frontmatter.description"
    :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2022/05/02">
        <TimelineRow>超级巨人训练营随着部落都城玩法一同推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
