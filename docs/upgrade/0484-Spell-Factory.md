---
title: "部落冲突 coc 法术工厂升级数据"
navTitle: "法术工厂"
shownTitle: "法术工厂"
module: upgrade-home
imgFolder: home_buildings/0484
wiki: https://clashofclans.fandom.com/wiki/Spell_Factory
canonical: /upgrade/0484-Spell-Factory
dataSyncedOn: 2026-10-13
description: "法术工厂是资深法师的家，比起在前线战斗，他们更适合去创造各种魔力武器。使用强大的法术，在战斗中扭转乾坤吧！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0484-Spell-Factory.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-11-17'">

<template #introduction>

- *如想查看配置暗黑法术的法术工厂，请访问：[暗黑法术工厂](/upgrade/0485-Dark-Spell-Factory)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Spell_Factory9.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/11/17">
        <TimelineRow>16 本新增 9 级法术工厂。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>1 ~ 5、7 ~ 8 级法术工厂的升级时间减少。</TimelineRow>
        <TimelineRow>8 级法术工厂的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>17 本推出，并在 15 本新增 8 级法术工厂。</TimelineRow>
        <TimelineRow>4 ~ 5、7 级法术工厂的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>7 级法术工厂的升级时间 9 天减少至 8 天。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>法术工厂升级时兵种可继续配置法术，但配置速度减半（配置时间翻倍）。</TimelineRow>
        <TimelineRow>15 本推出，并在 13 本新增 7 级法术工厂，可解锁新法术：回溯法术（召回法术）。</TimelineRow>
        <TimelineRow>5 ~ 7 级法术工厂的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/12/09">
        <TimelineRow>1 ~ 3 级法术工厂的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>4 ~ 5 级法术工厂的升级费用降低。</TimelineRow>
        <TimelineRow>5 级法术工厂的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/12/07">
        <TimelineRow>11 本新增 6 级法术工厂，新法术：隐形法术。</TimelineRow>
    </TimelineItem>
        <TimelineItem date="2019/04/02">
        <TimelineRow>包含大量降低发展成本和提高发展速度的调整，其中 1 ~ 3 级法术工厂的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
