---
title: "部落冲突 coc 都城骷髅召唤法术工厂升级数据"
navTitle: "骷髅召唤法术工厂"
shownTitle: "骷髅召唤法术工厂"
module: upgrade-capital
imgFolder: capital_buildings/2385
wiki: https://clashofclans.fandom.com/wiki/Clan_Capital_Spell_Factories#Graveyard_Spell_Factory
canonical: /upgrade/2385-Graveyard-Spell-Factory
dataSyncedOn: 2026-10-13
description: "配制一桶桶骷髅召唤法术。是不是会有骨头咔嗒作响，你就当没听到吧。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/2385-Graveyard-Spell-Factory.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2022-12-12'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Graveyard_Spell_Factory4.png" :imgAlt="$frontmatter.navTitle"
    :description="$frontmatter.description"
    :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2022/12/12">
        <TimelineRow>新建筑：骷髅召唤法术工厂。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
