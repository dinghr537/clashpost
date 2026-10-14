---
title: "部落冲突 coc 狂暴宝石装备升级数据"
navTitle: "狂暴宝石"
shownTitle: "狂暴宝石"
module: upgrade-home
imgFolder: home_heroes/0782
wiki: https://clashofclans.fandom.com/wiki/Rage_Gem
canonical: /upgrade/0782-Rage-Gem
dataSyncedOn: 2026-10-13
description: "狂暴宝石是大守护者的一件普通装备。狂暴宝石装备可以在大守护者周围投射出魔法光环，当我方部队在光环内时，它们可以打出更高的伤害。狂暴宝石的效果不能与狂暴法术叠加。如果在光环内使用狂暴法术，则狂暴法术的效果会覆盖狂暴宝石的效果。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0782-Rage-Gem.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2024-09-09'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Rage_Gem_info.png" :imgAlt="$frontmatter.navTitle" description="附近友军单位会造成额外伤害。" />

<SmallTitle>说明</SmallTitle>

1. 狂暴宝石是 [大守护者](/upgrade/0202-Grand-Warden) 的一件普通装备。
2. 狂暴宝石装备可以在大守护者周围投射出魔法光环，当我方部队在光环内时，它们可以打出更高的伤害。
3. 狂暴宝石装备可以让大守护者自己获得更高的每秒伤害和攻击速度，但这不是光环的效果，是装备本身的属性。
4. 狂暴宝石的效果不能与 [狂暴法术](/upgrade/0102-Rage-Spell) 叠加。如果在光环内使用狂暴法术，则狂暴法术的效果会覆盖狂暴宝石的效果。
5. 与狂暴法术一样，狂暴宝石的效果对英雄减半，对攻城机器无效。
6. 与狂暴法术不同的是，狂暴宝石的光环不能提高部队的移动速度和攻击速度。

注：如果升级费用中有多种资源，则同时需要多种资源才能升级。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2024/09/09">
        <TimelineRow>1 - 14 级狂暴宝石装备给光环内部队提供的伤害加成比例提升。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>游戏新增装备系统，狂暴宝石是第一批推出的装备。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
