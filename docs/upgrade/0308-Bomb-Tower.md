---
title: "部落冲突 coc 炸弹塔升级数据"
navTitle: "炸弹塔"
shownTitle: "炸弹塔"
module: upgrade-home
imgFolder: home_buildings/0308
wiki: https://clashofclans.fandom.com/wiki/Bomb_Tower
canonical: /upgrade/0308-Bomb-Tower
dataSyncedOn: 2026-10-13
description: "炸弹塔可以投掷炸弹轰炸附近的地面部队，被摧毁后会产生一个大爆炸！近战部队最好离它远点吧！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0308-Bomb-Tower.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-11-17'">

<template #introduction>

- *如想查看都城的炸弹塔，请访问：[都城炸弹塔](/upgrade/2205-Bomb-Tower)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Bomb_Tower13.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/11/17">
        <TimelineRow>18 本推出，并在 18 本新增 13 级炸弹塔。</TimelineRow>
        <TimelineRow>12 级炸弹塔的升级时间和升级费用减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/10/06">
        <TimelineRow>10 ~ 11 级炸弹塔的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>1 ~ 5、7 ~ 11 级炸弹塔的升级时间减少。</TimelineRow>
        <TimelineRow>3 ~ 5、7 ~ 11 级炸弹塔的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/02/10">
        <TimelineRow>6 级炸弹塔的升级时间减少。</TimelineRow>
        <TimelineRow>6 级炸弹塔的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>17 本推出，并在 17 本新增 12 级炸弹塔。</TimelineRow>
        <TimelineRow>5、7 ~ 11 级炸弹塔的升级时间减少。</TimelineRow>
        <TimelineRow>6、8 ~ 11 级炸弹塔的升级费用降低。</TimelineRow>
        <TimelineRow>炸弹塔成为第二批可以充能的建筑。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/18">
        <TimelineRow>7 ~ 10 级炸弹塔的升级时间减少。</TimelineRow>
        <TimelineRow>7 ~ 10 级炸弹塔的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>16 本推出，并在 16 本新增 11 级炸弹塔。</TimelineRow>
        <TimelineRow>所有等级炸弹塔的升级时间减少。</TimelineRow>
        <TimelineRow>1 ~ 6、9 级炸弹塔的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>7 ~ 8 级炸弹塔的升级时间减少。</TimelineRow>
        <TimelineRow>7 ~ 8 级炸弹塔的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>15 本推出，并在 15 本新增 10 级炸弹塔。</TimelineRow>
        <TimelineRow>4 ~ 9 级炸弹塔的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/12/09">
        <TimelineRow>1 ~ 8 级炸弹塔的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>14 本推出，并在 14 本新增 9 级炸弹塔。</TimelineRow>
        <TimelineRow>2 ~ 6 级炸弹塔的升级时间减少。</TimelineRow>
        <TimelineRow>1 ~ 6 级炸弹塔的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/03/30">
        <TimelineRow>13 本新增 8 级炸弹塔。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/02/28">
        <TimelineRow>5 ~ 7 级炸弹塔的血量由 1000/1200/1400 调整为 1050/1300/1600。</TimelineRow>
        <TimelineRow>5 ~ 7 级炸弹塔的每秒伤害由 46/52/60 调整为 48/56/64。</TimelineRow>
        <TimelineRow>6 ~ 7 级炸弹塔的摧毁爆炸伤害由 340/380 调整为 350/400。</TimelineRow>
    </TimelineItem>
        <TimelineItem date="2019/04/02">
        <TimelineRow>1 ~ 6 级炸弹塔的升级费用降低。</TimelineRow>
        <TimelineRow>1 ~ 5 级炸弹塔的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
