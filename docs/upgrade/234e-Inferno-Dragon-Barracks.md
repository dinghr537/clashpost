---
title: "部落冲突 coc 都城地狱飞龙训练营升级数据"
navTitle: "地狱飞龙训练营"
shownTitle: "地狱飞龙训练营"
module: upgrade-capital
imgFolder: capital_buildings/234e
wiki: https://clashofclans.fandom.com/wiki/Clan_Capital_Barracks#Inferno_Dragon_Barracks
canonical: /upgrade/234e-Inferno-Dragon-Barracks
dataSyncedOn: 2026-10-13
description: "地狱飞龙玩耍的地方，由超级建筑工人建造而成，使用的是防火性能最好的材料。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/234e-Inferno-Dragon-Barracks.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2022-12-12'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Inferno_Dragon_Barracks4.png" :imgAlt="$frontmatter.navTitle"
    :description="$frontmatter.description"
    :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2022/12/12">
        <TimelineRow>新建筑：地狱飞龙训练营。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
