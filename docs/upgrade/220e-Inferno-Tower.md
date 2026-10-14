---
title: "部落冲突 coc 都城地狱之塔升级数据"
navTitle: "地狱之塔"
shownTitle: "地狱之塔"
module: upgrade-capital
imgFolder: capital_buildings/220e
wiki: https://clashofclans.fandom.com/wiki/Inferno_Tower/Clan_Capital
canonical: /upgrade/220e-Inferno-Tower
dataSyncedOn: 2026-10-13
description: "地狱之塔是高生命值部队的克星，可对其持续锁定的目标造成毁灭性的伤害。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/220e-Inferno-Tower.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-09-14'">

<template #introduction>

- *如想查看家乡的地狱之塔，请访问：[地狱之塔](/upgrade/030a-Inferno-Tower)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Inferno_Tower5.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

<SmallTitle>重要说明</SmallTitle>

都城的地狱之塔只有单目标模式，没有像家乡的那种多目标模式。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/09/14">
        <TimelineRow>4 ~ 5 级地狱之塔的每秒伤害（第一阶段和第二阶段）降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/05/02">
        <TimelineRow>地狱之塔随着部落都城玩法一同推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
