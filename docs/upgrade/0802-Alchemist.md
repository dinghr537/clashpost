---
title: "部落冲突 coc 炼金术士升级数据"
navTitle: "炼金术士"
shownTitle: "炼金术士"
module: upgrade-home
imgFolder: home_tech/0802
wiki: https://clashofclans.fandom.com/wiki/Alchemist
canonical: /upgrade/0802-Alchemist
dataSyncedOn: 2026-10-13
description: "炼金术士可以将资源转换为不同类型！她每天工作一次，升级炼金术士可提高她的工作效率！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0802-Alchemist.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-02-10'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Alchemist_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

1. 炼金术士在家乡 [大本营](/upgrade/0400-Town-Hall) 达到 11 级后可以解锁。
2. 解锁后，炼金术士可以立即将该仓库的一部分资源转化为另一种资源。
    - 炼金术士的转化是立即完成的，游戏内播放的一小时动画并没有实际作用。
    - 炼金术士的冷却时间为 23 小时。
3. 转化后的资源最多为满库，游戏没给你溢出的选项。
4. 在下方的升级数据表中，转化率 101% 的意思是可以将 150 万金币转化为 151.5 万圣水或 1.01 万黑油。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/02/10">
        <TimelineRow>新角色：炼金术士，11 本可解锁。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
