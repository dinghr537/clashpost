---
title: "部落冲突 coc 巨石投手（蓝胖）升级数据"
navTitle: "巨石投手"
shownTitle: "巨石投手（蓝胖）"
module: upgrade-home
imgFolder: home_tech/0086
wiki: https://clashofclans.fandom.com/wiki/Bowler
canonical: /upgrade/0086-Bowler
dataSyncedOn: 2026-10-13
description: "这个蓝皮大个子一辈子只做两件简单的事：狂饮暗黑重油和扔石头。他扔出的巨石击中第一个目标后仍会向前弹跳，可以继续对撞到的目标造成伤害。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0086-Bowler.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-11-17'">

<template #introduction>

- *如想查看该兵种的强化版本，请访问：[超级巨石投手](/upgrade/060c-Super-Bowler)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Bowler_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

\* 巨石投手扔出去的石头落地后还能再次弹起来，对建筑造成二次伤害。石头的第一个落地距离蓝胖 3 格，第二个落点距离蓝胖 7 格。巨石投手只能看到第一个目标，二次范围伤害是顺带的，巨石投手并不知道石头会溅到哪儿。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/11/17">
        <TimelineRow>18 本推出，并在 18 本新增 10 级巨石投手。</TimelineRow>
        <TimelineRow>9 级巨石投手的升级时间和升级费用减少。</TimelineRow>
        <TimelineRow>9 级巨石投手的每秒伤害和生命值增加。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/10/06">
        <TimelineRow>4 ~ 8 级巨石投手的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/27">
        <TimelineRow>部队的训练时间取消，但增加了捐赠费用。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>3 ~ 8 级巨石投手的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/02/10">
        <TimelineRow>17 本新增 9 级巨石投手。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/02/10">
        <TimelineRow>巨石投手的训练时间由 1:00 改为 0:50</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>2 ~ 8 级巨石投手的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/18">
        <TimelineRow>6 ~ 7 级巨石投手的升级时间减少。</TimelineRow>
        <TimelineRow>6 ~ 7 级巨石投手的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/03">
        <TimelineRow>2 ~ 6 级巨石投手的每秒伤害提升。</TimelineRow>
        <TimelineRow>2 ~ 7 级巨石投手的生命值提升。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/02/27">
        <TimelineRow>16 本新增 8 级巨石投手。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>2 ~ 7 级巨石投手的升级时间减少。</TimelineRow>
        <TimelineRow>6 级巨石投手的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>15 本新增 7 级巨石投手。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>2 ~ 6 级巨石投手的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/06/27">
        <TimelineRow>1 ~ 5 级巨石投手的生命值增加。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/12/09">
        <TimelineRow>2 ~ 5 级巨石投手的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/09/27">
        <TimelineRow>14 本新增 6 级巨石投手。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>2 ~ 3 级巨石投手的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/10/12">
        <TimelineRow>2 ~ 3 级巨石投手的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/12/09">
        <TimelineRow>13 本开放，新增 5 级巨石投手。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/04/02">
        <TimelineRow>3 级巨石投手的升级费用和升级时间减少。</TimelineRow>
        <TimelineRow>所有等级巨石投手的训练费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
