---
title: "部落冲突 coc 都城冰霜法术工厂（霜冻法术工厂）升级数据"
navTitle: "冰霜法术工厂"
shownTitle: "冰霜法术工厂（霜冻法术工厂）"
module: upgrade-capital
imgFolder: capital_buildings/2383
wiki: https://clashofclans.fandom.com/wiki/Clan_Capital_Spell_Factories#Frost_Spell_Factory
canonical: /upgrade/2383-Frost-Spell-Factory
dataSyncedOn: 2026-10-13
description: "配制一桶桶冰霜法术。如果要来参观，最好穿暖和点！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/2383-Frost-Spell-Factory.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2022-05-02'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Frost_Spell_Factory5.png" :imgAlt="$frontmatter.navTitle"
    :description="$frontmatter.description"
    :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2022/05/02">
        <TimelineRow>冰霜法术工厂随着部落都城玩法一同推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
