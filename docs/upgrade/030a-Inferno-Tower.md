---
title: "部落冲突 coc 地狱之塔升级数据"
navTitle: "地狱之塔"
shownTitle: "地狱之塔"
module: upgrade-home
imgFolder: home_buildings/030a
wiki: https://clashofclans.fandom.com/wiki/Inferno_Tower/Home_Village
canonical: /upgrade/030a-Inferno-Tower
dataSyncedOn: 2026-10-13
description: "建造有暗黑重油加持火焰的地狱之塔，可以对单一目标造成难以估算的伤害，或者一次对多重目标进行持续攻击。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/030a-Inferno-Tower.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2026-02-23'">

<template #introduction>

- *如想查看 13 本及以上的自带武器，请访问 [巨型地狱之塔](/upgrade/030d-Giga-Inferno)。*
- *如想查看都城的地狱之塔，请访问 [都城地狱之塔](/upgrade/220e-Inferno-Tower)。*

<SwitchTabs contentClass="cp-unit-items" :stickyTabs="true" :pageTabs="true">
    <SwitchTab tabId="cp-unit-item-0" :activeTab="true">单一目标模式</SwitchTab>
    <SwitchTab tabId="cp-unit-item-1">多重目标模式</SwitchTab>
</SwitchTabs>

<SwitchTabGroup id="cp-unit-item-0" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Inferno_Tower12.png" imgAlt="地狱之塔（单一目标模式）" :description="$frontmatter.description" :isSmallImg="true" />

<SmallTitle>重要说明</SmallTitle>

1. 单头地狱塔是三段伤害，初始伤害切二段需要 1.5 秒，二段切三段是 3.75 秒，因此单头塔锁定目标 1.5 + 3.75 = 5.25 秒后到达最高伤害。
2. 地狱之塔必须装弹才能工作，这个装弹操作会在玩家登录游戏时自动进行，但如果玩家长时间不登录，弹药就会用完，从而导致防御失效。
    - 地狱之塔有 1000 发弹药，每一发 0.128 秒，所以它的弹药在 2 分 08 秒内可以用完。
3. 冰牙和小冰怪的减速效果可以延后单一目标模式的 [地狱塔](/upgrade/030a-Inferno-Tower) 和 [地狱飞龙](/upgrade/0604-Inferno-Dragon) 达到最高伤害的时间。
4. [雷电法术](/upgrade/0100-Lightning-Spell) 的伤害、[灵狐](/upgrade/0288-Spirit-Fox)、[隐形药水瓶](/upgrade/0741-Invisibility-Vial) 和 [隐形法术](/upgrade/0106-Invisibility-Spell) 的隐形效果可以打断单头地狱之塔的攻击，使其伤害从头开始累积。

\*  地狱之塔有两种模式：单一目标模式（单头）和多重目标模式（多头），两种模式由玩家选择。单头塔只能攻击一个目标，其伤害会随着时间推移越来越高；多头塔可以同时攻击多个目标，其伤害不会随时间增加。

</SwitchTabGroup>

<SwitchTabGroup id="cp-unit-item-1" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Inferno_Tower12_Multi.png" imgAlt="地狱之塔（多重目标模式）" :description="$frontmatter.description" :isSmallImg="true" />

<SmallTitle>重要说明</SmallTitle>

1. 单头地狱塔是三段伤害，初始伤害切二段需要 1.5 秒，二段切三段是 3.75 秒，因此单头塔锁定目标 1.5 + 3.75 = 5.25 秒后到达最高伤害。
2. 地狱之塔必须装弹才能工作，这个装弹操作会在玩家登录游戏时自动进行，但如果玩家长时间不登录，弹药就会用完，从而导致防御失效。
    - 地狱之塔有 1000 发弹药，每一发 0.128 秒，所以它的弹药在 2 分 08 秒内可以用完。
3. 冰牙和小冰怪的减速效果可以延后单一目标模式的 [地狱塔](/upgrade/030a-Inferno-Tower) 和 [地狱飞龙](/upgrade/0604-Inferno-Dragon) 达到最高伤害的时间。
4. [雷电法术](/upgrade/0100-Lightning-Spell) 的伤害、[灵狐](/upgrade/0288-Spirit-Fox)、[隐形药水瓶](/upgrade/0741-Invisibility-Vial) 和 [隐形法术](/upgrade/0106-Invisibility-Spell) 的隐形效果可以打断单头地狱之塔的攻击，使其伤害从头开始累积。

