---
title: "部落冲突 coc 都城超级巨人岗哨升级数据"
navTitle: "超级巨人岗哨"
shownTitle: "超级巨人岗哨"
module: upgrade-capital
imgFolder: capital_buildings/2210
wiki: https://clashofclans.fandom.com/wiki/Super_Giant_Post
canonical: /upgrade/2210-Super-Giant-Post
dataSyncedOn: 2026-10-13
description: "超级巨人跃跃欲试，准备给入侵的敌军一顿痛揍。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/2210-Super-Giant-Post.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2022-05-02'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Super_Giant_Post5.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2022/05/02">
        <TimelineRow>超级巨人岗哨随着部落都城玩法一同推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
