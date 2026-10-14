---
title: "部落冲突 coc 皇家幽灵升级数据"
navTitle: "皇家幽灵"
shownTitle: "皇家幽灵"
module: upgrade-temp
imgFolder: temp_troops/0e07
wiki: https://clashofclans.fandom.com/wiki/Royal_Ghost
canonical: /upgrade/0e07-Royal-Ghost
dataSyncedOn: 2026-10-13
description: "透明的皇家幽灵很难被人注意到，他为此很苦恼，因此决心大肆破坏来找回应有的存在感。皇家幽灵实在太透明了，有时候连城墙都不会阻拦他！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0e07-Royal-Ghost.json";
</script>

<SyncedUnitData :data="unitData">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Royal_Ghost_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

\* 皇家幽灵在部署后的 12 秒内不能被锁定为目标，也不能被城墙阻拦。此外，被皇家幽灵命中的目标还有减速效果。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2022/10">
        <TimelineRow>该兵种第 3 次推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/10">
        <TimelineRow>该兵种第 2 次推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/10">
        <TimelineRow>该兵种第 1 次推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
