---
title: "部落冲突 coc 都城巨型地雷升级数据"
navTitle: "巨型地雷"
shownTitle: "巨型地雷"
module: upgrade-capital
imgFolder: capital_buildings/2281
wiki: https://clashofclans.fandom.com/wiki/Mega_Mine/Clan_Capital
canonical: /upgrade/2281-Mega-Mine
dataSyncedOn: 2026-10-13
description: "一个隐藏的强力爆炸陷阱。可选择对地或对空！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/2281-Mega-Mine.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2022-05-02'">

<template #introduction>

- *如想查看夜世界的巨型地雷，请访问：[夜世界巨型地雷](/upgrade/1183-Mega-Mine)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Mega_Mine5.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2022/05/02">
        <TimelineRow>巨型地雷随着部落都城玩法一同推出。。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
