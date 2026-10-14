---
title: "部落冲突 coc 灵狐（狐狸）升级数据"
navTitle: "灵狐"
shownTitle: "灵狐（狐狸）"
module: upgrade-home
imgFolder: home_heroes/0288
wiki: https://clashofclans.fandom.com/wiki/Spirit_Fox
canonical: /upgrade/0288-Spirit-Fox
dataSyncedOn: 2026-10-13
description: "灵狐生性极其害羞，最喜欢独自待在村庄外的树林里。被召唤到战场时，灵狐会与它的英雄并肩作战，并帮助其隐身。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0288-Spirit-Fox.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-03-24'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Spirit_Fox_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

1. 灵狐的技能（灵隐诡步）：每隔一段时间使自己和跟随的英雄隐身。
2. 只有当灵狐在场上时，隐形效果才会生效，如果灵狐死亡或被 [回溯法术](/upgrade/0107-Recall-Spell) 召回，则英雄无法隐身。如果灵狐跟随的英雄阵亡，则它只能让自己隐形。
3. 如果主人被召回或者阵亡，灵狐会变成一个自由单位，此时没有偏好。
4. 灵狐的隐形效果激活时可重置单头 [地狱塔](/upgrade/030a-Inferno-Tower) 和防守方 [地狱飞龙](/upgrade/0604-Inferno-Dragon) 的伤害。
5. 灵狐的移动速度较快，很容易跑在英雄前面导致过早死亡，因此灵狐很适合搭配移动速度同样较快的 [飞盾战神](/upgrade/0203-Royal-Champion)。另外，灵狐也可以搭配 [蛮王](/upgrade/0200-Barbarian-King)，延长蛮王的存活时间，让蛮王的坦克潜力充分发挥。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/03/24">
        <TimelineRow>2 ~ 10 级灵狐的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>2 ~ 10 级灵狐的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/03/26">
        <TimelineRow>1 ~ 10 级灵狐的隐身效果冷却时间由 5 秒增加到 6 秒。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/02/27">
        <TimelineRow>移除了灵狐进行攻击时的冰霜视觉效果。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>16 本推出，可解锁一个新宠物：灵狐。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
