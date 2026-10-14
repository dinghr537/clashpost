---
title: "部落冲突 coc 夜世界空中炸弹发射器升级数据"
navTitle: "空中炸弹发射器"
shownTitle: "空中炸弹发射器"
module: upgrade-bh
imgFolder: bh_buildings/1107
wiki: https://clashofclans.fandom.com/wiki/Air_Bombs
canonical: /upgrade/1107-Air-Bombs
dataSyncedOn: 2026-10-13
description: "要应对繁重的空中防御任务，使用空中炸弹发射器准没错。它能持续不断地向空中发射木桶，木桶会在空中爆炸重创敌军！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/1107-Air-Bombs.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-05-15'">

<template #introduction>

- *如想查看都城的空中炸弹发射器，请访问：[都城空中炸弹发射器](/upgrade/2208-Air-Bombs)。*
- *如想查看家乡的陷阱空中炸弹，请访问：[空中炸弹](/upgrade/0382-Air-Bomb)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Air_Bombs10.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/05/15">
        <TimelineRow>夜世界重做，建筑的数值重新平衡，伤害、生命值等数据有变化。</TimelineRow>
        <TimelineRow>5 ~ 9 级空中炸弹发射器的升级时间增加。</TimelineRow>
        <TimelineRow>夜世界 10 本推出，空中炸弹发射器可升至 10 级。</TimelineRow>
        <TimelineRow>为配合更小的地图，空中炸弹发射器的射程由 8 格降低到 7.5 格。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/06/18">
        <TimelineRow>夜世界 9 本推出，空中炸弹发射器可升至 9 级。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
