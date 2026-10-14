---
title: "部落冲突 coc 野蛮人木偶（野蛮人玩偶）装备升级数据"
navTitle: "野蛮人木偶"
shownTitle: "野蛮人木偶（野蛮人玩偶）"
module: upgrade-home
imgFolder: home_heroes/0700
wiki: https://clashofclans.fandom.com/wiki/Barbarian_Puppet
canonical: /upgrade/0700-Barbarian-Puppet
dataSyncedOn: 2026-10-13
description: "野蛮人木偶是野蛮人之王的两件初始装备之一。野蛮人木偶装备可以让野蛮人之王使用技能时召唤出大量处于狂暴状态下的野蛮人，这些野蛮人比普通的野蛮人伤害更高，移动速度更快。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0700-Barbarian-Puppet.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-02-10'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Barbarian_Puppet_info.png" :imgAlt="$frontmatter.navTitle" description="召唤一群狂暴野蛮人。" />

<SmallTitle>说明</SmallTitle>

1. 野蛮人木偶是 [野蛮人之王](/upgrade/0200-Barbarian-King) 的两件初始装备之一，另一件是 [狂暴药水瓶](/upgrade/0701-Rage-Vial)。
2. 野蛮人木偶装备可以让野蛮人之王使用技能时召唤出大量处于狂暴状态下的 [野蛮人](/upgrade/0000-Barbarian)，这些野蛮人比普通的野蛮人伤害更高，移动速度更快。
   - 装备召唤出的野蛮人不会一直处于狂暴状态，技能失效后这些部队就会变成普通的野蛮人，总狂暴时间为 20 秒。
   - 野蛮人木偶的召唤速度为每秒 10 个野蛮人。
   - 召唤出的野蛮人等级与进攻方 [实验室](/upgrade/0483-Laboratory) 中野蛮人的等级相同。
3. 除了召唤野蛮人外，该装备还可以为蛮王提供额外的生命值，并且增加开技能时恢复的生命值。

注：如果升级费用中有多种资源，则同时需要多种资源才能升级。

在 2023 年 12 月装备系统发布时，已解锁野蛮人之王的玩家会有一个初始的装备等级，并且不需要解锁 [铁匠铺](/upgrade/0488-Blacksmith)。装备等级与玩家的英雄等级相关，具体如下表。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/02/10">
        <TimelineRow>所有等级野蛮人木偶的每秒伤害增加值和开启技能后生命值恢复加成提高。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/09/09">
        <TimelineRow>野蛮人被召唤出来后，其狂暴时间由 10 秒增加到 20 秒。</TimelineRow>
        <TimelineRow>13 - 18 级野蛮人木偶装备可以给英雄加更多生命值。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>游戏新增装备系统，野蛮人木偶是第一批推出的装备。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
