---
title: "部落冲突 coc 防空火箭升级数据"
navTitle: "防空火箭"
shownTitle: "防空火箭"
module: upgrade-home
imgFolder: home_buildings/0304
wiki: https://clashofclans.fandom.com/wiki/Air_Defense
canonical: /upgrade/0304-Air-Defense
dataSyncedOn: 2026-10-13
description: "防空火箭是歼灭敌军空中部队的利器，可惜它不能攻击地面上的敌人。请巧妙部署防空火箭，最大限度保护您的领空。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0304-Air-Defense.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-11-17'">

<template #introduction>

- *如想查看夜世界的多管防空火炮，请访问：[夜世界防空火炮](/upgrade/1104-Firecrackers)。*
- *如想查看都城的多管防空火箭，请访问：[都城防空火箭](/upgrade/2203-Air-Defense)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Air_Defense16.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/11/17">
        <TimelineRow>18 本推出，并在 18 本新增 16 级防空火箭。</TimelineRow>
        <TimelineRow>15 级防空火箭的升级时间和升级费用减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/10/06">
        <TimelineRow>14 级防空火箭的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>1、3 ~ 6、14 级防空火箭的升级时间减少。</TimelineRow>
        <TimelineRow>3、10 ~ 14 级防空火箭的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/02/10">
        <TimelineRow>1 ~ 2 级防空火箭的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>17 本推出，并在 17 本新增 15 级防空火箭。</TimelineRow>
        <TimelineRow>10 ~ 14 级防空火箭的升级时间减少。</TimelineRow>
        <TimelineRow>11 ~ 14 级防空火箭的升级费用降低。</TimelineRow>
        <TimelineRow>防空火箭成为第二批可以充能的建筑。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/18">
        <TimelineRow>2 ~ 4、10 ~ 13 级防空火箭的升级时间减少。</TimelineRow>
        <TimelineRow>12 ~ 13 级防空火箭的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>16 本推出，并在 15 本新增 14 级防空火箭。</TimelineRow>
        <TimelineRow>2 ~ 13 级防空火箭的升级时间减少。</TimelineRow>
        <TimelineRow>5 ~ 6、8 ~ 9、12 ~ 13 级防空火箭的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>10 ~ 11 级防空火箭的升级时间减少。</TimelineRow>
        <TimelineRow>10 ~ 11 级防空火箭的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>15 本推出，并在 15 本新增 13 级防空火箭。</TimelineRow>
        <TimelineRow>8 ~ 12 级防空火箭的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/09/13">
        <TimelineRow>12 级防空火箭的每秒伤害增加。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/05/02">
        <TimelineRow>12 级防空火箭：生命值从 1600 提升至 1650。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/12/09">
        <TimelineRow>6 ~ 11 级防空火箭的升级费用降低。</TimelineRow>
    </TimelineItem>
        <TimelineItem date="2021/06/15">
        <TimelineRow>14 本新增 12 级防空火箭。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>1、6 ~ 9 级防空火箭的升级费用降低。</TimelineRow>
        <TimelineRow>8 ~ 9 级防空火箭的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/01/20">
        <TimelineRow>修复了 11 级防空火箭的命中效果。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/10/12">
        <TimelineRow>10 本的 8 级防空血量加 10，这样一来必须要 4 个 7 级闪电才能打掉一个 8 级防空。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/12/09">
        <TimelineRow>13 本新增 11 级防空火箭。</TimelineRow>
    </TimelineItem>
        <TimelineItem date="2019/04/02">
        <TimelineRow>7 ~ 10 级防空火箭的升级费用降低。</TimelineRow>
        <TimelineRow>3 ~ 7 级防空火箭的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
