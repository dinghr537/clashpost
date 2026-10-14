---
title: "部落冲突 coc 德鲁伊升级数据"
navTitle: "德鲁伊"
shownTitle: "德鲁伊"
module: upgrade-home
imgFolder: home_tech/008a
wiki: https://clashofclans.fandom.com/wiki/Druid
canonical: /upgrade/008a-Druid
dataSyncedOn: 2026-10-13
description: "德鲁伊的情绪复杂多变，上一秒他还在冷静地治疗友军，下一秒就变成了一只愤怒无比的巨熊。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/008a-Druid.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2026-01-12'">

<template #introduction>

<SwitchTabs contentClass="cp-unit-items" :stickyTabs="true" :pageTabs="true">
    <SwitchTab tabId="cp-unit-item-0" :activeTab="true">人类形态</SwitchTab>
    <SwitchTab tabId="cp-unit-item-1">巨熊形态</SwitchTab>
</SwitchTabs>

<SwitchTabGroup id="cp-unit-item-0" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Druid_info.png" imgAlt="德鲁伊（人类形态）"
    description="德鲁伊的情绪复杂多变，上一秒他还在冷静地治疗友军，下一秒就变成了一只愤怒无比的巨熊。" />

<SmallTitle>重要说明</SmallTitle>

1. 德鲁伊有两种形态：可以治疗友军的人类形态以及可以进攻的巨熊形态。
2. 在德鲁伊被部署后的前 30 秒，他处于人类形态，当 30 秒时间耗尽或生命值归零时，他会变身为巨熊形态。
   - 如果德鲁伊被 [隐形弹簧](/upgrade/0381-Spring-Trap) 弹飞，他将无法变身。
3. 在人类形态下，德鲁伊的治疗效果可以最多弹射到 4 个目标（含第一个治疗目标）身上。
   - 德鲁伊的治疗效果无法弹射到攻城机器身上（攻城机器免疫所有治疗效果）。
   - 德鲁伊可以同时治疗地面和空中部队，而天使只能治疗地面部队。
   - 与天使和 [疗伤法术](/upgrade/0101-Healing-Spell) 不同的是，德鲁伊对英雄的治疗量没有衰减。
   - 当多个治疗单位治疗同一目标时，治疗量会衰减。
   - 在人类形态下，德鲁伊不能反击。在没有治疗目标时，即使受到伤害也会保持静止。
4. 在巨熊形态下，德鲁伊是一种优先攻击防御建筑的兵种。
5. 人类形态下的德鲁伊可以跳墙，巨熊形态下则不能。
6. 两种形态的德鲁伊占用的人口数不一样，人类形态为 16 人口，巨熊形态为 10 人口。

</SwitchTabGroup>

<SwitchTabGroup id="cp-unit-item-1" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Bear_info.png" imgAlt="德鲁伊（巨熊形态）"
    description="德鲁伊变身成愤怒的熊灵之后，拥有较高的生命值，会冲向防御建筑并摧毁它们！" />

<SmallTitle>重要说明</SmallTitle>

1. 德鲁伊有两种形态：可以治疗友军的人类形态以及可以进攻的巨熊形态。
2. 在德鲁伊被部署后的前 30 秒，他处于人类形态，当 30 秒时间耗尽或生命值归零时，他会变身为巨熊形态。
   - 如果德鲁伊被 [隐形弹簧](/upgrade/0381-Spring-Trap) 弹飞，他将无法变身。
3. 在人类形态下，德鲁伊的治疗效果可以最多弹射到 4 个目标（含第一个治疗目标）身上。
   - 德鲁伊的治疗效果无法弹射到攻城机器身上（攻城机器免疫所有治疗效果）。
   - 德鲁伊可以同时治疗地面和空中部队，而天使只能治疗地面部队。
   - 与天使和 [疗伤法术](/upgrade/0101-Healing-Spell) 不同的是，德鲁伊对英雄的治疗量没有衰减。
   - 当多个治疗单位治疗同一目标时，治疗量会衰减。
   - 在人类形态下，德鲁伊不能反击。在没有治疗目标时，即使受到伤害也会保持静止。
4. 在巨熊形态下，德鲁伊是一种优先攻击防御建筑的兵种。
5. 人类形态下的德鲁伊可以跳墙，巨熊形态下则不能。
6. 两种形态的德鲁伊占用的人口数不一样，人类形态为 16 人口，巨熊形态为 10 人口。

</SwitchTabGroup>

</template>

<template #history>

<Timeline>
    <TimelineItem date="2026/01/12">
        <TimelineRow>德鲁伊在人类形态下最多可存活的时间由 25 秒增加至 30 秒。</TimelineRow>
        <TimelineRow>所有等级德鲁伊在人类形态下的治疗量增加。</TimelineRow>
        <TimelineRow>4 ~ 5 级德鲁伊在巨熊形态下的每秒伤害和生命值增加。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/11/17">
        <TimelineRow>5 级德鲁伊的升级时间和升级费用减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/10/06">
        <TimelineRow>3 ~ 4 级德鲁伊的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/06/16">
        <TimelineRow>在 17 本新增 5 级德鲁伊。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/27">
        <TimelineRow>部队的训练时间取消，但增加了捐赠费用。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>2 ~ 4 级德鲁伊的升级时间减少。</TimelineRow>
        <TimelineRow>德鲁伊在巨熊形态下占用的人口数由 16 调整为 10.</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/02/10">
        <TimelineRow>德鲁伊的训练时间由 2:30 改为 2:20</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>4 级德鲁伊的升级时间减少。</TimelineRow>
        <TimelineRow>2 ~ 4 级德鲁伊的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/10/02">
        <TimelineRow>德鲁伊在人类形态下的每秒治疗量减少约 42%.</TimelineRow>
        <TimelineRow>德鲁伊在人类形态下最多可存活的时间减少（30 秒 → 25 秒）。</TimelineRow>
        <TimelineRow>德鲁伊在巨熊形态下的伤害降低 50%.</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/09/09">
        <TimelineRow>德鲁伊最多可治疗的目标数量由 4 个减少到 3 个。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/18">
        <TimelineRow>14 本可解锁新兵种：德鲁伊。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
