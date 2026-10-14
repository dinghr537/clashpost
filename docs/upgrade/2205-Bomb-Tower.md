---
title: "部落冲突 coc 都城炸弹塔升级数据"
navTitle: "炸弹塔"
shownTitle: "炸弹塔"
module: upgrade-capital
imgFolder: capital_buildings/2205
wiki: https://clashofclans.fandom.com/wiki/Bomb_Tower/Clan_Capital
canonical: /upgrade/2205-Bomb-Tower
dataSyncedOn: 2026-10-13
description: "炸弹塔可以投掷炸弹轰炸附近的地面部队，被摧毁后会产生一个大爆炸！近战部队最好离它远点吧！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/2205-Bomb-Tower.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-09-14'">

<template #introduction>

- *如想查看家乡的炸弹塔，请访问：[炸弹塔](/upgrade/0308-Bomb-Tower)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Bomb_Tower5.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/09/14">
        <TimelineRow>2 ~ 5 级都城炸弹塔的每秒伤害降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/05/02">
        <TimelineRow>炸弹塔随着部落都城玩法一同推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
