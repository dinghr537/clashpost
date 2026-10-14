---
title: "部落冲突 coc 火焰喷射器升级数据"
navTitle: "火焰喷射器"
shownTitle: "火焰喷射器"
module: upgrade-home
imgFolder: home_buildings/0316
wiki: https://clashofclans.fandom.com/wiki/Firespitter
canonical: /upgrade/0316-Firespitter
dataSyncedOn: 2026-10-13
description: "火焰喷射器喷射火焰的速度比 X 连弩的攻速还要快！即使打歪了，火焰喷射器的攻击也会越过目标，对后方的敌人造成伤害。它只能朝向一个方向，所以要仔细考虑如何放置它！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0316-Firespitter.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2026-02-23'">

<template #introduction>

- 如想查看夜世界的一座机制类似的建筑，请访问：[夜世界熔岩火炮](/upgrade/1109-Roaster)。

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Firespitter3.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

<SmallTitle>重要说明</SmallTitle>

1. 火焰喷射器的攻击方式是先以极快的速度打出 20 发子弹（熔化的铁球），休息 1 秒后再发起下一轮攻击，其机制类似于夜世界的 [熔岩火炮](/upgrade/1109-Roaster)。
2. 每发子弹可以击中两个目标。
    - 火焰喷射器的子弹可以同时击中地面和空中目标，不像 [投石炮](/upgrade/030e-Scattershot) 一样，瞄准地面就无法溅射到空中。
    - 火焰喷射器的子弹击中两个目标后就会自动消失。
3. 火焰喷射器的射击有一定的偏移角度，精度不是很高，如果目标较远则有可能打不中。
4. 火焰喷射器只能覆盖约 150° 的扇形区域。
5. 和 [空气炮](/upgrade/0306-Air-Sweeper) 一样，你可以旋转火焰喷射器，使其朝向你想要的方向。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2026/02/23">
        <TimelineRow>在 18 本添加了 3 级火焰喷射器</TimelineRow>
        <TimelineRow>移除了火焰喷射器的充能等级。</TimelineRow>
        <TimelineRow>更改了 1 ~ 2 级火焰喷射器在游戏面板中显示的伤害值（实际伤害没变，只是更改了显示算法）。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/11/17">
        <TimelineRow>1 ~ 2 级及两个充能等级的火焰喷射器的升级时间和升级费用减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>17 本推出，并在 17 本新增火焰喷射器。</TimelineRow>
        <TimelineRow>火焰喷射器在刚推出的时候就支持充能，属于第二批可以充能的建筑。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
