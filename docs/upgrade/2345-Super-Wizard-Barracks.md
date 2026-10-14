---
title: "部落冲突 coc 都城超级法师训练营升级数据"
navTitle: "超级法师训练营"
shownTitle: "超级法师训练营"
module: upgrade-capital
imgFolder: capital_buildings/2345
wiki: https://clashofclans.fandom.com/wiki/Clan_Capital_Barracks#Super_Wizard_Barracks
canonical: /upgrade/2345-Super-Wizard-Barracks
dataSyncedOn: 2026-10-13
description: "看起来像是超级法师的训练营，但接连不断的爆炸吓得大家都不敢靠近。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/2345-Super-Wizard-Barracks.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2022-05-02'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Super_Wizard_Barracks5.png" :imgAlt="$frontmatter.navTitle"
    :description="$frontmatter.description"
    :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2022/05/02">
        <TimelineRow>超级法师训练营随着部落都城玩法一同推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
