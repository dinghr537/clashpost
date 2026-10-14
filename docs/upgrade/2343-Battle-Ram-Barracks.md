---
title: "部落冲突 coc 都城野蛮人攻城槌训练营升级数据"
navTitle: "野蛮人攻城槌训练营"
shownTitle: "野蛮人攻城槌训练营"
module: upgrade-capital
imgFolder: capital_buildings/2343
wiki: https://clashofclans.fandom.com/wiki/Clan_Capital_Barracks#Battle_Ram_Barracks
canonical: /upgrade/2343-Battle-Ram-Barracks
dataSyncedOn: 2026-10-13
description: "这东西竟然能塞进这么多根攻城槌！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/2343-Battle-Ram-Barracks.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2022-05-02'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Battle_Ram_Barracks5.png" :imgAlt="$frontmatter.navTitle"
    :description="$frontmatter.description"
    :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2022/05/02">
        <TimelineRow>野蛮人攻城槌训练营随着部落都城玩法一同推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
