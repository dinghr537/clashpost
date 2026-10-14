---
title: "部落冲突 coc 都城城墙升级数据"
navTitle: "城墙"
shownTitle: "城墙"
module: upgrade-capital
imgFolder: capital_buildings/2200
wiki: https://clashofclans.fandom.com/wiki/Wall/Clan_Capital
canonical: /upgrade/2200-Walls
dataSyncedOn: 2026-10-13
description: "城墙可以保卫子城，阻挡敌人的进攻。同一个子城内，所有城墙会同时升级，等级始终保持一致。 同心建设，并肩战斗，子城城墙，同步升级！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/2200-Walls.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2022-05-02'">

<template #introduction>

- *如想查看家乡的城墙，请访问：[城墙](/upgrade/0300-Walls)。*
- *如想查看夜世界的城墙，请访问：[夜世界城墙](/upgrade/110c-Walls)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Wall5.png" :imgAlt="$frontmatter.navTitle"
    description="城墙可以保卫子城，阻挡敌人的进攻。<br>同一个子城内，所有城墙会同时升级，等级始终保持一致。同心建设，并肩战斗，子城城墙，同步升级！"
    :isSmallImg="true" />

\* 这里列出的是每块城墙的成本。由于都城的城墙是整个子城一块升级的，因此实际的升级成本是整个子城的城墙总数乘以每个城墙的升级成本。

注：当子城是 1 级时不能升级城墙，因此上表不列出。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2022/05/02">
        <TimelineRow>城墙随着部落都城玩法一同推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
