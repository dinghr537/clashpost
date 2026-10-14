---
title: "部落冲突 coc 都城狂暴法术升级数据"
navTitle: "狂暴法术"
shownTitle: "狂暴法术"
module: upgrade-capital
imgFolder: capital_tech/2104
wiki: https://clashofclans.fandom.com/wiki/Rage_Spell/Clan_Capital
canonical: /upgrade/2104-Rage-Spell
dataSyncedOn: 2026-10-13
description: "让部队士气飙涨，变得更快、更强！施放狂暴法术会产生一个狂暴效果光环！在此光环中的部队速度增快，攻击力增强。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/2104-Rage-Spell.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2022-06-30'">

<template #introduction>

- *如想查看家乡的狂暴法术，请访问：[狂暴法术](/upgrade/0102-Rage-Spell)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Rage_Spell_info.png" :imgAlt="$frontmatter.navTitle"
    description="让部队士气飙涨，变得更快、更强！<br>施放狂暴法术会产生一个狂暴效果光环！在此光环中的部队速度增快，攻击力增强。"
    :isSmallImg="true" />

<SmallTitle>重要说明</SmallTitle>

当都城之巅的大本营升到 6 级，并且解锁飞龙悬崖后，系统会自动建造 [狂暴法术工厂](/upgrade/2384-Rage-Spell-Factory)，建造完成后即解锁狂暴法术。

\* 这里的 8 点移动速度代表 1 格/秒。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2022/06/30">
        <TimelineRow>将狂暴法术的“伤害提升”属性降低 20%.</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/05/02">
        <TimelineRow>狂暴法术随着部落都城玩法一同推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
