---
title: "部落冲突 coc 训练营升级数据"
navTitle: "训练营"
shownTitle: "训练营"
module: upgrade-home
imgFolder: home_buildings/0481
wiki: https://clashofclans.fandom.com/wiki/Barracks
canonical: /upgrade/0481-Barracks
dataSyncedOn: 2026-10-13
description: "在训练营训练部队助您征战。升级训练营可解锁更高级的兵种，助您在史诗般的战斗中赢得胜利。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0481-Barracks.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-11-17'">

<template #introduction>

- *如想查看训练黑水兵的训练营，请访问：[暗黑训练营](/upgrade/0482-Dark-Barracks)。*
- *如想查看夜世界的建筑大师训练营，请访问：[夜世界建筑大师训练营](/upgrade/1280-Builder-Barracks)。*
- *都城的训练营比较多，这里就不放链接了，如有需求请自行前往相关页面查看。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Barracks19_hd.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

\# 根据安装包解析的结果，玩家可以在 1 本把训练营升到 3 级，但这仅仅是理论上的，实际上新手教程会直接引导玩家升到 2 本，根本没有在 1 本升级训练营的机会。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/11/17">
        <TimelineRow>17 本新增 19 级训练营。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/10/06">
        <TimelineRow>14 ~ 18 级训练营的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/06/16">
        <TimelineRow>1 ~ 8 级训练营的生命值减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>2 ~ 3、5 ~ 13、17 ~ 18 级训练营的升级时间减少。</TimelineRow>
        <TimelineRow>8、13、15、18 级训练营的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/02/10">
        <TimelineRow>2 ~ 4 级训练营的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>17 本推出，并在 16 本新增 18 级训练营。</TimelineRow>
        <TimelineRow>5、11 ~ 17 级训练营的升级时间减少。</TimelineRow>
        <TimelineRow>14、17 级训练营的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/18">
        <TimelineRow>16 ~ 17 级训练营的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>16 本推出，并在 15 本新增 17 级训练营。</TimelineRow>
        <TimelineRow>15 ~ 16 级训练营的升级时间减少。</TimelineRow>
        <TimelineRow>9 ~ 10 级训练营的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>14 ~ 15 级训练营的升级费用和时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>15 本推出，并在 14 本新增 16 级训练营，可解锁新兵种：雷霆泰坦。</TimelineRow>
        <TimelineRow>四个训练营合并为一个，更新后的兵种训练时间等同于更新前四个训练营的训练时间。</TimelineRow>
        <TimelineRow>训练营升级时兵种可继续训练部队，但训练速度减半（训练时间翻倍）。</TimelineRow>
        <TimelineRow>5 ~ 15 级训练营的升级费用和升级时间增加。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/12/09">
        <TimelineRow>6 ~ 12 级训练营的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/06/15">
        <TimelineRow>13 本新增 15 级训练营，新兵种：龙骑士。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>1 ~ 2、11 ~ 12 级训练营的升级费用降低。</TimelineRow>
        <TimelineRow>3、10 ~ 13 级训练营的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/12/09">
        <TimelineRow>13 本推出，并在 13 本新增 14 级训练营，可解锁新兵种：大雪怪。</TimelineRow>
    </TimelineItem>
        <TimelineItem date="2019/04/02">
        <TimelineRow>2 ~ 13 级训练营的升级时间减少。</TimelineRow>
        <TimelineRow>9 ~ 12 级训练营的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
