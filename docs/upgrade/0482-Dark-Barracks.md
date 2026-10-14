---
title: "部落冲突 coc 暗黑训练营升级数据"
navTitle: "暗黑训练营"
shownTitle: "暗黑训练营"
module: upgrade-home
imgFolder: home_buildings/0482
wiki: https://clashofclans.fandom.com/wiki/Dark_Barracks
canonical: /upgrade/0482-Dark-Barracks
dataSyncedOn: 2026-10-13
description: "暗黑训练营将向源于暗黑重油的生物敞开大门。升级暗黑训练营解锁更多有独特战斗力的部队。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0482-Dark-Barracks.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-10-06'">

<template #introduction>

- *如想查看训练圣水兵的训练营，请访问：[训练营](/upgrade/0481-Barracks)。*
- *如想查看夜世界的建筑大师训练营，请访问：[夜世界建筑大师训练营](/upgrade/1280-Builder-Barracks)。*
- *都城的训练营比较多，这里就不放链接了，如有需求请自行前往相关页面查看。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Dark_Barracks12_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/10/06">
        <TimelineRow>10 ~ 11 级暗黑训练营的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>15 本新增 12 级暗黑训练营，新兵种：烈焰熔炉。</TimelineRow>
        <TimelineRow>10 ~ 11 级暗黑训练营的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>5 ~ 11 级暗黑训练营的升级时间减少。</TimelineRow>
        <TimelineRow>8 ~ 9 级暗黑训练营的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/18">
        <TimelineRow>10 级暗黑训练营的升级时间减少。</TimelineRow>
        <TimelineRow>10 级暗黑训练营的升级费用降低。</TimelineRow>
        <TimelineRow>14 本新增 11 级暗黑训练营，新兵种：德鲁伊。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>1 ~ 4 级暗黑训练营的升级费用减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>13 本新增 10 级暗黑训练营。</TimelineRow>
        <TimelineRow>9 级暗黑训练营的升级时间减少。</TimelineRow>
        <TimelineRow>9 级暗黑训练营的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>两个训练营合并为一个，更新后的兵种训练时间等同于更新前两个训练营的训练时间。</TimelineRow>
        <TimelineRow>训练营升级时兵种可继续训练部队，但训练速度减半（训练时间翻倍）。</TimelineRow>
        <TimelineRow>1 ~ 7 级暗黑训练营的升级时间增加。</TimelineRow>
        <TimelineRow>8 ~ 9 级暗黑训练营的升级时间减少。</TimelineRow>
        <TimelineRow>1 ~ 9 级暗黑训练营的升级费用增加。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/12/09">
        <TimelineRow>1 ~ 6 级暗黑训练营的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>所有等级暗黑训练营的升级费用降低。</TimelineRow>
        <TimelineRow>1 ~ 4、8 级暗黑训练营的升级费时间减少。</TimelineRow>
    </TimelineItem>
     <TimelineItem date="2020/06/22">
        <TimelineRow>12 本新增 9 级暗黑训练营。</TimelineRow>
    </TimelineItem>
        <TimelineItem date="2019/04/02">
        <TimelineRow>所有等级暗黑训练营的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
