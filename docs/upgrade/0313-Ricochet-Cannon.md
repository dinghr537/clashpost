---
title: "部落冲突 coc 跳弹加农炮（弹跳加农炮）升级数据"
navTitle: "跳弹加农炮"
shownTitle: "跳弹加农炮（弹跳加农炮）"
module: upgrade-home
imgFolder: home_buildings/0313
wiki: https://clashofclans.fandom.com/wiki/Ricochet_Cannon
canonical: /upgrade/0313-Ricochet-Cannon
dataSyncedOn: 2026-10-13
description: "建筑工人凭借他的奇妙想法发明了一种威力巨大的炮弹，这种炮弹会弹射击中第二个目标。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0313-Ricochet-Cannon.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2026-01-28'">

<template #introduction>

- *如想查看合并前的建筑，请访问 [加农炮](/upgrade/0301-Cannon)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Ricochet_Cannon4.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

<SmallTitle>重要说明</SmallTitle>

1. 跳弹加农炮不能直接建造，必须由两个 [加农炮](/upgrade/0301-Cannon) 合并而成，两座用来合并的建筑必须已达到最高等级。
    - 合并一旦开始就无法取消。
    - 合并建筑的操作是永久性的，一旦合并就无法拆开。
    - 升本前必须合并完所有可以合并的建筑。
2. 如果在距离第一个目标 3.5 格范围内存在其他敌方单位，则炮弹将会弹射到第二个目标并造成伤害。
3. 第二个目标受到的伤害是第一个目标的 70%.

</template>

<template #history>

<Timeline>
    <TimelineItem date="2026/01/28">
        <TimelineRow>跳弹加农炮第二个目标受到的伤害由 100% 降低到 70%.</TimelineRow>
        <TimelineRow>跳弹加农炮的最远弹射距离由 4.5 格减少到 3.5 格。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/11/17">
        <TimelineRow>18 本推出，并在 18 本新增 4 级跳弹加农炮。</TimelineRow>
        <TimelineRow>3 级跳弹加农炮的升级时间和升级费用减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/10/06">
        <TimelineRow>1 ~ 2 级跳弹加农炮的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>1 ~ 2 级跳弹加农炮的升级费用和时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>17 本推出，并在 17 本新增 3 级跳弹加农炮。</TimelineRow>
        <TimelineRow>17 本新解锁一个跳弹加农炮。</TimelineRow>
        <TimelineRow>1 ~ 2 级跳弹加农炮的升级费用和时间减少。</TimelineRow>
        <TimelineRow>跳弹加农炮成为第二批可以充能的建筑。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>16 本推出，并在 16 本新增建筑：跳弹加农炮，共设两个等级。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
