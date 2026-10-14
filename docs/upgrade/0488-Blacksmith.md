---
title: "部落冲突 coc 铁匠铺升级数据"
navTitle: "铁匠铺"
shownTitle: "铁匠铺"
module: upgrade-home
imgFolder: home_buildings/0488
wiki: https://clashofclans.fandom.com/wiki/Blacksmith
canonical: /upgrade/0488-Blacksmith
dataSyncedOn: 2026-10-13
description: "把合适的魔法矿石带到这来，升级英雄的装备，让他们变得更加强大！熔炉冒出的烟可用于熏制美味的牛腩，虽然这并不健康。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0488-Blacksmith.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-10-06'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Blacksmith9.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

<SmallTitle>重要说明</SmallTitle>

1. 升级铁匠铺可以使英雄装备升级到更高的等级，并解锁新的装备，同时也可以增加矿石的最大储量。
2. 所谓的矿石指闪亮矿石（蓝矿）、璀璨矿石（紫矿）、星辉矿石（黄矿）这三种资源，这三种资源只在升级装备时使用，其中蓝矿最常见，黄矿最稀缺。
3. 英雄装备可以赋予英雄一定的技能，详情请前往对应的装备页面查看。
4. 升级装备不需要时间，只需花费矿石。
5. 升级装备不占用 [建筑工人](/upgrade/0500-Builders-Hut)，也不占用 [实验室](/upgrade/0483-Laboratory)。
6. 铁匠铺免疫 [雷电法术](/upgrade/0100-Lightning-Spell) 伤害，理论上属于资源类建筑，但不被 [哥布林](/upgrade/0003-Goblin) 优先攻击。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/10/06">
        <TimelineRow>6 ~ 9 级铁匠铺的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>1 ~ 6、8 ~ 9 级铁匠铺的升级时间减少。</TimelineRow>
        <TimelineRow>1 ~ 2、5 ~ 9 级铁匠铺的升级费用降低。</TimelineRow>
        <TimelineRow>5 级铁匠铺可以再解锁一个装备：贵族哑铃。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/02/10">
        <TimelineRow>3 级铁匠铺可以再解锁一个装备：铁甲短裤。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>8 级铁匠铺的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/02/27">
        <TimelineRow>铁匠铺改为使用圣水升级。</TimelineRow>
        <TimelineRow>现在 7 ~ 8 级铁匠铺可以解锁新装备了。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>16 本推出，新建筑：铁匠铺，共设 9 个等级。其中前 6 个等级可解锁新装备，后 3 个等级不解锁任何装备。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
