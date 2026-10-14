---
title: "部落冲突 coc 毒药法术（施毒法术）升级数据"
navTitle: "毒药法术"
shownTitle: "毒药法术（施毒法术）"
module: upgrade-home
imgFolder: home_tech/0180
wiki: https://clashofclans.fandom.com/wiki/Poison_Spell
canonical: /upgrade/0180-Poison-Spell
dataSyncedOn: 2026-10-13
description: "借助危险的毒药法术，让您的部队在对抗敌军中占据上风！用毒药法术让敌军处于萦绕着的毒雾中，他们的移动和攻击速度都会变慢，并且受到的伤害会随着时间而加重。毒药法术对建筑物无效。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0180-Poison-Spell.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-11-17'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Poison_Spell.png" :imgAlt="$frontmatter.navTitle"
    description="借助危险的毒药法术，让您的部队在对抗敌军中占据上风！用毒药法术让敌军处于萦绕着的毒雾中，他们的移动和攻击速度都会变慢，并且受到的伤害会随着时间而加重。毒药法术对建筑物无效。"
    :isSmallImg="true" />

<SmallTitle>重要说明</SmallTitle>

1. 毒药法术对敌方英雄有效，伤害只有其他单位的 5％，但减速效果是全额的。
2. 毒药法术不能对建筑造成伤害，也不能减缓建筑的攻击速度。
3. 中毒状态下，兵种的每次伤害和非中毒状态一致，并不会因为攻速变慢而产生更高的每次伤害。
4. 毒药法术的伤害成二次函数递增，约 8 秒达到最大伤害。离开毒药范围后伤害递减，递减速度是增加的两倍。
5. 毒药 [法术塔](/upgrade/0311-Spell-Tower)、[猛蜥](/upgrade/0286-Poison-Lizard) 和 14 - 16 级 [大本营](/upgrade/0400-Town-Hall) 爆炸后的毒药也具有和毒药法术类似的伤害递增特性，但是这些毒药的属性和毒药法术不同。
6. [英雄猎手](/upgrade/0088-Headhunter) 的攻击也具有和毒药法术类似的减速效果，但中毒伤害不是随时间递增的，而是会立即达到最大伤害。
7. 毒药法术的毒药效果和其他具有毒药效果的单位叠加时取效果最强的那个。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/11/17">
        <TimelineRow>18 本推出，并在 18 本新增 12 级毒药法术。</TimelineRow>
        <TimelineRow>11 级毒药法术的升级时间和升级费用减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/10/06">
        <TimelineRow>8 ~ 10 级毒药法术的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/27">
        <TimelineRow>法术的配置时间取消，但新增了捐赠费用。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>2 ~ 3、5 ~ 10 级毒药法术的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/02/10">
        <TimelineRow>17 本新增 11 级毒药法术。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>4、6、7、9、10 级毒药法术的升级时间减少。</TimelineRow>
        <TimelineRow>2 ~ 10 级毒药法术的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/18">
        <TimelineRow>8 ~ 9 级毒药法术的升级时间减少。</TimelineRow>
        <TimelineRow>8 ~ 9 级毒药法术的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>16 本推出，并在 16 本新增 10 级毒药法术。</TimelineRow>
        <TimelineRow>5 ~ 9 级毒药法术的升级时间减少。</TimelineRow>
        <TimelineRow>2 ~ 3、8 级毒药法术的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>6 ~ 7 级毒药法术的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>15 本推出，并在 15 本新增 9 级毒药法术。</TimelineRow>
        <TimelineRow>4 ~ 8 级毒药法术的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/02/15">
        <TimelineRow>“毒药法术”的简体中文名称改为“伤害药水法术”，网站仍然使用旧名称。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/12/09">
        <TimelineRow>2 ~ 6 级毒药法术的升级费用降低。</TimelineRow>
        <TimelineRow>2 ~ 4 级毒药法术的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>14 本推出，并在 14 本新增 8 级毒药法术。</TimelineRow>
        <TimelineRow>2 ~ 3 级毒药法术的升级费用降低。</TimelineRow>
        <TimelineRow>2 ~ 5 级毒药法术的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/03/30">
        <TimelineRow>13 本新增 7 级毒药法术。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/06/18">
        <TimelineRow>12 本新增 6 级毒药法术。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
