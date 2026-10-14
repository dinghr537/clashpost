---
title: "部落冲突 coc 夜世界防空火炮升级数据"
navTitle: "防空火炮"
shownTitle: "防空火炮"
module: upgrade-bh
imgFolder: bh_buildings/1104
wiki: https://clashofclans.fandom.com/wiki/Firecrackers
canonical: /upgrade/1104-Firecrackers
dataSyncedOn: 2026-10-13
description: "发射一连串的小型火箭来驱赶“飞虫”！就像灭虫器一样，但它的造型更加美观。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/1104-Firecrackers.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-05-15'">

<template #introduction>

- *如想查看家乡的防空火箭，请访问：[防空火箭](/upgrade/0304-Air-Defense)。*
- *如想查看都城的防空火箭，请访问：[都城防空火箭](/upgrade/2203-Air-Defense)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Firecrackers10.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

\* 防空火炮的攻击节奏是 0.064 秒一发，4 发后冷却 0.8 秒。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/05/15">
        <TimelineRow>夜世界重做，建筑的数值重新平衡，伤害、生命值等数据有变化。</TimelineRow>
        <TimelineRow>6 ~ 9 级防空火炮的升级时间增加。</TimelineRow>
        <TimelineRow>夜世界 10 本推出，防空火炮可升至 10 级。</TimelineRow>
        <TimelineRow>为配合更小的地图，防空火炮的射程由 10 格降低到 9 格。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/06/18">
        <TimelineRow>夜世界 9 本推出，防空火炮可升至 9 级。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
