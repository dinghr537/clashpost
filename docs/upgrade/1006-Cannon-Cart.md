---
title: "部落冲突 coc 夜世界加农炮战车升级数据"
navTitle: "加农炮战车"
shownTitle: "加农炮战车"
module: upgrade-bh
imgFolder: bh_tech/1006
wiki: https://clashofclans.fandom.com/wiki/Cannon_Cart
canonical: /upgrade/1006-Cannon-Cart
dataSyncedOn: 2026-10-13
description: "带轮子的加农炮？等等！它怎么又变成了迫击炮？敌军肯定想不到！它不仅威力巨大而且功能全面！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/1006-Cannon-Cart.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-05-15'">

<template #introduction>

- *如想查看都城的突袭炮车，请访问：[都城突袭炮车](/upgrade/2009-Raid-Cart)。*

<SwitchTabs contentClass="cp-unit-items" :stickyTabs="true" :pageTabs="true">
    <SwitchTab tabId="cp-unit-item-0" :activeTab="true">加农炮模式</SwitchTab>
    <SwitchTab tabId="cp-unit-item-1">迫击炮模式</SwitchTab>
</SwitchTabs>

<SwitchTabGroup id="cp-unit-item-0" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Cannon_Cart_info.png" imgAlt="加农炮战车（加农炮模式）" :description="$frontmatter.description" />

\* 加农炮战车可以在 2 种模式间快速切换，能移动的短程攻击模式（默认的加农炮模式）平均每秒伤害较高，不能移动的远程攻击模式（迫击炮模式）平均每秒伤害较低。

</SwitchTabGroup>

<SwitchTabGroup id="cp-unit-item-1" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Mortar_Cart_info.png" imgAlt="加农炮战车（迫击炮模式）" :description="$frontmatter.description" />

\* 加农炮战车可以在 2 种模式间快速切换，能移动的短程攻击模式（默认的加农炮模式）平均每秒伤害较高，不能移动的远程攻击模式（迫击炮模式）平均每秒伤害较低。

</SwitchTabGroup>

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/05/15">
        <TimelineRow>新增 19 - 20 级加农炮战车。</TimelineRow>
        <TimelineRow>由于夜世界重做，部队的伤害、生命值等数据都有变化。</TimelineRow>
        <TimelineRow>废除以前的“奋战到底”技能，改为两种模式切换的技能。</TimelineRow>
        <TimelineRow>加农炮战车的移动速度由 16（2 格/秒）提升至 19.2（2.4 格/秒）。</TimelineRow>
        <TimelineRow>加农炮战车的兵种重量从 8 提升至 16。</TimelineRow>
        <TimelineRow>现在加农炮战车一解锁就是 7 级，你不需要从 1 级开始升了。如果更新前部队高于 7 级，更新后等级不会重置。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/06/22">
        <TimelineRow>加农炮战车的兵种重量从 5 提升至 8。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/06/18">
        <TimelineRow>夜世界 9 本开放，所有兵种可升至 18 级。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
