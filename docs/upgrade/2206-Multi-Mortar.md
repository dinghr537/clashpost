---
title: "部落冲突 coc 都城多管迫击炮升级数据"
navTitle: "多管迫击炮"
shownTitle: "多管迫击炮"
module: upgrade-capital
imgFolder: capital_buildings/2206
wiki: https://clashofclans.fandom.com/wiki/Multi_Mortar/Clan_Capital
canonical: /upgrade/2206-Multi-Mortar
dataSyncedOn: 2026-10-13
description: "远距离发射多枚能造成溅射伤害的炮弹，以保证最大可能命中目标！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/2206-Multi-Mortar.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-09-14'">

<template #introduction>

- *如想查看家乡改装后的迫击炮，请访问该页面后切换为“连发模式”：[迫击炮](/upgrade/0303-Mortar)。*
- *如想查看夜世界的多管迫击炮，请访问：[夜世界多管迫击炮](/upgrade/1108-Multi-Mortar)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Multi_Mortar5.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

\* 多管迫击炮的攻击节奏是：4 连发期间每发 0.5 秒，之后休息 5 秒。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/09/14">
        <TimelineRow>2 ~ 5 级都城多管迫击炮的每秒伤害降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/05/02">
        <TimelineRow>多管迫击炮随着部落都城玩法一同推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
