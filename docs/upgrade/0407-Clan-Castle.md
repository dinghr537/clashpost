---
title: "部落冲突 coc 部落城堡升级数据"
navTitle: "部落城堡"
shownTitle: "部落城堡"
module: upgrade-home
imgFolder: home_buildings/0407
wiki: https://clashofclans.fandom.com/wiki/Clan_Castle
canonical: /upgrade/0407-Clan-Castle
dataSyncedOn: 2026-10-13
description: "宝库以及部落成员增援的部队和法术都会存放在您的部落城堡中。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0407-Clan-Castle.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-11-17'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Clan_Castle14_hd.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

1. 部落城堡内可存储的资源数量只与玩家的大本营等级和部落等级有关，而与部落城堡等级无关，详见页面下方的表格。
2. 部落城堡升级时仍然可以请求援兵。
3. [雷电法术](/upgrade/0100-Lightning-Spell) 不能对部落城堡造成伤害，[地震法术](/upgrade/0181-Earthquake-Spell) 可以。
4. 自 2021 年 4 月更新起，部落城堡可收到的兵种等级有限制。

2：理论上来说，玩家只有升级到 3 级大本营才能达到 10 000 的资源储量用来修复城堡，但是如果玩家在 2 级大本营时遇到夯木节（升级建筑的费用减半）活动，或者购买资源礼包，那么就可以提前解锁城堡。
2：将部落城堡升到 12 级并不意味着你能在战斗中同时使用两种攻城机器，只是可以装两种不同的攻城机器，供你在战斗时切换。

<SwitchTabs contentClass="cp-upgrade-clan-level">
    <SwitchTab tabId="cp-upgrade-clan-0" :activeTab="true">无部落或 1 级部落</SwitchTab>
    <SwitchTab tabId="cp-upgrade-clan-2">2 ~ 3 级部落</SwitchTab>
    <SwitchTab tabId="cp-upgrade-clan-4">4 ~ 5 级部落</SwitchTab>
    <SwitchTab tabId="cp-upgrade-clan-6">6 ~ 7 级部落</SwitchTab>
    <SwitchTab tabId="cp-upgrade-clan-8">8 ~ 9 级部落</SwitchTab>
    <SwitchTab tabId="cp-upgrade-clan-10">10 级及以上部落</SwitchTab>
</SwitchTabs>

<SwitchTabGroup id="cp-upgrade-clan-0" class="cp-upgrade-clan-level">

</SwitchTabGroup>

<SwitchTabGroup id="cp-upgrade-clan-2" class="cp-upgrade-clan-level">

</SwitchTabGroup>

<SwitchTabGroup id="cp-upgrade-clan-4" class="cp-upgrade-clan-level">

</SwitchTabGroup>

<SwitchTabGroup id="cp-upgrade-clan-6" class="cp-upgrade-clan-level">

</SwitchTabGroup>

<SwitchTabGroup id="cp-upgrade-clan-8" class="cp-upgrade-clan-level">

</SwitchTabGroup>

<SwitchTabGroup id="cp-upgrade-clan-10" class="cp-upgrade-clan-level">

</SwitchTabGroup>

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/11/17">
        <TimelineRow>18 本推出，并在 18 本新增 14 级部落城堡。</TimelineRow>
        <TimelineRow>13 级部落城堡的升级时间和升级费用减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/06/16">
        <TimelineRow>1 ~ 3 级部落城堡的生命值减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>2、5 ~ 8、11 ~ 12 级部落城堡的升级时间减少。</TimelineRow>
        <TimelineRow>2 ~ 3、5 ~ 12 级部落城堡的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>17 本推出，并在 17 本新增 13 级部落城堡。</TimelineRow>
        <TimelineRow>6 ~ 12 级部落城堡的升级时间减少。</TimelineRow>
        <TimelineRow>8、11 ~ 12 级部落城堡的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/18">
        <TimelineRow>8 ~ 11 级部落城堡的升级时间减少。</TimelineRow>
        <TimelineRow>11 级部落城堡的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/04/17">
        <TimelineRow>在 16 本新增 12 级部落城堡。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>10 ~ 11 级部落城堡的升级时间减少。</TimelineRow>
        <TimelineRow>10 级部落城堡的升级费用 1800 万减少至 1260 万。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>8 ~ 9 级部落城堡的升级时间减少。</TimelineRow>
        <TimelineRow>8 ~ 9 级部落城堡的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>15 本推出，并在 15 本新增 11 级部落城堡。</TimelineRow>
        <TimelineRow>6 ~ 10 级部落城堡的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/06/27">
        <TimelineRow>现在所有等级的部落城堡均需使用圣水升级，所需圣水的数量与之前所需的金币数相同。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>14 本推出，并在 14 本新增 10 级部落城堡。</TimelineRow>
        <TimelineRow>现在部落城堡可收到的兵种等级有限制，援兵无法再碾压低本了。</TimelineRow>
        <TimelineRow>4 ~ 7 级部落城堡的升级费用降低。</TimelineRow>
        <TimelineRow>7 级部落城堡的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/12/07">
        <TimelineRow>雷电法术不再对部落城堡造成伤害。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/12/09">
        <TimelineRow>13 本推出，并在 13 本新增 9 级部落城堡。</TimelineRow>
        <TimelineRow>12 级大本营的城堡可存储的资源量增加。</TimelineRow>
    </TimelineItem>
        <TimelineItem date="2019/04/02">
        <TimelineRow>6 ~ 7 级部落城堡的升级费用降低。</TimelineRow>
        <TimelineRow>2 级部落城堡的升级时间增加，4 ~ 6 级部落城堡的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
