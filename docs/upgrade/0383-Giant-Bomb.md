---
title: "部落冲突 coc 巨型炸弹（大炸弹、巨炸）升级数据"
navTitle: "巨型炸弹"
shownTitle: "巨型炸弹（大炸弹、巨炸）"
module: upgrade-home
imgFolder: home_buildings/0383
wiki: https://clashofclans.fandom.com/wiki/Giant_Bomb
canonical: /upgrade/0383-Giant-Bomb
dataSyncedOn: 2026-10-13
description: "如果你想要的是一场大爆炸，那选巨型炸弹准没错。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0383-Giant-Bomb.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-11-17'">

<template #introduction>

- 游戏中还存在另一种大炸弹，详见：[终极炸弹](/upgrade/0387-Giga-Bomb)。

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Giant_Bomb_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/11/17">
        <TimelineRow>11 级巨型炸弹的升级时间和升级费用减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/10/06">
        <TimelineRow>8 ~ 9 级巨型炸弹的升级时间减少。</TimelineRow>
        <TimelineRow>8 ~ 9 级巨型炸弹的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>2 ~ 6、8 ~ 10 级巨型炸弹的升级时间减少。</TimelineRow>
        <TimelineRow>3 ~ 10 级巨型炸弹的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/02/10">
        <TimelineRow>7 级巨型炸弹的升级时间减少。</TimelineRow>
        <TimelineRow>7 级巨型炸弹的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>17 本推出，并在 17 本新增 11 级巨型炸弹和新解锁一个巨型炸弹。</TimelineRow>
        <TimelineRow>3 ~ 7、9 ~ 10 级巨型炸弹的升级时间减少。</TimelineRow>
        <TimelineRow>8 ~ 10 级巨型炸弹的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/18">
        <TimelineRow>6 ~ 9 级巨型炸弹的升级时间减少。</TimelineRow>
        <TimelineRow>8 ~ 9 级巨型炸弹的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>16 本推出，并在 16 本新增 10 级巨型炸弹。</TimelineRow>
        <TimelineRow>2 ~ 9 级巨型炸弹的升级时间减少。</TimelineRow>
        <TimelineRow>3 ~ 8 级巨型炸弹的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>15 本新增 9 级巨型炸弹。</TimelineRow>
        <TimelineRow>6 ~ 7 级巨型炸弹的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>5 ~ 8 级巨型炸弹的升级时间减少。</TimelineRow>
        <TimelineRow>4 ~ 8 级巨型炸弹的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/06/15">
        <TimelineRow>14 本新增 8 级巨型炸弹。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>14 本推出，并在 14 本新解锁一个巨型炸弹。</TimelineRow>
        <TimelineRow>3 ~ 4 级巨型炸弹的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/12/07">
        <TimelineRow>13 本新增 7 级巨型炸弹。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/12/09">
        <TimelineRow>13 本推出，并在 13 本新增 6 级巨型炸弹。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/04/02">
        <TimelineRow>玩家上线后，所有的陷阱将自动被重新布置，重新布置不再需要花费金币。然而，如果玩家不上线，陷阱就不会被重新布置，所以你仍然可以攻击到陷阱失效的村庄。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
