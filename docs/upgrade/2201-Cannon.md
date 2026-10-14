---
title: "部落冲突 coc 都城加农炮升级数据"
navTitle: "加农炮"
shownTitle: "加农炮"
module: upgrade-capital
imgFolder: capital_buildings/2201
wiki: https://clashofclans.fandom.com/wiki/Cannon/Clan_Capital
canonical: /upgrade/2201-Cannon
dataSyncedOn: 2026-10-13
description: "加农炮威力巨大，弥补了它射速缓慢的不足。它的另一个缺点是炮口没法向上抬太高，因此攻击不到空中目标。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/2201-Cannon.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-09-14'">

<template #introduction>

- *如想查看家乡的加农炮，请访问：[加农炮](/upgrade/0301-Cannon)。*
- *如想查看夜世界的加农炮，请访问：[夜世界加农炮](/upgrade/1100-Cannon)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Cannon5.png" :imgAlt="$frontmatter.navTitle"
    description="加农炮威力巨大，弥补了它射速缓慢的不足。<br>它的另一个缺点是炮口没法向上抬太高，因此攻击不到空中目标。"
    :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/09/14">
        <TimelineRow>3 ~ 5 级都城加农炮的生命值降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/05/02">
        <TimelineRow>加农炮随着部落都城玩法一同推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
