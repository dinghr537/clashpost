---
title: "部落冲突 coc 都城大本营升级数据"
navTitle: "都城大本营"
shownTitle: "都城大本营"
module: upgrade-capital
imgFolder: capital_buildings/2400
wiki: https://clashofclans.fandom.com/wiki/Capital_Hall
canonical: /upgrade/2400-Capital-Hall
dataSyncedOn: 2026-10-13
description: "它是都城的核心！升级都城大本营以解锁新的子城，并提高都城之巅建筑的等级上限。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/2400-Capital-Hall.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2022-05-02'">

<template #introduction>

- *如想查看家乡的大本营，请访问：[大本营](/upgrade/0400-Town-Hall)。*
- *如想查看夜世界的大本营，请访问：[建筑大师大本营](/upgrade/1200-Builder-Hall)，[夜世界奥仔哨站](/upgrade/1240-O.T.T.O's-Outpost)。*
- *如想查看子城大本营，请访问：[子城大本营](/upgrade/2401-District-Hall)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Capital_Hall10.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2022/05/02">
        <TimelineRow>都城大本营随着部落都城玩法一同推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
