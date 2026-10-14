---
title: "部落冲突 coc 迫击炮升级数据"
navTitle: "迫击炮"
shownTitle: "迫击炮"
module: upgrade-home
imgFolder: home_buildings/0303
wiki: https://clashofclans.fandom.com/wiki/Mortar
canonical: /upgrade/0303-Mortar
dataSyncedOn: 2026-10-13
description: "迫击炮可以发出威力无比的炮弹，其造成的溅射伤害可以击败大群敌军。注意，要防止敌军过于接近迫击炮！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0303-Mortar.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2026-02-23'">

<template #introduction>

- *如想查看夜世界的多管迫击炮，请访问 [夜世界多管迫击炮](/upgrade/1108-Multi-Mortar)。*
- *如想查看都城的多管迫击炮，请访问：[都城多管迫击炮](/upgrade/2206-Multi-Mortar)。*

<SwitchTabs contentClass="cp-unit-items" :stickyTabs="true" :pageTabs="true">
    <SwitchTab tabId="cp-unit-item-0" :activeTab="true">标准模式</SwitchTab>
    <SwitchTab tabId="cp-unit-item-1">快速模式</SwitchTab>
</SwitchTabs>

<SwitchTabGroup id="cp-unit-item-0" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Mortar18.png" imgAlt="迫击炮（标准模式）"
    :description="$frontmatter.description" :isSmallImg="true" />

</SwitchTabGroup>

<SwitchTabGroup id="cp-unit-item-1" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Mortar18B.png" imgAlt="迫击炮（快速模式）"
    :description="$frontmatter.description" :isSmallImg="true" />

\* 多管迫击炮的攻击间隔是：3 连发期间每发 0.5 秒，之后停顿 4 秒。如果目标在多管还没打完 3 连发之前死亡，导致多管没有发射全部3发炮弹时，每发没有射出去的炮弹会减少 0.5 秒攻击间隔。上述的 5 秒指的是一整个周期的时间，0.5 * (3 - 1) + 4 = 5 (秒)

</SwitchTabGroup>

注：迫击炮改装后每秒伤害会略微提高。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2026/02/23">
        <TimelineRow>添加了 18 级迫击炮。</TimelineRow>
        <TimelineRow>移除了 17 级迫击炮的超级充能。</TimelineRow>
        <TimelineRow>更改了多管迫击炮在游戏面板中显示的伤害值（实际伤害没变，只是更改了显示算法）。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/11/17">
        <TimelineRow>17 级及两个充能等级的迫击炮的升级时间和升级费用减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/10/06">
        <TimelineRow>15 ~ 16 级迫击炮的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>1 ~ 9、11、13 ~ 16 级迫击炮的升级时间减少。</TimelineRow>
        <TimelineRow>3 ~ 4、6 ~ 16 级迫击炮的升级费用降低。</TimelineRow>
        <TimelineRow>迫击炮的改装费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/02/10">
        <TimelineRow>在 17 本新增 17 级迫击炮。</TimelineRow>
        <TimelineRow>10、12 级迫击炮的升级时间减少。</TimelineRow>
        <TimelineRow>10、12 级迫击炮的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>9 ~ 16 级迫击炮的升级时间减少。</TimelineRow>
        <TimelineRow>11 ~ 16 级迫击炮的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/09/09">
        <TimelineRow>超级充能推出，迫击炮是第一批可以充能的建筑之一。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/18">
        <TimelineRow>1 ~ 15 级迫击炮的升级时间减少。</TimelineRow>
        <TimelineRow>14 ~ 15 级迫击炮的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>4 ~ 15 级迫击炮的升级时间减少。</TimelineRow>
        <TimelineRow>5 ~ 6、8 ~ 14 级迫击炮的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>11 ~ 13 级迫击炮的升级时间减少。</TimelineRow>
        <TimelineRow>11 ~ 13 级迫击炮的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>15 本推出，并在 15 本新增 15 级迫击炮。</TimelineRow>
        <TimelineRow>8 ~ 14 级迫击炮的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/06/27">
        <TimelineRow>9 ~ 14 级迫击炮的生命值增加。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/01/20">
        <TimelineRow>修复了改装后的迫击炮首发箭矢射出位置不合理的问题。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/12/09">
        <TimelineRow>4 ~ 13 级迫击炮的升级费用降低。</TimelineRow>
    </TimelineItem>
        <TimelineItem date="2021/09/27">
        <TimelineRow>14 本新增 14 级迫击炮。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>1 ~ 11 级迫击炮的升级费用降低。</TimelineRow>
        <TimelineRow>2 ~ 10 级迫击炮的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/03/30">
        <TimelineRow>13 本新增 13 级迫击炮。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/12/09">
        <TimelineRow>所有等级多管迫击炮的伤害提高 10%.</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/09/11">
        <TimelineRow>12 级迫击炮的生命值由 950 提升至 980。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/06/18">
        <TimelineRow>12 本新增 12 级迫击炮。</TimelineRow>
    </TimelineItem>
        <TimelineItem date="2019/04/02">
        <TimelineRow>1 级迫击炮的新建时间减少。</TimelineRow>
    </TimelineItem>
        <TimelineItem date="2019/02/22">
        <TimelineRow>5 ~ 12 级迫击炮的伤害提高。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
