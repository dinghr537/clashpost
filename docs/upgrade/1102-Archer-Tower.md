---
title: "部落冲突 coc 夜世界箭塔升级数据"
navTitle: "箭塔"
shownTitle: "箭塔"
module: upgrade-bh
imgFolder: bh_buildings/1102
wiki: https://clashofclans.fandom.com/wiki/Archer_Tower/Builder_Base
canonical: /upgrade/1102-Archer-Tower
dataSyncedOn: 2026-10-13
description: "没人能逃过弓箭手的箭。这种箭塔有一个特殊开关，可在远程攻击和快速攻击两种模式间切换！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/1102-Archer-Tower.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-05-15'">

<template #introduction>

- *如想查看家乡的箭塔，请访问：[箭塔](/upgrade/0302-Archer-Tower)。*

<SwitchTabs contentClass="cp-unit-items" :stickyTabs="true" :pageTabs="true">
    <SwitchTab tabId="cp-unit-item-0" :activeTab="true">标准模式</SwitchTab>
    <SwitchTab tabId="cp-unit-item-1">快速模式</SwitchTab>
</SwitchTabs>

<SwitchTabGroup id="cp-unit-item-0" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Archer_Tower10.png" imgAlt="箭塔（标准模式）"
    :description="$frontmatter.description" :isSmallImg="true" />

</SwitchTabGroup>

<SwitchTabGroup id="cp-unit-item-1" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Archer_Tower10B.png" imgAlt="箭塔（快速模式）"
    :description="$frontmatter.description" :isSmallImg="true" />

</SwitchTabGroup>

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/05/15">
        <TimelineRow>夜世界重做，建筑的数值重新平衡，伤害、生命值等数据有变化。</TimelineRow>
        <TimelineRow>6 ~ 9 级箭塔的升级时间增加。</TimelineRow>
        <TimelineRow>夜世界 10 本推出，箭塔可升至 10 级。</TimelineRow>
        <TimelineRow>为配合更小的地图，箭塔在标准模式下的射程由 11 格降低到 10 格。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/06/18">
        <TimelineRow>夜世界 9 本推出，箭塔可升至 9 级。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
