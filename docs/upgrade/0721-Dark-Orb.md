---
title: "部落冲突 coc 暗黑魔球装备升级数据"
navTitle: "暗黑魔球"
shownTitle: "暗黑魔球"
module: upgrade-home
imgFolder: home_heroes/0721
wiki: https://clashofclans.fandom.com/wiki/Dark_Orb
canonical: /upgrade/0721-Dark-Orb
dataSyncedOn: 2026-10-13
description: "暗黑魔球是亡灵王子的两件初始装备之一。暗黑魔球装备可以让亡灵王子使用技能时召唤出一颗水晶，并向他所面对的方向移动。水晶移动时会对周围的部队造成少量伤害，并在一段时间内减慢敌方单位的移动速度和攻击速度。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0721-Dark-Orb.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-11-17'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Dark_Orb_info.png" :imgAlt="$frontmatter.navTitle" description="对命中的所有目标造成伤害，并减缓目标的速度" />

<SmallTitle>说明</SmallTitle>

1. 暗黑魔球是 [亡灵王子](/upgrade/0204-Minion-Prince) 的两件初始装备之一，另一件是 [护卫玩偶](/upgrade/0720-Henchmen-Puppet)。
2. 暗黑魔球装备可以让亡灵王子使用技能时召唤出一颗水晶，并向他所面对的方向移动。水晶移动时会对周围的部队造成少量伤害，并在一段时间内减慢敌方单位的移动速度和攻击速度。
    - 水晶的伤害和减速效果对敌方的建筑、援军、英雄都有效。
    - 由于水晶只对亡灵王子前方的单位有效，因此使用技能时需要注意亡灵王子面对的方向，以免浪费技能。
3. 除了召唤水晶外，该装备还可以为亡灵王子提供额外的每秒伤害和生命值。

注意：

4. 如果升级费用中有多种资源，则同时需要多种资源才能升级。
5. 如果玩家升级到了 9 本并解锁了亡灵王子，即使玩家没有马上升 [铁匠铺](/upgrade/0488-Blacksmith) 也可以升级护卫玩偶装备。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/11/17">
        <TimelineRow>现在亡灵王子的所有装备都提供 500 生命值加成。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>亡灵王子的初始装备随英雄的推出而同步推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
