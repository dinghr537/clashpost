---
title: "部落冲突 coc 冰封箭矢（寒冰箭）装备升级数据"
navTitle: "冰封箭矢"
shownTitle: "冰封箭矢（寒冰箭）"
module: upgrade-home
imgFolder: home_heroes/0744
wiki: https://clashofclans.fandom.com/wiki/Frozen_Arrow
canonical: /upgrade/0744-Frozen-Arrow
dataSyncedOn: 2026-10-13
description: "冰封箭矢是弓箭女皇的第一件史诗装备，它在 2024 年 2 月的龙年佳节活动中首次开放购买。带上冰封箭矢装备后，被女王打中的目标在一段时间内移动速度和攻击速度会变慢。另外，冰封箭矢还能增加女王的每秒伤害。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0744-Frozen-Arrow.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2024-11-25'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Frozen_Arrow_info.png" :imgAlt="$frontmatter.navTitle" description="冰封箭矢会减缓被命中目标的速度。" />

<SmallTitle>说明</SmallTitle>

1. 冰封箭矢是 [弓箭女皇](/upgrade/0201-Archer-Queen) 的第一件史诗装备，它在 2024 年 2 月的龙年佳节活动中首次开放购买。
2. 带上冰封箭矢装备后，被女王打中的目标在一段时间内移动速度和攻击速度会变慢。
3. 另外，冰封箭矢还能增加女王的每秒伤害。

\# 攻击速度和移动速度的减速比例相同。

注意：如果升级费用中有多种资源，则同时需要多种资源才能升级。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2024/11/25">
        <TimelineRow>现在 8 本就可以解锁弓箭女皇了，该页面的部分信息需要同步更改。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/09/09">
        <TimelineRow>所有等级冰封箭矢击中目标后的减速效果变弱（减速比例降低）。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/02/08">
        <TimelineRow>新装备：冰封箭矢。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
