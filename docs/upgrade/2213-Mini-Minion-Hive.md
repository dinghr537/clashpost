---
title: "部落冲突 coc 都城迷你亡灵巢升级数据"
navTitle: "迷你亡灵巢"
shownTitle: "迷你亡灵巢"
module: upgrade-capital
imgFolder: capital_buildings/2213
wiki: https://clashofclans.fandom.com/wiki/Mini-Minion_Hive
canonical: /upgrade/2213-Mini-Minion-Hive
dataSyncedOn: 2026-10-13
description: "这座防御建筑下面藏着一个地下巢穴，每次打开都会释放一群迷你亡灵，它们誓死捍卫自己的领地且极其凶猛，绝不放过任何来犯敌军。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/2213-Mini-Minion-Hive.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2022-12-12'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Mini-Minion_Hive4.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

\* 迷你亡灵巢的攻击节奏是 0.23 秒一发，12 发后休息 1.5 秒。注意：**连发期间迷你亡灵巢不会切换目标，可使用骷髅这种小单位反制。**

</template>

<template #history>

<Timeline>
    <TimelineItem date="2022/12/12">
        <TimelineRow>都城新防御：迷你亡灵巢。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
