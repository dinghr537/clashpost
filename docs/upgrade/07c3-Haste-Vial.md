---
title: "部落冲突 coc 急速药水瓶装备升级数据"
navTitle: "急速药水瓶"
shownTitle: "急速药水瓶"
module: upgrade-home
imgFolder: home_heroes/07c3
wiki: https://clashofclans.fandom.com/wiki/Haste_Vial
canonical: /upgrade/07c3-Haste-Vial
dataSyncedOn: 2026-10-13
description: "急速药水瓶是飞盾战神的一件普通装备。急速药水瓶可以让飞盾战神在开启技能后获得更快的移动速度和攻击速度。即使不开启技能，急速药水瓶也可以提升飞盾战神在常规状态下的每秒伤害和攻击速度。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/07c3-Haste-Vial.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2024-09-09'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Haste_Vial_info.png" :imgAlt="$frontmatter.navTitle" description="使飞盾战神获得急速效果。" />

<SmallTitle>说明</SmallTitle>

1. 急速药水瓶是 [飞盾战神](/upgrade/0203-Royal-Champion) 的一件普通装备。
2. 急速药水瓶可以让飞盾战神在开启技能后获得更快的移动速度和攻击速度。
3. 即使不开启技能，急速药水瓶也可以提升飞盾战神在常规状态下的每秒伤害和攻击速度。

注意：

4. 上表的 8 点移动速度代表 1 格/秒。
5. 如果升级费用中有多种资源，则同时需要多种资源才能升级。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2024/09/09">
        <TimelineRow>所有等级急速药水瓶装备的技能持续时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/04/17">
        <TimelineRow>9 - 18 级急速药水瓶给飞盾战神（非技能状态下）的攻击速度加成降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/02/27">
        <TimelineRow>在 15 本新增急速药水瓶装备。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
