---
title: "部落冲突 coc 都城防空火箭升级数据"
navTitle: "防空火箭"
shownTitle: "防空火箭"
module: upgrade-capital
imgFolder: capital_buildings/2203
wiki: https://clashofclans.fandom.com/wiki/Air_Defense
canonical: /upgrade/2203-Air-Defense
dataSyncedOn: 2026-10-13
description: "防空火箭是歼灭敌军空中部队的利器，可惜它不能攻击地面上的敌人。请巧妙部署防空火箭，最大限度保护您的领空。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/2203-Air-Defense.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-09-14'">

<template #introduction>

- *如想查看家乡的防空火箭，请访问：[防空火箭](/upgrade/0304-Air-Defense)。*
- *如想查看夜世界的防空火炮，请访问：[夜世界防空火炮](/upgrade/1104-Firecrackers)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Air_Defense5.png" :imgAlt="$frontmatter.navTitle"
    description="防空火箭是歼灭敌军空中部队的利器，可惜它不能攻击地面上的敌人。<br>请巧妙部署防空火箭，最大限度保护您的领空。"
    :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/09/14">
        <TimelineRow>5 级防空火箭的每秒伤害降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/30">
        <TimelineRow>将防空火箭攻击速度从 1 秒每次降低到 1.5 秒每次。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/05/02">
        <TimelineRow>防空火箭随着部落都城玩法一同推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
