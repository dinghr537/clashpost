---
title: "部落冲突 coc 空中炸弹（红炸）升级数据"
navTitle: "空中炸弹"
shownTitle: "空中炸弹（红炸）"
module: upgrade-home
imgFolder: home_buildings/0382
wiki: https://clashofclans.fandom.com/wiki/Air_Bomb
canonical: /upgrade/0382-Air-Bomb
dataSyncedOn: 2026-10-13
description: "作为防空领域的一大革新之作，这种陷阱可以对小范围内的多个空中目标造成伤害。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0382-Air-Bomb.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-11-17'">

<template #introduction>

- 本页内容不是搜空地雷，如想查看搜空地雷的数据，请访问：[搜空地雷](/upgrade/0384-Seeking-Air-Mine)。
- 如想查看夜世界的空中炸弹发射器，请访问：[夜世界空中炸弹发射器](/upgrade/1107-Air-Bombs)。
- 如想查看都城的空中炸弹发射器，请访问：[都城空中炸弹发射器](/upgrade/2208-Air-Bombs)。

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Air_Bomb_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/11/17">
        <TimelineRow>18 本推出，并在 18 本新增 13 级空中炸弹。</TimelineRow>
        <TimelineRow>12 级空中炸弹的升级时间和升级费用减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/10/06">
        <TimelineRow>7 ~ 9 级空中炸弹的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>2 ~ 7、9 ~ 11 级空中炸弹的升级时间减少。</TimelineRow>
        <TimelineRow>3 ~ 11 级空中炸弹的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/02/10">
        <TimelineRow>8 级空中炸弹的升级时间减少。</TimelineRow>
        <TimelineRow>8 级空中炸弹的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>17 本推出，并在 17 本新增 12 级空中炸弹。</TimelineRow>
        <TimelineRow>4 ~ 11 级空中炸弹的升级时间减少。</TimelineRow>
        <TimelineRow>9 ~ 11 级空中炸弹的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/18">
        <TimelineRow>8 ~ 10 级空中炸弹的升级时间减少。</TimelineRow>
        <TimelineRow>10 级空中炸弹的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>16 本推出，并在 16 本新增 11 级空中炸弹。</TimelineRow>
        <TimelineRow>2 ~ 9 级空中炸弹的升级时间减少。</TimelineRow>
        <TimelineRow>3 ~ 5、7 ~ 9 级空中炸弹的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>6 ~ 8 级空中炸弹的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>15 本推出，并在 15 本新增 10 级空中炸弹。</TimelineRow>
        <TimelineRow>7 ~ 9 级空中炸弹的升级时间减少。</TimelineRow>
        <TimelineRow>5 ~ 9 级空中炸弹的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/06/27">
        <TimelineRow>5 ~ 9 级空中炸弹的伤害提高。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/12/09">
        <TimelineRow>4 ~ 5 级空中炸弹的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/06/15">
        <TimelineRow>14 本新增 9 级空中炸弹。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>14 本推出，并在 14 本新解锁一个空中炸弹。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/12/07">
        <TimelineRow>13 本新增 8 级空中炸弹。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/03/30">
        <TimelineRow>4 级空中炸弹的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/12/09">
        <TimelineRow>13 本推出，并在 13 本新增 7 级空中炸弹。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/04/02">
        <TimelineRow>玩家上线后，所有的陷阱将自动被重新布置，重新布置不再需要花费金币。然而，如果玩家不上线，陷阱就不会被重新布置，所以你仍然可以攻击到陷阱失效的村庄。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
