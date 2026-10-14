---
title: "部落冲突 coc 灵蛇手镯装备升级数据"
navTitle: "灵蛇手镯"
shownTitle: "灵蛇手镯"
module: upgrade-home
imgFolder: home_heroes/0706
wiki: https://clashofclans.fandom.com/wiki/Snake_Bracelet
canonical: /upgrade/0706-Snake-Bracelet
dataSyncedOn: 2026-10-13
description: "灵蛇手镯是野蛮人之王的第三件史诗装备，它在 2025 年 2 月的灵蛇庆典活动中首次开放购买。当蛮王带上灵蛇手镯装备后，蛮王每受到 300 点伤害就会召唤蛇，蛇的等级和最大召唤数量与装备等级有关。此外，灵蛇手镯装备还可以提高蛮王的每秒伤害、生命值和攻击速度。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0706-Snake-Bracelet.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-02-07'">

<template #introduction>

- *如想查看由临时兵种灵蛇飞桶召唤的灵蛇，请移步：[灵蛇飞桶](/upgrade/0e15-Snake-Barrel)。*

<SwitchTabs contentClass="cp-unit-items" :stickyTabs="true" :pageTabs="true">
    <SwitchTab tabId="cp-unit-item-0" :activeTab="true">灵蛇手镯</SwitchTab>
    <SwitchTab tabId="cp-unit-item-1">灵蛇</SwitchTab>
</SwitchTabs>

<SwitchTabGroup id="cp-unit-item-0" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Snake_Bracelet_info.png" imgAlt="灵蛇手镯" description="受到伤害时，召唤灵蛇与您并肩作战。" />

<SmallTitle>说明</SmallTitle>

1. 灵蛇手镯是 [野蛮人之王](/upgrade/0200-Barbarian-King) 的第三件史诗装备，它在 2025 年 2 月的灵蛇庆典活动中首次开放购买。
2. 当蛮王带上灵蛇手镯装备后，蛮王每受到 300 点伤害就会召唤蛇，蛇的等级和最大召唤数量与装备等级有关。
3. 此外，灵蛇手镯装备还可以提高蛮王的每秒伤害、生命值和攻击速度。

注：如果升级费用中有多种资源，则同时需要多种资源才能升级。

</SwitchTabGroup>

<SwitchTabGroup id="cp-unit-item-1" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Snake_info.png" imgAlt="灵蛇手镯召唤的灵蛇"
    description="这些饥饿的大蛇被一只神秘的古老手镯召唤出来，它们只有一个目的——咬碎一切！" />

</SwitchTabGroup>

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/02/07">
        <TimelineRow>新装备：灵蛇手镯。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
