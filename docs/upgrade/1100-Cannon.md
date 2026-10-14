---
title: "部落冲突 coc 夜世界加农炮升级数据"
navTitle: "加农炮"
shownTitle: "加农炮"
module: upgrade-bh
imgFolder: bh_buildings/1100
wiki: https://clashofclans.fandom.com/wiki/Cannon/Builder_Base
canonical: /upgrade/1100-Cannon
dataSyncedOn: 2026-10-13
description: "标志性地面防御建筑，经典铸就永恒！这一经典之作让建筑大师不免心生几分感怀。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/1100-Cannon.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-05-15'">

<template #introduction>

- *如想查看夜世界的双管加农炮，请访问：[夜世界双管加农炮](/upgrade/1101-Double-Cannon)。*
- *如想查看夜世界的巨型加农炮，请访问：[夜世界巨型加农炮](/upgrade/110a-Giant-Cannon)。*
- *如想查看家乡的加农炮，请访问：[加农炮](/upgrade/0301-Cannon)。*
- *如想查看都城的加农炮，请访问：[都城加农炮](/upgrade/2201-Cannon)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Cannon10.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/05/15">
        <TimelineRow>夜世界重做，建筑的数值重新平衡，伤害、生命值等数据有变化。</TimelineRow>
        <TimelineRow>6 ~ 9 级加农炮的升级时间增加。</TimelineRow>
        <TimelineRow>夜世界 10 本推出，加农炮可升至 10 级。</TimelineRow>
        <TimelineRow>为配合更小的地图，加农炮的射程由 9 格降低到 8.5 格。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/06/18">
        <TimelineRow>夜世界 9 本推出，加农炮可升至 9 级。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
