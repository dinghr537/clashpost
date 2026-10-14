---
title: "部落冲突 coc 巨大火球装备升级数据"
navTitle: "巨大火球"
shownTitle: "巨大火球"
module: upgrade-home
imgFolder: home_heroes/0784
wiki: https://clashofclans.fandom.com/wiki/Fireball
canonical: /upgrade/0784-Fireball
dataSyncedOn: 2026-10-13
description: "巨大火球是大守护者的第一件史诗装备，它在 2024 年 3 月的超级飞龙大舞台活动中首次开放购买。巨大火球装备可以让大守护者在开启技能时投掷一个巨大的火球，造成巨大的溅射伤害。该火球会瞄准最近的防御建筑，没有距离限制。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0784-Fireball.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-02-10'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Fireball_info.png" :imgAlt="$frontmatter.navTitle" description="向距离最近的防御建筑扔出一个巨大的爆炸火球。" />

<SmallTitle>说明</SmallTitle>

1. 巨大火球是 [大守护者](/upgrade/0202-Grand-Warden) 的第一件史诗装备，它在 2024 年 3 月的超级飞龙大舞台活动中首次开放购买。
2. 巨大火球装备可以让大守护者在开启技能时投掷一个巨大的火球，造成巨大的溅射伤害。该火球会瞄准最近的防御建筑，没有距离限制。如果没有防御建筑，则火球会瞄准非防御建筑，甚至是敌方部队。
   - 火球不仅可以对建筑造成伤害，也可以对敌方部队造成伤害。
   - 如果火球击中建筑物、地面部队，又或者未击中任何目标，则火球只能对地面目标造成伤害，只有在火球瞄准空中部队的时候才能对空中部队造成伤害。也就是说，火球不能同时击中地面目标和空中目标。
   - 如果所有的目标都被 [隐形法术](/upgrade/0106-Invisibility-Spell) 或 [蔓生法术](/upgrade/0185-Overgrowth-Spell) 覆盖，则火球会飞到地图最上方的角落。角落的这次爆炸仍然会造成溅射伤害。
3. 除了扔火球外，这个装备还可以增加大守护者的每秒伤害。

注：如果升级费用中有多种资源，则同时需要多种资源才能升级。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/02/10">
        <TimelineRow>18 ~ 23 级巨大火球的溅射半径减小。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/03/11">
        <TimelineRow>新装备：巨大火球。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
