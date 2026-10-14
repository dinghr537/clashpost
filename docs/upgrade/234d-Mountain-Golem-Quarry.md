---
title: "部落冲突 coc 都城高山戈仑石场升级数据"
navTitle: "高山戈仑石场"
shownTitle: "高山戈仑石场"
module: upgrade-capital
imgFolder: capital_buildings/234d
wiki: https://clashofclans.fandom.com/wiki/Clan_Capital_Barracks#Mountain_Golem_Quarry
canonical: /upgrade/234d-Mountain-Golem-Quarry
dataSyncedOn: 2026-10-13
description: "一个形似戈仑石人的巨坑，希望不是每次训练高山戈仑都要挖一个新坑。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/234d-Mountain-Golem-Quarry.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2022-05-02'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Mountain_Golem_Quarry5.png" :imgAlt="$frontmatter.navTitle"
    :description="$frontmatter.description"
    :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2022/05/02">
        <TimelineRow>高山戈仑石场随着部落都城玩法一同推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
