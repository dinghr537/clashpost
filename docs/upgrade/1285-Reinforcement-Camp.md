---
title: "部落冲突 coc 夜世界预备营升级数据"
navTitle: "预备营"
shownTitle: "预备营"
module: upgrade-bh
imgFolder: bh_buildings/1285
wiki: https://clashofclans.fandom.com/wiki/Reinforcement_Camp
canonical: /upgrade/1285-Reinforcement-Camp
dataSyncedOn: 2026-10-13
description: "进入相应区域后，预备营会提供增援助您一臂之力。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/1285-Reinforcement-Camp.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-05-15'">

<template #introduction>

- *如想查看夜世界的兵营，请访问：[夜世界兵营](/upgrade/1281-Army-Camp)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Reinforcement_Camp.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/05/15">
        <TimelineRow>夜世界重做，现在 6 本可解锁新建筑：预备营。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
