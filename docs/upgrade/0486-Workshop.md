---
title: "部落冲突 coc 攻城机器工坊升级数据"
navTitle: "攻城机器工坊"
shownTitle: "攻城机器工坊"
module: upgrade-home
imgFolder: home_buildings/0486
wiki: https://clashofclans.fandom.com/wiki/Workshop
canonical: /upgrade/0486-Workshop
dataSyncedOn: 2026-10-13
description: "攻城机器工坊是专门建造攻城机器的地方。升级攻城机器工坊以解锁不同的攻城机器！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0486-Workshop.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-10-06'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Workshop8.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/10/06">
        <TimelineRow>3 ~ 8 级攻城机器工坊的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>1 ~ 3、5 ~ 8 级攻城机器工坊的升级时间减少。</TimelineRow>
        <TimelineRow>2 ~ 8 级攻城机器工坊的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/02/10">
        <TimelineRow>16 本新增 8 级攻城机器工坊，新攻城机器：部队发射器。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>3 ~ 7 级攻城机器工坊的升级时间减少。</TimelineRow>
        <TimelineRow>1 ~ 3、7 级攻城机器工坊的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/18">
        <TimelineRow>4 ~ 7 级攻城机器工坊的升级时间减少。</TimelineRow>
        <TimelineRow>7 级攻城机器工坊的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>6 ~ 7 级攻城机器工坊厂的升级时间减少。</TimelineRow>
        <TimelineRow>6 级攻城机器工坊厂的升级费用 1650 万减少到 1400 万。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>1 ~ 5 级攻城机器工坊的升级时间减少。</TimelineRow>
        <TimelineRow>1 ~ 5 级攻城机器工坊的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>攻城机器工坊升级时兵种可继续建造攻城机器，但建造速度减半（建造时间翻倍）。</TimelineRow>
        <TimelineRow>15 本推出，并在 15 本新增 7 级攻城机器工坊，可解锁新的攻城机器：攻城钻机。</TimelineRow>
        <TimelineRow>1 ~ 6 级攻城机器工坊的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/12/09">
        <TimelineRow>1 ~ 2 级攻城机器工坊的升级费用降低。</TimelineRow>
        <TimelineRow>14 本新增 6 级攻城机器工坊，新攻城机器：攻城烈焰车。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/12/07">
        <TimelineRow>13 本可以将攻城机器工坊升到 5 级了，新攻城机器：攻城滚木车。</TimelineRow>
    </TimelineItem>
        <TimelineItem date="2019/04/02">
        <TimelineRow>13 本可以将攻城机器工坊升到 4 级了，新攻城机器：攻城训练营。</TimelineRow>
        <TimelineRow>攻城机器工坊的占地面积由 5*5 改为 4*4，但是判定面积没变。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
