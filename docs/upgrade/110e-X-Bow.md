---
title: "部落冲突 coc 夜世界X连弩（十字连弩）升级数据"
navTitle: "X连弩"
shownTitle: "X连弩（十字连弩）"
module: upgrade-bh
imgFolder: bh_buildings/110e
wiki: https://clashofclans.fandom.com/wiki/X-Bow/Builder_Base
canonical: /upgrade/110e-X-Bow
dataSyncedOn: 2026-10-13
description: "X连弩会发射威力巨大的弩箭。您可将X连弩设置为攻击地面单位，或攻击空中单位。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/110e-X-Bow.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-05-15'">

<template #introduction>

- 如需查看家乡的X连弩，请访问：[X连弩](/upgrade/0309-X-Bow)。

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="X-Bow5_Ground.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

\* 夜世界的X连弩要么只对空，要么只对地，没有家乡那种空地两用的模式。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/05/15">
        <TimelineRow>夜世界 10 本推出，新建筑：X连弩。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
