---
title: "部落冲突 coc 贪婪渡鸦升级数据"
navTitle: "贪婪渡鸦"
shownTitle: "贪婪渡鸦"
module: upgrade-home
imgFolder: home_heroes/028b
wiki: https://clashofclans.fandom.com/wiki/Greedy_Raven
canonical: /upgrade/028b-Greedy-Raven
dataSyncedOn: 2026-10-13
description: "更可怕的稻草人，也挡不住贪婪渡鸦扑向闪亮的战利品！这只蒙面怪鸟快速挥动羽翼，专门攻击资源建筑和关键目标，对其造成额外伤害。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/028b-Greedy-Raven.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2026-02-23'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Greedy_Raven_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

贪婪渡鸦的技能（闪光扫击）：优先攻击英雄附近的资源类建筑，并对资源类建筑造成额外伤害。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2026/02/23">
        <TimelineRow>新战宠：贪婪渡鸦。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
