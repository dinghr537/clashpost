---
title: "部落冲突 coc 夜世界时光钟楼升级数据"
navTitle: "时光钟楼"
shownTitle: "时光钟楼"
module: upgrade-bh
imgFolder: bh_buildings/1283
wiki: https://clashofclans.fandom.com/wiki/Clock_Tower
canonical: /upgrade/1283-Clock-Tower
dataSyncedOn: 2026-10-13
description: "时光钟楼使您基地中的项目运行加快！采集资源、研究和建造的速度加快。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/1283-Clock-Tower.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-05-15'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Clock_Tower10.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/05/15">
        <TimelineRow>夜世界重做，建筑的数值重新平衡，伤害、生命值等数据有变化。</TimelineRow>
        <TimelineRow>5 ~ 9 级时光钟楼的升级费用增加。</TimelineRow>
        <TimelineRow>夜世界 10 本推出，时光钟楼可升至 10 级。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/05/15">
        <TimelineRow>考虑到部队训练时间和战争机器恢复时间都被移除，更新后，时光钟楼将主要作用于加速建筑和资源生产，具体调整如下：</TimelineRow>
        <TimelineRow>时光钟楼的提速效果从原来的 8 倍提升至 10 倍；</TimelineRow>
        <TimelineRow>时光钟楼提速时长从原来的 3 ~ 11 分钟对应提升至 14 ~ 30 分钟；</TimelineRow>
        <TimelineRow>时光钟楼提速冷却时间从 7 小时延长至 22 小时；</TimelineRow>
        <TimelineRow>跳过时光钟楼提速冷却时间所需的宝石数量减少。</TimelineRow>
    </TimelineItem>
     <TimelineItem date="2019/06/18">
        <TimelineRow>夜世界 9 本推出，时光钟楼可升至 9 级。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
