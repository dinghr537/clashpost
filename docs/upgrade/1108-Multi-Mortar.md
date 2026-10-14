---
title: "部落冲突 coc 夜世界多管迫击炮升级数据"
navTitle: "多管迫击炮"
shownTitle: "多管迫击炮"
module: upgrade-bh
imgFolder: bh_buildings/1108
wiki: https://clashofclans.fandom.com/wiki/Multi_Mortar
canonical: /upgrade/1108-Multi-Mortar
dataSyncedOn: 2026-10-13
description: "远距离发射多枚能造成溅射伤害的炮弹，以保证最大可能命中目标！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/1108-Multi-Mortar.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-05-15'">

<template #introduction>

- *如想查看家乡改装后的迫击炮，请访问该页面后切换为“连发模式”：[迫击炮](/upgrade/0303-Mortar)。*
- *如想查看都城的多管迫击炮，请访问：[都城多管迫击炮](/upgrade/2206-Multi-Mortar)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Multi_Mortar10.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

\* 多管迫击炮的攻击节奏是：4 连发期间每发 0.5 秒，之后停顿 3.5 秒。如果目标在多管还没打完 4 连发之前死亡，导致多管没有发射全部 4 发炮弹时，每发没有射出去的炮弹会减少 0.5 秒攻击间隔。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/05/15">
        <TimelineRow>夜世界重做，建筑的数值重新平衡，伤害、生命值等数据有变化。</TimelineRow>
        <TimelineRow>6 ~ 9 级多管迫击炮的升级时间增加。</TimelineRow>
        <TimelineRow>夜世界 10 本推出，多管迫击炮可升至 10 级。</TimelineRow>
    </TimelineItem>
        <TimelineItem date="2019/12/09">
        <TimelineRow>所有等级多管迫击炮的每秒伤害减少（更新公告里没有这个，但是确实削了）。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/06/18">
        <TimelineRow>夜世界 9 本推出，多管迫击炮可升至 9 级。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
