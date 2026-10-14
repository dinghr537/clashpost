---
title: "部落冲突 coc 骷髅巨人升级数据"
navTitle: "骷髅巨人"
shownTitle: "骷髅巨人"
module: upgrade-temp
imgFolder: temp_troops/0e03
wiki: https://clashofclans.fandom.com/wiki/Giant_Skeleton
canonical: /upgrade/0e03-Giant-Skeleton
dataSyncedOn: 2026-10-13
description: "骷髅巨人从小就骨骼粗大，他能炸毁的可不只是城墙。被消灭后，他的超大炸弹能对周围的一切造成伤害。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0e03-Giant-Skeleton.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2017-12-28'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Giant_Skeleton_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

\* 理论上来说，1 级大本营可以解锁骷髅巨人，但因为新手教程会引导玩家升级至 2 本，所以实际上 2 本才能训练和使用骷髅巨人。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2022/10">
        <TimelineRow>该兵种第 4 次推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2018/10">
        <TimelineRow>该兵种第 3 次推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2017/12/28">
        <TimelineRow>该兵种第 2 次推出，有效期至 2018/01/03.</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2017/10">
        <TimelineRow>该兵种第 1 次推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
