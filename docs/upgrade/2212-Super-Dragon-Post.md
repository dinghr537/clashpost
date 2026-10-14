---
title: "部落冲突 coc 都城超级飞龙岗哨升级数据"
navTitle: "超级飞龙岗哨"
shownTitle: "超级飞龙岗哨"
module: upgrade-capital
imgFolder: capital_buildings/2212
wiki: https://clashofclans.fandom.com/wiki/Super_Dragon_Post
canonical: /upgrade/2212-Super-Dragon-Post
dataSyncedOn: 2026-10-13
description: "超级飞龙领地意识极强，任何来犯之敌都逃不过它们的龙息炙烤。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/2212-Super-Dragon-Post.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2022-05-02'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Super_Dragon_Post4.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2022/05/02">
        <TimelineRow>超级飞龙岗哨随着部落都城玩法一同推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
