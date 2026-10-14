---
title: "部落冲突 coc 攻城战车升级数据"
navTitle: "攻城战车"
shownTitle: "攻城战车"
module: upgrade-home
imgFolder: home_tech/0240
wiki: https://clashofclans.fandom.com/wiki/Wall_Wrecker
canonical: /upgrade/0240-Wall-Wrecker
dataSyncedOn: 2026-10-13
description: "攻城战车的作用简单直接：攻破挡在路上的一切障碍将部落援军运送到村庄核心地带。它由坚固材料打造而成，可以承受不少伤害。法术对攻城战车无效。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0240-Wall-Wrecker.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2026-01-12'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Wall_Wrecker_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

1. 攻城战车部署后会直线前往 [大本营](/upgrade/0400-Town-Hall) 方向，并攻击碰到的防御。
2. 当攻城战车的血量清零或到达大本营时，攻城战车就会解体并释放里面的援军。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2026/01/12">
        <TimelineRow>5 ~ 6 级攻城战车的每秒伤害和生命值增加。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/11/17">
        <TimelineRow>18 本推出，并在 18 本新增 6 级攻城战车。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/27">
        <TimelineRow>攻城机器的建造时间被取消。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>2 ~ 5 级攻城战车的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/18">
        <TimelineRow>5 级攻城战车的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>2 ~ 5 级攻城战车的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>15 本新增 5 级攻城战车。</TimelineRow>
        <TimelineRow>2 ~ 4 级攻城战车的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>2 ~ 4 级攻城战车的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/01/20">
        <TimelineRow>所有等级攻城战车的生命值提升。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/10/12">
        <TimelineRow>如果您没有部署攻城机器，当其他军队都被消灭后，战斗不再会自动结束。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/06/22">
        <TimelineRow>13 本新增 4 级攻城战车,优化了攻城战车的寻路系统。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
