---
title: "部落冲突 coc 粉碎者升级数据"
navTitle: "粉碎者"
shownTitle: "粉碎者"
module: upgrade-home
imgFolder: home_th/0841
wiki: https://clashofclans.fandom.com/wiki/Smasher
canonical: /upgrade/0841-Smasher
dataSyncedOn: 2026-10-13
description: "这位重型守卫会对地面和空中部队造成溅射伤害。粉碎者是个输不起的暴躁角色——如果大本营被摧毁，他就会勃然大怒；如果他自己被击倒，他也会留下愤怒的余威。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0841-Smasher.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2026-01-12'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Smasher_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

- 粉碎者的特殊技能（败局狂怒）：大本营被摧毁会进入狂暴状态，这种状态会持续到他被击倒为止。另外，粉碎者在被击倒后会释放一个狂暴法术，其效果与 [狂暴法术塔](/upgrade/0311-Spell-Tower) 相同，可强化防御建筑和防守方单位。
    - 无论粉碎者被击倒前是否进入了狂暴状态，这个狂暴法术都会释放。

警戒半径：（待证实）如果敌军进入这个范围，守卫会看向部队的方向，准备反击。<br>
巡逻半径：（待证实）在没有敌人的情况下，守卫也会走动，而这个走动的范围叫巡逻半径。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2026/01/12">
        <TimelineRow>巡逻半径从 10 格增加到 12 格。</TimelineRow>
        <TimelineRow>警戒半径从 12 格增加到 14 格。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/11/17">
        <TimelineRow>推出守卫系统，粉碎者是第一批推出的守卫。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
