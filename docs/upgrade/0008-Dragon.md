---
title: "部落冲突 coc 飞龙（大龙、火龙）升级数据"
navTitle: "飞龙"
shownTitle: "飞龙（大龙、火龙）"
module: upgrade-home
imgFolder: home_tech/0008
wiki: https://clashofclans.fandom.com/wiki/Dragon
canonical: /upgrade/0008-Dragon
dataSyncedOn: 2026-10-13
description: "飞龙喷出的烈焰让人胆寒，这种恐怖的空中生物面对敌军毫不留情，任何人都难以逃出它的魔掌。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0008-Dragon.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-11-17'">

<template #introduction>

- *如想查看该兵种的强化版本，请访问：[超级飞龙](/upgrade/060d-Super-Dragon)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Dragon_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/11/17">
        <TimelineRow>12 级飞龙的升级时间和升级费用减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/10/06">
        <TimelineRow>7、8、10 级飞龙的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/27">
        <TimelineRow>部队的训练时间取消，但增加了捐赠费用。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>9 ~ 11 级飞龙的升级时间减少。</TimelineRow>
        <TimelineRow>10 ~ 11 级飞龙的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/02/10">
        <TimelineRow>飞龙的训练时间由 3:00 改为 2:50</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>17 本推出，并在 17 本新增 12 级飞龙。</TimelineRow>
        <TimelineRow>5 ~ 11 级飞龙的升级时间减少。</TimelineRow>
        <TimelineRow>7 ~ 11 级飞龙的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/02/27">
        <TimelineRow>11 级飞龙的生命值提升。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>16 本推出，同时在 16 本新增 11 级飞龙。</TimelineRow>
        <TimelineRow>5 ~ 10 级飞龙的升级时间减少。</TimelineRow>
        <TimelineRow>9 级飞龙的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>15 本新增 10 级飞龙。</TimelineRow>
        <TimelineRow>7 ~ 8 级飞龙的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>5 ~ 9 级飞龙的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/05/02">
        <TimelineRow>家乡所有空军的攻击距离减少 0.5 格（超级飞龙除外，这玩意削了 1 格）。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/12/09">
        <TimelineRow>2 ~ 6 级飞龙的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/08/12">
        <TimelineRow>4 级飞龙的生命值从 2600 提升至 2700。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/06/15">
        <TimelineRow>14 本新增 9 级飞龙。。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>2 ~ 7 级飞龙的升级费用降低。</TimelineRow>
        <TimelineRow>2 ~ 6 级飞龙的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/03/30">
        <TimelineRow>3 ~ 5 级飞龙的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/12/09">
        <TimelineRow>13 本开放，新增 8 级飞龙。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/09/11">
        <TimelineRow>5 ~ 7 级飞龙的生命值提升。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/04/02">
        <TimelineRow>2 ~ 6 级飞龙的升级时间减少。</TimelineRow>
        <TimelineRow>所有等级飞龙的训练费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
