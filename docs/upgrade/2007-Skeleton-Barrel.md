---
title: "部落冲突 coc 都城骷髅飞桶升级数据"
navTitle: "骷髅飞桶"
shownTitle: "骷髅飞桶"
module: upgrade-capital
imgFolder: capital_tech/2007
wiki: https://clashofclans.fandom.com/wiki/Skeleton_Barrel/Clan_Capital
canonical: /upgrade/2007-Skeleton-Barrels
dataSyncedOn: 2026-10-13
description: "是谁说飞桶嘉年华来着？这本来是一场空中骷髅派对，直到飞桶上的气球都破了......然后就变成了地上的骷髅派对！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/2007-Skeleton-Barrel.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2022-12-12'">

<template #introduction>

- *如想查看家乡的同名临时兵种，请访问：[骷髅飞桶](/upgrade/0e04-Skeleton-Barrel)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Skeleton_Barrel_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

1. 骷髅飞桶的解锁条件是建造 [骷髅飞桶训练营](/upgrade/2347-Skeleton-Barrel-Barracks)，而这需要部落解锁气球环礁，并且 [都城大本营](/upgrade/2400-Capital-Hall) 达到 4 级。
2. 骷髅飞桶攻击一次后会爆出 [骷髅](/upgrade/20c1-Skeleton)。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2022/12/12">
        <TimelineRow>所有等级骷髅飞桶的生命值提升。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/05/02">
        <TimelineRow>骷髅飞桶随着部落都城玩法一同推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
