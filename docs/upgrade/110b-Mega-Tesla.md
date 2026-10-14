---
title: "部落冲突 coc 夜世界超级特斯拉电磁塔升级数据"
navTitle: "超级特斯拉电磁塔"
shownTitle: "超级特斯拉电磁塔"
module: upgrade-bh
imgFolder: bh_buildings/110b
wiki: https://clashofclans.fandom.com/wiki/Mega_Tesla
canonical: /upgrade/110b-Mega-Tesla
dataSyncedOn: 2026-10-13
description: "如果特斯拉电磁塔变得超级庞大会怎样？即使面对最强大的敌军，它的超强力电流也能对他们造成重创！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/110b-Mega-Tesla.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-05-15'">

<template #introduction>

- *如想查看夜世界的特斯拉电磁塔，请访问：[夜世界特斯拉电磁塔](/upgrade/1103-Hidden-Tesla)。*
- *如想查看家乡的巨型特斯拉电磁塔（12 本自带武器），请访问：[巨型特斯拉电磁塔](/upgrade/030c-Giga-Tesla)。*
- *如想查看都城的超级特斯拉电磁塔，请访问：，请访问：[超级特斯拉电磁塔](/upgrade/220b-Hidden-Mega-Tesla)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Mega_Tesla10.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/05/15">
        <TimelineRow>夜世界重做，建筑的数值重新平衡，伤害、生命值等数据有变化。</TimelineRow>
        <TimelineRow>所有等级超级特斯拉电磁塔的升级时间增加。</TimelineRow>
        <TimelineRow>夜世界 10 本推出，超级特斯拉电磁塔可升至 10 级。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/06/18">
        <TimelineRow>夜世界 9 本推出，超级特斯拉电磁塔可升至 9 级。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
