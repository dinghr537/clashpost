---
title: "部落冲突 coc 法师升级数据"
navTitle: "法师"
shownTitle: "法师"
module: upgrade-home
imgFolder: home_tech/0006
wiki: https://clashofclans.fandom.com/wiki/Wizard
canonical: /upgrade/0006-Wizard
dataSyncedOn: 2026-10-13
description: "法师的出现为战场蒙上了一层恐怖色彩。集结一群法师，他们将摧毁各种陆空目标！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0006-Wizard.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-11-17'">

<template #introduction>

- *如想查看该兵种的强化版本，请访问：[超级法师（超法）](/upgrade/0609-Super-Wizard)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Wizard_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/11/17">
        <TimelineRow>18 本推出，并在 18 本新增 14 级法师。</TimelineRow>
        <TimelineRow>13 级法师的升级时间和升级费用减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/10/06">
        <TimelineRow>8 ~ 11 级法师的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/27">
        <TimelineRow>部队的训练时间取消，但增加了捐赠费用。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>2 ~ 5、8 ~ 12 级法师的升级时间减少。</TimelineRow>
        <TimelineRow>3 ~ 4、6 ~ 12 级法师的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>17 本推出，并在 17 本新增 13 级法师。</TimelineRow>
        <TimelineRow>3 ~ 4、6 ~ 7、9 ~ 12 级法师的升级时间减少。</TimelineRow>
        <TimelineRow>8 ~ 12 级法师的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/18">
        <TimelineRow>11 级法师的升级时间减少。</TimelineRow>
        <TimelineRow>11 级法师的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>16 本推出，同时在 16 本新增 12 级法师。</TimelineRow>
        <TimelineRow>7 ~ 11 级法师的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>9 ~ 10 级法师的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>15 本推出，并在 15 本新增 11 级法师。</TimelineRow>
        <TimelineRow>7 ~ 10 级法师的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/12/09">
        <TimelineRow>2 ~ 10 级法师的升级费用和升级时间减少。</TimelineRow>
        <TimelineRow>4 ~ 7 级法师的生命值提升。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>3 ~ 9 级法师的升级费用降低。</TimelineRow>
        <TimelineRow>3 ~ 6、8 ~ 9 级法师的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/10/12">
        <TimelineRow>13 本新增 10 级法师。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/03/30">
        <TimelineRow>5 ~ 7 级法师的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/04/02">
        <TimelineRow>5 ~ 8 级法师的升级时间减少。</TimelineRow>
        <TimelineRow>所有等级法师的训练费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
