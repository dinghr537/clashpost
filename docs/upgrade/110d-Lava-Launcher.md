---
title: "部落冲突 coc 夜世界熔岩发射器升级数据"
navTitle: "熔岩发射器"
shownTitle: "熔岩发射器"
module: upgrade-bh
imgFolder: bh_buildings/110d
wiki: https://clashofclans.fandom.com/wiki/Lava_Launcher
canonical: /upgrade/110d-Lava-Launcher
dataSyncedOn: 2026-10-13
description: "它向很远的地方发射熔岩团，点燃地面。让敌军地面部队尝尝灼烧的滋味！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/110d-Lava-Launcher.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-05-15'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Lava_Launcher10.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

<SmallTitle>重要说明</SmallTitle>

2023 年 6 月更新后，熔岩的递增伤害被取消，现在熔岩的每秒伤害是固定的。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/05/15">
        <TimelineRow>夜世界重做，建筑的数值重新平衡，伤害、生命值等数据有变化。</TimelineRow>
        <TimelineRow>所有等级熔岩发射器的升级时间增加。</TimelineRow>
        <TimelineRow>夜世界 10 本推出，熔岩发射器可升至 10 级。</TimelineRow>
        <TimelineRow>为配合更小的地图，熔岩的射程由 10 ~ 20 格降低到 6 ~ 13 格。</TimelineRow>
        <TimelineRow>熔岩的递增伤害被取消，现在熔岩的每秒伤害是固定的。</TimelineRow>
​    </TimelineItem>
    <TimelineItem date="2019/06/18">
        <TimelineRow>夜世界 9 本推出，新建筑：熔岩发射器。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
