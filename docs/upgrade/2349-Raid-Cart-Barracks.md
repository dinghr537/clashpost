---
title: "部落冲突 coc 都城突袭炮车训练营升级数据"
navTitle: "突袭炮车训练营"
shownTitle: "突袭炮车训练营"
module: upgrade-capital
imgFolder: capital_buildings/2349
wiki: https://clashofclans.fandom.com/wiki/Clan_Capital_Barracks#Raid_Cart_Barracks
canonical: /upgrade/2349-Raid-Cart-Barracks
dataSyncedOn: 2026-10-13
description: "制造突袭炮车的工坊。突袭炮车是如何组装起来的倒是好理解，可这些野蛮人是从哪来的呢？"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/2349-Raid-Cart-Barracks.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2022-05-02'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Raid_Cart_Barracks5.png" :imgAlt="$frontmatter.navTitle"
    :description="$frontmatter.description"
    :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2022/05/02">
        <TimelineRow>突袭炮车训练营随着部落都城玩法一同推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
