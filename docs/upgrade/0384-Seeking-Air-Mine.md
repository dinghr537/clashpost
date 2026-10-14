---
title: "部落冲突 coc 搜空地雷（黑炸）升级数据"
navTitle: "搜空地雷"
shownTitle: "搜空地雷（黑炸）"
module: upgrade-home
imgFolder: home_buildings/0384
wiki: https://clashofclans.fandom.com/wiki/Seeking_Air_Mine
canonical: /upgrade/0384-Seeking-Air-Mine
dataSyncedOn: 2026-10-13
description: "鸟儿？飞机？不管是什么，反正搜空地雷会把它炸飞。这类陷阱会对单个空中部队造成毁灭性打击。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0384-Seeking-Air-Mine.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2026-02-23'">

<template #introduction>

- *本页内容不是空中炸弹，如想查看空中炸弹的数据，请访问：[空中炸弹](/upgrade/0382-Air-Bomb)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Seeking_Air_Mine_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2026/02/23">
        <TimelineRow>在 18 本推出 8 级搜空地雷。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/11/17">
        <TimelineRow>7 级搜空地雷的升级时间和升级费用减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/10/06">
        <TimelineRow>4 ~ 6 级搜空地雷的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>4 ~ 6 级搜空地雷的升级时间减少。</TimelineRow>
        <TimelineRow>2 ~ 6 级搜空地雷的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>17 本推出，并在 17 本新增 7 级搜空地雷。</TimelineRow>
        <TimelineRow>17 本可以新解锁一个搜空地雷。</TimelineRow>
        <TimelineRow>5 ~ 6 级搜空地雷的升级费用和时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/18">
        <TimelineRow>5 级搜空地雷的升级时间减少。</TimelineRow>
        <TimelineRow>5 级搜空地雷的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/02/27">
        <TimelineRow>16 本新增 6 级搜空地雷。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>2 ~ 4 级搜空地雷的升级时间减少。</TimelineRow>
        <TimelineRow>1 ~ 4 级搜空地雷的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>15 本新增 5 级搜空地雷。</TimelineRow>
        <TimelineRow>4 级搜空地雷的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>4 级搜空地雷的升级时间减少。</TimelineRow>
        <TimelineRow>3 ~ 4 级搜空地雷的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/05/02">
        <TimelineRow>4 级搜空地雷的伤害从 2400 提升至 2500。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/08/12">
        <TimelineRow>搜空地雷的飞行速度从每秒 2.5 格提升至每秒 3.5 格。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>14 本推出，并在 14 本新解锁一个搜空地雷。</TimelineRow>
        <TimelineRow>2 ~ 3 级搜空地雷的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/06/22">
        <TimelineRow>如果触发了搜空地雷的敌方单位在被地雷炸中之前就被消灭，搜空地雷不会再去追踪地图另一边的飞行单位。</TimelineRow>
        <TimelineRow>现在搜空地雷的最大追踪半径为其触发半径的 2 倍。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/03/30">
        <TimelineRow>2 ~ 3 级搜空地雷的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/12/09">
        <TimelineRow>13 本推出，并在 13 本新增 4 级搜空地雷。</TimelineRow>
        <TimelineRow>13 本新解锁一个搜空地雷。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/04/02">
        <TimelineRow>玩家上线后，所有的陷阱将自动被重新布置，重新布置不再需要花费金币。然而，如果玩家不上线，陷阱就不会被重新布置，所以你仍然可以攻击到陷阱失效的村庄。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
