---
title: "部落冲突 coc 子城大本营升级数据"
navTitle: "子城大本营"
shownTitle: "子城大本营"
module: upgrade-capital
imgFolder: capital_buildings/2401
wiki: https://clashofclans.fandom.com/wiki/District_Hall
canonical: /upgrade/2401-District-Hall
dataSyncedOn: 2026-10-13
description: "村民们和超级建筑工人在这里管理着子城。升级子城大本营以提高子城建筑的等级上限。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/2401-District-Hall.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2022-05-02'">

<template #introduction>

- *如想查看家乡的大本营，请访问：[大本营](/upgrade/0400-Town-Hall)。*
- *如想查看夜世界的大本营，请访问：[建筑大师大本营](/upgrade/1200-Builder-Hall)，[夜世界奥仔哨站](/upgrade/1240-O.T.T.O's-Outpost)。*
- *如想查看都城大本营，请访问：[都城大本营](/upgrade/2400-Capital-Hall)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="District_Hall5.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2022/05/02">
        <TimelineRow>子城大本营随着部落都城玩法一同推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
