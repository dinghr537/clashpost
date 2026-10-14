---
title: "部落冲突 coc 巨石碑（擎天巨柱、黑油塔）升级数据"
navTitle: "巨石碑"
shownTitle: "巨石碑（擎天巨柱、黑油塔）"
module: upgrade-home
imgFolder: home_buildings/0312
wiki: https://clashofclans.fandom.com/wiki/Monolith
canonical: /upgrade/0312-Monolith
dataSyncedOn: 2026-10-13
description: "建筑工人首次尝试使用暗黑重油，建造出了一个极其可怕的庞然大物。巨石碑面对的目标越强，造成的伤害就越高。它是保卫村庄的利器，也是敌人的噩梦。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0312-Monolith.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-11-17'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Monolith4_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

1. 巨石碑每次攻击不仅会造成基础伤害，还会以目标的最大生命值为基准造成一定百分比的额外伤害，因此巨石碑对高生命值单位极具威胁。
2. [狂暴法术塔](/upgrade/0311-Spell-Tower) 释放出来的狂暴法术只能提升巨石碑的普通攻击，不能提升巨石碑的额外伤害。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/11/17">
        <TimelineRow>4 级巨石碑的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>17 本新增 4 级巨石碑，并成为可以充能的建筑。</TimelineRow>
        <TimelineRow>1 ~ 3 级巨石碑的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>1 ~ 3 级巨石碑的升级时间减少。</TimelineRow>
        <TimelineRow>2 ~ 3 级巨石碑的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/18">
        <TimelineRow>1 ~ 2 级巨石碑的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/04/17">
        <TimelineRow>16 本新增 3 级巨石碑。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>所有等级巨石碑的额外伤害减少 1%.</TimelineRow>
        <TimelineRow>2 级巨石碑的每秒基础伤害降低 25。</TimelineRow>
        <TimelineRow>所有等级巨石碑的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/12/12">
        <TimelineRow>所有等级巨石碑的额外伤害减少 2%.</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>15 本推出，并在 15 本新增建筑：巨石碑。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