\*  地狱之塔有两种模式：单一目标模式（单头）和多重目标模式（多头），两种模式由玩家选择。单头塔只能攻击一个目标，其伤害会随着时间推移越来越高；多头塔可以同时攻击多个目标，其伤害不会随时间增加。

</SwitchTabGroup>

</template>

<template #history>

<Timeline>
    <TimelineItem date="2026/02/23">
        <TimelineRow>在 18 本添加了 12 级地狱之塔。</TimelineRow>
        <TimelineRow>移除了地狱之塔的充能等级。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/11/17">
        <TimelineRow>11 级及两个充能等级的地狱之塔的升级时间和升级费用减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/10/06">
        <TimelineRow>6 ~ 10 级地狱之塔的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>17 本新增 11 级地狱之塔。</TimelineRow>
        <TimelineRow>1 ~ 4、6、8 ~ 10 级地狱之塔的升级时间减少。</TimelineRow>
        <TimelineRow>1 ~ 3、6、8 ~ 10 级地狱之塔的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/02/10">
        <TimelineRow>5 级地狱之塔的升级时间减少。</TimelineRow>
        <TimelineRow>5 级地狱之塔的升级费用降低。</TimelineRow>
        <TimelineRow>地狱之塔的充能时间和充能费用减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>4、6 ~ 10 级地狱之塔的升级时间减少。</TimelineRow>
        <TimelineRow>7 ~ 10 级地狱之塔的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/09/09">
        <TimelineRow>超级充能推出，地狱之塔是第一批可以充能的建筑之一。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/18">
        <TimelineRow>6 ~ 9 级地狱之塔的升级时间减少。</TimelineRow>
        <TimelineRow>8 ~ 9 级地狱之塔的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/03">
        <TimelineRow>4 ~ 9 级多头塔地狱塔的每秒伤害降低。</TimelineRow>
        <TimelineRow>4 级单头塔的初始伤害降低，5 ~ 9 级单头塔的三段伤害都有降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/02/27">
        <TimelineRow>16 本新增 10 级地狱之塔。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>所有等级地狱之塔的升级时间减少。</TimelineRow>
        <TimelineRow>1 ~ 6、8 级地狱之塔的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/09/28">
        <TimelineRow>所有等级地狱之塔的每秒伤害降低（含单头和多头模式）。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>6 ~ 7 级地狱之塔的升级时间减少。</TimelineRow>
        <TimelineRow>6 ~ 7 级地狱之塔的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>15 本推出，并在 15 本新增 9 级地狱之塔。</TimelineRow>
        <TimelineRow>1 ~ 8 级地狱之塔的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/06/27">
        <TimelineRow>6 级地狱之塔的伤害降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/12/09">
        <TimelineRow>1 ~ 7 级 地狱之塔的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>14 本推出，并在 14 本新增 8 级地狱之塔。</TimelineRow>
        <TimelineRow>地狱塔在多目标模式下不再固定为 5 个目标了，8 级地狱塔最多可以攻击 6 个目标。</TimelineRow>
        <TimelineRow>1 ~ 5 级地狱塔的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/05/20">
        <TimelineRow>7 级地狱之塔处于单一目标模式时的每秒伤害（第三段伤害）降低 100。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/12/09">
        <TimelineRow>13 本推出，并在 13 本新增 7 级地狱之塔。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/09/11">
        <TimelineRow>2 ~ 3 级地狱塔的伤害降低。</TimelineRow>
    </TimelineItem>
        <TimelineItem date="2019/04/02">
        <TimelineRow>4 级地狱之塔的升级费用降低。</TimelineRow>
        <TimelineRow>玩家上线后，地狱之塔的弹药将自动被填充，填充不再需要花费暗黑重油。然而，如果玩家不上线， 地狱之塔的弹药就不会被填充，所以你仍然可以攻击到地狱之塔的弹药用完的村庄。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
