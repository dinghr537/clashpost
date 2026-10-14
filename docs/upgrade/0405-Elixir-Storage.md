---
title: "部落冲突 coc 圣水瓶升级数据"
navTitle: "圣水瓶"
shownTitle: "圣水瓶"
module: upgrade-home
imgFolder: home_buildings/0405
wiki: https://clashofclans.fandom.com/wiki/Elixir_Storage
canonical: /upgrade/0405-Elixir-Storage
dataSyncedOn: 2026-10-13
description: "圣水瓶用来保存从地下收集的圣水。升级圣水瓶以提升其存储上限。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0405-Elixir-Storage.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-11-17'">

<template #introduction>

- *如想查看夜世界的圣水瓶，请访问：[夜世界圣水瓶](/upgrade/1204-Elixir-Storage)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Elixir_Storage19.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

<SmallTitle>重要说明</SmallTitle>

[雷电法术](/upgrade/0100-Lightning-Spell) 和 [地震法术](/upgrade/0181-Earthquake-Spell) 不能对资源仓库造成伤害。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/11/17">
        <TimelineRow>18 本推出，并在 18 本新增 19 级圣水瓶。</TimelineRow>
        <TimelineRow>18 级圣水瓶的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/06/16">
        <TimelineRow>1 ~ 9 级圣水瓶的生命值减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>3 ~ 6、8 ~ 17 级圣水瓶的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/02/10">
        <TimelineRow>17 ~ 18 级圣水瓶的资源储量增加。</TimelineRow>
        <TimelineRow>2 ~ 8 级圣水瓶的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>17 本推出，并在 17 本新增 18 级圣水瓶。</TimelineRow>
        <TimelineRow>15 ~ 17 级圣水瓶的升级费用降低。</TimelineRow>
        <TimelineRow>17 级圣水瓶的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/18">
        <TimelineRow>12 ~ 16 级圣水瓶的升级时间减少。</TimelineRow>
        <TimelineRow>15 级圣水瓶的升级费用降低，与储金罐保持一致。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>新增 17 级圣水瓶，16 级大本营可解锁。</TimelineRow>
        <TimelineRow>15 级圣水瓶的升级费用由 550 万降低到 450 万。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>13 ~ 14 级圣水瓶的升级时间减少。</TimelineRow>
        <TimelineRow>13 ~ 14 级圣水瓶的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>15 本推出，并在 15 本新增 16 级圣水瓶。</TimelineRow>
        <TimelineRow>12 ~ 15 级圣水瓶的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>14 本推出，并在 14 本新增 15 级圣水瓶。</TimelineRow>
        <TimelineRow>2 ~ 3 级圣水瓶的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/12/09">
        <TimelineRow>新增 14 级圣水瓶，13 级大本营可解锁。</TimelineRow>
        <TimelineRow>13 级圣水瓶的容量增加 50 万。</TimelineRow>
        <TimelineRow>12 级大本营可掠夺的金币增加至 50 万（不含采集器和城堡）。</TimelineRow>
    </TimelineItem>
        <TimelineItem date="2019/04/02">
        <TimelineRow>10 ~ 13 级圣水瓶的升级时间减少。</TimelineRow>
        <TimelineRow>12 ~ 13 级圣水瓶的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
