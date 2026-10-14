---
title: "部落冲突 coc 弹跳法术升级数据"
navTitle: "弹跳法术"
shownTitle: "弹跳法术"
module: upgrade-home
imgFolder: home_tech/0103
wiki: https://clashofclans.fandom.com/wiki/Jump_Spell
canonical: /upgrade/0103-Jump-Spell
dataSyncedOn: 2026-10-13
description: "城墙挡了您的去路？那就开辟一条捷径吧！在敌军城墙附近施放该法术，就可以在城墙上方创建通道，方便您的大军直接跳过这段城墙，保证畅通无阻！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0103-Jump-Spell.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-03-27'">

<template #introduction>

- *如想查看都城的弹跳法术，请访问：[都城弹跳法术](/upgrade/2101-Jump-Spell)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Jump_Spell.png" :imgAlt="$frontmatter.navTitle"
    description="城墙挡了您的去路？那就开辟一条捷径吧！<br>在敌军城墙附近施放该法术，就可以在城墙上方创建通道，方便您的大军直接跳过这段城墙，保证畅通无阻！"
    :isSmallImg="true" />

作用目标：弹跳法术对我方英雄有效，对攻城机器无效。弹跳法术的弹跳能力不能与 [野猪骑士](/upgrade/0081-Hog-Rider) 这类兵种自带的跳墙能力叠加，也不能让 [掘地矿工](/upgrade/000b-Miner) 改变钻地的机制。<br>
两次脉冲的间隔时间：脉冲效果和 [狂暴法术](/upgrade/0102-Rage-Spell) 一样是给士兵提供增益。游戏中有可能出现兵种离开弹跳法术范围，但是仍然跳过了下一堵墙的现象，这是因为兵种移动过快导致在离开法术半径的 0.1 ~ 0.4 秒内跳过了墙。

注：实际上 3 级弹跳法术的持续时间约为 199 * 0.3 = 59.7 秒，60 秒是四舍五入的结果。把弹跳法术从 2 级升到 3 级时，游戏面板可能会显示3级弹跳的持续时间是
59 秒，这是 59.7 向下取整的结果。不管是 59 秒还是 60 秒，弹跳还是那个弹跳，并没有被暗改。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/03/27">
        <TimelineRow>法术的配置时间取消，但新增了捐赠费用。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>2 级弹跳法术的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>2 ~ 5 级弹跳法术的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/18">
        <TimelineRow>5 级弹跳法术的升级时间减少。</TimelineRow>
        <TimelineRow>5 级弹跳法术的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>2 ~ 5 级弹跳法术的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>4 级弹跳法术的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>15 本推出，并在 15 本新增 5 级弹跳法术。</TimelineRow>
        <TimelineRow>3 ~ 4 级弹跳法术的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/12/09">
        <TimelineRow>2 ~ 4 级弹跳法术的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/06/22">
        <TimelineRow>走出弹跳法术效果范围的部队不会再重新选择目标，这是为了避免部队卡在其法术效果范围内。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/12/09">
        <TimelineRow>13 本推出，并在 13 本新增 4 级弹跳法术。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/04/02">
        <TimelineRow>包含大量降低发展成本和提高发展速度的调整，其中 2 级弹跳法术的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
