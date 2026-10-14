---
title: "部落冲突 coc 飞龙公爵升级数据"
navTitle: "飞龙公爵"
shownTitle: "飞龙公爵"
module: upgrade-home
imgFolder: home_heroes/0205
wiki: https://clashofclans.fandom.com/wiki/Dragon_Duke
canonical: /upgrade/0205-Dragon-Duke
dataSyncedOn: 2026-10-13
description: "这名坦克型飞行英雄因为情绪管理问题被关了起来，一旦远离友方飞行单位，他就会变得更加愤怒与强大！进入皇室狂暴状态后，他的伤害会提升 100、攻击速度提升 50%，同时使自身受到的陷阱伤害减半。在防守时，他只能被敌方的对空单位攻击。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0205-Dragon-Duke.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2026-03-01'">

<template #introduction>

- *如想查看飞龙公爵的创作原型，请访问：[飞龙](/upgrade/0008-Dragon)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Dragon_Duke_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

1. 下方的数据均为不含装备的数据。
2. 英雄在防守时没有装备。

搜索半径：如果敌军进入这个范围，英雄会奔向敌军，并进行反击。<br>
巡逻半径：在没有敌人的情况下，英雄也会走动，而这个走动的范围叫巡逻半径。

下表中的生命值恢复量是基础属性，与装备无关。即使没有装备，开技能也会回血。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2026/03/01">
        <TimelineRow>飞龙公爵正式推出，15 本可解锁。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2026/02/23">
        <TimelineRow>飞龙公爵已经添加到游戏中，但需要通过活动获取。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
