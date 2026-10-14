---
title: "部落冲突 coc 夜世界治疗小屋升级数据"
navTitle: "治疗小屋"
shownTitle: "治疗小屋"
module: upgrade-bh
imgFolder: bh_buildings/1286
wiki: https://clashofclans.fandom.com/wiki/Healing_Hut
canonical: /upgrade/1286-Healing-Hut
dataSyncedOn: 2026-10-13
description: "按照建筑大师祖母的秘方，熬制一大锅丰盛又美味的汤。在进攻下一区域前，部队喝些汤可恢复部分生命值。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/1286-Healing-Hut.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-05-15'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Healing_Hut6.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/05/15">
        <TimelineRow>夜世界重做，现在 6 本可解锁新建筑：治疗小屋。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
