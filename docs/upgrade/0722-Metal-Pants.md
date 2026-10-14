---
title: "部落冲突 coc 铁甲短裤（铁裤衩）装备升级数据"
navTitle: "铁甲短裤"
shownTitle: "铁甲短裤（铁裤衩）"
module: upgrade-home
imgFolder: home_heroes/0722
wiki: https://clashofclans.fandom.com/wiki/Metal_Pants
canonical: /upgrade/0722-Metal-Pants
dataSyncedOn: 2026-10-13
description: "铁甲短裤是亡灵王子的一件普通装备。带上铁甲短裤装备后，亡灵王子在开技能后的一段时间内受到的伤害会减少。除了减少伤害外，铁甲短裤装备还可以增加开启技能时的回血量以及日常状态下的生命值。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0722-Metal-Pants.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-11-17'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Metal_Pants_info.png" :imgAlt="$frontmatter.navTitle" description="生成一层防护屏障，暂时减少所受伤害。"  />

<SmallTitle>说明</SmallTitle>

1. 铁甲短裤是 [亡灵王子](/upgrade/0204-Minion-Prince) 的一件普通装备。
2. 带上铁甲短裤装备后，亡灵王子在开技能后的一段时间内受到的伤害会减少。
3. 除了减少伤害外，铁甲短裤装备还可以增加开启技能时的回血量以及日常状态下的生命值。

注意：如果升级费用中有多种资源，则同时需要多种资源才能升级。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/11/17">
        <TimelineRow>现在亡灵王子的所有装备都提供 500 生命值加成。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/02/10">
        <TimelineRow>新装备：铁甲短裤。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
