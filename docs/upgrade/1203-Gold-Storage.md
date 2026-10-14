---
title: "部落冲突 coc 夜世界储金罐升级数据"
navTitle: "储金罐"
shownTitle: "储金罐"
module: upgrade-bh
imgFolder: bh_buildings/1203
wiki: https://clashofclans.fandom.com/wiki/Gold_Storage/Builder_Base
canonical: /upgrade/1203-Gold-Storage
dataSyncedOn: 2026-10-13
description: "您珍贵的金币都存在这里！不要让狡猾的哥布林有机可乘！升级储金罐，提高它们的容量和抗打击能力。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/1203-Gold-Storage.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-05-15'">

<template #introduction>

- *如想查看家乡的储金罐，请访问：[储金罐](/upgrade/0404-Gold-Storage)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Gold_Storage10.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/05/15">
        <TimelineRow>夜世界重做，建筑的数值重新平衡，伤害、生命值等数据有变化。</TimelineRow>
        <TimelineRow>5 ~ 9 级储金罐的升级费用增加。</TimelineRow>
        <TimelineRow>夜世界 10 本推出，储金罐可升至 10 级。</TimelineRow>
    </TimelineItem>
     <TimelineItem date="2019/06/18">
        <TimelineRow>夜世界 9 本推出，储金罐可升至 9 级。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
