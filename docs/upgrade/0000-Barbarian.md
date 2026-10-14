---
title: "部落冲突 coc 野蛮人升级数据"
navTitle: "野蛮人"
shownTitle: "野蛮人"
module: upgrade-home
imgFolder: home_tech/0000
wiki: https://clashofclans.fandom.com/wiki/Barbarian
canonical: /upgrade/0000-Barbarian
dataSyncedOn: 2026-10-13
description: "这些无畏的勇士长着引人注目的胡子，凭借一身壮硕的肌肉在敌人的村庄肆虐。训练一队野蛮人，他们将为您出生入死！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0000-Barbarian.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-10-06'">

<template #introduction>

- *如想查看该兵种的强化版本，请访问：[超级野蛮人](/upgrade/0600-Super-Barbarian)。*
- *如想查看以野蛮人为原型的英雄，请访问：[野蛮人之王（蛮王、男王）](/upgrade/0200-Barbarian-King)。*
- *如想查看夜世界的狂暴野蛮人，请访问：[夜世界狂暴野蛮人](/upgrade/1000-Raged-Barbarian)。*
- *如想查看都城的野蛮人（仅作为派生兵种），请访问：[都城野蛮人](/upgrade/20c0-Barbarian)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Barbarian_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/10/06">
        <TimelineRow>9 ~ 12 级野蛮人的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/06/16">
        <TimelineRow>1 ~ 3 级野蛮人的每秒伤害值提升。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/27">
        <TimelineRow>部队的训练时间取消，但增加了捐赠费用。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>2 ~ 12 级野蛮人的升级时间减少。</TimelineRow>
        <TimelineRow>2 ~ 9、12 级野蛮人的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/02/10">
        <TimelineRow>2 级野蛮人的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>3 ~ 7、9 ~ 12 级野蛮人的升级时间减少。</TimelineRow>
        <TimelineRow>9 ~ 12 级野蛮人的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/18">
        <TimelineRow>7 ~ 11 级野蛮人的升级时间减少。</TimelineRow>
        <TimelineRow>10 ~ 11 级野蛮人的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>16 本推出，同时在 16 本新增 12 级野蛮人。</TimelineRow>
        <TimelineRow>7 ~ 11 级野蛮人的升级时间减少。</TimelineRow>
        <TimelineRow>8 ~ 10 级野蛮人的升级花费降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>9 级野蛮人的升级时间减少。</TimelineRow>
        <TimelineRow>9 级野蛮人的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>15 本推出，并在 15 本新增 11 级野蛮人。</TimelineRow>
        <TimelineRow>7 ~ 10 级野蛮人的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/12/09">
        <TimelineRow>2 ~ 9 级野蛮人的升级费用降低。</TimelineRow>
        <TimelineRow>2 ~ 9 级野蛮人的升级时间减少。</TimelineRow>
        <TimelineRow>4 ~ 7 级野蛮人的生命值提升。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>14 本新增 10 级野蛮人。</TimelineRow>
        <TimelineRow>1 ~ 2 级野蛮人的训练费用：25/40 圣水 → 15/30 圣水</TimelineRow>
        <TimelineRow>2 ~ 9 级野蛮人的升级费用降低。</TimelineRow>
        <TimelineRow>3 ~ 8 级野蛮人的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/03/30">
        <TimelineRow>5 ~ 8 级野蛮人的升级费用降低。</TimelineRow>
        <TimelineRow>12 本新增 9 级野蛮人。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/04/02">
        <TimelineRow>包含大量降低发展成本和提高发展速度的调整，其中 5 ~ 8 级野蛮人的升级时间下调。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/02/22">
        <TimelineRow>7 ~ 8 级野蛮人的生命值提高。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
