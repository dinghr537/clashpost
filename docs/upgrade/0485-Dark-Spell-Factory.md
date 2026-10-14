---
title: "部落冲突 coc 暗黑法术工厂升级数据"
navTitle: "暗黑法术工厂"
shownTitle: "暗黑法术工厂"
module: upgrade-home
imgFolder: home_buildings/0485
wiki: https://clashofclans.fandom.com/wiki/Dark_Spell_Factory
canonical: /upgrade/0485-Dark-Spell-Factory
dataSyncedOn: 2026-10-13
description: "只有那些最聪明，或者最鲁莽的法术大师才敢使用暗黑重油来配制法术。要精通这些空间较小的暗黑法术需要敏锐的洞察力，不过这也能带来独一无二的战术优势。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0485-Dark-Spell-Factory.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-10-06'">

<template #introduction>

- *如想查看配置圣水法术的法术工厂，请访问：[法术工厂](/upgrade/0484-Spell-Factory)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Dark_Spell_Factory7_hd.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/10/06">
        <TimelineRow>7 级暗黑法术工厂的升级时间减少。</TimelineRow>
        <TimelineRow>7 级暗黑法术工厂的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/06/19">
        <TimelineRow>新增 7 级暗黑法术工厂，14 本可解锁。新法术：冰障法术。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>2 级暗黑法术工厂的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>5 ~ 6 级暗黑法术工厂的升级时间减少。</TimelineRow>
        <TimelineRow>6 级暗黑法术工厂的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/02/27">
        <TimelineRow>新增 6 级暗黑法术工厂，12 本可解锁。新法术：蔓生法术。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>1 ~ 2 级暗黑法术工厂的升级费用 150k/300k 减少至 130k/260k。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>法术工厂升级时兵种可继续配置法术，但配置速度减半（配置时间翻倍）。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/12/09">
        <TimelineRow>所有等级暗黑法术工厂的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>所有等级暗黑法术工厂的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
        <TimelineItem date="2019/04/02">
        <TimelineRow>1 ~ 4 级暗黑法术工厂的升级时间减少。</TimelineRow>
        <TimelineRow>所有等级暗黑法术工厂的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
