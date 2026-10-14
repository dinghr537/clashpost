---
title: "部落冲突 coc 巨型手套装备升级数据"
navTitle: "巨型手套"
shownTitle: "巨型手套"
module: upgrade-home
imgFolder: home_heroes/0704
wiki: https://clashofclans.fandom.com/wiki/Giant_Gauntlet
canonical: /upgrade/0704-Giant-Gauntlet
dataSyncedOn: 2026-10-13
description: "巨型手套是野蛮人之王的第一件史诗装备，它在 2023 年 12 月的饼干大作战活动中首次开放购买。当蛮王带上巨型手套装备时，开启技能后蛮王受到的伤害减少，而且会造成范围伤害。另外，巨型手套还会增加蛮王的每秒伤害，并给予他自愈的能力。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0704-Giant-Gauntlet.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2026-01-28'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Giant_Gauntlet_info.png" :imgAlt="$frontmatter.navTitle" description="野蛮人之王体型变大，可造成范围伤害且减少所受伤害。" />

<SmallTitle>说明</SmallTitle>

1. 巨型手套是 [野蛮人之王](/upgrade/0200-Barbarian-King) 的第一件史诗装备，它在 2023 年 12 月的饼干大作战活动中首次开放购买。
2. 当蛮王带上巨型手套装备时，开启技能后蛮王受到的伤害减少，而且会造成范围伤害。
3. 另外，巨型手套还会增加蛮王的每秒伤害，并给予他自愈的能力。

注：如果升级费用中有多种资源，则同时需要多种资源才能升级。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2026/01/28">
        <TimelineRow>所有等级巨型手套装备的减伤效果提升。</TimelineRow>
        <TimelineRow>所有等级巨型手套装备的技能持续时间增加。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/09/09">
        <TimelineRow>21 - 22、24 - 27级巨型手套的伤害减免比例降低。</TimelineRow>
        <TimelineRow>19 - 27 级巨型手套可以给英雄提供的每秒伤害加成减少。</TimelineRow>
        <TimelineRow>20 - 27 级巨型手套给英雄提供的自愈能力略微降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/18">
        <TimelineRow>新装备：巨型手套。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
