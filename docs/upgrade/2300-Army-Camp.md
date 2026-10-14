---
title: "部落冲突 coc 都城兵营升级数据"
navTitle: "兵营"
shownTitle: "兵营"
module: upgrade-capital
imgFolder: capital_buildings/2300
wiki: https://clashofclans.fandom.com/wiki/Army_Camp/Clan_Capital
canonical: /upgrade/2300-Army-Camp
dataSyncedOn: 2026-10-13
description: "等待突袭开始的日子里，您的部落大军可以在这里休息放松。升级兵营可增加部队容量。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/2300-Army-Camp.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-09-14'">

<template #introduction>

- *如想查看家乡的兵营，请访问：[兵营](/upgrade/0480-Army-Camp)。*
- *如想查看夜世界的兵营，请访问：[夜世界兵营](/upgrade/1281-Army-Camp)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Army_Camp5.png" :imgAlt="$frontmatter.navTitle"
    :description="$frontmatter.description"
    :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/09/14">
        <TimelineRow>3 ~ 5 级都城兵营的生命值降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/05/02">
        <TimelineRow>兵营随着部落都城玩法一同推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
