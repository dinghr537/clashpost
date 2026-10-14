---
title: "部落冲突 coc 气球兵升级数据"
navTitle: "气球兵"
shownTitle: "气球兵"
module: upgrade-home
imgFolder: home_tech/0005
wiki: https://clashofclans.fandom.com/wiki/Balloon
canonical: /upgrade/0005-Balloon
dataSyncedOn: 2026-10-13
description: "这些乘着气球的高级骷髅兵对于摧毁敌人的防御乐此不疲。精心部署气球兵，他们将为您扫除各种障碍！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0005-Balloon.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-11-17'">

<template #introduction>

- *如想查看该兵种的强化版本，请访问：[火箭气球兵（超球）](/upgrade/060b-Rocket-Balloon)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Balloon_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/11/17">
        <TimelineRow>12 级气球兵的升级时间和升级费用减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/10/06">
        <TimelineRow>7 ~ 10 级气球兵的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/06/16">
        <TimelineRow>在 17 本新增 12 级气球兵。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/27">
        <TimelineRow>部队的训练时间取消，但增加了捐赠费用。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>2 ~ 3、9 ~ 11 级气球兵的升级时间减少。</TimelineRow>
        <TimelineRow>2、7、9、11 级气球兵的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>6 ~ 11 级气球兵的升级时间减少。</TimelineRow>
        <TimelineRow>8 ~ 11 级气球兵的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>16 本推出，同时在 16 本新增 11 级气球兵。</TimelineRow>
        <TimelineRow>7 ~ 10 级气球兵的升级时间减少。</TimelineRow>
        <TimelineRow>4 ~ 5 级气球兵的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>8 ~ 9 级气球兵的升级时间减少。</TimelineRow>
        <TimelineRow>8 ~ 9 级气球兵的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>7 ~ 10 级气球兵的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/05/02">
        <TimelineRow>家乡所有空军的攻击距离减少 0.5 格（超级飞龙除外，这玩意削了 1 格）。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/12/09">
        <TimelineRow>2 ~ 8 级气球兵的升级费用降低。</TimelineRow>
        <TimelineRow>2 ~ 8 级气球兵的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/06/15">
        <TimelineRow>14 本新增 10 级气球兵。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/03/30">
        <TimelineRow>6 级气球兵的升级费用降低。</TimelineRow>
        <TimelineRow>3、6、7 级气球兵的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/12/09">
        <TimelineRow>13 本开放，新增 9 级气球兵。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/04/02">
        <TimelineRow>5 ~ 7 级气球兵的升级时间减少。</TimelineRow>
        <TimelineRow>1 ~ 3 级气球兵的训练费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
