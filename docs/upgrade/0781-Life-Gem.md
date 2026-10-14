---
title: "部落冲突 coc 生命宝石装备升级数据"
navTitle: "生命宝石"
shownTitle: "生命宝石"
module: upgrade-home
imgFolder: home_heroes/0781
wiki: https://clashofclans.fandom.com/wiki/Life_Gem
canonical: /upgrade/0781-Life-Gem
dataSyncedOn: 2026-10-13
description: "生命宝石是大守护者的两件初始装备之一。生命宝石装备可以在大守护者周围投射出魔法光环，当我方部队在光环内时，它们会获得额外的生命值。当守护者学徒的光环与生命宝石装备的光环叠加时，以加血百分比高的那个为准。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0781-Life-Gem.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2026-01-12'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Life_Gem_info.png" :imgAlt="$frontmatter.navTitle" description="附近友军单位获得额外生命值。" />

<SmallTitle>说明</SmallTitle>

1. 生命宝石是 [大守护者](/upgrade/0202-Grand-Warden) 的两件初始装备之一，另一件是 [永恒书卷](/upgrade/0780-Eternal-Tome)。
2. 生命宝石装备可以在大守护者周围投射出魔法光环，当我方部队在光环内时，它们会获得额外的生命值。
3. 生命宝石装备可以让大守护者自己获得更高的每秒伤害和生命值，但这不是光环的效果，是装备本身的属性。
4. 当 [守护者学徒](/upgrade/0089-Apprentice-Warden) 的光环与生命宝石装备的光环叠加时，以加血百分比高的那个为准。守护者学徒的光环在生命值更高的单位上会更强，因为守护者学徒的加血没有上限。
5. 什么是加血上限呢？假如你的生命宝石装备是 18 级，加血比例 100%，上限 725. 现在你有个 100 血的兵，加血 100% 就是提升 100 滴血，这个数字没有超过 725 的上限，所以最后这个兵在大守护者的光环下可以实实在在地加 100 滴血。但是如果你这个兵有 10 000 滴血呢？10 000 滴血明显超过了 725 的上限，因此最后这个兵在光环下只能加 725 血。这就是所谓的上限。

注意：

6. 如果升级费用中有多种资源，则同时需要多种资源才能升级。<br>
7. 如果玩家升级到了 11 本并解锁了大守护者，即使玩家没有马上升 [铁匠铺](/upgrade/0488-Blacksmith) 也可以升级生命宝石装备。

在 2023 年 12 月装备系统发布时，已解锁大守护者的玩家会有一个初始的装备等级，并且不需要解锁铁匠铺。装备等级与玩家的英雄等级相关，具体如下表。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2026/01/12">
        <TimelineRow>1 ~ 18 级生命宝石装备的光环加血百分比、光环加血上限、英雄生命值增加值提升。</TimelineRow>
        <TimelineRow>4 ~ 18 级生命宝石装备的英雄每秒伤害增加值提升。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/02/10">
        <TimelineRow>所有等级生命宝石装备的光环加血上限、英雄每秒伤害增加值和英雄生命值增加值提升。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/09/09">
        <TimelineRow>所有等级生命宝石装备的光环加血上限提升。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>游戏新增装备系统，生命宝石是第一批推出的装备。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
