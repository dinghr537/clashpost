---
title: "部落冲突 coc 都城狂暴法术工厂升级数据"
navTitle: "狂暴法术工厂"
shownTitle: "狂暴法术工厂"
module: upgrade-capital
imgFolder: capital_buildings/2384
wiki: https://clashofclans.fandom.com/wiki/Clan_Capital_Spell_Factories#Rage_Spell_Factory
canonical: /upgrade/2384-Rage-Spell-Factory
dataSyncedOn: 2026-10-13
description: "配制一桶桶狂暴法术。稍微离它近一点，你都会变得异常狂暴。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/2384-Rage-Spell-Factory.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2022-05-02'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Rage_Spell_Factory5.png" :imgAlt="$frontmatter.navTitle"
    :description="$frontmatter.description"
    :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2022/05/02">
        <TimelineRow>狂暴法术工厂随着部落都城玩法一同推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
