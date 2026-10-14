---
title: "部落冲突 coc 储金罐升级数据"
navTitle: "储金罐"
shownTitle: "储金罐"
module: upgrade-home
imgFolder: home_buildings/0404
wiki: https://clashofclans.fandom.com/wiki/Gold_Storage
canonical: /upgrade/0404-Gold-Storage
dataSyncedOn: 2026-10-13
description: "您珍贵的金币都存在这里！不要让狡猾的哥布林有机可乘！升级储金罐，提高它们的容量和抗打击能力。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0404-Gold-Storage.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-11-17'">

<template #introduction>

- *如想查看夜世界的储金罐，请访问：[夜世界储金罐](/upgrade/1203-Gold-Storage)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Gold_Storage19.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

<SmallTitle>重要说明</SmallTitle>

[雷电法术](/upgrade/0100-Lightning-Spell) 和 [地震法术](/upgrade/0181-Earthquake-Spell) 不能对资源仓库造成伤害。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/11/17">
        <TimelineRow>18 本推出，并在 18 本新增 19 级储金罐。</TimelineRow>
        <TimelineRow>18 级储金罐的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/06/16">
        <TimelineRow>1 ~ 9 级储金罐的生命值减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>3 ~ 6、8 ~ 17 级储金罐的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/02/10">
        <TimelineRow>17 ~ 18 级储金罐的资源储量增加。</TimelineRow>
        <TimelineRow>2 ~ 8 级储金罐的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>17 本推出，并在 17 本新增 18 级储金罐。</TimelineRow>
        <TimelineRow>15 ~ 17 级储金罐的升级费用降低。</TimelineRow>
        <TimelineRow>17 级储金罐的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/18">
        <TimelineRow>12 ~ 16 级储金罐的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>新增 17 级储金罐，16 级大本营可解锁。</TimelineRow>
        <TimelineRow>15 级储金罐的升级费由 550 万降低到 450 万。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>13 ~ 14 级储金罐的升级时间减少。</TimelineRow>
        <TimelineRow>13 ~ 14 级储金罐的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>15 本推出，并在 15 本新增 16 级储金罐。</TimelineRow>
        <TimelineRow>12 ~ 15 级储金罐的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>14 本推出，并在 14 本新增 15 级储金罐。</TimelineRow>
        <TimelineRow>2 ~ 3 级储金罐的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/12/09">
        <TimelineRow>新增 14 级储金罐，13 级大本营可解锁。</TimelineRow>
        <TimelineRow>13 级储金罐的容量增加 50 万。</TimelineRow>
        <TimelineRow>12 级大本营可掠夺的金币增加至 50 万（不含采集器和城堡）。</TimelineRow>
    </TimelineItem>
        <TimelineItem date="2019/04/02">
        <TimelineRow>10 ~ 13 级储金罐的升级时间减少。</TimelineRow>
        <TimelineRow>12 ~ 13 级储金罐的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
