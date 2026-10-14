---
title: "部落冲突 coc 都城哥布林大本营数据"
navTitle: "哥布林大本营"
shownTitle: "哥布林大本营"
module: upgrade-capital
imgFolder: capital_buildings/2509
wiki: https://clashofclans.fandom.com/wiki/Houses
canonical: /upgrade/2509-Goblin-Hall
dataSyncedOn: 2026-10-13
description: "一座异常安静的哥布林大本营，没有平日里密谋策略的声音，也没有金币声。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/2509-Goblin-Hall.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-10-09'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Goblin_Hall.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/10/09">
        <TimelineRow>新建筑：哥布林大本营。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
