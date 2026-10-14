---
title: "部落冲突 coc 夜世界巨型地雷升级数据"
navTitle: "巨型地雷"
shownTitle: "巨型地雷"
module: upgrade-bh
imgFolder: bh_buildings/1183
wiki: https://clashofclans.fandom.com/wiki/Mega_Mine
canonical: /upgrade/1183-Mega-Mine
dataSyncedOn: 2026-10-13
description: "一个隐藏的强力爆炸陷阱。可选择对地或对空！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/1183-Mega-Mine.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-10-20'">

<template #introduction>

- 如想查看夜世界的地雷，请访问：[夜世界地雷](/upgrade/1182-Mine)。
- 如想查看都城的巨型地雷，请访问：[都城巨型地雷](/upgrade/2281-Mega-Mine)。

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Mega_Mine10.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/10/20">
        <TimelineRow>3 ~ 10 级巨型地雷的爆炸伤害降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/05/15">
        <TimelineRow>夜世界重做，建筑的数值重新平衡，伤害、生命值等数据有变化。</TimelineRow>
        <TimelineRow>所有等级巨型地雷的爆炸伤害增加。</TimelineRow>
        <TimelineRow>所有等级巨型地雷的升级费用增加。</TimelineRow>
        <TimelineRow>触发巨型地雷的最低兵种重量调整为 3，这意味着骷髅兵不能触发巨型地雷了。</TimelineRow>
        <TimelineRow>夜世界 10 本推出，巨型地雷可升至 10 级。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/06/18">
        <TimelineRow>夜世界 9 本推出，巨型地雷可升至 9 级。</TimelineRow>
        <TimelineRow>9 本新增一个巨型地雷。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
