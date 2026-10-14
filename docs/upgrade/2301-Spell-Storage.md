---
title: "部落冲突 coc 都城法术仓库升级数据"
navTitle: "法术仓库"
shownTitle: "法术仓库"
module: upgrade-capital
imgFolder: capital_buildings/2301
wiki: https://clashofclans.fandom.com/wiki/Spell_Storage
canonical: /upgrade/2301-Spell-Storage
dataSyncedOn: 2026-10-13
description: "储存都城里配制的法术。升级法术仓库可提升突袭时的法术容量。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/2301-Spell-Storage.json";
</script>

<SyncedUnitData :data="unitData">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Spell_Storage5.png" :imgAlt="$frontmatter.navTitle"
    :description="$frontmatter.description"
    :isSmallImg="true" />

</template>

</SyncedUnitData>
