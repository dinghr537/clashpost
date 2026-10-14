---
title: "部落冲突 coc 飞龙宝宝（小龙）升级数据"
navTitle: "飞龙宝宝"
shownTitle: "飞龙宝宝（小龙）"
module: upgrade-home
imgFolder: home_tech/000a
wiki: https://clashofclans.fandom.com/wiki/Baby_Dragon
canonical: /upgrade/000a-Baby-Dragon
dataSyncedOn: 2026-10-13
description: "会喷火的飞龙宝宝在其他空中部队旁边时显得有些害羞，不过要是落单了，它可会大发雷霆。当周围没有其他空中部队时，飞龙宝宝会变得狂暴，攻击伤害和攻击速度都会提升。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/000a-Baby-Dragon.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2026-02-23'">

<template #introduction>

- *如想查看该兵种的强化版本，请访问：[地狱飞龙](/upgrade/0604-Inferno-Dragon)。*
- *如想查看夜世界的飞龙宝宝，请访问：[夜世界飞龙宝宝](/upgrade/1005-Baby-Dragon)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Baby_Dragon_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

如果飞龙宝宝附近 4.5 格无空军会触发狂暴，狂暴时秒伤为原来的 3 倍，攻速为 0.67 秒/次，即每次伤害为原来的 2 倍。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2026/02/23">
        <TimelineRow>在 18 本新增 12 级飞龙宝宝。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/11/17">
        <TimelineRow>11 级飞龙宝宝的升级时间和升级费用减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/10/06">
        <TimelineRow>5 ~ 10 级飞龙宝宝的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/27">
        <TimelineRow>部队的训练时间取消，但增加了捐赠费用。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>3 ~ 10 级飞龙宝宝的升级时间减少。</TimelineRow>
        <TimelineRow>2 ~ 7、9 ~ 10 级飞龙宝宝的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/02/10">
        <TimelineRow>飞龙宝宝的训练时间由 1:30 改为 1:25</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>17 本推出，并在 17 本新增 11 级飞龙宝宝。</TimelineRow>
        <TimelineRow>2 ~ 10 级飞龙宝宝的升级时间减少。</TimelineRow>
        <TimelineRow>5、8 ~ 10 级飞龙宝宝的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/18">
        <TimelineRow>9 级飞龙宝宝的升级时间减少。</TimelineRow>
        <TimelineRow>9 级飞龙宝宝的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/02/27">
        <TimelineRow>16 本新增 10 级飞龙宝宝。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>4 ~ 9 级飞龙宝宝的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>15 本新增 9 级飞龙宝宝。</TimelineRow>
        <TimelineRow>6 ~ 7 级飞龙宝宝的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>3 ~ 8 级飞龙宝宝的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/05/02">
        <TimelineRow>家乡所有空军的攻击距离减少 0.5 格（超级飞龙除外，这玩意削了 1 格）。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/12/09">
        <TimelineRow>2 ~ 5、7 级飞龙宝宝的升级费用降低。</TimelineRow>
        <TimelineRow>2 ~ 4、7 级飞龙宝宝的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>14 本推出，并在 14 本新增 8 级飞龙宝宝。</TimelineRow>
        <TimelineRow>2 ~ 5 级飞龙宝宝的升级费用降低。</TimelineRow>
        <TimelineRow>2 ~ 3、5 ~ 6 级飞龙宝宝的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/06/22">
        <TimelineRow>13 本新增 7 级飞龙宝宝。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/03/30">
        <TimelineRow>2 ~ 4 级飞龙宝宝的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/04/02">
        <TimelineRow>2 ~ 6 级飞龙宝宝的升级时间减少。</TimelineRow>
        <TimelineRow>所有等级飞龙宝宝的训练费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
