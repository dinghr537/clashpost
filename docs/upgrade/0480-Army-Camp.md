---
title: "部落冲突 coc 兵营升级数据"
navTitle: "兵营"
shownTitle: "兵营"
module: upgrade-home
imgFolder: home_buildings/0480
wiki: https://clashofclans.fandom.com/wiki/Army_Camp
canonical: /upgrade/0480-Army-Camp
dataSyncedOn: 2026-10-13
description: "部队驻扎在兵营。建造并升级兵营以容纳更多部队。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0480-Army-Camp.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-11-17'">

<template #introduction>

- *如想查看夜世界的兵营，请访问：[夜世界兵营](/upgrade/1281-Army-Camp)。*
- *如想查看都城的兵营，请访问：[都城兵营](/upgrade/2300-Army-Camp)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Army_Camp13_hd.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/11/17">
        <TimelineRow>13 级兵营的升级时间和升级费用减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/10/06">
        <TimelineRow>9 ~ 12 级兵营的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/06/16">
        <TimelineRow>1 ~ 6 级兵营的生命值减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>17 本新增 13 级兵营。</TimelineRow>
        <TimelineRow>1 ~ 5 级兵营的升级时间减少。</TimelineRow>
        <TimelineRow>6、11、12 级兵营的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>9 ~ 12 级兵营的升级时间减少。</TimelineRow>
        <TimelineRow>10、12 级兵营的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/18">
        <TimelineRow>12 级兵营的升级时间减少。</TimelineRow>
        <TimelineRow>12 级兵营的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>12 级兵营的升级时间 16 天减少到 12 天 12 小时。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>10 ~ 11 级兵营的升级时间减少。</TimelineRow>
        <TimelineRow>10 ~ 11 级兵营的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>15 本推出，并在 15 本新增 12 级兵营。</TimelineRow>
        <TimelineRow>8 ~ 11 级兵营的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>14 本推出，并在 14 本新增 15 级兵营。</TimelineRow>
        <TimelineRow>2 ~ 3 级兵营的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/10/12">
        <TimelineRow>13 本新增 11 级兵营。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/12/09">
        <TimelineRow>兵营的占地面积由 5*5 改为 4*4。</TimelineRow>
    </TimelineItem>
        <TimelineItem date="2019/04/02">
        <TimelineRow>8 ~ 9 级兵营的升级费用降低。</TimelineRow>
        <TimelineRow>5 ~ 9 级兵营的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
