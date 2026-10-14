---
title: "部落冲突 coc 特斯拉电磁塔（电塔）升级数据"
navTitle: "特斯拉电磁塔"
shownTitle: "特斯拉电磁塔（电塔）"
module: upgrade-home
imgFolder: home_buildings/0307
wiki: https://clashofclans.fandom.com/wiki/Hidden_Tesla
canonical: /upgrade/0307-Hidden-Tesla
dataSyncedOn: 2026-10-13
description: "隐藏在地下的特斯拉电磁塔就像一个危险陷阱！法师在这个防御建筑中注入了雷电的力量，当敌军地面或空中部队靠近时，特斯拉电磁塔会弹出并运用雷电之力攻击这些倒霉蛋。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0307-Hidden-Tesla.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2026-02-23'">

<template #introduction>

- *如想查看 12 本的自带武器，请访问 [巨型特斯拉电磁塔](/upgrade/030c-Giga-Tesla)。*
- *如想查看夜世界的特斯拉电磁塔，请访问：[夜世界特斯拉电磁塔](/upgrade/1103-Hidden-Tesla)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Hidden_Tesla17.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2026/02/23">
        <TimelineRow>在 18 本添加了 17 级特斯拉电磁塔。</TimelineRow>
        <TimelineRow>移除了特斯拉电磁塔的充能等级。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/11/17">
        <TimelineRow>16 级及两个充能等级的特斯拉电磁塔的升级时间和升级费用减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/10/06">
        <TimelineRow>13 ~ 15 级特斯拉电磁塔的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>3、7 ~ 11、13 ~ 15 级特斯拉电磁塔的升级时间减少。</TimelineRow>
        <TimelineRow>3 ~ 5、7、9 ~ 15 级特斯拉电磁塔的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/02/10">
        <TimelineRow>17 本新增 16 级特斯拉电磁塔。</TimelineRow>
        <TimelineRow>4、5、12 级特斯拉电磁塔的升级时间减少。</TimelineRow>
        <TimelineRow>12 级特斯拉电磁塔的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>7 ~ 8、11 ~ 15 级特斯拉电磁塔的升级时间减少。</TimelineRow>
        <TimelineRow>11 ~ 15 级特斯拉电磁塔的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/09/09">
        <TimelineRow>超级充能推出，特斯拉电磁塔是第一批可以充能的建筑之一。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/18">
        <TimelineRow>10 ~ 14 级特斯拉电磁塔的升级时间减少。</TimelineRow>
        <TimelineRow>13 ~ 14 级特斯拉电磁塔的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/02/27">
        <TimelineRow>16 本新增 15 级特斯拉电磁塔。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>3 ~ 14 级特斯拉电磁塔的升级时间减少。</TimelineRow>
        <TimelineRow>1 ~ 9、13 级特斯拉电磁塔的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>15 本新增 14 级特斯拉电磁塔。</TimelineRow>
        <TimelineRow>10 ~ 12 级特斯拉电磁塔的升级时间减少。</TimelineRow>
        <TimelineRow>10 ~ 12 级特斯拉电磁塔的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>8 ~ 13 级特斯拉电磁塔的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/12/09">
        <TimelineRow>2 ~ 12 级特斯拉电磁塔的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>14 本推出，并在 14 本新增 13 级特斯拉电磁塔。</TimelineRow>
        <TimelineRow>1 ~ 9 级特斯拉电磁塔的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/10/12">
        <TimelineRow>13 本新增 12 级特斯拉电磁塔。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/12/09">
        <TimelineRow>13 本开放，新增 11 级特斯拉电磁塔。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/09/11">
        <TimelineRow>10 级特斯拉电磁塔的生命值由 950 提高到 980。</TimelineRow>
    </TimelineItem>
        <TimelineItem date="2019/04/02">
        <TimelineRow>1 ~ 8 级电塔的升级时间减少。</TimelineRow>
        <TimelineRow>1 ~ 9 级电塔的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
