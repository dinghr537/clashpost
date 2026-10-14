---
title: "部落冲突 coc 巨矛投手（粉胖）升级数据"
navTitle: "巨矛投手"
shownTitle: "巨矛投手（粉胖）"
module: upgrade-home
imgFolder: home_tech/0011
wiki: https://clashofclans.fandom.com/wiki/Thrower
canonical: /upgrade/0011-Thrower
dataSyncedOn: 2026-10-13
description: "这位力大无穷的投手目标明确，志在必得！他会从远处向敌人和防御建筑投掷威力十足的长矛。他哪来那么大力气？秘诀就在于他那浓密的胡须！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0011-Thrower.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2026-02-23'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Thrower_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2026/02/23">
        <TimelineRow>4 级巨矛投手的每秒伤害和生命值减少（回滚到 2026/01 平衡性调整的数据）。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2026/01/28">
        <TimelineRow>所有等级巨矛投手的生命值提升。</TimelineRow>
        <TimelineRow>2 ~ 4 级巨矛投手的伤害提升。</TimelineRow>
        <TimelineRow>巨矛投手的移动速度由 2 格/秒 提升到 2.25 格/秒。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/11/17">
        <TimelineRow>18 本推出，并在 18 本新增 4 级巨矛投手。</TimelineRow>
        <TimelineRow>2 ~ 3 级巨矛投手的升级时间和升级费用减少。</TimelineRow>
        <TimelineRow>3 级巨矛投手的生命值和每秒伤害增加。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/06/30">
        <TimelineRow>所有等级巨矛投手的生命值增加。</TimelineRow>
        <TimelineRow>所有等级巨矛投手的每秒伤害提升。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/27">
        <TimelineRow>部队的训练时间取消，但增加了捐赠费用。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/02/10">
        <TimelineRow>巨矛投手的训练时间由 3:10 改为 2:20</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>17 本推出，并在 16 本新增巨矛投手，共推出 3 个等级。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
