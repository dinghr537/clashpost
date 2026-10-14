---
title: "部落冲突 coc 都城野蛮人升级数据"
navTitle: "野蛮人"
shownTitle: "野蛮人"
module: upgrade-capital
imgFolder: capital_tech/20c0
wiki: https://clashofclans.fandom.com/wiki/Barbarian/Clan_Capital
canonical: /upgrade/20c0-Barbarian
dataSyncedOn: 2026-10-13
description: "这些无畏的勇士长着引人注目的胡子，凭借一身壮硕的肌肉在敌人的村庄肆虐。训练一队野蛮人，他们将为您出生入死！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/20c0-Barbarian.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2022-12-12'">

<template #introduction>

- *如想查看家乡的野蛮人，请访问：[野蛮人](/upgrade/0000-Barbarian)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Barbarian_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

1. 都城野蛮人是 [野蛮人攻城槌](/upgrade/2003-Battle-Ram) 和 [突袭炮车](/upgrade/2009-Raid-Cart) 的派生兵种，不能单独部署。
2. 都城的野蛮人属性相同。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2022/12/12">
        <TimelineRow>本次更新后，兵种拥有了防守人口属性。每个都城野蛮人占 1.25 人口。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
