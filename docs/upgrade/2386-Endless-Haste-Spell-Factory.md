---
title: "部落冲突 coc 都城永恒急速法术工厂升级数据"
navTitle: "永恒急速法术工厂"
shownTitle: "永恒急速法术工厂"
module: upgrade-capital
imgFolder: capital_buildings/2386
wiki: https://clashofclans.fandom.com/wiki/Clan_Capital_Spell_Factories#Endless_Haste_Spell_Factory
canonical: /upgrade/2386-Endless-Haste-Spell-Factory
dataSyncedOn: 2026-10-13
description: "配制一桶桶永恒急速法术。村民们每次路过这里都会加快脚步。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/2386-Endless-Haste-Spell-Factory.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-10-09'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Endless_Haste_Spell_Factory4.png" :imgAlt="$frontmatter.navTitle"
    :description="$frontmatter.description"
    :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/10/09">
        <TimelineRow>新建筑：永恒急速法术工厂。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
