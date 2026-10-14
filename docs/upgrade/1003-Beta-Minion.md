---
title: "部落冲突 coc 夜世界异变亡灵（变异亡灵）升级数据"
navTitle: "异变亡灵"
shownTitle: "异变亡灵（变异亡灵）"
module: upgrade-bh
imgFolder: bh_tech/1003
wiki: https://clashofclans.fandom.com/wiki/Beta_Minion
canonical: /upgrade/1003-Beta-Minion
dataSyncedOn: 2026-10-13
description: "可远距离攻击目标，在暗夜中闪闪发光，于舞池中疯狂不已。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/1003-Beta-Minion.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-05-15'">

<template #introduction>

- *如想查看家乡的亡灵，请访问：[亡灵](/upgrade/0080-Minion)。*
- *如想查看家乡的超级亡灵，请访问：[超级亡灵](/upgrade/0608-Super-Minion)。*
- *如想查看都城的亡灵大军，请访问：[都城亡灵大军](/upgrade/2004-Minion-Horde)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Beta_Minion_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

\* 超强狙击：异变亡灵的前几次攻击速度更快，攻击距离更远，并造成额外伤害。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/05/15">
        <TimelineRow>新增 19 - 20 级异变亡灵。</TimelineRow>
        <TimelineRow>由于夜世界重做，部队的伤害、生命值等数据都有变化。</TimelineRow>
        <TimelineRow>异变亡灵的移动速度由 32（4 格/秒） 提升至 38.4（4.8 格/秒）。</TimelineRow>
        <TimelineRow>现在异变亡灵一解锁就是 3 级，你不需要从 1 级开始升了。如果更新前部队高于 3 级，更新后等级不会重置。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/05/02">
        <TimelineRow>夜世界所有空军的攻击距离减少 0.5 格（蝙蝠除外）。</TimelineRow>
        <TimelineRow>异变亡灵的远程狙杀技能的攻击距离减少 0.5 格。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/06/18">
        <TimelineRow>夜世界 9 本开放，所有兵种可升至 18 级。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
