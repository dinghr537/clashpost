---
title: "部落冲突 coc 都城超级电磁炮升级数据"
navTitle: "超级电磁炮"
shownTitle: "超级电磁炮"
module: upgrade-capital
imgFolder: capital_tech/2010
wiki: https://clashofclans.fandom.com/wiki/Mega_Sparky
canonical: /upgrade/2010-Mega-Sparky
dataSyncedOn: 2026-10-13
description: "这台机器无所畏惧，似乎无人可挡，总是从容不迫地发射雷鸣般的电磁冲击波摧毁防御，这将是敌人永远无法摆脱的噩梦吧？"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/2010-Mega-Sparky.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-10-09'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Mega_Sparky_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

超级电磁炮的解锁条件是建造 [超级电磁炮工坊](/upgrade/2350-Mega-Sparky-Workshop)，而这需要部落解锁哥布林矿井这个子城升到 2 本，且 [都城大本营](/upgrade/2400-Capital-Hall) 达到 9 级。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/10/09">
        <TimelineRow>新兵种：超级电磁炮。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
