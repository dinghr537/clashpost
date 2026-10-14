---
title: "部落冲突 coc 电击车升级数据"
navTitle: "电击车"
shownTitle: "电击车"
module: upgrade-bh
imgFolder: bh_buildings/1241
wiki: https://clashofclans.fandom.com/wiki/Zappy
canonical: /upgrade/1241-Zappy
dataSyncedOn: 2026-10-13
description: "电击车永远充满能量，随时做好防御准备！谁要敢来破坏哨站，它们会立马释放能量发动电击！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/1241-Zappy.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-05-15'">

<template #introduction>

- 如想查看夜世界的另一个大本营，请访问：[建筑大师大本营](/upgrade/1200-Builder-Hall)。
- 如想查看奥仔哨站被摧毁后释放的电击车，请访问：[夜世界电击车](/upgrade/1241-Zappy)。

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Zappy_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

<SmallTitle>重要说明</SmallTitle>

1. 当奥仔哨站被摧毁后，它会释放电击车。
2. 电击车的等级和奥仔哨站的等级同步。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/05/15">
        <TimelineRow>夜世界重做，现在当你升到 6 本后即可直接解锁奥仔哨站，电击车是奥仔哨站的派生单位。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
