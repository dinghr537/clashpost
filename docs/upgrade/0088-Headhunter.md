---
title: "部落冲突 coc 英雄猎手（头号杀手）升级数据"
navTitle: "英雄猎手"
shownTitle: "英雄猎手（头号杀手）"
module: upgrade-home
imgFolder: home_tech/0088
wiki: https://clashofclans.fandom.com/wiki/Headhunter
canonical: /upgrade/0088-Headhunter
dataSyncedOn: 2026-10-13
description: "英雄猎手在战场上只有一个任务：消灭敌方英雄。此外，她还在村庄药剂师那儿兼职。身体轻盈的她能轻松跳过城墙，而且她的兵器可以减缓目标的移动速度和攻击速度。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0088-Headhunter.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-03-27'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Headhunter_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

1. 英雄猎手的技能：攻击时有毒药效果，可以减缓敌军的移动速度和攻击速度。此外，英雄猎手还可以跳墙。
2. 英雄猎手的毒药效果只对部队、英雄和攻城机器有效，它不能对建筑造成伤害，也不能减缓建筑的攻击速度。
3. 英雄猎手的毒药效果和其他具有毒药效果的单位（如 [猛蜥](/upgrade/0286-Poison-Lizard)、[毒药法术](/upgrade/0180-Poison-Spell)）叠加时取效果最强的那个。另外，英雄猎手的毒药效果对英雄没有衰减（不但没有衰减甚至还有 4 倍伤害）。
4. 英雄猎手也具有和毒药法术类似的减速效果，但英雄猎手的伤害不是随时间递增的，而是会立即达到最大伤害，这一点又和毒药法术不同。

\* 毒药法术效果：移动速度降低 / 攻击速度降低。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/03/27">
        <TimelineRow>部队的训练时间取消，但增加了捐赠费用。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>2 ~ 3 级英雄猎手的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/02/10">
        <TimelineRow>英雄猎手的训练时间由 1:00 改为 0:50</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>2 ~ 3 级英雄猎手的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>2 ~ 3 级英雄猎手的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>2 ~ 3 级英雄猎手的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/29">
        <TimelineRow>1 ~ 3 级英雄猎手的每秒伤害从 108/120/132 降至 105/115/125。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
    <TimelineRow>修复了英雄猎手的淬毒效果持续时间计时不太准确的问题。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/06/22">
        <TimelineRow>12 本可解锁新兵种：英雄猎手。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
