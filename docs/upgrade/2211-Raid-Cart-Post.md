---
title: "部落冲突 coc 都城突袭炮车岗哨升级数据"
navTitle: "突袭炮车岗哨"
shownTitle: "突袭炮车岗哨"
module: upgrade-capital
imgFolder: capital_buildings/2211
wiki: https://clashofclans.fandom.com/wiki/Raid_Cart_Post
canonical: /upgrade/2211-Raid-Cart-Post
dataSyncedOn: 2026-10-13
description: "如果突袭炮车也能感受到快乐，那它最快乐的事一定是朝敌人开炮。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/2211-Raid-Cart-Post.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2022-05-02'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Raid_Cart_Post5.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2022/05/02">
        <TimelineRow>突袭炮车岗哨随着部落都城玩法一同推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
