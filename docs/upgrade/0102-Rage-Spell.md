---
title: "部落冲突 coc 狂暴法术升级数据"
navTitle: "狂暴法术"
shownTitle: "狂暴法术"
module: upgrade-home
imgFolder: home_tech/0102
wiki: https://clashofclans.fandom.com/wiki/Rage_Spell
canonical: /upgrade/0102-Rage-Spell
dataSyncedOn: 2026-10-13
description: "让部队士气飙涨，变得更快、更强！施放狂暴法术会产生一个狂暴效果光环！在此光环中的部队速度增快，攻击力增强。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0102-Rage-Spell.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-03-27'">

<template #introduction>

- *如想查看都城的狂暴法术，请访问：[都城狂暴法术](/upgrade/2104-Rage-Spell)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Rage_Spell.png" :imgAlt="$frontmatter.navTitle"
    description="让部队士气飙涨，变得更快、更强！<br>施放狂暴法术会产生一个狂暴效果光环！在此光环中的部队速度增快，攻击力增强。"
    :isSmallImg="true" />

<SmallTitle>重要说明</SmallTitle>

1. 狂暴法术可以增加兵种的移动速度和伤害，但不能增加兵种的攻击速度。
2. 狂暴法术对我方英雄的效果减半，对攻城机器无效。
3. 狂暴法术并不能提高所有类型的伤害。举个例子，狂暴法术只能提升 [超级炸弹人](/upgrade/0603-Super-Wall-Breaker) 的主动伤害，不能提升其死亡伤害。
4. 与其他具有狂暴效果的单位（如 [阿啾](/upgrade/028a-Sneezy) 的愤怒状态、[暗黑皇冠](/upgrade/0724-Dark-Crown) 的伤害增益）叠加时，通常取效果最强的。

\* 脉冲次数指狂暴法术给兵提供效果的次数，不可叠加。增益时间指受到脉冲效果后的持续时间。

伤害增加：伤害增加 170% 的意思是兵种的伤害是原来的 1 + 170% = 2.7 倍，其它同理。<br>
速度增加：这里的速度增加值和游戏内兵种移动速度的显示是一个意思，移动速度 8 等于实际的 1 格/秒。<br>
所需实验室等级：如果玩家升级到 7 级大本营并且解锁了狂暴法术，即使玩家没有立即升实验室也可以升级狂暴法术。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/03/27">
        <TimelineRow>法术的配置时间取消，但新增了捐赠费用。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>2 ~ 6 级狂暴法术的升级时间减少。</TimelineRow>
        <TimelineRow>4 ~ 5 级狂暴法术的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>6 级狂暴法术的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>6 级狂暴法术的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>6 级狂暴法术的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>6 级狂暴法术的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/12/09">
        <TimelineRow>2 ~ 5 级狂暴法术的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>2 ~ 4 级狂暴法术的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/06/18">
        <TimelineRow>12 本新增 6 级狂暴法术。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/04/02">
        <TimelineRow>4 ~ 5 级狂暴法术的升级时间减少。</TimelineRow>
        <TimelineRow>所有等级狂暴法术的配置费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
