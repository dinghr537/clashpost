---
title: "部落冲突 coc 冷冽冰晶装备升级数据"
navTitle: "冷冽冰晶"
shownTitle: "冷冽冰晶"
module: upgrade-home
imgFolder: home_heroes/07c6
wiki: https://clashofclans.fandom.com/wiki/Frost_Flake
canonical: /upgrade/07c6-Frost-Flake
dataSyncedOn: 2026-10-13
description: "冷冽冰晶是飞盾战神的第三件史诗装备，它在 2025 年 12 月的熔岩危机活动中首次开放购买。当飞盾战神装备冷冽冰晶时，开启技能时，能攻击距离飞盾战神最近的建筑并冻结它们几秒。除此之外，冷冽冰晶还可以提升飞盾战神的生命值。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/07c6-Frost-Flake.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-12-08'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Frost_Flake_info.png" :imgAlt="$frontmatter.navTitle" description="向距离最近的防御建筑投掷冰晶，将其冻住。" :isSmallImg="true" />

<SmallTitle>说明</SmallTitle>

1. 冷冽冰晶是 [飞盾战神](/upgrade/0203-Royal-Champion) 的第三件史诗装备，它在 2025 年 12 月的熔岩危机活动中首次开放购买。
2. 开启技能时，冷冽冰晶能同时发射一定数量的冰晶，攻击距离飞盾战神最近的建筑，造成少量伤害并冻结几秒。
3. 除此之外，冷冽冰晶还可以提升飞盾战神的生命值。

注意：如果升级费用中有多种资源，则同时需要多种资源才能升级。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/12/08">
        <TimelineRow>新装备：冷冽冰晶。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
