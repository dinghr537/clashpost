---
title: "部落冲突 coc 都城超级电磁炮工坊升级数据"
navTitle: "超级电磁炮工坊"
shownTitle: "超级电磁炮工坊"
module: upgrade-capital
imgFolder: capital_buildings/2350
wiki: https://clashofclans.fandom.com/wiki/Clan_Capital_Barracks#Mega_Sparky_Workshop
canonical: /upgrade/2350-Mega-Sparky-Workshop
dataSyncedOn: 2026-10-13
description: "闪电反复击中玻璃球，于是就有了这台超级电磁炮。这足以让经过的人毛发悚立。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/2350-Mega-Sparky-Workshop.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-10-09'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Mega_Sparky_Workshop4.png" :imgAlt="$frontmatter.navTitle"
    :description="$frontmatter.description"
    :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/10/09">
        <TimelineRow>新建筑：超级电磁炮工坊。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
