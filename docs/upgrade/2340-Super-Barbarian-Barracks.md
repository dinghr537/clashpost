---
title: "部落冲突 coc 都城超级野蛮人训练营升级数据"
navTitle: "超级野蛮人训练营"
shownTitle: "超级野蛮人训练营"
module: upgrade-capital
imgFolder: capital_buildings/2340
wiki: https://clashofclans.fandom.com/wiki/Clan_Capital_Barracks#Super_Barbarian_Barracks
canonical: /upgrade/2340-Super-Barbarian-Barracks
dataSyncedOn: 2026-10-13
description: "超级野蛮人互相切磋的场地。充斥着他们的汗臭味和放狠话的声音。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/2340-Super-Barbarian-Barracks.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2022-05-02'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Super_Barbarian_Barracks5.png" :imgAlt="$frontmatter.navTitle"
    :description="$frontmatter.description"
    :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2022/05/02">
        <TimelineRow>超级野蛮人训练营随着部落都城玩法一同推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
