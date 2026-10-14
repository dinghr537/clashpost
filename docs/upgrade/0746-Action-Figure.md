---
title: "部落冲突 coc 动作人偶装备升级数据"
navTitle: "动作人偶"
shownTitle: "动作人偶"
module: upgrade-home
imgFolder: home_heroes/0746
wiki: https://clashofclans.fandom.com/wiki/Action_Figure
canonical: /upgrade/0746-Action-Figure
dataSyncedOn: 2026-10-13
description: "动作人偶是弓箭女皇的第三件史诗装备，它在 2025 年 4 月的是敌是友活动中首次开放购买。动作人偶装备可以在使用技能时召唤一个霸天巨人，其各项数据与同名临时兵种相同。霸天巨人的等级取决于装备等级。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0746-Action-Figure.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-04-08'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Action_Figure_info.png" :imgAlt="$frontmatter.navTitle" description="召唤霸天巨人与弓箭女皇并肩作战。" />

<SmallTitle>说明</SmallTitle>

1. 动作人偶是 [弓箭女皇](/upgrade/0201-Archer-Queen) 的第三件史诗装备，它在 2025 年 4 月的是敌是友活动中首次开放购买。
2. 动作人偶装备可以在使用技能时召唤一个 [霸天巨人](/upgrade/0e17-Giant-Giant)，其各项数据与同名临时兵种相同。霸天巨人的等级取决于装备等级。
3. 带上动作人偶装备后，弓箭女皇使用技能时可以隐形一秒，因此可以重置防御建筑的攻击。
4. 除了以上能力，动作人偶装备还可以让弓箭女皇拥有更高的每秒伤害和生命值，还可以让弓箭女皇拥有自我疗愈能力。

注：如果升级费用中有多种资源，则同时需要多种资源才能升级。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/04/08">
        <TimelineRow>新装备：动作人偶。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
