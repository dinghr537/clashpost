---
title: "部落冲突 coc 贵族哑铃装备升级数据"
navTitle: "贵族哑铃"
shownTitle: "贵族哑铃"
module: upgrade-home
imgFolder: home_heroes/0723
wiki: https://clashofclans.fandom.com/wiki/Noble_Iron
canonical: /upgrade/0723-Noble-Iron
dataSyncedOn: 2026-10-13
description: "贵族哑铃是亡灵王子的一件普通装备。带上贵族哑铃装备后，亡灵王子在部署后的前几次射击射程更远，伤害更高（类似于超级亡灵的能力）。除了上述能力外，贵族哑铃装备还可以提升亡灵王子的攻击速度。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0723-Noble-Iron.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2026-01-28'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Noble_Iron_info.png" :imgAlt="$frontmatter.navTitle" description="提升亡灵王子前几次攻击的速度、范围和威力。"  />

<SmallTitle>说明</SmallTitle>

1. 贵族哑铃是 [亡灵王子](/upgrade/0204-Minion-Prince) 的一件普通装备。
2. 带上贵族哑铃装备后，亡灵王子在部署后的前几次射击射程更远，伤害更高（类似于 [超级亡灵](/upgrade/0608-Super-Minion) 的能力）。
3. 除了上述能力外，贵族哑铃装备还有以下功能：
    - 提升攻击速度；
    - 增加生命值（与是否开技能无关）。

注意：如果升级费用中有多种资源，则同时需要多种资源才能升级。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2026/01/28">
        <TimelineRow>所有等级贵族哑铃给英雄提供的远程攻击的射程和次数增加。</TimelineRow>
        <TimelineRow>所有等级贵族哑铃给英雄提供攻击速度加成效果提升。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/11/17">
        <TimelineRow>现在亡灵王子的所有装备都提供 500 生命值加成。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>新装备：贵族哑铃。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
