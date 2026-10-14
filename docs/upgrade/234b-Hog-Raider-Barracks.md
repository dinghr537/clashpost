---
title: "部落冲突 coc 都城野猪突袭队训练营（野猪特攻队训练营）升级数据"
navTitle: "野猪突袭队训练营"
shownTitle: "野猪突袭队训练营（野猪特攻队训练营）"
module: upgrade-capital
imgFolder: capital_buildings/234b
wiki: https://clashofclans.fandom.com/wiki/Clan_Capital_Barracks#Hog_Raider_Barracks
canonical: /upgrade/234b-Hog-Raider-Barracks
dataSyncedOn: 2026-10-13
description: "屋子里的尖叫声就没停过，我猜野猪骑士和野猪飞骑都很高兴见到彼此吧。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/234b-Hog-Raider-Barracks.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2022-05-02'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Hog_Raider_Barracks5.png" :imgAlt="$frontmatter.navTitle"
    :description="$frontmatter.description"
    :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2022/05/02">
        <TimelineRow>野猪突袭队训练营（野猪特攻队训练营）随着部落都城玩法一同推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
