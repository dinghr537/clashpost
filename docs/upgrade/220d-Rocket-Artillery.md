---
title: "部落冲突 coc 都城火箭炮升级数据"
navTitle: "火箭炮"
shownTitle: "火箭炮"
module: upgrade-capital
imgFolder: capital_buildings/220d
wiki: https://clashofclans.fandom.com/wiki/Rocket_Artillery
canonical: /upgrade/220d-Rocket-Artillery
dataSyncedOn: 2026-10-13
description: "向空中和地面目标发射会爆炸的火箭。它百发百中，从未失手，真是令人惊叹！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/220d-Rocket-Artillery.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-09-14'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Rocket_Artillery5.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/09/14">
        <TimelineRow>2 ~ 5级火箭炮的每秒伤害降低</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/30">
        <TimelineRow>所有等级火箭炮的每秒伤害减少 10 点。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/05/02">
        <TimelineRow>火箭炮随着部落都城玩法一同推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
