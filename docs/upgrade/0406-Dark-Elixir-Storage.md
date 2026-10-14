---
title: "部落冲突 coc 暗黑重油罐升级数据"
navTitle: "暗黑重油罐"
shownTitle: "暗黑重油罐"
module: upgrade-home
imgFolder: home_buildings/0406
wiki: https://clashofclans.fandom.com/wiki/Dark_Elixir_Storage
canonical: /upgrade/0406-Dark-Elixir-Storage
dataSyncedOn: 2026-10-13
description: "暗黑重油蕴藏的巨大能量是圣水的三倍，无法存储在普通的圣水瓶中，所以我们得建造一个立方体的暗黑重油罐来存储它。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0406-Dark-Elixir-Storage.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-11-17'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Dark_Elixir_Storage13.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

<SmallTitle>重要说明</SmallTitle>

[雷电法术](/upgrade/0100-Lightning-Spell) 和 [地震法术](/upgrade/0181-Earthquake-Spell) 不能对资源仓库造成伤害。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/11/17">
        <TimelineRow>18 本推出，并在 18 本新增 13 级暗黑重油罐。</TimelineRow>
        <TimelineRow>12 级暗黑重油罐的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/10/06">
        <TimelineRow>8 ~ 11 级暗黑重油罐的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>7 ~ 11 级暗黑重油罐的升级时间减少。</TimelineRow>
        <TimelineRow>6、9 ~ 11 级暗黑重油罐的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/02/10">
        <TimelineRow>10 ~ 12 级暗黑重油罐的资源储量增加。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>17 本推出，并在 17 本新增 12 级暗黑重油罐。</TimelineRow>
        <TimelineRow>5、10 ~ 11 级暗黑重油罐的升级时间减少。</TimelineRow>
        <TimelineRow>10 级暗黑重油罐的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/18">
        <TimelineRow>8 ~ 10 级暗黑重油罐的升级时间减少。</TimelineRow>
        <TimelineRow>9 ~ 10 级暗黑重油罐的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>新增 10 级暗黑重油罐，16 级大本营可解锁。</TimelineRow>
        <TimelineRow>6, 8 ~ 10 级暗黑重油罐的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>8 级暗黑重油罐的升级时间减少。</TimelineRow>
        <TimelineRow>7 ~ 8 级暗黑重油罐的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>15 本推出，并在 15 本新增 10 级暗黑重油罐。</TimelineRow>
        <TimelineRow>7 ~ 9 级暗黑重油罐的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>14 本推出，并在 14 本新增 9 级暗黑重油罐。</TimelineRow>
        <TimelineRow>1 ~ 2 级暗黑重油罐的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/12/09">
        <TimelineRow>新增 14 级暗黑重油罐，8 级大本营可解锁。</TimelineRow>
        <TimelineRow>12 级大本营可掠夺的黑油增加至 4000（不含采集器和城堡）。</TimelineRow>
    </TimelineItem>
        <TimelineItem date="2019/04/02">
        <TimelineRow>1 ~ 6 级暗黑重油罐的升级费用降低，7 级暗黑重油罐的升级费用提升。</TimelineRow>
        <TimelineRow>所有等级暗黑重油罐的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
