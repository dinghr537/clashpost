---
title: "部落冲突 coc 夜世界隐秘弓箭手升级数据"
navTitle: "隐秘弓箭手"
shownTitle: "隐秘弓箭手"
module: upgrade-bh
imgFolder: bh_tech/1001
wiki: https://clashofclans.fandom.com/wiki/Sneaky_Archer
canonical: /upgrade/1001-Sneaky-Archer
dataSyncedOn: 2026-10-13
description: "弓箭手隐身于月色中，她们甚至可以在被发现之前就将目标消灭。她们的弱点？高傲自负。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/1001-Sneaky-Archer.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-05-15'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Sneaky_Archer_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/05/15">
        <TimelineRow>新增 19 - 20 级隐秘弓箭手。</TimelineRow>
        <TimelineRow>由于夜世界重做，部队的伤害、生命值等数据都有变化。</TimelineRow>
        <TimelineRow>隐秘弓箭手的兵种重量从 2 提升至 3.</TimelineRow>
        <TimelineRow>隐秘弓箭手的移动速度由 24（3 格/秒）提升至 28.8（3.6 格/秒）。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>修复了狂暴野蛮人、超级野蛮人和隐秘弓箭手的技能持续时间计时不太准确的问题。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/06/22">
        <TimelineRow>隐秘弓箭手的兵种重量从 1 提升至 2.</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/06/18">
        <TimelineRow>夜世界 9 本开放，所有兵种可升至 18 级。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
