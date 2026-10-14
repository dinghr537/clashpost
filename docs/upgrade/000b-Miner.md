---
title: "部落冲突 coc 掘地矿工升级数据"
navTitle: "掘地矿工"
shownTitle: "掘地矿工"
module: upgrade-home
imgFolder: home_tech/000b
wiki: https://clashofclans.fandom.com/wiki/Miner
canonical: /upgrade/000b-Miner
dataSyncedOn: 2026-10-13
description: "聪明的掘地矿工可穿行于地底，钻过城墙，在攻击目标旁破土而出。他们在地底时不会受到任何伤害并且不会触发陷阱，不过即便在地下他们也能受到法术的增益效果。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/000b-Miner.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-11-17'">

<template #introduction>

- *如想查看该兵种的强化版本，请访问：[超级矿工](/upgrade/060e-Super-Miner)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Miner_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

1. 掘地矿工在地底下不会受到伤害，但是依然可以受到法术的增益效果。
2. 掘地矿工击败目标后，需要 1 到 1.25 秒才会再次钻地。这个延时依然能够躲避 12 到 16 级 [大本营](/upgrade/0400-Town-Hall) 的爆炸伤害，但不能躲避 [炸弹塔](/upgrade/0308-Bomb-Tower) 被摧毁后的爆炸伤害。
3. 13 到 16 级 [大本营](/upgrade/0400-Town-Hall) 自爆后的毒雾伤害对处于地底的掘地矿工无效。
4. 掘地矿工能免疫 [飓风陷阱](/upgrade/0386-Tornado-Trap) 的转圈效果。
5. 掘地矿工在防守时不会钻地。
6. 掘地矿工仅在移动时会钻地，攻击时不会钻地，因此归类为地面近战单位。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/11/17">
        <TimelineRow>18 本推出，并在 18 本新增 12 级掘地矿工。</TimelineRow>
        <TimelineRow>11 级掘地矿工的升级时间和升级费用减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/10/06">
        <TimelineRow>4 ~ 10 级掘地矿工的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/06/30">
        <TimelineRow>8 ~ 11 级掘地矿工的生命值增加。</TimelineRow>
        <TimelineRow>10 ~ 11 级掘地矿工的每秒伤害提升。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/27">
        <TimelineRow>部队的训练时间取消，但增加了捐赠费用。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>4 ~ 10 级掘地矿工的升级时间减少。</TimelineRow>
        <TimelineRow>2 ~ 4、6 ~ 10 级掘地矿工的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/02/10">
        <TimelineRow>17 本新增 11 级掘地矿工。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>2 ~ 10 级掘地矿工的升级时间减少。</TimelineRow>
        <TimelineRow>5 ~ 10 级掘地矿工的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/18">
        <TimelineRow>6、8、9 级掘地矿工的升级时间减少。</TimelineRow>
        <TimelineRow>8、9 级掘地矿工的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>16 本推出，同时在 16 本新增 10 级掘地矿工。</TimelineRow>
        <TimelineRow>2 ~ 3、5 ~ 9 级掘地矿工的升级时间减少。</TimelineRow>
        <TimelineRow>8 级掘地矿工的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>6 ~ 7 级掘地矿工的升级费用和升级时间减少。</TimelineRow>
    <TimelineRow>9 级掘地矿工的生命值由 1200 提升到 1250。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/12/12">
        <TimelineRow>地下单位于地面上行走（不包含进攻半身冒出地面）的移动速度降低 30%，会影响防守时的掘地矿工和参观村庄时在兵营等地方看到的地下单位。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>2 ~ 8 级掘地矿工的升级费用和升级时间减少。</TimelineRow>
        <TimelineRow>15 本推出，并在 15 本新增 9 级掘地矿工。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/12/09">
        <TimelineRow>2 ~ 7 级掘地矿工的升级费用降低。</TimelineRow>
        <TimelineRow>2 ~ 6 级掘地矿工的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/09/27">
        <TimelineRow>14 本新增 8 级掘地矿工。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>2 ~ 5 级掘地矿工的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/03/30">
        <TimelineRow>2 ~ 3 级掘地矿工的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/12/09">
        <TimelineRow>13 本新增 7 级掘地矿工。</TimelineRow>
        <TimelineRow>6 级掘地矿工的生命值由 870 增加到 900。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
