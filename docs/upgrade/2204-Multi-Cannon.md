---
title: "部落冲突 coc 都城多管加农炮升级数据"
navTitle: "多管加农炮"
shownTitle: "多管加农炮"
module: upgrade-capital
imgFolder: capital_buildings/2204
wiki: https://clashofclans.fandom.com/wiki/Multi_Cannon
canonical: /upgrade/2204-Cannon
dataSyncedOn: 2026-10-13
description: "拥有多根炮管的加农炮！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/2204-Multi-Cannon.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2022-05-02'">

<template #introduction>

- *如想查看家乡改装后的加农炮，请访问该页面后切换为“连发模式”：[加农炮](/upgrade/0301-Cannon)。*
- *如想查看夜世界的加农炮，请访问：[夜世界双管加农炮](/upgrade/1100-Cannon)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Multi_Cannon5.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

* 多管加农炮的攻击节奏是 0.16 秒一发，8 发后休息 1.6 秒。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2022/05/02">
        <TimelineRow>多管加农炮随着部落都城玩法一同推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
