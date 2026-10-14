---
title: "部落冲突 coc 瓦基丽武神升级数据"
navTitle: "瓦基丽武神"
shownTitle: "瓦基丽武神"
module: upgrade-home
imgFolder: home_tech/0082
wiki: https://clashofclans.fandom.com/wiki/Valkyrie
canonical: /upgrade/0082-Valkyrie
dataSyncedOn: 2026-10-13
description: "这位光荣的勇士擅长使用双手斧，她在相邻的建筑物之间跑动，能够通过狂暴旋风将多个敌人或建筑一同粉碎！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0082-Valkyrie.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-10-06'">

<template #introduction>

- *如想查看该兵种的强化版本，请访问：[超级瓦基丽武神](/upgrade/0607-Super-Valkyrie)。*
- *如想查看作为临时兵种推出的超级强化版本，请访问：[铁臂终结者](/upgrade/0e19-The-Disarmer)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Valkyrie_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/10/06">
        <TimelineRow>5 ~ 11 级瓦基丽武神的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/27">
        <TimelineRow>部队的训练时间取消，但增加了捐赠费用。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>2、4 ~ 11 级瓦基丽武神的升级时间减少。</TimelineRow>
        <TimelineRow>9 级瓦基丽武神的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/02/10">
        <TimelineRow>瓦基丽武神的训练时间由 1:30 改为 1:10</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>2 ~ 11 级瓦基丽武神的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/09/09">
        <TimelineRow>11 级瓦基丽武神的生命值减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/18">
        <TimelineRow>9 ~ 10 级瓦基丽武神的升级时间减少。</TimelineRow>
        <TimelineRow>9 ~ 10 级瓦基丽武神的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/03">
        <TimelineRow>6 ~ 8 级瓦基丽武神的每秒伤害提升。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>16 本推出，并在 16 本新增 11 级瓦基丽武神。</TimelineRow>
        <TimelineRow>5 ~ 10 级瓦基丽武神的升级时间减少。</TimelineRow>
        <TimelineRow>2 ~ 5、9 级瓦基丽武神的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>15 本新增 10 级瓦基丽武神。</TimelineRow>
        <TimelineRow>7 ~ 8 级瓦基丽武神的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>5 ~ 9 级瓦基丽武神的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/06/27">
        <TimelineRow>5 ~ 9 级瓦基丽武神的生命值增加。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/12/09">
        <TimelineRow>2 ~ 7 级瓦基丽武神的升级时间减少。</TimelineRow>
        <TimelineRow>2 ~ 6 级瓦基丽武神的生命值提升。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/08/12">
        <TimelineRow>9 级瓦基丽武神的生命值从 1850 提升至 1900。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>14 本推出，并在 14 本新增 9 级瓦基丽武神。</TimelineRow>
        <TimelineRow>2 ~ 7 级瓦基丽武神的升级费用降低。</TimelineRow>
        <TimelineRow>2 ~ 4、7 级瓦基丽武神的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/10/12">
        <TimelineRow>2 ~ 6 级瓦基丽武神的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/03/30">
        <TimelineRow>2 ~ 5 级瓦基丽武神的升级费用降低。</TimelineRow>
        <TimelineRow>13 本新增 8 级瓦基丽武神。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/12/09">
        <TimelineRow>13 本开放，7 级瓦基丽武神的生命值由 1400 提高到 1450。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/09/11">
        <TimelineRow>7 级瓦基丽武神的生命值由 1300 提高到 1400。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
