---
title: "部落冲突 coc 夜世界双管加农炮升级数据"
navTitle: "双管加农炮"
shownTitle: "双管加农炮"
module: upgrade-bh
imgFolder: bh_buildings/1101
wiki: https://clashofclans.fandom.com/wiki/Double_Cannon
canonical: /upgrade/1101-Double-Cannon
dataSyncedOn: 2026-10-13
description: "双管加农炮，每管二连发。四倍炮弹，四倍火力！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/1101-Double-Cannon.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-05-15'">

<template #introduction>

- *如想查看夜世界的加农炮，请访问：[夜世界加农炮](/upgrade/1100-Cannon)。*
- *如想查看夜世界的巨型加农炮，请访问：[夜世界巨型加农炮](/upgrade/110a-Giant-Cannon)。*
- *如想查看家乡改装后的加农炮，请访问该页面后切换为“连发模式”：[加农炮](/upgrade/0301-Cannon)。*
- *如想查看都城的多管加农炮，请访问：[都城多管加农炮](/upgrade/2204-Multi-Cannon)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Double_Cannon10.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

\* 双管加农炮的攻击节奏是 0.192 秒一发，4 发后冷却 1.6 秒。

\# 这里的每秒伤害数据是游戏中显示的近似值，如果双管加农炮在攻击期间被打断，则实际的每秒伤害就会降低。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/05/15">
        <TimelineRow>夜世界重做，建筑的数值重新平衡，伤害、生命值等数据有变化。</TimelineRow>
        <TimelineRow>6 ~ 9 级双管加农炮的升级时间增加。</TimelineRow>
        <TimelineRow>夜世界 10 本推出，双管加农炮可升至 10 级。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/06/18">
        <TimelineRow>夜世界 9 本推出，双管加农炮可升至 9 级。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
