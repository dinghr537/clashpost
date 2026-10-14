---
title: "部落冲突 coc 都城投矛器（投矛机）升级数据"
navTitle: "投矛器"
shownTitle: "投矛器（投矛机）"
module: upgrade-capital
imgFolder: capital_buildings/2202
wiki: https://clashofclans.fandom.com/wiki/Spear_Thrower
canonical: /upgrade/2202-Spear-Thrower
dataSyncedOn: 2026-10-13
description: "向地面和空中的敌方单位投掷长矛，令人生畏。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/2202-Spear-Thrower.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-09-14'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Spear_Thrower5.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/09/14">
        <TimelineRow>2 ~ 5 级都城投矛器的每秒伤害降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/05/02">
        <TimelineRow>投矛器随着部落都城玩法一同推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
