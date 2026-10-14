---
title: "部落冲突 coc 尖刺足球装备升级数据"
navTitle: "尖刺足球"
shownTitle: "尖刺足球"
module: upgrade-home
imgFolder: home_heroes/0705
wiki: https://clashofclans.fandom.com/wiki/Spiky_Ball
canonical: /upgrade/0705-Spiky-Ball
dataSyncedOn: 2026-10-13
description: "尖刺足球是野蛮人之王的第二件史诗装备，它在 2024 年 5 月的并肩哈兰德活动中首次开放购买。当蛮王带上尖刺足球装备时，开启技能后蛮王会踢出一个能在建筑物之间弹跳的足球。足球会选择距离自己最近的建筑物，如果阵型中没有建筑或者所有建筑都被隐形，则足球会飞往地图最上方的角落。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0705-Spiky-Ball.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2024-09-09'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Spiky_Ball_info.png" :imgAlt="$frontmatter.navTitle" description="发射一个尖刺足球，可在建筑之间弹射并造成伤害。" />

<SmallTitle>说明</SmallTitle>

1. 尖刺足球是 [野蛮人之王](/upgrade/0200-Barbarian-King) 的第二件史诗装备，它在 2024 年 5 月的并肩哈兰德活动中首次开放购买。
2. 当蛮王带上尖刺足球装备时，开启技能后蛮王会踢出一个能在建筑物之间弹跳的足球。
   - 足球会选择距离自己最近的建筑物，如果阵型中没有建筑或者所有建筑都被隐形，则足球会飞往地图最上方的角落。
   - 这次攻击没有偏好。即使蛮王被 [水母](/upgrade/0289-Angry-Jelly) 影响，蛮王踢出的足球也不会优先攻击防御建筑。
   - 每个建筑最多只能被命中一次。
3. 另外，尖刺足球还会增加蛮王的每秒伤害与生命值。

注：如果升级费用中有多种资源，则同时需要多种资源才能升级。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2024/09/09">
        <TimelineRow>所有等级（18 级除外）尖刺足球装备可弹跳的目标数量减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/05/07">
        <TimelineRow>新装备：尖刺足球。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
