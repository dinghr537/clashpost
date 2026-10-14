---
title: "部落冲突 coc 天使木偶（天使玩偶）装备升级数据"
navTitle: "天使木偶"
shownTitle: "天使木偶（天使玩偶）"
module: upgrade-home
imgFolder: home_heroes/0743
wiki: https://clashofclans.fandom.com/wiki/Healer_Puppet
canonical: /upgrade/0743-Healer-Puppet
dataSyncedOn: 2026-10-13
description: "天使木偶是弓箭女皇的一件普通装备。天使木偶可以使弓箭女皇在使用技能使召唤天使，还可以给女王提供额外的生命值，并赋予女王自愈能力。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0743-Healer-Puppet.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-12-12'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Healer_Puppet_info.png" :imgAlt="$frontmatter.navTitle" description="召唤一群天使。" />

<SmallTitle>说明</SmallTitle>

1. 天使木偶是 [弓箭女皇](/upgrade/0201-Archer-Queen) 的一件普通装备。
2. 天使木偶可以使弓箭女皇在使用技能使召唤 [天使](/upgrade/0007-Healer)。
   - 和 [野蛮人木偶](/upgrade/0700-Barbarian-Puppet) 和 [弓箭手木偶](/upgrade/0740-Archer-Puppet) 不同，天使的等级取决于装备等级，而非你在 [实验室](/upgrade/0483-Laboratory) 中的天使等级。
3. 除了召唤天使外，天使木偶还可以给女王提供额外的生命值，并赋予女王自愈能力。

注意：如果升级费用中有多种资源，则同时需要多种资源才能升级。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/12/12">
        <TimelineRow>游戏新增装备系统，天使木偶是第一批推出的装备。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
