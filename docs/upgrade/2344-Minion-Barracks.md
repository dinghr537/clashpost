---
title: "部落冲突 coc 都城亡灵训练营升级数据"
navTitle: "亡灵训练营"
shownTitle: "亡灵训练营"
module: upgrade-capital
imgFolder: capital_buildings/2344
wiki: https://clashofclans.fandom.com/wiki/Clan_Capital_Barracks#Minion_Barracks
canonical: /upgrade/2344-Minion-Barracks
dataSyncedOn: 2026-10-13
description: "多亏了新技术，小小亡灵如今已发展成亡灵大军！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/2344-Minion-Barracks.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2022-05-02'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Minion_Barracks5.png" :imgAlt="$frontmatter.navTitle"
    :description="$frontmatter.description"
    :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2022/05/02">
        <TimelineRow>亡灵训练营随着部落都城玩法一同推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
