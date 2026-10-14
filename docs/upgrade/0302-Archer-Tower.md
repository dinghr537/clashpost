---
title: "部落冲突 coc 箭塔升级数据"
navTitle: "箭塔"
shownTitle: "箭塔"
module: upgrade-home
imgFolder: home_buildings/0302
wiki: https://clashofclans.fandom.com/wiki/Archer_Tower
canonical: /upgrade/0302-Archer-Tower
dataSyncedOn: 2026-10-13
description: "箭塔范围比加农炮远，而且还可以攻击空中目标。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0302-Archer-Tower.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-10-06'">

<template #introduction>

- *如想查看由两个箭塔合成的多人箭塔，请访问 [多人箭塔](/upgrade/0314-Multi-Archer-Tower)。*
- *如想查看由一个加农炮和一个箭塔合成的建筑，请访问：[复合机械塔]( /upgrade/0317-Multi-Gear-Tower)。*
- *如想查看夜世界的箭塔，请访问：[夜世界箭塔](/upgrade/1102-Archer-Tower)。*

<SwitchTabs contentClass="cp-unit-items" :stickyTabs="true" :pageTabs="true">
    <SwitchTab tabId="cp-unit-item-0" :activeTab="true">标准模式</SwitchTab>
    <SwitchTab tabId="cp-unit-item-1">快速模式</SwitchTab>
</SwitchTabs>

<SwitchTabGroup id="cp-unit-item-0" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Archer_Tower21.png" imgAlt="箭塔（标准模式）"
    :description="$frontmatter.description" :isSmallImg="true" />

在 16 级大本营，游戏引入合并建筑功能，这里的建筑数量指的是将所有可合并的建筑都合并后的数量。

</SwitchTabGroup>

<SwitchTabGroup id="cp-unit-item-1" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Archer_Tower21B.png" imgAlt="箭塔（快速模式）"
    :description="$frontmatter.description" :isSmallImg="true" />

在 16 级大本营，游戏引入合并建筑功能，这里的建筑数量指的是将所有可合并的建筑都合并后的数量。

</SwitchTabGroup>

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/10/06">
        <TimelineRow>16 ~ 21 级箭塔的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>1 ~ 5、7 ~ 9、11 ~ 12、14、16、18、20 ~ 21 级箭塔的升级时间减少。</TimelineRow>
        <TimelineRow>5 ~ 21 级箭塔的升级费用降低。</TimelineRow>
        <TimelineRow>箭塔的改装费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/02/10">
        <TimelineRow>1、2、6、10、13、15、17、19 级箭塔的升级时间减少。</TimelineRow>
        <TimelineRow>13、15、17、19 级箭塔的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>17 本推出，其中 2 个箭塔可以被合并为 1 个多人箭塔。</TimelineRow>
        <TimelineRow>17 本新解锁一个箭塔。</TimelineRow>
        <TimelineRow>7 ~ 9、12、14、16、18、20 ~ 21 级箭塔的升级时间减少。</TimelineRow>
        <TimelineRow>16 ~ 21 级箭塔的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/18">
        <TimelineRow>14 ~ 21 级箭塔的升级时间减少。</TimelineRow>
        <TimelineRow>16 ~ 18、20 ~ 21 级箭塔的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/03">
        <TimelineRow>12 ~ 20 级箭塔的每秒伤害降低。</TimelineRow>
        <TimelineRow>自本次更新后，快速模式秒伤 = 2 倍标准模式秒伤，标准模式次伤 = 快速模式次伤这两个规律不再成立。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/04/09">
        <TimelineRow>16 ~ 17 级箭塔的生命值减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>16 本推出，其中 4 个箭塔可以被合并为 2 个多人箭塔。</TimelineRow>
        <TimelineRow>5 ~ 21 级箭塔的升级时间减少。</TimelineRow>
        <TimelineRow>6 ~ 12、14 ~ 15、20 ~ 21 级箭塔的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>16 ~ 19 级箭塔的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>15 本推出，并在 15 本新增 21 级箭塔。</TimelineRow>
        <TimelineRow>12 ~ 20 级箭塔的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/06/27">
        <TimelineRow>16 ~ 17 级箭塔的伤害降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/12/09">
        <TimelineRow>8 ~ 19 级箭塔的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/06/15">
        <TimelineRow>14 本新增 20 级箭塔。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>8 ~ 13 级箭塔的升级费用降低。</TimelineRow>
        <TimelineRow>2、5、7、9 ~ 16 级箭塔的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/01/20">
        <TimelineRow>修复了改装后的箭塔首发箭矢射出位置不合理的问题。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/10/12">
        <TimelineRow>13 本新增 19 级箭塔。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/03/30">
        <TimelineRow>13 本新增 18 级箭塔。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/04/02">
        <TimelineRow>10 ~ 16 级箭塔的升级费用降低。</TimelineRow>
        <TimelineRow>6 ~ 13、16 级箭塔的升级时间减少。</TimelineRow>
        <TimelineRow>12 级大本营新增 17 级箭塔。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/02/22">
        <TimelineRow>10 ~ 16 级箭塔的伤害降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
