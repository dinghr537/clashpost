---
title: "部落冲突 coc 亡灵（苍蝇）升级数据"
navTitle: "亡灵"
shownTitle: "亡灵（苍蝇）"
module: upgrade-home
imgFolder: home_tech/0080
wiki: https://clashofclans.fandom.com/wiki/Minion
canonical: /upgrade/0080-Minion
dataSyncedOn: 2026-10-13
description: "这些飞行的小家伙诞生于暗黑重油。它们在战场上来去自如，不会被搜空地雷检测到，但是在我们的世界里它们很脆弱。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0080-Minion.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-11-17'">

<template #introduction>

- *如想查看该兵种的强化版本，请访问：[超级亡灵（马云）](/upgrade/0608-Super-Minion)。*
- *如想查看以亡灵为原型的英雄，请访问：[亡灵王子（苍蝇王）](/upgrade/0204-Minion-Prince)。*
- *如想查看夜世界的异变亡灵，请访问：[夜世界异变亡灵](/upgrade/1003-Beta-Minion)。*
- *如想查看都城的亡灵大军，请访问：[都城亡灵大军](/upgrade/2004-Minion-Horde)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Minion_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

注：亡灵不能触发 [搜空地雷](/upgrade/0384-Seeking-Air-Mine)。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/11/17">
        <TimelineRow>18 本推出，并在 18 本新增 14 级亡灵。</TimelineRow>
        <TimelineRow>13 级亡灵的升级时间和升级费用减少。</TimelineRow>
        <TimelineRow>13 级亡灵的每秒伤害和生命值增加。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/10/06">
        <TimelineRow>8 ~ 12 级亡灵的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/27">
        <TimelineRow>部队的训练时间取消，但增加了捐赠费用。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>2 ~ 4、6 ~ 12 级亡灵的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/02/10">
        <TimelineRow>亡灵的训练时间由 0:18 改为 0:16</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>17 本推出，并在 17 本新增 13 级亡灵。</TimelineRow>
        <TimelineRow>3 ~ 12 级亡灵的升级时间减少。</TimelineRow>
        <TimelineRow>2 ~ 12 级亡灵的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/18">
        <TimelineRow>10 ~ 11 级亡灵的升级时间减少。</TimelineRow>
        <TimelineRow>10 ~ 11 级亡灵的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/02/27">
        <TimelineRow>16 本新增 12 级亡灵。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>6 ~ 11 级亡灵的升级时间减少。</TimelineRow>
        <TimelineRow>2 ~ 6、10 级亡灵的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>8 ~ 9 级亡灵的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
    <TimelineRow>15 本推出，并在 15 本新增 11 级亡灵。</TimelineRow>
        <TimelineRow>6 ~ 10 级亡灵的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/05/02">
        <TimelineRow>家乡所有空军的攻击距离减少 0.5 格（超级飞龙除外，这玩意削了 1 格）。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/12/09">
        <TimelineRow>2 ~ 6 级亡灵的升级时间减少。</TimelineRow>
    <TimelineRow>1 ~ 4 级亡灵的伤害增加。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>14 本推出，并在 14 本新增 10 级亡灵。</TimelineRow>
        <TimelineRow>2 ~ 5、8 级亡灵的升级费用降低。</TimelineRow>
        <TimelineRow>2 ~ 7 级亡灵的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/10/12">
        <TimelineRow>2 ~ 7 级亡灵的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/03/30">
        <TimelineRow>6 级亡灵的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/04/02">
        <TimelineRow>所有等级亡灵的升级时间减少。</TimelineRow>
    <TimelineRow>2 ~ 6 级亡灵的训练费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
