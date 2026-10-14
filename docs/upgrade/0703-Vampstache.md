---
title: "部落冲突 coc 嗜血胡须（治疗胡须）装备升级数据"
navTitle: "嗜血胡须"
shownTitle: "嗜血胡须（治疗胡须）"
module: upgrade-home
imgFolder: home_heroes/0703
wiki: https://clashofclans.fandom.com/wiki/Vampstache
canonical: /upgrade/0703-Vampstache
dataSyncedOn: 2026-10-13
description: "嗜血胡须是野蛮人之王的一件普通装备。嗜血胡须可以使蛮王每次攻击时都能回血，此外，嗜血胡须还可以提高蛮王的攻击速度和每秒伤害。例外：被凤凰复活的蛮王不能回血。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0703-Vampstache.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-02-10'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Vampstache_info.png" :imgAlt="$frontmatter.navTitle" description="野蛮人之王每次攻击都会治疗自身" />

<SmallTitle>说明</SmallTitle>

1. 嗜血胡须是 [野蛮人之王](/upgrade/0200-Barbarian-King) 的一件普通装备。
2. 嗜血胡须可以使蛮王每次攻击时都能回血，此外，嗜血胡须还可以提高蛮王的攻击速度和每秒伤害。
   - 例外：被 [凤凰](/upgrade/0287-Phoenix) 复活的蛮王不能回血。
3. 该装备的英文名称 Vampstache 取自吸血鬼（vampire）这个单词的前半边和胡须（mustache）这个单词的后半边，因此顾名思义这个装备有吸血效果，网站出于准确性原则采用了“嗜血胡须”这个翻译。

注：如果升级费用中有多种资源，则同时需要多种资源才能升级。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/02/10">
        <TimelineRow>所有等级嗜血胡须的每秒伤害增加值提高。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>游戏新增装备系统，嗜血胡须是第一批推出的装备。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
