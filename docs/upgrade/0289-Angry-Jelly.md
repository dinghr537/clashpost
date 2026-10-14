---
title: "部落冲突 coc 愤怒水母升级数据"
navTitle: "愤怒水母"
shownTitle: "愤怒水母"
module: upgrade-home
imgFolder: home_heroes/0289
wiki: https://clashofclans.fandom.com/wiki/Angry_Jelly
canonical: /upgrade/0289-Angry-Jelly
dataSyncedOn: 2026-10-13
description: "这团愤怒的水母在村庄附近等得不耐烦了，它渴望一场酣畅淋漓的战斗。在战斗中，它会说服其跟随的英雄优先攻击防御建筑，然后再分头作战。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0289-Angry-Jelly.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-03-24'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Angry_Jelly_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

1. 愤怒水母的技能（洗脑，又称心灵控制）：让跟随的英雄在部署后的一段时间内优先攻击防御建筑。
2. 水母是飞行单位，可以对防御建筑进行远程攻击。
3. 水母处于跟随状态时不会成为目标或受到伤害，也不会触发陷阱。
4. 当水母跟随的英雄被击倒，或英雄被 [回溯法术](/upgrade/0107-Recall-Spell) 召回，水母会变成普通部队，可以成为目标以及受到伤害，也可以触发陷阱了。
5. 如果愤怒水母跟随的英雄未被击倒，则不占用回溯法术的空间。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/03/24">
        <TimelineRow>2 ~ 10 级愤怒水母的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>2 ~ 10 级愤怒水母的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/04/17">
        <TimelineRow>新战宠：愤怒水母。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
