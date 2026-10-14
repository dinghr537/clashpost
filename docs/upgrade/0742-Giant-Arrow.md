---
title: "部落冲突 coc 巨型箭矢（穿云箭）装备升级数据"
navTitle: "巨型箭矢"
shownTitle: "巨型箭矢（穿云箭）"
module: upgrade-home
imgFolder: home_heroes/0742
wiki: https://clashofclans.fandom.com/wiki/Giant_Arrow
canonical: /upgrade/0742-Giant-Arrow
dataSyncedOn: 2026-10-13
description: "巨型箭矢是弓箭女皇的一件普通装备。巨型箭矢装备可以让女王在使用技能时发射一支非常大的箭，这支箭可以穿透整个阵型。除了射出一支巨大的箭之外，巨型箭矢装备还可以给女王提供额外的每秒伤害和生命值。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0742-Giant-Arrow.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-11-17'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Giant_Arrow_info.png" :imgAlt="$frontmatter.navTitle" description="发射一支穿透力极强的巨大箭矢，穿过整个村庄。" />

<SmallTitle>说明</SmallTitle>

1. 巨型箭矢是 [弓箭女皇](/upgrade/0201-Archer-Queen) 的一件普通装备。
2. 巨型箭矢装备可以让女王在使用技能时发射一支非常大的箭，这支箭（巨箭）可以穿透整个阵型，类似于夜世界的 [巨型加农炮](/upgrade/110a-Giant-Cannon)。
   - 巨箭的行进方向取决于女王使用技能时的目标位置以及女王自身的位置。沿着女王和目标的中心点画一条射线，这条线就是巨箭的路径。如果使用技能时场上所有的目标都被 [隐形法术](/upgrade/0106-Invisibility-Spell) 隐藏了，则巨箭的方向就是女王正对着的方向。
   - 如果敌方部队正好在巨箭的路径上，则地面部队和空中部队都可以被击中。
   - [狂暴法术](/upgrade/0102-Rage-Spell) 不能提升巨箭的伤害。
3. 除了射出一支巨大的箭之外，巨型箭矢装备还可以给女王提供额外的每秒伤害和生命值。

注意：如果升级费用中有多种资源，则同时需要多种资源才能升级。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/11/17">
        <TimelineRow>18 级巨型箭矢的伤害提升。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>游戏新增装备系统，巨型箭矢是第一批推出的装备。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
