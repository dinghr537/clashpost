---
title: "部落冲突 coc 都城火箭气球兵训练营升级数据"
navTitle: "火箭气球兵训练营"
shownTitle: "火箭气球兵训练营"
module: upgrade-capital
imgFolder: capital_buildings/2346
wiki: https://clashofclans.fandom.com/wiki/Clan_Capital_Barracks#Rocket_Balloon_Barracks
canonical: /upgrade/2346-Rocket-Balloon-Barracks
dataSyncedOn: 2026-10-13
description: "既然要造火箭气球兵，哪还有时间去管安不安全。最重要的是快！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/2346-Rocket-Balloon-Barracks.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2022-05-02'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Rocket_Balloon_Barracks5.png" :imgAlt="$frontmatter.navTitle"
    :description="$frontmatter.description"
    :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2022/05/02">
        <TimelineRow>火箭气球兵训练营随着部落都城玩法一同推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
