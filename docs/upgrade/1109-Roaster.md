---
title: "部落冲突 coc 夜世界熔岩火炮升级数据"
navTitle: "熔岩火炮"
shownTitle: "熔岩火炮"
module: upgrade-bh
imgFolder: bh_buildings/1109
wiki: https://clashofclans.fandom.com/wiki/Roaster
canonical: /upgrade/1109-Roaster
dataSyncedOn: 2026-10-13
description: "用滚烫的岩浆给敌军洗个澡！地面部队和空中部队都将会感受到这个灼热！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/1109-Roaster.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-05-15'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Roaster10.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

\* 熔岩火炮的攻击节奏是：0.14 秒一发，15 发之后冷却 1.8 秒。

\# 这里的每秒伤害数据是游戏中显示的近似值，如果熔岩火炮在攻击期间被打断，则实际的每秒伤害就会降低。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/05/15">
        <TimelineRow>夜世界重做，建筑的数值重新平衡，伤害、生命值等数据有变化。</TimelineRow>
        <TimelineRow>所有等级熔岩火炮的升级时间增加。</TimelineRow>
        <TimelineRow>夜世界 10 本推出，熔岩火炮可升至 10 级。</TimelineRow>
    </TimelineItem>
        <TimelineItem date="2019/12/09">
        <TimelineRow>所有等级熔岩火炮的每秒伤害减少（更新公告里没有这个，但是确实削了）。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/06/18">
        <TimelineRow>夜世界 9 本推出，熔岩火炮可升至 9 级。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
