---
title: "部落冲突 coc 都城地狱飞龙升级数据"
navTitle: "地狱飞龙"
shownTitle: "地狱飞龙"
module: upgrade-capital
imgFolder: capital_tech/200e
wiki: https://clashofclans.fandom.com/wiki/Inferno_Dragon/Clan_Capital
canonical: /upgrade/200e-Inferno-Dragon
dataSyncedOn: 2026-10-13
description: "地狱飞龙不会因为落单而狂暴，因为它学会了将怒火转化为一道烈焰射线，而且射线造成的伤害会随着时间递增！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/200e-Inferno-Dragon.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-09-14'">

<template #introduction>

- *如想查看家乡的地狱飞龙，请访问：[地狱飞龙](/upgrade/0604-Inferno-Dragon)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Inferno_Dragon_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

1. 地狱飞龙的解锁条件是建造 [ 地狱飞龙训练营](/upgrade/234e-Inferno-Dragon-Barracks)，而这需要部落解锁骷髅乐园，且 [都城大本营](/upgrade/2400-Capital-Hall) 达到 8 级。
2. 地狱飞龙的技能（地狱烈焰）：持续攻击同一目标时，地狱飞龙的攻击伤害会随着时间递增。初始伤害切换二段伤害需要 1.7 秒，二段到三段需要 1.5 秒。也就是说从初始伤害到最高伤害需要 3.2 秒。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/09/14">
        <TimelineRow>攻击距离增加至 3 格（原为 2.75 格）。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/12/12">
        <TimelineRow>都城新增地狱飞龙，推出 4 个等级。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
