---
title: "部落冲突 coc 远袭者升级数据"
navTitle: "远袭者"
shownTitle: "远袭者"
module: upgrade-home
imgFolder: home_th/0840
wiki: https://clashofclans.fandom.com/wiki/Longshot
canonical: /upgrade/0840-Longshot
dataSyncedOn: 2026-10-13
description: "动动脑子！远袭者能从颅骨发射远程爆炸弩箭，让入侵者满满当当地尝到溅射伤害的滋味。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0840-Longshot.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2026-01-12'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Longshot_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

- 远袭者的特殊技能（致命一击）：被击倒后会造成爆炸伤害。
    - 这个爆炸没有与 [巨型炸弹](/upgrade/0383-Giant-Bomb) 类似的击退效果。

警戒半径：（待证实）如果敌军进入这个范围，守卫会看向部队的方向，准备反击。<br>
巡逻半径：（待证实）在没有敌人的情况下，守卫也会走动，而这个走动的范围叫巡逻半径。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2026/01/12">
        <TimelineRow>攻击距离从 12 格减少到 11 格。</TimelineRow>
        <TimelineRow>巡逻半径从 18 格减少到 17 格。</TimelineRow>
        <TimelineRow>警戒半径从 20 格减少到 19 格。</TimelineRow>
        <TimelineRow>普攻伤害半径从 1.5 格减少到 1 格。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/11/17">
        <TimelineRow>推出守卫系统，远袭者是第一批推出的守卫。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
