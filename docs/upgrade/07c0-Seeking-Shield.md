---
title: "部落冲突 coc 寻踪飞盾（追踪神盾）装备升级数据"
navTitle: "寻踪飞盾"
shownTitle: "寻踪飞盾（追踪神盾）"
module: upgrade-home
imgFolder: home_heroes/07c0
wiki: https://clashofclans.fandom.com/wiki/Seeking_Shield
canonical: /upgrade/07c0-Seeking-Shield
dataSyncedOn: 2026-10-13
description: "寻踪飞盾是飞盾战神的两件初始装备之一。寻踪飞盾装备可以让飞盾战神在使用技能时投掷一个盾牌，盾牌会击中四个不同的目标，对每个目标造成固定伤害。盾牌优先攻击防御建筑的特点使它非常适合用来清理阵型中间的关键防御，它攻击距离无限的特点使它十分适合用来在战斗结束时清理角落的建筑工人小屋。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/07c0-Seeking-Shield.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-12-12'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Seeking_Shield_info.png" :imgAlt="$frontmatter.navTitle" description="投掷盾牌，在防御建筑间弹跳并造成伤害。" />

<SmallTitle>说明</SmallTitle>

1. 寻踪飞盾是 [飞盾战神](/upgrade/0203-Royal-Champion) 的两件初始装备之一，另一件是 [皇家宝石](/upgrade/07c1-Royal-Gem)。
2. 寻踪飞盾装备可以让飞盾战神在使用技能时投掷一个盾牌，盾牌会击中四个不同的目标，对每个目标造成固定伤害。
   - 盾牌优先攻击防御建筑。如果场上至少有 4 个防御建筑，则盾牌只攻击防御建筑。如果剩余的防御建筑少于 4 个，则盾牌会击中所有防御，剩下的名额才会留给防守方部队以及非防御建筑。
   - 由于盾牌优先攻击防御的特点，它非常适合用来清理阵型中间的关键防御。
   - 盾牌的攻击距离是无限的，因此十分适合用来在战斗结束时清理角落的 [建筑工人小屋](/upgrade/0500-Builders-Hut)。
3. 除了投掷盾牌外，寻踪飞盾装备还可以增加飞盾战神的生命值。

注意：

4. 如果升级费用中有多种资源，则同时需要多种资源才能升级。<br>
5. 如果玩家升级到了 13 本并解锁了飞盾战神，即使玩家没有马上升 [铁匠铺](/upgrade/0488-Blacksmith) 也可以升级寻踪飞盾装备。

在 2023 年 12 月装备系统发布时，已解锁飞盾战神的玩家会有一个初始的装备等级，并且不需要解锁铁匠铺。装备等级与玩家的英雄等级相关，具体如下表。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/12/12">
        <TimelineRow>游戏新增装备系统，寻踪飞盾是第一批推出的装备。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
