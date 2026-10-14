---
title: "部落冲突 coc 火箭飞矛装备升级数据"
navTitle: "火箭飞矛"
shownTitle: "火箭飞矛"
module: upgrade-home
imgFolder: home_heroes/07c4
wiki: https://clashofclans.fandom.com/wiki/Rocket_Spear
canonical: /upgrade/07c4-Rocket-Spear
dataSyncedOn: 2026-10-13
description: "火箭飞矛是飞盾战神的第一件史诗装备，它在 2024 年 6 月的超级炸弹人大舞台活动中首次开放购买。火箭飞矛装备可以让飞盾战神在接下来的几次攻击中威力更强，范围更远，并且拥有范围伤害。除此之外，火箭飞矛还可以增加飞盾战神不开技能时的每秒伤害和生命值。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/07c4-Rocket-Spear.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2024-09-09'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Rocket_Spear_info.png" :imgAlt="$frontmatter.navTitle" description="她接下来几次投掷的飞矛威力更强，范围更远。" />

<SmallTitle>说明</SmallTitle>

1. 火箭飞矛是 [飞盾战神](/upgrade/0203-Royal-Champion) 的第一件史诗装备，它在 2024 年 6 月的超级炸弹人大舞台活动中首次开放购买。
2. 火箭飞矛装备可以让飞盾战神在接下来的几次攻击中威力更强，范围更远，并且拥有**范围伤害**。
3. 除此之外，火箭飞矛还可以增加飞盾战神不开技能时的每秒伤害和生命值。

注意：

4. 上表的 8 点移动速度代表 1 格/秒。
5. 如果升级费用中有多种资源，则同时需要多种资源才能升级。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2024/09/09">
        <TimelineRow>所有等级火箭飞矛装备的技能攻击次数提高。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/11">
        <TimelineRow>新装备：火箭飞矛。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
