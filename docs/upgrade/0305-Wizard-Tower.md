---
title: "部落冲突 coc 法师塔升级数据"
navTitle: "法师塔"
shownTitle: "法师塔"
module: upgrade-home
imgFolder: home_buildings/0305
wiki: https://clashofclans.fandom.com/wiki/Wizard_Tower
canonical: /upgrade/0305-Wizard-Tower
dataSyncedOn: 2026-10-13
description: "感受神秘法术的威力吧！塔上的法师会施放威力强大的范围性攻击法术，抵御侵入领土和领空的敌军。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0305-Wizard-Tower.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-11-17'">

<template #introduction>

- *如想查看由两个法师塔合成的超级法师塔，请访问 [超级法师塔](/upgrade/0318-Super-Wizard-Tower)。*
- *如想查看都城的超级法师塔，请访问：[都城超级法师塔](/upgrade/2207-Super-Wizard-Tower)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Wizard_Tower17.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

注：18 本可新建一个法师塔，合并两个超级法师塔，因此法师塔的数量为 5 + 1 - 2 * 2 = 2 个。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/11/17">
        <TimelineRow>17 级法师塔的升级时间和升级费用减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/10/06">
        <TimelineRow>16 级法师塔的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>1、3 ~ 5、7 ~ 8、10 ~ 12、14 ~ 16 级法师塔的升级时间减少。</TimelineRow>
        <TimelineRow>1 ~ 16 级法师塔的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/02/10">
        <TimelineRow>2、6、9、13 级法师塔的升级时间减少。</TimelineRow>
        <TimelineRow>13 级法师塔的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>17 本推出，并在 17 本新增 17 级法师塔。</TimelineRow>
        <TimelineRow>8 ~ 16 级法师塔的升级时间减少。</TimelineRow>
        <TimelineRow>7 ~ 16 级法师塔的升级费用降低。</TimelineRow>
        <TimelineRow>法师塔成为第二批可以充能的建筑。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/18">
        <TimelineRow>11 ~ 15 级法师塔的升级时间减少。</TimelineRow>
        <TimelineRow>11 ~ 15 级法师塔的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/03">
        <TimelineRow>9 ~ 14 级法师塔的生命值降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>16 本推出，并在 16 本新增 16 级法师塔。</TimelineRow>
        <TimelineRow>2 ~ 15 级法师塔的升级时间减少。</TimelineRow>
        <TimelineRow>3 ~ 10、14 级法师塔的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>11 ~ 13 级法师塔的升级时间减少。</TimelineRow>
        <TimelineRow>11 ~ 13 级法师塔的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>15 本推出，并在 15 本新增 15 级法师塔。</TimelineRow>
        <TimelineRow>8 ~ 14 级法师塔的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/12/09">
        <TimelineRow>1 ~ 6、8 ~ 13 级法师塔的升级费用降低。</TimelineRow>
    </TimelineItem>
        <TimelineItem date="2021/06/15">
        <TimelineRow>14 本新增 14 级法师塔。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>3 ~ 8、10 级法师塔的升级时间减少。</TimelineRow>
        <TimelineRow>1 ~ 8、10 级法师塔的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/06/22">
        <TimelineRow>13 本新增 13 级法师塔。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/12/09">
        <TimelineRow>13 本推出，并在 13 本新增 12 级法师塔。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/06/18">
        <TimelineRow>8 ~ 9 级法师塔的伤害降低。</TimelineRow>
    </TimelineItem>
        <TimelineItem date="2019/04/02">
        <TimelineRow>所有等级法师塔的升级时间减少。</TimelineRow>
        <TimelineRow>7 ~ 9 级法师塔的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
