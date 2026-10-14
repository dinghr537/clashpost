---
title: "部落冲突 coc 攻城钻机升级数据"
navTitle: "攻城钻机"
shownTitle: "攻城钻机"
module: upgrade-home
imgFolder: home_tech/0246
wiki: https://clashofclans.fandom.com/wiki/Battle_Drill
canonical: /upgrade/0246-Battle-Drill
dataSyncedOn: 2026-10-13
description: "攻城钻机完美体现了哥布林的聪明才智。它能够深入地底，钻向距离最近的防御建筑。到达目的地后，它会冒出地面，使用威力十足的钻头瘫痪并摧毁目标。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0246-Battle-Drill.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-11-17'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Battle_Drill_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

1. 和 [掘地矿工](/upgrade/000b-Miner) 类似，部署攻城钻机后，它会在地下行进，避开路线上的一系列防御建筑，之后在目标建筑附近破土而出，直接攻击目标建筑。
2. 攻城钻机从地下出来的一瞬间可以破掉两层墙，也就是说当 [城墙](/upgrade/0300-Walls) 和防御中间隔着一格时可以破墙，隔两格不行。

<Pic src="/upgrade/description/Battle_Drill_Splash.jpg" caption="攻城钻机破墙图示" :lazyLoading="false" width="750" height="435" />

3. 攻城钻机从地下钻出时可以对建筑造成眩晕效果。
4. 当攻城钻机的血量清零时，攻城钻机就会自动解体并释放部落城堡内的部队。
5. 攻城钻机能免疫 [飓风陷阱](/upgrade/0386-Tornado-Trap) 的转圈效果。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/11/17">
        <TimelineRow>5 级攻城钻机的升级时间和升级费用减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/27">
        <TimelineRow>攻城机器的建造时间被取消。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>3 ~ 4 级攻城钻机的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>17 本推出，并在 17 本新增 5 级攻城钻机。</TimelineRow>
        <TimelineRow>2 ~ 4 级攻城钻机的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/18">
        <TimelineRow>2 ~ 4 级攻城钻机的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>3 ~ 4 级攻城钻机的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>15 本推出，并在 15 本新增攻城机器：攻城钻机。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
