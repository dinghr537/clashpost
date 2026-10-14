---
title: "部落冲突 coc 皇家宝石装备升级数据"
navTitle: "皇家宝石"
shownTitle: "皇家宝石"
module: upgrade-home
imgFolder: home_heroes/07c1
wiki: https://clashofclans.fandom.com/wiki/Royal_Gem
canonical: /upgrade/07c1-Royal-Gem
dataSyncedOn: 2026-10-13
description: "皇家宝石是飞盾战神的两件初始装备之一。皇家宝石可以使飞盾战神在使用技能时恢复大量生命值，这个属性可以与英雄本身的回血属性叠加。另外，皇家宝石可以增加飞盾战神的每秒伤害和生命值。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/07c1-Royal-Gem.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-12-12'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Royal_Gem_info.png" :imgAlt="$frontmatter.navTitle" description="为飞盾战神提供大量额外治疗。" />

<SmallTitle>说明</SmallTitle>

1. 皇家宝石是 [飞盾战神](/upgrade/0203-Royal-Champion) 的两件初始装备之一，另一件是 [寻踪飞盾](/upgrade/07c0-Seeking-Shield)。
2. 皇家宝石可以使飞盾战神在使用技能时恢复大量生命值，这个属性可以与英雄本身的回血属性叠加。
3. 另外，皇家宝石可以增加飞盾战神日常状态下的每秒伤害和生命值。

注意：

4. 如果升级费用中有多种资源，则同时需要多种资源才能升级。<br>
5. 如果玩家升级到了 13 本并解锁了飞盾战神，即使玩家没有马上升 [铁匠铺](/upgrade/0488-Blacksmith) 也可以升级皇家宝石装备。

在 2023 年 12 月装备系统发布时，已解锁飞盾战神的玩家会有一个初始的装备等级，并且不需要解锁铁匠铺。装备等级与玩家的英雄等级相关，具体如下表。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/12/12">
        <TimelineRow>游戏新增装备系统，皇家宝石是第一批推出的装备。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
