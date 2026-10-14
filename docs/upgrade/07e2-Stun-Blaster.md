---
title: "部落冲突 coc 爆震器装备升级数据"
navTitle: "爆震器"
shownTitle: "爆震器"
module: upgrade-home
imgFolder: home_heroes/07e2
wiki: https://clashofclans.fandom.com/wiki/Stun_Blaster
canonical: /upgrade/07e2-Stun-Blaster
dataSyncedOn: 2026-10-13
description: "释放冲击波，对周围的敌人和建筑造成伤害并附带击晕/瘫痪效果。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/07e2-Stun-Blaster.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2026-02-23'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Stun_Blaster_info.png" :imgAlt="$frontmatter.navTitle" description="释放冲击波，对周围的敌人和建筑造成伤害并附带击晕/瘫痪效果。" />

<SmallTitle>说明</SmallTitle>

1. 爆震器是 [飞龙公爵](/upgrade/0205-Dragon-Duke) 的一件普通装备。在铁匠铺 9 级时解锁，需要 16 本。
2. 使用时，爆震器创造冲击波，对周边防御部队和建筑造成伤害和击晕效果。
3. 爆震器装备还可以增加飞龙公爵的每秒伤害和生命值。

注意：如果升级费用中有多种资源，则同时需要多种资源才能升级。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2026/02/23">
        <TimelineRow>新装备：爆震器。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
