---
title: "部落冲突 coc 陨石法杖装备升级数据"
navTitle: "陨石法杖"
shownTitle: "陨石法杖"
module: upgrade-home
imgFolder: home_heroes/0725
wiki: https://clashofclans.fandom.com/wiki/Meteor_Staff
canonical: /upgrade/0725-Meteor-Staff
dataSyncedOn: 2026-10-13
description: "陨石法杖是亡灵王子的第二件史诗装备。当亡灵王子带上陨石法杖装备后，他会周期性地在最近的防御建筑上召唤陨石，这些陨石会对地面和空中单位造成伤害，其伤害足以波及相邻建筑。除了召唤陨石外，陨石法杖还可以提升亡灵王子在常规状态下的伤害和生命值。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0725-Meteor-Staff.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-11-17'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Meteor_Staff_info.png" :imgAlt="$frontmatter.navTitle" description="召唤出神秘的陨石，反复轰击最近的防御建筑。"  />

<SmallTitle>说明</SmallTitle>

1. 陨石法杖是 [亡灵王子](/upgrade/0204-Minion-Prince) 的第二件史诗装备，它在 2025 年 10 月的宇宙摇滚活动中首次开放购买。
2. 当亡灵王子带上陨石法杖装备后，他会周期性地在最近的防御建筑上召唤陨石，这些陨石会对地面和空中单位造成伤害，其伤害足以波及相邻建筑。
3. 只要建筑未被 [隐身](/upgrade/0106-Invisibility-Spell) 且未被 [蔓生法术](/upgrade/0185-Overgrowth-Spell) 的藤蔓缠住，建筑就能被攻击。即使该建筑距离亡灵王子很远，只要满足“最近建筑”这个条件，也会被攻击。
    - 如果地图上没有防御建筑，陨石会攻击最近的建筑。如果地图上没有可攻击的建筑，则陨石不会生成。
4. 除了召唤陨石外，陨石法杖还可以提升亡灵王子在常规状态下的伤害和生命值。

注意：如果升级费用中有多种资源，则同时需要多种资源才能升级。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/11/17">
        <TimelineRow>现在亡灵王子的所有装备都提供 500 生命值加成。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/10/10">
        <TimelineRow>新装备：陨石法杖。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
