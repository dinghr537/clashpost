---
title: "部落冲突 coc 都城滚木陷阱升级数据"
navTitle: "滚木陷阱"
shownTitle: "滚木陷阱"
module: upgrade-capital
imgFolder: capital_buildings/2282
wiki: https://clashofclans.fandom.com/wiki/Log_Trap
canonical: /upgrade/2282-Log-Trap
dataSyncedOn: 2026-10-13
description: "小心滚木。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/2282-Log-Trap.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2022-05-02'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Log_Trap5.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

\* 只有当兵种站在陷阱前方时才能触发。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2022/05/02">
        <TimelineRow>滚木陷阱随着部落都城玩法一同推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
