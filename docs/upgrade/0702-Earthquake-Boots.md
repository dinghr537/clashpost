---
title: "部落冲突 coc 地震金靴（震地金靴）装备升级数据"
navTitle: "地震金靴"
shownTitle: "地震金靴（震地金靴）"
module: upgrade-home
imgFolder: home_heroes/0702
wiki: https://clashofclans.fandom.com/wiki/Earthquake_Boots
canonical: /upgrade/0702-Earthquake-Boots
dataSyncedOn: 2026-10-13
description: "地震金靴是野蛮人之王的一件普通装备。地震金靴可以时蛮王在使用技能时制造一场地震。这次地震可以立即摧毁周围的城墙，并且对建筑物造成一定百分比的破坏。地震金靴可以对半径内的所有地面单位（包括部队）造成少量额外伤害……"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0702-Earthquake-Boots.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2026-02-23'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Earthquake_Boots_info.png" :imgAlt="$frontmatter.navTitle" description="引发强烈地震，摧毁城墙并对建筑造成伤害。" />

<SmallTitle>说明</SmallTitle>

1. 地震金靴是 [野蛮人之王](/upgrade/0200-Barbarian-King) 的一件普通装备。
2. 地震金靴可以时蛮王在使用技能时制造一场地震。这次地震可以立即摧毁周围的城墙，并且对建筑物造成一定百分比的破坏。
   - 地震金靴造成的伤害是相对于部队或建筑最大生命值的，即使残血也按满血算。
   - 地震金靴的伤害并不均匀，位于地震范围边缘的城墙会受到伤害，但不会倒塌。
   - 地震金靴引起的地震**可以**激活 12 级及以上 [大本营](/upgrade/0400-Town-Hall) 自带的武器。
   - 和 [地震法术](/upgrade/0181-Earthquake-Spell) 不同的是，地震金靴引起的地震**可以**对资源仓库造成破坏。
   - 当地震金靴引起的地震和地震法术叠加时，建筑物的损坏效果会减弱，具体公式可前往地震法术页面查看，你把地震金靴装备当作一瓶地震法术即可。
3. 除了制造地震之外，地震金靴装备还可以提高蛮王的每秒伤害和最大生命值。

注：如果升级费用中有多种资源，则同时需要多种资源才能升级。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2026/02/23">
        <TimelineRow>地震金靴的地震效果可以对地面部队造成伤害了（同步地震法术的更改）。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/02/10">
        <TimelineRow>9 ~ 18 级地震金靴的百分比伤害降低。</TimelineRow>
        <TimelineRow>地震金靴 100 点左右的固定伤害取消，现在地震金靴不能杀死骷髅了。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/09/09">
        <TimelineRow>9 - 18 级地震金靴装备的伤害百分比增加。</TimelineRow>
        <TimelineRow>12 - 18 级地震金靴装备可以给英雄加更多生命值。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>游戏新增装备系统，地震金靴是第一批推出的装备。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
