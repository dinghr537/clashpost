---
title: "部落冲突 coc 夜世界圣水收集器升级数据"
navTitle: "圣水收集器"
shownTitle: "圣水收集器"
module: upgrade-bh
imgFolder: bh_buildings/1202
wiki: https://clashofclans.fandom.com/wiki/Elixir_Collector/Builder_Base
canonical: /upgrade/1202-Elixir-Collector
dataSyncedOn: 2026-10-13
description: "圣水收集器可以从村庄地下的圣泉中收集圣水。升级您的圣水收集器以使圣水产量最大化。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/1202-Elixir-Collector.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-05-15'">

<template #introduction>

- *如想查看家乡的圣水收集器，请访问：[圣水收集器](/upgrade/0402-Elixir-Collector)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Elixir_Collector10.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

一般来说，损坏的建筑不视为解锁，比如说时光钟楼 4 本解锁。按照这个逻辑，夜世界 1 本的圣水收集器和圣水收集器数量应为 0. 但考虑到 1 本常常是新手教程，比较特殊，为了方便玩家理解，这里没有按照上述规则来。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/05/15">
        <TimelineRow>夜世界重做，建筑的数值重新平衡，伤害、生命值等数据有变化。</TimelineRow>
        <TimelineRow>5 ~ 9 级圣水收集器的升级费用增加。</TimelineRow>
        <TimelineRow>夜世界 10 本推出，圣水收集器可升至 10 级。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/10/16">
        <TimelineRow>填满夜世界的金矿和圣水收集器所需的时间由 12 小时变成 24 小时。</TimelineRow>
    </TimelineItem>
     <TimelineItem date="2019/06/18">
        <TimelineRow>夜世界 9 本推出，圣水收集器可升至 9 级。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
