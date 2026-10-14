---
title: "部落冲突 coc 法术塔升级数据"
navTitle: "法术塔"
shownTitle: "法术塔"
module: upgrade-home
imgFolder: home_buildings/0311
wiki: https://clashofclans.fandom.com/wiki/Spell_Tower
canonical: /upgrade/0311-Spell-Tower
dataSyncedOn: 2026-10-13
description: "多年来，法师在战场上只有火球这一种魔法，一次还只能扔一颗。现在，他们发明了一种全自动的魔法利器，可以使用不同魔法扰乱敌人的进攻！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0311-Spell-Tower.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2026-02-23'">

<template #introduction>

<SwitchTabs contentClass="cp-unit-items" :stickyTabs="true" :pageTabs="true">
    <SwitchTab tabId="cp-unit-item-0" :activeTab="true">狂暴法术塔</SwitchTab>
    <SwitchTab tabId="cp-unit-item-1">毒药法术塔</SwitchTab>
    <SwitchTab tabId="cp-unit-item-2">隐形法术塔</SwitchTab>
    <SwitchTab tabId="cp-unit-item-3">地震法术塔</SwitchTab>
</SwitchTabs>

<SwitchTabGroup id="cp-unit-item-0" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Spell_Tower4_Rage.png" imgAlt="狂暴法术塔"
    :description="$frontmatter.description" :isSmallImg="true" />

<SmallTitle>重要说明</SmallTitle>

1. 法术塔的机制：法术塔升级后可以施放不同的法术，你可以在部署阵型时选择法术塔要释放的法术。
2. 法术塔被摧毁后会自动释放一次法术，也就是说法术塔至少会发挥一次作用。
3. 法术塔的触发机制见：揭秘——法术塔触发机制。

</SwitchTabGroup>

<SwitchTabGroup id="cp-unit-item-1" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Spell_Tower4_Poison.png" imgAlt="毒药法术塔"
    :description="$frontmatter.description" :isSmallImg="true" />

\* 毒药法术塔的毒药效果对英雄只有 20% 伤害，但减速效果是全额的。
</SwitchTabGroup>

<SwitchTabGroup id="cp-unit-item-2" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Spell_Tower4_Invisibility.png" imgAlt="隐形法术塔"
    :description="$frontmatter.description" :isSmallImg="true" />

\* 法术塔释放的隐形法术和普通的 [隐形法术](/upgrade/0106-Invisibility-Spell) 一样不分敌我，也就是说这个隐形法术会把进攻方和防守方都隐形掉。
</SwitchTabGroup>

<SwitchTabGroup id="cp-unit-item-3" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Spell_Tower4_Earthquake.png" imgAlt="地震法术塔"
    :description="$frontmatter.description" :isSmallImg="true" />

</SwitchTabGroup>

注：法术塔释放的法术与 [法术工厂](/upgrade/0484-Spell-Factory) / [暗黑法术工厂](/upgrade/0485-Dark-Spell-Factory) 中释放的法术并不完全相同，上述链接只是方便对照，切勿生搬硬套。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2026/02/23">
        <TimelineRow>在 17 本添加了 4 级法术塔。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/10/06">
        <TimelineRow>3 级法术塔的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>1 ~ 3 级法术塔的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>1 ~ 3 级法术塔的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/18">
        <TimelineRow>1 ~ 3 级法术塔的升级时间减少。</TimelineRow>
        <TimelineRow>2 ~ 3 级法术塔的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>狂暴法术塔的法术范围从 6 格减少至 5 格。</TimelineRow>
        <TimelineRow>狂暴法术塔的提高伤害从 +90% 减少至 +60%.</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>狂暴法术塔的重新填充时间增加 20 秒。</TimelineRow>
        <TimelineRow>毒药法术塔和隐形法术塔的重新填充时间增加 10 秒。</TimelineRow>
        <TimelineRow>狂暴法术塔的狂暴效果由 +100% 调整为 +90%.</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/12/12">
        <TimelineRow>毒药法术塔 “降低攻击速度” 的效果由 -35% 调整为 -25%.</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>15 本推出，并在 15 本新增建筑：法术塔。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
