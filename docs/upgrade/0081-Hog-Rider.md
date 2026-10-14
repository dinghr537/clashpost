---
title: "部落冲突 coc 野猪骑士升级数据"
navTitle: "野猪骑士"
shownTitle: "野猪骑士"
module: upgrade-home
imgFolder: home_tech/0081
wiki: https://clashofclans.fandom.com/wiki/Hog_Rider
canonical: /upgrade/0081-Hog-Rider
dataSyncedOn: 2026-10-13
description: "驯服了狂暴的跳跳猪后，野猪骑士可以直接攻击那些躲在城墙后面的鼠辈了！有暗黑重油的滋养，这些勇士战无不胜！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0081-Hog-Rider.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2026-02-23'">

<template #introduction>

- *如想查看该兵种的强化版本，请访问：[超级野猪骑士](/upgrade/060f-Super-Hog-Rider)。*
- *如想查看夜世界的野猪飞骑，请访问：[夜世界野猪飞骑](/upgrade/100a-Hog-Glider)。*
- *如想查看都城的野猪突袭队，请访问：[都城野猪突袭队](/upgrade/200b-Hog-Raiders)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Hog_Rider_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2026/02/23">
        <TimelineRow>在 18 本新增 15 级野猪骑士。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/11/17">
        <TimelineRow>14 级野猪骑士的升级时间和升级费用减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/10/06">
        <TimelineRow>9 ~ 13 级野猪骑士的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/27">
        <TimelineRow>部队的训练时间取消，但增加了捐赠费用。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>在 17 本新增 14 级野猪骑士。</TimelineRow>
        <TimelineRow>7 ~ 13 级野猪骑士的升级时间减少。</TimelineRow>
        <TimelineRow>10 级野猪骑士的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/02/10">
        <TimelineRow>野猪骑士的训练时间由 0:45 改为 0:42</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>3、4、6、10 ~ 13 级野猪骑士的升级时间减少。</TimelineRow>
        <TimelineRow>2 ~ 13 级野猪骑士的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/18">
        <TimelineRow>6 ~ 9、11 ~ 12 级野猪骑士的升级时间减少。</TimelineRow>
        <TimelineRow>9、11 ~ 12 级野猪骑士的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/03">
        <TimelineRow>7 ~ 10 级野猪骑士的每秒伤害提升。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/02/27">
        <TimelineRow>16 本新增 13 级野猪骑士。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>6 ~ 12 级野猪骑士的升级时间减少。</TimelineRow>
        <TimelineRow>2 ~ 6、11 级野猪骑士的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>15 本新增 12 级野猪骑士。</TimelineRow>
        <TimelineRow>8 ~ 10 级野猪骑士的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>6 ~ 11 级野猪骑士的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/12/09">
        <TimelineRow>2 ~ 6 级野猪骑士的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/09/27">
        <TimelineRow>14 本新增 11 级野猪骑士。</TimelineRow>
        <TimelineRow>3 ~ 5 级野猪骑士的生命值提升。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>2 ~ 5、8 级野猪骑士的升级费用降低。</TimelineRow>
        <TimelineRow>2 ~ 8 级野猪骑士的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/10/12">
        <TimelineRow>2 ~ 8 级野猪骑士的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/03/30">
        <TimelineRow>6 级野猪骑士的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/12/09">
        <TimelineRow>13 本开放，并且新增 10 级野猪骑士。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/09/11">
        <TimelineRow>9 级野猪骑士的生命值由 920 降低至 890。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/04/02">
        <TimelineRow>1 ~ 8 级野猪骑士的升级时间减少。</TimelineRow>
        <TimelineRow>4 ~ 6 级野猪骑士的训练费用降低。</TimelineRow>
        <TimelineRow>新增 9 级野猪骑士，10 级实验室可解锁。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
