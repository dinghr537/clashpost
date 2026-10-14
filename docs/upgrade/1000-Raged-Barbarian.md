---
title: "部落冲突 coc 夜世界狂暴野蛮人升级数据"
navTitle: "狂暴野蛮人"
shownTitle: "狂暴野蛮人"
module: upgrade-bh
imgFolder: bh_tech/1000
wiki: https://clashofclans.fandom.com/wiki/Raged_Barbarian
canonical: /upgrade/1000-Raged-Barbarian
dataSyncedOn: 2026-10-13
description: "为什么野蛮人会狂暴不安、横冲直撞还满身戾气？没人敢去问他。也许是因为他找不到自己的剑了？"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/1000-Raged-Barbarian.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-10-09'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Raged_Barbarian_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/10/09">
        <TimelineRow>15 ~ 20 级狂暴野蛮人的每秒伤害增加。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/05/15">
        <TimelineRow>新增 19 - 20 级狂暴野蛮人。</TimelineRow>
        <TimelineRow>由于夜世界重做，部队的伤害、生命值等数据都有变化。</TimelineRow>
        <TimelineRow>狂暴野蛮人的兵种重量从 2 提升至 4.</TimelineRow>
        <TimelineRow>狂暴野蛮人的移动速度由 16 提升至 19.2.</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>修复了狂暴野蛮人、超级野蛮人和隐秘弓箭手的技能持续时间计时不太准确的问题。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/06/22">
        <TimelineRow>狂暴野蛮人的兵种重量从 1 提升至 2.</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/06/18">
        <TimelineRow>夜世界 9 本开放，所有兵种可升至 18 级。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
