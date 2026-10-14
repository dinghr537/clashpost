---
title: "部落冲突 coc 龙骑士升级数据"
navTitle: "龙骑士"
shownTitle: "龙骑士"
module: upgrade-home
imgFolder: home_tech/000e
wiki: https://clashofclans.fandom.com/wiki/Dragon_Rider
canonical: /upgrade/000e-Dragon-Rider
dataSyncedOn: 2026-10-13
description: "这台热衷破坏的飞行机器很乐意，甚至是非常兴奋能够摧毁范围内的任何防御建筑。坐在里面的骷髅兵发誓说他绝不会碰那些控制装置。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/000e-Dragon-Rider.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-11-17'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Dragon_Rider_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/11/17">
        <TimelineRow>18 本推出，并在 18 本新增 6 级龙骑士。</TimelineRow>
        <TimelineRow>5 级龙骑士的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/10/06">
        <TimelineRow>2 ~ 3 级龙骑士的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/06/30">
        <TimelineRow>4 ~ 5 级龙骑士的生命值增加。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/27">
        <TimelineRow>部队的训练时间取消，但增加了捐赠费用。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>2 ~ 4 级龙骑士的升级时间减少。</TimelineRow>
        <TimelineRow>4 级龙骑士的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/02/10">
        <TimelineRow>龙骑士的训练时间由 4:10 改为 3:30</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>17 本推出，并在 17 本新增 5 级龙骑士。</TimelineRow>
        <TimelineRow>2 ~ 4 级龙骑士的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>16 本推出，同时在 16 本新增 4 级龙骑士。</TimelineRow>
        <TimelineRow>3 级龙骑士的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>2 级龙骑士的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>2 ~ 3 级龙骑士的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/05/02">
        <TimelineRow>家乡所有空军的攻击距离减少 0.5 格（超级飞龙除外，这玩意削了 1 格）。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/01/20">
        <TimelineRow>2 ~ 3 级龙骑士的生命值减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/09/27">
        <TimelineRow>龙骑士的射程降低 0.5 格。射程的降低意味着龙骑士需要更加靠近攻击目标才能发起远程攻击。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/06/15">
        <TimelineRow>13 本可解锁新兵种：龙骑士。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
