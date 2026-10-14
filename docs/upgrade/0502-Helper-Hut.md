---
title: "部落冲突 coc 帮手小屋升级数据"
navTitle: "帮手小屋"
shownTitle: "帮手小屋"
module: upgrade-home
imgFolder: home_buildings/0502
wiki: https://clashofclans.fandom.com/wiki/Helper_Hut
canonical: /upgrade/0502-Helper-Hut
dataSyncedOn: 2026-10-13
description: "在这个舒适的小屋里，帮手们躺在暖和的高低床上休息！前往帮手小屋，给帮手们指派村庄里的工作。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0502-Helper-Hut.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-02-10'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Helper_Hut_hd.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

1. 你可以在帮手小屋里给帮手们分配任务。
2. 升级帮手小屋无需宝石，但升级帮手需要宝石。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/02/10">
        <TimelineRow>新帮手：炼金术士。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>新建筑：帮手小屋。现在你可以在帮手小屋里给帮手们分配任务。最初帮手小屋总共有两个帮手：实验助手和建筑工人学徒。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
