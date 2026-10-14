---
title: "部落冲突 coc 都城疗伤法术工厂升级数据"
navTitle: "疗伤法术工厂"
shownTitle: "疗伤法术工厂"
module: upgrade-capital
imgFolder: capital_buildings/2380
wiki: https://clashofclans.fandom.com/wiki/Clan_Capital_Spell_Factories#Heal_Spell_Factory
canonical: /upgrade/2380-Heal-Spell-Factory
dataSyncedOn: 2026-10-13
description: "配制一桶桶疗伤法术。里面散发出的花香能让你的头疼奇迹般消失。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/2380-Heal-Spell-Factory.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2022-05-02'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Heal_Spell_Factory5.png" :imgAlt="$frontmatter.navTitle"
    :description="$frontmatter.description"
    :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2022/05/02">
        <TimelineRow>疗伤法术工厂随着部落都城玩法一同推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
