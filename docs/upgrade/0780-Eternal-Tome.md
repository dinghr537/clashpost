---
title: "部落冲突 coc 永恒书卷装备升级数据"
navTitle: "永恒书卷"
shownTitle: "永恒书卷"
module: upgrade-home
imgFolder: home_heroes/0780
wiki: https://clashofclans.fandom.com/wiki/Eternal_Tome
canonical: /upgrade/0780-Eternal-Tome
dataSyncedOn: 2026-10-13
description: "永恒书卷是大守护者的两件初始装备之一。永恒书卷装备可以在大守护者技能生效期间使他周围的单位（包括他自己）在短时间内拥有无敌效果。无敌只能抵消直接伤害，不能抵消减速和击退效果。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0780-Eternal-Tome.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-06-16'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Eternal_Tome_info.png" :imgAlt="$frontmatter.navTitle" description="大守护者和附近所有友军单位免疫伤害。" />

<SmallTitle>说明</SmallTitle>

1. 永恒书卷是 [大守护者](/upgrade/0202-Grand-Warden) 的两件初始装备之一，另一件是 [生命宝石](/upgrade/0781-Life-Gem)。
2. 永恒书卷装备可以在大守护者技能生效期间使他周围的单位（包括他自己）在短时间内拥有无敌效果。
3. 无敌只能抵消直接伤害，不能抵消减速和击退效果，例如：
   - [毒药法术塔](/upgrade/0311-Spell-Tower) 和 [英雄猎手](/upgrade/0088-Headhunter) 的减速效果；
   - [巨型炸弹](/upgrade/0383-Giant-Bomb) 对小单位的击退效果；
   - [空气炮](/upgrade/0306-Air-Sweeper) 的击退效果；
   - [隐形弹簧](/upgrade/0381-Spring-Trap) 的击飞效果。
4. 永恒书卷装备无法让 [炸弹人](/upgrade/0004-Wall-Breaker) 和 [超级炸弹人](/upgrade/0603-Super-Wall-Breaker) 攻击后存活，无法阻止部队被 [隐形弹簧](/upgrade/0381-Spring-Trap) 弹飞，也无法延长 [凤凰](/upgrade/0287-Phoenix) 的无敌效果。
5. 永恒书卷装备的无敌效果在开启技能时生效，仅对光环内的单位有效，走出光环 1 秒后的部队就会失去无敌效果。技能开启后进入光环或在光环内生成的部队可以获得无敌效果。

注意：

6. 如果升级费用中有多种资源，则同时需要多种资源才能升级。<br>
7. 如果玩家升级到了 11 本并解锁了大守护者，即使玩家没有马上升 [铁匠铺](/upgrade/0488-Blacksmith) 也可以升级永恒书卷装备。

在 2023 年 12 月装备系统发布时，已解锁大守护者的玩家会有一个初始的装备等级，并且不需要解锁铁匠铺。装备等级与玩家的英雄等级相关，具体如下表。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/06/16">
        <TimelineRow>所有等级永恒书卷的技能持续时间增加 0.2 秒。</TimelineRow>
        <TimelineRow>现在走出光环 1 秒后的部队会失去无敌效果。</TimelineRow>
        <TimelineRow>现在开启技能后进入的部队可以获得无敌效果了。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/09/09">
        <TimelineRow>6 - 18 级永恒书卷装备的无敌效果持续时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>游戏新增装备系统，永恒书卷是第一批推出的装备。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
