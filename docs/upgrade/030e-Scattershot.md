---
title: "部落冲突 coc 投石炮（投石机）升级数据"
navTitle: "投石炮"
shownTitle: "投石炮（投石机）"
module: upgrade-home
imgFolder: home_buildings/030e
wiki: https://clashofclans.fandom.com/wiki/Scattershot
canonical: /upgrade/030e-Scattershot
dataSyncedOn: 2026-10-13
description: "投石炮朝射程内最近的目标发射又大又重的石块，但这些石块捆得并不牢固，它们撞击目标后会散开，对目标后方的部队造成溅射伤害。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/030e-Scattershot.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-11-17'">

<template #introduction>

- *玩家所说的投石车指的是攻城烈焰车，而不是投石炮，攻城烈焰车的数据请参考： [攻城烈焰车](/upgrade/0245-Flame-Flinger)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Scattershot6_hd.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

<SmallTitle>重要说明</SmallTitle>

1. 投石炮的溅射伤害会随着距离增加而减小。它会对瞄准的目标造成最大伤害，对距离目标 1 格的单位造成最小伤害。
2. 投石炮击中目标后会爆炸，爆炸后会对攻击方向向前 1 ~ 5 格散射 90° 并造成散射伤害，这个伤害随距离递减。最大散射伤害是对距离目标 1 格的单位造成的，最小散射伤害是对距离目标 5 格的单位造成的。
3. 投石炮的溅射伤害和散射伤害不能同时作用于地面目标和空中目标，瞄准地面目标就无法对空中目标造成伤害，反之亦然。
4. 投石炮必须装弹才能工作，这个装弹操作会在玩家登录游戏时自动进行，但如果玩家长时间不登录，弹药就会用完，从而导致防御失效。
    - 用完投石炮的弹药需要 4 分 51 秒。

\* 按照官方说法，投石炮的攻速为 3.228 秒/次，但经实测，这个零头并不存在，其实际攻速就是 3.2 秒/次。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/11/17">
        <TimelineRow>6 级投石炮的升级时间和升级费用减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/10/06">
        <TimelineRow>1 ~ 5 级投石炮的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/06/30">
        <TimelineRow>3 ~ 6 级投石炮的每秒伤害值减少。</TimelineRow>
        <TimelineRow>投石炮充能提升的每秒伤害值减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>1 ~ 5 级投石炮的升级时间减少。</TimelineRow>
        <TimelineRow>3 ~ 5 级投石炮的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/02/10">
        <TimelineRow>17 本新增 6 级投石炮。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>1 ~ 5 级投石炮的升级时间减少。</TimelineRow>
        <TimelineRow>1 ~ 2、4 ~ 5 级投石炮的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/09/09">
        <TimelineRow>超级充能推出，投石炮是第一批可以充能的建筑之一。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/18">
        <TimelineRow>4 级投石炮的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/02/27">
        <TimelineRow>16 本新增 5 级投石炮。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>所有等级投石炮的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/09/28">
        <TimelineRow>3 级投石炮的升级费用降低。</TimelineRow>
        <TimelineRow>4 级投石炮的每秒伤害降低 15。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>15 本新增 4 级投石炮。</TimelineRow>
        <TimelineRow>1 ~ 2 级投石炮的升级时间减少。</TimelineRow>
        <TimelineRow>1 ~ 2 级投石炮的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>1 ~ 3 级投石炮的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>14 本推出，并在 14 本新增 3 级投石炮。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/12/07">
        <TimelineRow>投石炮的攻击速度从 3.036 秒/次减慢至 3.228 秒/次。</TimelineRow>
        <TimelineRow>投石炮的每秒伤害值降低 10。</TimelineRow>
        <TimelineRow>提升投石炮的生命值。（1 级：3000 → 3600，2 级：3500 → 4200）</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/06/22">
        <TimelineRow>投石炮的攻击速度从 3 秒/次减慢到 3.036 秒/次。</TimelineRow>
        <TimelineRow>投石炮现在可能会出现弹药用尽的情况，和X连弩、地狱之塔类似。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/12/09">
        <TimelineRow>13 本推出，并在 13 本新增建筑：投石炮。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
