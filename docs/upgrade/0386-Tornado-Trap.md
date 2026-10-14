---
title: "部落冲突 coc 飓风陷阱（旋风）升级数据"
navTitle: "飓风陷阱"
shownTitle: "飓风陷阱（旋风）"
module: upgrade-home
imgFolder: home_buildings/0386
wiki: https://clashofclans.fandom.com/wiki/Tornado_Trap
canonical: /upgrade/0386-Tornado-Trap
dataSyncedOn: 2026-10-13
description: "飞沙走石会造成皮肉伤，而飓风陷阱还能让敌人晕头转向！把飓风陷阱埋在地下，它产生的漩涡能把敌军卷至飓风中心，阻挡他们的进攻。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0386-Tornado-Trap.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-03-24'">

<template #introduction>

- 本页内容不是空中炸弹，如想查看空中炸弹的数据，请访问：[空中炸弹](/upgrade/0382-Air-Bomb)。

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Tornado_Trap_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

<SmallTitle>重要说明</SmallTitle>

1. 飓风陷阱可以让部队转圈，也可以对部队造成少量伤害，但不能阻止部队发动攻击。
2. [掘地矿工](/upgrade/000b-Miner)、[超级矿工](/upgrade/060e-Super-Miner)、[地兽](/upgrade/0285-Diggy) 和 [攻城钻机](/upgrade/0246-Battle-Drill) 能免疫飓风陷阱的转圈效果。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/03/24">
        <TimelineRow>2 ~ 3 级飓风陷阱的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>2 ~ 3 级飓风陷阱的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/12/09">
        <TimelineRow>1 级飓风陷阱的建造费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/04/02">
        <TimelineRow>玩家上线后，所有的陷阱将自动被重新布置，重新布置不再需要花费金币。然而，如果玩家不上线，陷阱就不会被重新布置，所以你仍然可以攻击到陷阱失效的村庄。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
