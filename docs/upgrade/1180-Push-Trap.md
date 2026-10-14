---
title: "部落冲突 coc 夜世界弹射陷阱升级数据"
navTitle: "弹射陷阱"
shownTitle: "弹射陷阱"
module: upgrade-bh
imgFolder: bh_buildings/1180
wiki: https://clashofclans.fandom.com/wiki/Push_Trap
canonical: /upgrade/1180-Push-Trap
dataSyncedOn: 2026-10-13
description: "将敌军地面部队弹向您设定的方向。走你！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/1180-Push-Trap.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-05-15'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Push_Trap10.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/05/15">
        <TimelineRow>夜世界重做，建筑的数值重新平衡，伤害、生命值等数据有变化。</TimelineRow>
        <TimelineRow>1 ~ 3 级弹射陷阱的弹射能力增加，4 ~ 9 级弹射陷阱的弹射能力减弱。</TimelineRow>
        <TimelineRow>6 ~ 9 级弹射陷阱的升级费用增加。</TimelineRow>
        <TimelineRow>夜世界 10 本推出，弹射陷阱可升至 10 级。</TimelineRow>
        <TimelineRow>弹射陷阱现在可以弹射弹跳单位，如野猪骑士。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/06/22">
        <TimelineRow>1 级和 2 级弹射陷阱的弹射能力从 5/7 提升至 6/8.</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/06/18">
        <TimelineRow>夜世界 9 本推出，弹射陷阱可升至 9 级。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
