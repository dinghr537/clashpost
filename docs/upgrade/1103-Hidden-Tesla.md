---
title: "部落冲突 coc 夜世界特斯拉电磁塔升级数据"
navTitle: "特斯拉电磁塔"
shownTitle: "特斯拉电磁塔"
module: upgrade-bh
imgFolder: bh_buildings/1103
wiki: https://clashofclans.fandom.com/wiki/Hidden_Tesla/Builder_Base
canonical: /upgrade/1103-Hidden-Tesla
dataSyncedOn: 2026-10-13
description: "有点像塔，有点像陷阱，绝对震撼！用科学的力量电击敌军空中和地面部队！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/1103-Hidden-Tesla.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-10-20'">

<template #introduction>

- *如想查看夜世界的超级特斯拉电磁塔，请访问：[夜世界超级特斯拉电磁塔](/upgrade/110b-Mega-Tesla)。*
- *如想查看家乡的特斯拉电磁塔，请访问：[特斯拉电磁塔](/upgrade/0307-Hidden-Tesla)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Hidden_Tesla10.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/10/20">
        <TimelineRow>所有等级级特斯拉电磁塔的每秒伤害降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/05/15">
        <TimelineRow>夜世界重做，建筑的数值重新平衡，伤害、生命值等数据有变化。</TimelineRow>
        <TimelineRow>6 ~ 9 级特斯拉电磁塔的升级时间增加。</TimelineRow>
        <TimelineRow>夜世界 10 本推出，特斯拉电磁塔可升至 10 级。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/06/18">
        <TimelineRow>夜世界 9 本推出，特斯拉电磁塔可升至 9 级。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
