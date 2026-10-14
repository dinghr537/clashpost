---
title: "部落冲突 coc 空气炮（吹风机）升级数据"
navTitle: "空气炮"
shownTitle: "空气炮（吹风机）"
module: upgrade-home
imgFolder: home_buildings/0306
wiki: https://clashofclans.fandom.com/wiki/Air_Sweeper
canonical: /upgrade/0306-Air-Sweeper
dataSyncedOn: 2026-10-13
description: "空气炮利用强力气流控制着天空，可以击退飞行的敌人。空气炮仅能朝一个方向喷射气流，因此请旋转它们来发挥最大作用！。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0306-Air-Sweeper.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-03-24'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Air_Sweeper7.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

旋转时的调整角度：旋转时的调整角度是指玩家每次点击旋转按钮时调整的空气炮吹气口角度。<br>
可攻击的范围角：设定好方向后，空气炮可发现在 1 ~ 15 格范围内，且在空气炮的吹气口正前方正负 52.5° 的目标。<br>
气波角度：空气炮攻击时，可以发出 45° 大小的扇形气流。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/03/24">
        <TimelineRow>1 ~ 4 级空气炮的升级时间减少。</TimelineRow>
        <TimelineRow>1 ~ 5 级空气炮的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>6 ~ 7 级空气炮的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/12/09">
        <TimelineRow>6 ~ 7 级空气炮的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>所有等级空气炮的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/04/02">
        <TimelineRow>1 ~ 6 级空气炮的升级时间减少。</TimelineRow>
        <TimelineRow>4 ~ 7 级空气炮的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
