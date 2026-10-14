---
title: "部落冲突 coc 复合机械塔升级数据"
navTitle: "复合机械塔"
shownTitle: "复合机械塔"
module: upgrade-home
imgFolder: home_buildings/0317
wiki: https://clashofclans.fandom.com/wiki/Multi-Gear_Tower
canonical: /upgrade/0317-Multi-Gear-Tower
dataSyncedOn: 2026-10-13
description: "复合机械塔是两种经典防御建筑的强力结合体！选择适合您的攻击模式，释放毁灭之力！可攻击空中和地面单位。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0317-Multi-Gear-Tower.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2026-01-28'">

<template #introduction>

- *如想查看合并前的建筑，请移步：[加农炮](/upgrade/0301-Cannon)、[箭塔](/upgrade/0302-Archer-Tower)。*

<SwitchTabs contentClass="cp-unit-items" :stickyTabs="true" :pageTabs="true">
    <SwitchTab tabId="cp-unit-item-0" :activeTab="true">远程攻击模式</SwitchTab>
    <SwitchTab tabId="cp-unit-item-1">快速攻击模式</SwitchTab>
</SwitchTabs>

<SwitchTabGroup id="cp-unit-item-0" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Multi-Gear_Tower3_LongRange_hd.png" imgAlt="复合机械塔（远程攻击模式）" :description="$frontmatter.description" :isSmallImg="true" />

<SmallTitle>重要说明</SmallTitle>

1. 复合机械塔由一个改装后的 21 级 [加农炮](/upgrade/0301-Cannon) 和一个改装后的 21 级 [箭塔](/upgrade/0302-Archer-Tower) 合并而来。
    - 合并一旦开始就无法取消。
    - 合并建筑的操作是永久性的，一旦合并就无法拆开。
    - 如果你的加农炮或箭塔未改装，则无法合并。
    - 升本前必须合并完所有可以合并的建筑。
2. 复合机械塔有两种模式，远程攻击模式和快速攻击模式。其中远程攻击模式的射程更远，但伤害略低，且攻速较慢（伤害溢出高）；快速攻击模式攻速快（伤害溢出低）、伤害高，但射程较近。

</SwitchTabGroup>

<SwitchTabGroup id="cp-unit-item-1" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Multi-Gear_Tower3_FastAttack_hd.png" imgAlt="复合机械塔（快速攻击模式）" :description="$frontmatter.description" :isSmallImg="true" />

<SmallTitle>重要说明</SmallTitle>

1. 复合机械塔由一个改装后的 21 级 [加农炮](/upgrade/0301-Cannon) 和一个改装后的 21 级 [箭塔](/upgrade/0302-Archer-Tower) 合并而来。
    - 合并一旦开始就无法取消。
    - 如果你的加农炮或箭塔未改装，则无法合并。
    - 升本前必须合并完所有可以合并的建筑。
2. 复合机械塔有两种模式，远程攻击模式和快速攻击模式。其中远程攻击模式的射程更远，但伤害略低，且攻速较慢（伤害溢出高）；快速攻击模式攻速快（伤害溢出低）、伤害高，但射程较近。

\* 在快速攻击模式下，4 连发期间每发 0.192 秒，之后停顿 0.383 秒。如果目标在复合机械塔还没打完 4 连发之前死亡，导致复合机械塔没有发射全部 4 发炮弹时，每发没有射出去的炮弹会减少 0.192 秒攻击间隔。这里的 0.96 是这么算的：0.192 * (4 - 1) + 0.383 = 0.959 (秒) ≈ 0.96 (秒)。

</SwitchTabGroup>

</template>

<template #history>

<Timeline>
    <TimelineItem date="2026/01/28">
        <TimelineRow>所有等级复合机械塔在远程攻击模式下的伤害提升，在快速攻击模式下的伤害降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/11/17">
        <TimelineRow>18 本推出，并在 18 本新增 3 级复合机械塔。</TimelineRow>
        <TimelineRow>1 ~ 2 级复合机械塔的升级时间和升级费用减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>复合机械塔成为可以充能的建筑。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/02/10">
        <TimelineRow>在 17 本新增复合机械塔。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
