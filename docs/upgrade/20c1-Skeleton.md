---
title: "部落冲突 coc 都城骷髅升级数据"
navTitle: "骷髅"
shownTitle: "骷髅"
module: upgrade-capital
imgFolder: capital_tech/20c1
wiki: https://clashofclans.fandom.com/wiki/Barbarian/Clan_Capital
canonical: /upgrade/20c1-Skeleton
dataSyncedOn: 2026-10-13
description: "这些不死生物独自行动时并不具备什么威胁，但它们从不单打独斗，而是成群结队，并肩作战！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/20c1-Skeleton.json";
</script>

<SyncedUnitData :data="unitData">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Skeleton_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

都城骷髅是 [骷髅飞桶](/upgrade/2007-Skeleton-Barrel) 和 [飞行堡垒](/upgrade/2008-Flying-Fortress) 的派生兵种，不能单独部署。

</template>

</SyncedUnitData>
