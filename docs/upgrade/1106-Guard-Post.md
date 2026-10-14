---
title: "部落冲突 coc 夜世界守卫岗哨升级数据"
navTitle: "守卫岗哨"
shownTitle: "守卫岗哨"
module: upgrade-bh
imgFolder: bh_buildings/1106
wiki: https://clashofclans.fandom.com/wiki/Guard_Post
canonical: /upgrade/1106-Guard-Post
dataSyncedOn: 2026-10-13
description: "部队驻扎于此，协助守卫村庄！这些士气高昂的部队肯定能延缓敌军进攻。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/1106-Guard-Post.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-05-15'">

<template #introduction>

- *如需查看都城的那几个岗哨，请自行前往相关页面。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Guard_Post10.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

追击距离：当敌军进入这个范围时，守卫岗哨中的部队会追击敌军。<br>
巡逻距离：当部队未进入追击距离时，守卫岗哨中的兵种会在建筑周围 3 格行走。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/05/15">
        <TimelineRow>夜世界重做，建筑的数值重新平衡，伤害、生命值等数据有变化。</TimelineRow>
        <TimelineRow>6 ~ 9 级守卫岗哨的升级时间增加。</TimelineRow>
        <TimelineRow>夜世界 10 本推出，守卫岗哨可升至 10 级。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/06/18">
        <TimelineRow>夜世界 9 本推出，守卫岗哨可升至 9 级。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
