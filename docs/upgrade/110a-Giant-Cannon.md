---
title: "部落冲突 coc 夜世界巨型加农炮升级数据"
navTitle: "巨型加农炮"
shownTitle: "巨型加农炮"
module: upgrade-bh
imgFolder: bh_buildings/110a
wiki: https://clashofclans.fandom.com/wiki/Giant_Cannon
canonical: /upgrade/110a-Giant-Cannon
dataSyncedOn: 2026-10-13
description: "什么都无法阻挡巨型加农炮的攻击。它发射的巨型加农炮弹可以射穿任何东西，并一直向前飞行，一直向前……"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/110a-Giant-Cannon.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-05-15'">

<template #introduction>

- *如想查看夜世界的双管加农炮，请访问：[夜世界双管加农炮](/upgrade/1101-Double-Cannon)。*
- *如想查看都城的巨型加农炮，请访问：[都城巨型加农炮](/upgrade/220c-Giant-Cannon)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Giant_Cannon10.png" :imgAlt="$frontmatter.navTitle"
    description="什么都无法阻挡巨型加农炮的攻击。<br>它发射的巨型加农炮弹可以射穿任何东西，并一直向前飞行，一直向前……"
    :isSmallImg="true" />

伤害类型：穿透伤害：对炮弹经过的目标都造成伤害。<br>
射程：巨型加农炮只能发现 9.5 格以内的目标并进行攻击，但它的炮弹会一直穿过整个地图， 并对被炮弹击中的目标造成伤害。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/05/15">
        <TimelineRow>夜世界重做，建筑的数值重新平衡，伤害、生命值等数据有变化。</TimelineRow>
        <TimelineRow>所有等级巨型加农炮的升级时间增加。</TimelineRow>
        <TimelineRow>夜世界 10 本推出，巨型加农炮可升至 10 级。</TimelineRow>
        <TimelineRow>巨型加农炮的射程由 9 格提升到 9.5 格。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/06/18">
        <TimelineRow>夜世界 9 本推出，巨型加农炮可升至 9 级。</TimelineRow>
        <TimelineRow>巨型加农炮不再对战争机器造成多倍伤害。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
