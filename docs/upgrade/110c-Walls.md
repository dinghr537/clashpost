---
title: "部落冲突 coc 夜世界城墙升级数据"
navTitle: "城墙"
shownTitle: "城墙"
module: upgrade-bh
imgFolder: bh_buildings/110c
wiki: https://clashofclans.fandom.com/wiki/Wall/Builder_Base
canonical: /upgrade/110c-Walls
dataSyncedOn: 2026-10-13
description: "城墙是保护村庄、阻挡敌军的最好防线。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/110c-Walls.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-05-15'">

<template #introduction>

- *如想查看家乡的城墙，请访问：[城墙](/upgrade/0300-Walls)。*
- *如想查看都城的城墙，请访问：[都城城墙](/upgrade/2200-Walls)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Wall10.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

注：升级城墙时，金币、圣水、戒指任选其一即可。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/05/15">
        <TimelineRow>更新后夜世界的城墙不再是 5 个一组了，你现在可以单独摆放每块城墙。</TimelineRow>
        <TimelineRow>为了适应上一条所说的改动，所有等级城墙的升级花费有调整。调整后，除了 1 级城墙外，其余等级单个城墙的升级花费都降低了。</TimelineRow>
        <TimelineRow>所有等级城墙的生命值减少。</TimelineRow>
        <TimelineRow>夜世界 10 本推出，城墙可升至 10 级。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/06/18">
        <TimelineRow>升级 6 ~ 8 级夜世界城墙所需的壁垒之戒减少。</TimelineRow>
        <TimelineRow>夜世界 9 本推出，城墙可升至 9 级。</TimelineRow>
        <TimelineRow>夜世界 9 本新增 4 组城墙。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
