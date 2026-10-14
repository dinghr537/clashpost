---
title: "部落冲突 coc 都城雷霆皮卡训练营（威能皮卡训练营、超级皮卡训练营）升级数据"
navTitle: "雷霆皮卡训练营"
shownTitle: "雷霆皮卡训练营（威能皮卡训练营、超级皮卡训练营）"
module: upgrade-capital
imgFolder: capital_buildings/234a
wiki: https://clashofclans.fandom.com/wiki/Clan_Capital_Barracks#Power_P.E.K.K.A_Barracks
canonical: /upgrade/234a-Power-P.E.K.K.A-Barracks
dataSyncedOn: 2026-10-13
description: "雷霆皮卡到底是怎么把自己塞进去的？拆成一块一块吗？"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/234a-Power-P.E.K.K.A-Barracks.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2022-05-02'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Power_P.E.K.K.A_Barracks5.png" :imgAlt="$frontmatter.navTitle"
    :description="$frontmatter.description"
    :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2022/05/02">
        <TimelineRow>雷霆皮卡训练营随着部落都城玩法一同推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
