---
title: "部落冲突 coc 都城雷电法术工厂升级数据"
navTitle: "雷电法术工厂"
shownTitle: "雷电法术工厂"
module: upgrade-capital
imgFolder: capital_buildings/2382
wiki: https://clashofclans.fandom.com/wiki/Clan_Capital_Spell_Factories#Lightning_Spell_Factory
canonical: /upgrade/2382-Lightning-Spell-Factory
dataSyncedOn: 2026-10-13
description: "配制一桶桶雷电法术。别靠近它，否则头发会炸，运气会差。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/2382-Lightning-Spell-Factory.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2022-05-02'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Lightning_Spell_Factory5.png" :imgAlt="$frontmatter.navTitle"
    :description="$frontmatter.description"
    :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2022/05/02">
        <TimelineRow>雷电法术工厂随着部落都城玩法一同推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
