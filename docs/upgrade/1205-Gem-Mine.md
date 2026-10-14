---
title: "部落冲突 coc 夜世界宝石矿井升级数据"
navTitle: "宝石矿井"
shownTitle: "宝石矿井"
module: upgrade-bh
imgFolder: bh_buildings/1205
wiki: https://clashofclans.fandom.com/wiki/Gem_Mine
canonical: /upgrade/1205-Gem-Mine
dataSyncedOn: 2026-10-13
description: "宝石矿井中藏有少量宝石，这是极其珍贵的资源！开采宝石既费时又费力。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/1205-Gem-Mine.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-05-15'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Gem_Mine10.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/05/15">
        <TimelineRow>夜世界重做，建筑的数值重新平衡，伤害、生命值等数据有变化。</TimelineRow>
        <TimelineRow>5 ~ 9 级宝石矿井的升级费用增加。</TimelineRow>
        <TimelineRow>夜世界 10 本推出，宝石矿井可升至 10 级。</TimelineRow>
    </TimelineItem>
     <TimelineItem date="2019/06/18">
        <TimelineRow>夜世界 9 本推出，宝石矿井可升至 9 级。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
