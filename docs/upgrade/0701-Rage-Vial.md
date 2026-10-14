---
title: "部落冲突 coc 狂暴药水瓶装备升级数据"
navTitle: "狂暴药水瓶"
shownTitle: "狂暴药水瓶"
module: upgrade-home
imgFolder: home_heroes/0701
wiki: https://clashofclans.fandom.com/wiki/Rage_Vial
canonical: /upgrade/0701-Rage-Vial
dataSyncedOn: 2026-10-13
description: "狂暴药水瓶是野蛮人之王的两件初始装备之一。狂暴药水瓶可以使蛮王在技能生效期间伤害提高，移动速度也更快，也能提升使用技能时恢复的生命值。即使不使用技能，该装备也可提升蛮王的普攻伤害。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0701-Rage-Vial.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-12-12'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Rage_Vial_info.png" :imgAlt="$frontmatter.navTitle" description="使野蛮人之王获得狂暴效果。" />

<SmallTitle>说明</SmallTitle>

1. 狂暴药水瓶是 [野蛮人之王](/upgrade/0200-Barbarian-King) 的两件初始装备之一，另一件是 [野蛮人木偶](/upgrade/0700-Barbarian-Puppet)。
2. 狂暴药水瓶可以使蛮王在技能生效期间伤害提高，移动速度也更快，也能提升使用技能时恢复的生命值。
3. 即使不使用技能，该装备也可提升蛮王的普攻伤害。

注：1. 如果升级费用中有多种资源，则同时需要多种资源才能升级。<br>
4. 上表中 8 点移动速度等于 1 格/秒。<br>
5. 上表中伤害提升 120% 的意思是伤害变为原来的 220%.

在 2023 年 12 月装备系统发布时，已解锁野蛮人之王的玩家会有一个初始的装备等级，并且不需要解锁 [铁匠铺](/upgrade/0488-Blacksmith)。装备等级与玩家的英雄等级相关，具体如下表。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/12/12">
        <TimelineRow>游戏新增装备系统，狂暴药水瓶是第一批推出的装备。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
