---
title: "部落冲突 coc 雷电战靴装备升级数据"
navTitle: "雷电战靴"
shownTitle: "雷电战靴"
module: upgrade-home
imgFolder: home_heroes/07c5
wiki: https://clashofclans.fandom.com/wiki/Electro_Boots
canonical: /upgrade/07c5-Electro-Boots
dataSyncedOn: 2026-10-13
description: "雷电战靴是飞盾战神的第二件史诗装备，它在 2024 年 12 月的大闹玩具店活动中首次开放购买。装备雷电战靴后，飞盾战神周围会形成雷电光环，对敌方单位造成持续伤害。除了雷电光环外，雷电战靴装备还可以为飞盾战神提供额外生命值，并让飞盾战神拥有自行回血的能力。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/07c5-Electro-Boots.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-02-10'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Electro_Boots_info.png" :imgAlt="$frontmatter.navTitle" description="每隔一段时间对飞盾战神附近的一切造成伤害。" />

<SmallTitle>说明</SmallTitle>

1. 雷电战靴是 [飞盾战神](/upgrade/0203-Royal-Champion) 的第二件史诗装备，它在 2024 年 12 月的大闹玩具店活动中首次开放购买。
2. 装备雷电战靴后，飞盾战神周围会形成雷电光环，对敌方单位造成持续伤害。
3. 除了雷电光环外，雷电战靴装备还可以为飞盾战神提供额外生命值，并让飞盾战神拥有自行回血的能力。

注意：

4. 上表的 8 点移动速度代表 1 格/秒。
5. 如果升级费用中有多种资源，则同时需要多种资源才能升级。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/02/10">
        <TimelineRow>15 ~ 27 级雷电战靴对英雄的每秒回血值减小。</TimelineRow>
        <TimelineRow>所有等级雷电战靴的光环伤害降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/12/11">
        <TimelineRow>新装备：雷电战靴。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
