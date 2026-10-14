---
title: "部落冲突 coc 都城疾速火箭（多管火箭）升级数据"
navTitle: "疾速火箭"
shownTitle: "疾速火箭（多管火箭）"
module: upgrade-capital
imgFolder: capital_buildings/2209
wiki: https://clashofclans.fandom.com/wiki/Rapid_Rockets
canonical: /upgrade/2209-Rapid-Rockets
dataSyncedOn: 2026-10-13
description: "这台机器装填有多发火箭。和防空火箭相比，它射程更短，但攻势更猛烈，弥补了射程上的不足。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/2209-Rapid-Rockets.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-09-14'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Rapid_Rockets5.png" :imgAlt="$frontmatter.navTitle"
    description="这台机器装填有多发火箭。<br>和防空火箭相比，它射程更短，但攻势更猛烈，弥补了射程上的不足。"
    :isSmallImg="true" />

* 疾速的攻击节奏是 0.32 秒一发，5 发后休息 0.55 秒。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/09/14">
        <TimelineRow>2 ~ 5 级疾速火箭的每秒伤害降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/05/02">
        <TimelineRow>疾速火箭随着部落都城玩法一同推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
