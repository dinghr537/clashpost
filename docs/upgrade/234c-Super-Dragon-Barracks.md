---
title: "部落冲突 coc 都城超级飞龙训练营升级数据"
navTitle: "超级飞龙训练营"
shownTitle: "超级飞龙训练营"
module: upgrade-capital
imgFolder: capital_buildings/234c
wiki: https://clashofclans.fandom.com/wiki/Clan_Capital_Barracks#Super_Dragon_Barracks
canonical: /upgrade/234c-Super-Dragon-Barracks
dataSyncedOn: 2026-10-13
description: "现在想想，木头可能不太适合用来给飞龙造房子。这房子一直都没着火也是个奇迹。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/234c-Super-Dragon-Barracks.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2022-05-02'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Super_Dragon_Barracks5.png" :imgAlt="$frontmatter.navTitle"
    :description="$frontmatter.description"
    :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2022/05/02">
        <TimelineRow>超级飞龙训练营随着部落都城玩法一同推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
