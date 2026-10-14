---
title: "部落冲突 coc 急速法术（加速法术）升级数据"
navTitle: "急速法术"
shownTitle: "急速法术（加速法术）"
module: upgrade-home
imgFolder: home_tech/0182
wiki: https://clashofclans.fandom.com/wiki/Haste_Spell
canonical: /upgrade/0182-Haste-Spell
dataSyncedOn: 2026-10-13
description: "即使最笨重的兵种也能加点速了！急速法术虽不像狂暴法术能提升伤害，但却可以更好地提升移动速度。它占用空间小，您可以将更多急速法术带到战场之中！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0182-Haste-Spell.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-11-17'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Haste_Spell.png" :imgAlt="$frontmatter.navTitle"
    description="即使最笨重的兵种也能加点速了！<br>急速法术虽不像狂暴法术能提升伤害，但却可以更好地提升移动速度。它占用空间小，您可以将更多急速法术带到战场之中！"
    :isSmallImg="true" />

\* 脉冲有效时间比脉冲间隔时间要长，这意味着部队离开法术范围后，仍然会保持效果 0.7 到 1 秒。

\# 表格中每 8 点速度值代表 1 格/秒。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/11/17">
        <TimelineRow>18 本推出，并在 18 本新增 7 级急速法术。</TimelineRow>
        <TimelineRow>6 级急速法术的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/27">
        <TimelineRow>法术的配置时间取消，但新增了捐赠费用。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>2、4 ~ 4 级急速法术的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/02/10">
        <TimelineRow>17 本新增 6 级急速法术。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>3 ~ 5 级急速法术的升级时间减少。</TimelineRow>
        <TimelineRow>2 ~ 5 级急速法术的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/18">
        <TimelineRow>4 ~ 5 级急速法术的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>2 级急速法术的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>3 ~ 5 级急速法术的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/12/09">
        <TimelineRow>2 ~ 5 级急速法术的升级费用降低。</TimelineRow>
        <TimelineRow>2 ~ 4 级急速法术的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>2 ~ 4 级急速法术的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/12/09">
        <TimelineRow>2 ~ 5 级急速法术的配置费用提高。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/06/18">
        <TimelineRow>11 本新增 5 级急速法术。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
