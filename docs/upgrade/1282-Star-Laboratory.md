---
title: "部落冲突 coc 夜世界星空实验室升级数据"
navTitle: "星空实验室"
shownTitle: "星空实验室"
module: upgrade-bh
imgFolder: bh_buildings/1282
wiki: https://clashofclans.fandom.com/wiki/Star_Laboratory
canonical: /upgrade/1282-Star-Laboratory
dataSyncedOn: 2026-10-13
description: "星空实验室通过探索宇宙的奥秘来发掘兵种的全部潜能。可以提升兵种的生命值和伤害、减少兵种所需空间，还可以增强兵种的特殊技能！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/1282-Star-Laboratory.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-05-15'">

<template #introduction>

- 如想查看家乡的实验室，请访问：[实验室](/upgrade/0483-Laboratory)。

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Star_Laboratory10.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/05/15">
        <TimelineRow>夜世界重做，建筑的数值重新平衡，伤害、生命值等数据有变化。</TimelineRow>
        <TimelineRow>6 ~ 9 级星空实验室的升级费用增加。</TimelineRow>
        <TimelineRow>夜世界 10 本推出，星空实验室可升至 10 级。</TimelineRow>
    </TimelineItem>
     <TimelineItem date="2019/06/18">
        <TimelineRow>夜世界 9 本推出，星空实验室可升至 9 级。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
