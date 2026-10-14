---
title: "部落冲突 coc 都城撼地巨石升级数据"
navTitle: "撼地巨石"
shownTitle: "撼地巨石"
module: upgrade-capital
imgFolder: capital_buildings/220a
wiki: https://clashofclans.fandom.com/wiki/Crusher/Clan_Capital
canonical: /upgrade/220a-Crusher
dataSyncedOn: 2026-10-13
description: "撼地巨石非常在意自己的私人空间。这块巨石会凶狠地砸向入侵的地面部队，将他们碾压！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/220a-Crusher.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2022-05-02'">

<template #introduction>

- *如想查看夜世界的撼地巨石，请访问：[夜世界撼地巨石](/upgrade/1105-Crusher)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Crusher5.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2022/05/02">
        <TimelineRow>撼地巨石随着部落都城玩法一同推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
