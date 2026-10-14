---
title: "部落冲突 coc 都城野蛮人攻城槌升级数据"
navTitle: "野蛮人攻城槌"
shownTitle: "野蛮人攻城槌"
module: upgrade-capital
imgFolder: capital_tech/2003
wiki: https://clashofclans.fandom.com/wiki/Battle_Ram/Clan_Capital
canonical: /upgrade/2003-Battle-Ram
dataSyncedOn: 2026-10-13
description: "四个野蛮人托举着巨大的攻城槌向目标发起冲锋，攻城槌撞击目标时会造成大量伤害。攻城槌破裂后，他们将拿着剑继续奋力战斗！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/2003-Battle-Ram.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-05-15'">

<template #introduction>

- *如想查看家乡的同名临时兵种，请访问：[野蛮人攻城槌](/upgrade/0e01-Battle-Ram)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Battle_Ram_info.png" :imgAlt="$frontmatter.navTitle"
    :description="$frontmatter.description" :isSmallImg="true" />

<SmallTitle>重要说明</SmallTitle>

1. 野蛮人攻城槌的解锁条件是建造 [野蛮人攻城槌训练营](/upgrade/2343-Battle-Ram-Barracks)，而这需要部落解锁野蛮人兵营，并且 [都城大本营](/upgrade/2400-Capital-Hall) 达到 2 级。
2. 野蛮人攻城槌炸墙后会爆出 [野蛮人](/upgrade/20c0-Barbarian)。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/05/15">
         <TimelineRow>现在，野蛮人攻城槌不会在周围正好没有任何可用空间的墙体中被卡住。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/12/12">
        <TimelineRow>所有等级野蛮人攻城槌的生命值增加。</TimelineRow>
        <TimelineRow>所有等级野蛮人攻城槌的伤害减少。</TimelineRow>
        <TimelineRow>增加野蛮人攻城槌对城墙 20 倍伤害增加至 40 倍。</TimelineRow>
        <TimelineRow>野蛮人攻城槌不再计算防守人口。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/05/02">
        <TimelineRow>野蛮人攻城槌随着部落都城玩法一同推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
