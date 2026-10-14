---
title: "部落冲突 coc 都城超级特斯拉电磁塔升级数据"
navTitle: "超级特斯拉电磁塔"
shownTitle: "超级特斯拉电磁塔"
module: upgrade-capital
imgFolder: capital_buildings/220b
wiki: https://clashofclans.fandom.com/wiki/Hidden_Mega_Tesla
canonical: /upgrade/220b-Hidden-Mega-Tesla
dataSyncedOn: 2026-10-13
description: "如果特斯拉电磁塔变得超级庞大会怎样？即使面对最强大的敌军，它的超强力电流也能对他们造成重创！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/220b-Hidden-Mega-Tesla.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2022-05-02'">

<template #introduction>

- *如想查看家乡的巨型特斯拉电磁塔（12 本自带武器），请访问：[巨型特斯拉电磁塔](/upgrade/030c-Giga-Tesla)。*
- *如想查看夜世界的超级特斯拉电磁塔，请访问：[夜世界超级特斯拉电磁塔](/upgrade/110b-Mega-Tesla)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Hidden_Mega_Tesla5.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2022/05/02">
        <TimelineRow>超级特斯拉电磁塔随着部落都城玩法一同推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
