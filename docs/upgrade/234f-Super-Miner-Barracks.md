---
title: "部落冲突 coc 都城超级矿工训练营升级数据"
navTitle: "超级矿工训练营"
shownTitle: "超级矿工训练营"
module: upgrade-capital
imgFolder: capital_buildings/234f
wiki: https://clashofclans.fandom.com/wiki/Clan_Capital_Barracks#Super_Miner_Barracks
canonical: /upgrade/234f-Super-Miner-Barracks
dataSyncedOn: 2026-10-13
description: "超级矿工的快乐老家，这里非常接地气，还有一股浓浓的石油味。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/234f-Super-Miner-Barracks.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-10-09'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Super_Miner_Barracks4.png" :imgAlt="$frontmatter.navTitle"
    :description="$frontmatter.description"
    :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/10/09">
        <TimelineRow>新建筑：超级矿工训练营。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
