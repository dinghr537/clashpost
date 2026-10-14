---
title: "部落冲突 coc 都城飞行堡垒工坊（空中堡垒工坊）升级数据"
navTitle: "飞行堡垒工坊"
shownTitle: "飞行堡垒工坊（空中堡垒工坊）"
module: upgrade-capital
imgFolder: capital_buildings/2348
wiki: https://clashofclans.fandom.com/wiki/Clan_Capital_Barracks#Flying_Fortress_Yard
canonical: /upgrade/2348-Flying-Fortress-Yard
dataSyncedOn: 2026-10-13
description: "制造飞行堡垒的地方，之所以建在高山上，也许是因为建筑工人怕它飞不起来。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/2348-Flying-Fortress-Yard.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2022-05-02'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Flying_Fortress_Yard5.png" :imgAlt="$frontmatter.navTitle"
    :description="$frontmatter.description"
    :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2022/05/02">
        <TimelineRow>飞行堡垒工坊（空中堡垒工坊）随着部落都城玩法一同推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
