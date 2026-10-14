---
title: "部落冲突 coc 暗黑皇冠装备升级数据"
navTitle: "暗黑皇冠"
shownTitle: "暗黑皇冠"
module: upgrade-home
imgFolder: home_heroes/0724
wiki: https://clashofclans.fandom.com/wiki/Dark_Crown
canonical: /upgrade/0724-Dark-Crown
dataSyncedOn: 2026-10-13
description: "暗黑皇冠是亡灵王子的第一件史诗装备。当亡灵王子带上暗黑皇冠并在场时，每累计 60 人口的攻击方部队被击败，亡灵王子就可以获得一层生命值和伤害增益，最多 3 层，共需 180 人口。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0724-Dark-Crown.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-11-17'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Dark_Crown.png" :imgAlt="$frontmatter.navTitle" description="当友军被击倒时，提升生命值和伤害，共计 3 次。" :isSmallImg="true"  />

<SmallTitle>说明</SmallTitle>

1. 暗黑皇冠是 [亡灵王子](/upgrade/0204-Minion-Prince) 的第一件史诗装备，它在 2025 年 6 月的黑暗交易活动中首次开放购买。
2. 当亡灵王子带上暗黑皇冠并在场时，每累计 60 人口的攻击方部队被击败，亡灵王子就可以获得一层生命值和伤害增益，最多 3 层，共需 180 人口。
    - 除亡灵王子外的英雄均计入总人口，每个英雄为 25 人口。如果英雄被 [复苏法术](/upgrade/0108-Revive-Spell) 复苏后再次被击败，可重复计算人口。
    - 战宠视为 20 人口。
    - 召唤出来的部队会被计算在内，例如 [女巫](/upgrade/0084-Witch) 的骷髅兵、[攻城训练营](/upgrade/0243-Siege-Barracks) 召唤的皮卡等等。
    - 在攻击过程中自杀的部队也会被计算在内，如 [炸弹人](/upgrade/0004-Wall-Breaker)、[小雪怪](/upgrade/000d-Yeti)。
    - 法术不是部队，不会计入总人口。
    - 攻城机器、[镜像法术](/upgrade/0105-Clone-Spell) 复制的部队不会被计算在内。
    - 当 [德鲁伊](/upgrade/008a-Druid) 由人类形态转变为巨熊形态时，不会被计入总人口。当巨熊形态的德鲁伊因耗尽生命值死亡，或者德鲁伊直接被隐形弹簧弹飞，才会被计入总人口。
    - 在王子被召回期间，死亡的部队不能被计入总人口。
    - 即使亡灵王子被击败，暗黑皇冠仍会计算死亡部队。在亡灵王子复苏后，亡灵王子可直接享有被击败期间叠加的增益。
3. 暗黑皇冠的增益效果不能与 [狂暴法术](/upgrade/0102-Rage-Spell)、[守护者学徒](/upgrade/0089-Apprentice-Warden) 等单位的增益效果直接叠加，只能取其最高的增益效果。
4. 此外，暗黑皇冠装备还可以提高亡灵王子的生命值和攻击速度。

注意：如果升级费用中有多种资源，则同时需要多种资源才能升级。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/11/17">
        <TimelineRow>现在亡灵王子的所有装备都提供 500 生命值加成。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/06/10">
        <TimelineRow>新装备：暗黑皇冠。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
