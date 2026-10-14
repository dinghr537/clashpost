---
title: "部落冲突 coc 都城弹跳法术工厂升级数据"
navTitle: "弹跳法术工厂"
shownTitle: "弹跳法术工厂"
module: upgrade-capital
imgFolder: capital_buildings/2381
wiki: https://clashofclans.fandom.com/wiki/Clan_Capital_Spell_Factories#Jump_Spell_Factory
canonical: /upgrade/2381-Jump-Spell-Factory
dataSyncedOn: 2026-10-13
description: "配制一桶桶弹跳法术。这个工厂看起来好像随时会原地起飞。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/2381-Jump-Spell-Factory.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2022-05-02'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Jump_Spell_Factory5.png" :imgAlt="$frontmatter.navTitle"
    :description="$frontmatter.description"
    :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2022/05/02">
        <TimelineRow>弹跳法术工厂随着部落都城玩法一同推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
