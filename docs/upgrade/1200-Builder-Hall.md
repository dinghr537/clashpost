---
title: "部落冲突 coc 建筑大师大本营（夜世界大本营）升级数据"
navTitle: "建筑大师大本营"
shownTitle: "建筑大师大本营（夜世界大本营）"
module: upgrade-bh
imgFolder: bh_buildings/1200
wiki: https://clashofclans.fandom.com/wiki/Builder_Hall
canonical: /upgrade/1200-Builder-Hall
dataSyncedOn: 2026-10-13
description: "建筑大师的家，战斗中的主要目标。在进攻中摧毁敌军的建筑大师大本营可获得一颗胜利之星。摧毁一个区域中 50% 的建筑可获得第二颗胜利之星，摧毁率达到 100% 可获得该区域的三颗胜利之星奖励。
升级建筑大师大本营来解锁更高级的建筑和兵种！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/1200-Builder-Hall.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-05-15'">

<template #introduction>

- 如想查看夜世界的另一个大本营，请访问：[夜世界奥仔哨站](/upgrade/1240-O.T.T.O's-Outpost)。
- 如想查看家乡的大本营，请访问：[大本营](/upgrade/0400-Town-Hall)。
- 如想查看都城的大本营，请访问：[都城大本营](/upgrade/2400-Capital-Hall)、[子城大本营](/upgrade/2401-District-Hall)。

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Builder_Hall10.png" :imgAlt="$frontmatter.navTitle"
    description="建筑大师的家，战斗中的主要目标。<br>在进攻中摧毁敌军的建筑大师大本营可获得一颗胜利之星。摧毁一个区域中 50% 的建筑可获得第二颗胜利之星，摧毁率达到 100% 可获得该区域的三颗胜利之星奖励。<br>升级建筑大师大本营来解锁更高级的建筑和兵种！" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/05/15">
        <TimelineRow>1 级和 3 级建筑大师大本营的生命值增加，4 ~ 9 级建筑大师大本营的生命值减少。</TimelineRow>
        <TimelineRow>5 ~ 9 级建筑大师大本营的资源储量增加。</TimelineRow>
        <TimelineRow>新增 10 级建筑大师大本营。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/06/18">
        <TimelineRow>新增 9 级建筑大师大本营。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
