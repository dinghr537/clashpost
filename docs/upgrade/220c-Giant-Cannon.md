---
title: "部落冲突 coc 都城巨型加农炮升级数据"
navTitle: "巨型加农炮"
shownTitle: "巨型加农炮"
module: upgrade-capital
imgFolder: capital_buildings/220c
wiki: https://clashofclans.fandom.com/wiki/Giant_Cannon/Clan_Capital
canonical: /upgrade/220c-Giant-Cannon
dataSyncedOn: 2026-10-13
description: "什么都无法阻挡巨型加农炮的攻击。它发射的巨型加农炮弹可以射穿任何东西，并一直向前飞行，一直向前......"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/220c-Giant-Cannon.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2022-05-02'">

<template #introduction>

- *如想查看都城的加农炮，请访问：[都城加农炮](/upgrade/2201-Cannon)。*
- *如想查看都城的多管加农炮，请访问：[都城多管加农炮](/upgrade/2204-Multi-Cannon)。*
- *如想查看夜世界的巨型加农炮，请访问：[夜世界巨型加农炮](/upgrade/110a-Giant-Cannon)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Giant_Cannon5.png" :imgAlt="$frontmatter.navTitle"
    description="什么都无法阻挡巨型加农炮的攻击。<br>它发射的巨型加农炮弹可以射穿任何东西，并一直向前飞行，一直向前......"
    :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2022/05/02">
        <TimelineRow>巨型加农炮随着部落都城玩法一同推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
