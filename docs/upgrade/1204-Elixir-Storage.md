---
title: "部落冲突 coc 夜世界圣水瓶升级数据"
navTitle: "圣水瓶"
shownTitle: "圣水瓶"
module: upgrade-bh
imgFolder: bh_buildings/1204
wiki: https://clashofclans.fandom.com/wiki/Elixir_Storage/Builder_Base
canonical: /upgrade/1204-Elixir-Storage
dataSyncedOn: 2026-10-13
description: "圣水瓶用来保存从地下收集的圣水。升级圣水瓶以提升其存储上限。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/1204-Elixir-Storage.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-05-15'">

<template #introduction>

- *如想查看家乡的圣水瓶，请访问：[圣水瓶](/upgrade/0405-Elixir-Storage)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Elixir_Storage10.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/05/15">
        <TimelineRow>夜世界重做，建筑的数值重新平衡，伤害、生命值等数据有变化。</TimelineRow>
        <TimelineRow>5 ~ 9 级圣水瓶的升级费用增加。</TimelineRow>
        <TimelineRow>夜世界 10 本推出，圣水瓶可升至 10 级。</TimelineRow>
    </TimelineItem>
     <TimelineItem date="2019/06/18">
        <TimelineRow>夜世界 9 本推出，圣水瓶可升至 9 级。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
