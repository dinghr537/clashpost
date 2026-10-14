---
title: "部落冲突 coc 都城爆炸强弩升级数据"
navTitle: "爆炸强弩"
shownTitle: "爆炸强弩"
module: upgrade-capital
imgFolder: capital_buildings/220f
wiki: https://clashofclans.fandom.com/wiki/Blast_Bow
canonical: /upgrade/220f-Blast-Bow
dataSyncedOn: 2026-10-13
description: "树干那么粗的箭有多危险？爆炸强弩的出现让这个古老的问题有了答案，那就是：毫不意外，非常危险。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/220f-Blast-Bow.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-09-14'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Blast_Bow5.png" :imgAlt="$frontmatter.navTitle"
    description="树干那么粗的箭有多危险？<br>爆炸强弩的出现让这个古老的问题有了答案，那就是：毫不意外，非常危险。"
    :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/09/14">
        <TimelineRow>2 ~ 5 级爆炸强弩的每秒伤害降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/05/02">
        <TimelineRow>爆炸强弩随着部落都城玩法一同推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
