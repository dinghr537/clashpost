---
title: "部落冲突 coc 阿啾升级数据"
navTitle: "阿啾"
shownTitle: "阿啾"
module: upgrade-home
imgFolder: home_heroes/028a
wiki: https://clashofclans.fandom.com/wiki/Sneezy
canonical: /upgrade/028a-Sneezy
dataSyncedOn: 2026-10-13
description: "她的鼻子堵住了，随时准备打喷嚏！阿啾因过敏躲在英雄身后，朝建筑喷出黏糊糊的鼻涕小怪。跟随的英雄被击倒后，她仍会继续战斗！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/028a-Sneezy.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2026-01-12'">

<template #introduction>

<SwitchTabs contentClass="cp-unit-items" :stickyTabs="true" :pageTabs="true">
    <SwitchTab tabId="cp-unit-item-0" :activeTab="true">阿啾</SwitchTab>
    <SwitchTab tabId="cp-unit-item-1">鼻涕小怪</SwitchTab>
</SwitchTabs>

<SwitchTabGroup id="cp-unit-item-0" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Sneezy_info.png" imgAlt="阿啾"
    description="她的鼻子堵住了，随时准备打喷嚏！阿啾因过敏躲在英雄身后，朝建筑喷出黏糊糊的鼻涕小怪。跟随的英雄被击倒后，她仍会继续战斗！" />

<SmallTitle>重要说明</SmallTitle>

1. 阿啾的技能（哈啾！）：喷出空中支援部队。跟随的英雄被击倒后，她仍会继续战斗。
2. 当阿啾跟随的英雄被击倒时，阿啾会进入愤怒状态。愤怒状态大约有 1% 的微小伤害加成，持续 5 分钟，比每局游戏的持续时间都长，因此可视为永久性加成。这个愤怒状态可被 [狂暴法术](/upgrade/0102-Rage-Spell) 覆盖。
3. 当阿啾跟随的英雄未被击倒时，使用 [回溯法术](/upgrade/0107-Recall-Spell) 召回英雄时可一并召回阿啾，而无需占用回溯法术的空间。当阿啾跟随的英雄被击倒时，召回阿啾时就和其他战宠一样要占用空间了。

攻击距离：当阿啾跟随英雄未被击败时，它的攻击距离为 5.5 格，反之则为 1.5 格。

</SwitchTabGroup>

<SwitchTabGroup id="cp-unit-item-1" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Booger_info.png" imgAlt="鼻涕小怪"
    description="邪恶的鼻涕小怪从阿啾的鼻孔中喷射而出！这些生命值较高的空中部队能吸收伤害并攻击建筑。离纸巾远点就行！" />

<SmallTitle>重要说明</SmallTitle>

鼻涕小怪不能触发陷阱。

</SwitchTabGroup>

</template>

<template #history>

<Timeline>
    <TimelineItem date="2026/01/12">
        <TimelineRow>鼻涕小怪不再触发陷阱。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>新战宠：阿啾。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
