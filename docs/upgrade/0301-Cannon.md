---
title: "部落冲突 coc 加农炮升级数据"
navTitle: "加农炮"
shownTitle: "加农炮"
module: upgrade-home
imgFolder: home_buildings/0301
wiki: https://clashofclans.fandom.com/wiki/Cannon
canonical: /upgrade/0301-Cannon
dataSyncedOn: 2026-10-13
description: "加农炮很适合防御单个目标。升级加农炮可以增强火力。注意！防御建筑在升级时不能开火！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0301-Cannon.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-10-06'">

<template #introduction>

- *如想查看由两个加农炮合成的跳弹加农炮，请访问：[跳弹加农炮](/upgrade/0313-Ricochet-Cannon)。*
- *如想查看由一个加农炮和一个箭塔合成的建筑，请访问：[复合机械塔](/upgrade/0317-Multi-Gear-Tower)。*
- *如想查看夜世界的加农炮和双管加农炮，请访问：[夜世界加农炮](/upgrade/1100-Cannon)、[夜世界双管加农炮](/upgrade/1101-Double-Cannon)。*
- *如想查看都城的加农炮，请访问：[都城加农炮](/upgrade/2201-Cannon)。*

<SwitchTabs contentClass="cp-unit-items" :stickyTabs="true" :pageTabs="true">
    <SwitchTab tabId="cp-unit-item-0" :activeTab="true">标准模式</SwitchTab>
    <SwitchTab tabId="cp-unit-item-1">连发模式</SwitchTab>
</SwitchTabs>

<SwitchTabGroup id="cp-unit-item-0" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Cannon21.png" imgAlt="加农炮（标准模式）"
    :description="$frontmatter.description" :isSmallImg="true" />

在 16 级大本营，游戏引入合并建筑功能，这里的建筑数量指的是将所有可合并的建筑都合并后的数量。

\* 加农炮改装前（标准模式）每 0.8 秒攻击一次。改装后（连发模式）每轮发射 4 发，轮内每发间隔 0.192 秒；本次来源列出的轮间间隔为 1.6 秒。

</SwitchTabGroup>

<SwitchTabGroup id="cp-unit-item-1" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Cannon21B.png" imgAlt="加农炮（连发模式）"
    :description="$frontmatter.description" :isSmallImg="true" />

在 16 级大本营，游戏引入合并建筑功能，这里的建筑数量指的是将所有可合并的建筑都合并后的数量。

\* 加农炮改装前（标准模式）每 0.8 秒攻击一次。改装后（连发模式）每轮发射 4 发，轮内每发间隔 0.192 秒；本次来源列出的轮间间隔为 1.6 秒。

</SwitchTabGroup>

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/10/06">
        <TimelineRow>18 ~ 21 级加农炮的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/06/16">
        <TimelineRow>1 ~ 6 级加农炮的生命值减少。</TimelineRow>
        <TimelineRow>1 ~ 6 级加农炮的每秒伤害降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>1 ~ 9、11 ~ 12、14 ~ 16、18、20 ~ 21 级加农炮的升级时间减少。</TimelineRow>
        <TimelineRow>6 ~ 16、18、20 ~ 21 级加农炮的升级费用降低。</TimelineRow>
        <TimelineRow>加农炮的改装费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/02/10">
        <TimelineRow>2、3、10、13、15、17、19 级加农炮的升级时间减少。</TimelineRow>
        <TimelineRow>13、15、17、19 级加农炮的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>17 本推出，其中 2 个加农炮可以被合并为 1 个跳弹加农炮。</TimelineRow>
        <TimelineRow>8 ~ 9、12 ~ 21 级加农炮的升级时间减少。</TimelineRow>
        <TimelineRow>15 ~ 21 级加农炮的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/18">
        <TimelineRow>14 ~ 21 级加农炮的升级时间减少。</TimelineRow>
        <TimelineRow>16 ~ 21 级加农炮的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/03">
        <TimelineRow>14 ~ 19 级加农炮的每秒伤害降低。</TimelineRow>
        <TimelineRow>自本次更新后，连发模式秒伤 = 1.35 倍快速模式秒伤，标准模式次伤 = 连发模式次伤这两个规律不再成立。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>16 本推出，其中 4 个加农炮可以被合并为 2 个跳弹加农炮。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/09/28">
        <TimelineRow>12 ~ 20 级加农炮的每秒伤害降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>16 ~ 19 级加农炮的升级时间减少。</TimelineRow>
        <TimelineRow>16 ~ 19 级加农炮的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>15 本推出，并在 15 本新增 21 级加农炮。</TimelineRow>
        <TimelineRow>12 ~ 20 级加农炮的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/12/09">
        <TimelineRow>8 ~ 19 级加农炮的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>14 本推出，并在 14 本新增 20 级加农炮。</TimelineRow>
        <TimelineRow>2 ~ 14 级加农炮的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/06/22">
        <TimelineRow>13 本新增 19 级加农炮。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/03/30">
        <TimelineRow>18 级加农炮的生命值由 1860 调整到 1870。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/12/09">
        <TimelineRow>13 本推出，并在 13 本新增 18 级加农炮。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/04/02">
        <TimelineRow>10 ~ 16 级加农炮的升级费用降低。</TimelineRow>
        <TimelineRow>7 ~ 13、16 级加农炮的升级时间减少。</TimelineRow>
        <TimelineRow>12 级大本营新增 17 级加农炮。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/02/22">
        <TimelineRow>10 ~ 16 级加农炮的伤害降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
