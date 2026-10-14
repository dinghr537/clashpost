---
title: "部落冲突 coc 夜世界巨人拳击手升级数据"
navTitle: "巨人拳击手"
shownTitle: "巨人拳击手"
module: upgrade-bh
imgFolder: bh_tech/1002
wiki: https://clashofclans.fandom.com/wiki/Boxer_Giant
canonical: /upgrade/1002-Boxer-Giant
dataSyncedOn: 2026-10-13
description: "别看巨人行动笨拙、体壮如牛，他们可是一直在练习拳击！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/1002-Boxer-Giant.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-05-15'">

<template #introduction>

- *如想查看家乡的巨人，请访问：[巨人](/upgrade/0002-Giant)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Boxer_Giant_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

\* 如果玩家没有手动触发这个技能，那么即将死亡时会强制触发一次，提前触发的话即将死亡时就没有无敌效果了。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/05/15">
        <TimelineRow>新增 19 - 20 级巨人拳击手。</TimelineRow>
        <TimelineRow>由于夜世界重做，部队的伤害、生命值等数据都有变化。</TimelineRow>
        <TimelineRow>巨人拳击手现在有两个技能了，本次更新在原有“重拳出击”技能的基础上加了个一次性技能“拳手格挡”。</TimelineRow>
        <TimelineRow>巨人拳击手的兵种重量从 8 提升至 18。</TimelineRow>
        <TimelineRow>巨人拳击手的移动速度由 12（1.5 格/秒） 提升至 14.4（1.8 格/秒）。</TimelineRow>
        <TimelineRow>现在巨人拳击手一解锁就是 3 级，你不需要从 1 级开始升了。如果更新前部队高于 3 级，更新后等级不会重置。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/06/22">
        <TimelineRow>巨人拳击手的兵种重量从 5 提升至 8。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/06/18">
        <TimelineRow>夜世界 9 本开放，所有兵种可升至 18 级。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
