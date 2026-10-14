---
title: "部落冲突 coc 疗伤法术（治疗）升级数据"
navTitle: "疗伤法术"
shownTitle: "疗伤法术（治疗）"
module: upgrade-home
imgFolder: home_tech/0101
wiki: https://clashofclans.fandom.com/wiki/Healing_Spell
canonical: /upgrade/0101-Healing-Spell
dataSyncedOn: 2026-10-13
description: "恢复部队的元气，让他们保持战斗力！施放疗伤法术会产生一个治疗光环，治愈该法术光环之内的部队。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0101-Healing-Spell.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-11-17'">

<template #introduction>

- *如想查看都城的疗伤法术，请访问：[都城疗伤法术](/upgrade/2100-Healing-Spell)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Healing_Spell.png" :imgAlt="$frontmatter.navTitle"
    description="恢复部队的元气，让他们保持战斗力！<br>施放疗伤法术会产生一个治疗光环，治愈该法术光环之内的部队。"
    :isSmallImg="true" />

<SmallTitle>重要说明</SmallTitle>

1. 多个疗伤法术的效果可以叠加。
2. 疗伤法术治疗我方英雄时，其效果会减弱。疗伤法术对攻城机器无效。
3. 疗伤法术可以与 治疗单位 的治疗效果直接叠加。

\* 疗伤法术的治疗方式是每隔 0.3 秒给法术作用范围内兵种增加部分生命值。

最大总治疗量(部队)：表格中的总治疗量指的是每个兵都可以享受这么多治疗量。<br>
所需实验室等级：如果玩家升级到 6 级大本营并且解锁了疗伤法术，即使玩家没有立即升实验室也可以升级疗伤法术。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/11/17">
        <TimelineRow>18 本推出，并在 18 本新增 12 级疗伤法术。</TimelineRow>
        <TimelineRow>11 级疗伤法术的升级时间减少。</TimelineRow>
        <TimelineRow>11 级疗伤法术的每次治疗由65增加至67。</TimelineRow>
        <TimelineRow>所有等级疗伤法术的治疗次数由40增加至41。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/10/06">
        <TimelineRow>9 ~ 10 级疗伤法术的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/27">
        <TimelineRow>法术的配置时间取消，但新增了捐赠费用。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>2 ~ 6、9 ~ 10 级疗伤法术的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>17 本推出，并在 17 本新增 11 级疗伤法术。</TimelineRow>
        <TimelineRow>6 ~ 8、10 级疗伤法术的升级时间减少。</TimelineRow>
        <TimelineRow>8 ~ 10 级疗伤法术的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/18">
        <TimelineRow>9 级疗伤法术的升级时间减少。</TimelineRow>
        <TimelineRow>9 级疗伤法术的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>16 本推出，并在 16 本新增 10 级疗伤法术。</TimelineRow>
        <TimelineRow>6 ~ 9 级疗伤法术的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>8 级疗伤法术的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>15 本推出，并在 15 本新增 9 级疗伤法术。</TimelineRow>
        <TimelineRow>7 ~ 8 级疗伤法术的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/12/09">
        <TimelineRow>3 ~ 7 级疗伤法术的升级费用降低。</TimelineRow>
        <TimelineRow>2 ~ 7 级疗伤法术的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>2 ~ 7 级疗伤法术的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/12/09">
        <TimelineRow>13 本新增 8 级疗伤法术。</TimelineRow>
        <TimelineRow>游戏中对部队的治疗量和对英雄的治疗量分别显示在了面板上。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/04/02">
        <TimelineRow>包含大量降低发展成本和提高发展速度的调整，其中 5 ~ 6 级疗伤法术的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
