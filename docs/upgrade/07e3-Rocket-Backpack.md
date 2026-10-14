---
title: "部落冲突 coc 火箭背包装备升级数据"
navTitle: "火箭背包"
shownTitle: "火箭背包"
module: upgrade-home
imgFolder: home_heroes/07e3
wiki: https://clashofclans.fandom.com/wiki/Rocket_Backpack
canonical: /upgrade/07e3-Rocket-Backpack
dataSyncedOn: 2026-10-13
description: "火箭背包是飞龙公爵的第一件史诗装备。使用后，飞龙公爵会沿直线飞向基地中心并穿越整座基地，对路径上的目标造成伤害。除此之外，火箭背包还会提升飞龙公爵的每秒伤害、生命值和开启技能后的生命值恢复。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/07e3-Rocket-Backpack.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2026-04-08'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Rocket_Backpack_info.png" :imgAlt="$frontmatter.navTitle" description="让飞龙公爵沿直线穿越整个基地，同时对路径上的目标造成伤害。" />

<SmallTitle>说明</SmallTitle>

1. 火箭背包是 [飞龙公爵](/upgrade/0205-Dragon-Duke) 的第一件史诗装备，于 2026 年 4 月的冲突之声活动中开放获取。
2. 使用时，飞龙公爵会沿直线飞行，穿越整座基地，并对路径上的所有目标造成伤害。
3. 飞行期间，飞龙公爵不会被选为目标，也不会触发陷阱或部落城堡援军，但会触发特斯拉电磁塔。
4. 除了主动技能外，火箭背包还会提升飞龙公爵的每秒伤害、生命值，以及开启技能后的生命值恢复量。

注意：如果升级费用中有多种资源，则同时需要多种资源才能升级。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2026/04/08">
        <TimelineRow>新装备：火箭背包。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
