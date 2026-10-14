---
title: "部落冲突 coc 戈仑冰人升级数据"
navTitle: "戈仑冰人"
shownTitle: "戈仑冰人"
module: upgrade-home
imgFolder: home_tech/0087
wiki: https://clashofclans.fandom.com/wiki/Ice_Golem
canonical: /upgrade/0087-Ice-Golem
dataSyncedOn: 2026-10-13
description: "戈仑冰人个性冷酷而且毫无幽默感。他经过的地方无不冷冻成霜，被消灭时还会冻住四周的事物。聚会时要是有人跟他说话，戈仑冰人会原地冻住。抵御入侵村庄的敌军时，他的冰冻效果范围比进攻时小，持续时间也更短。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0087-Ice-Golem.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-11-17'">

<template #introduction>

- *本页面的内容不是戈仑石人，如想查看戈仑石人的页面，请访问：[戈仑石人](/upgrade/0083-Golem)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Ice_Golem_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

1. 戈仑冰人的普通攻击与 [冰冻法术](/upgrade/0104-Freeze-Spell) 不同，不能把敌方部队和建筑完全冻住，只是有一个减速效果。
2. 戈仑冰人死亡后的冰冻效果与冰冻法术类似，可以把敌方部队和建筑完全冻住。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/11/17">
        <TimelineRow>9 级戈仑冰人的升级时间和升级费用减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/10/06">
        <TimelineRow>2 ~ 8 级戈仑冰人的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/27">
        <TimelineRow>部队的训练时间取消，但增加了捐赠费用。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>在 17 本新增 9 级戈仑冰人。</TimelineRow>
        <TimelineRow>6 ~ 8 级戈仑冰人的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/02/10">
        <TimelineRow>戈仑冰人的训练时间由 2:30 改为 2:10</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>3 ~ 8 级戈仑冰人的升级时间减少。</TimelineRow>
        <TimelineRow>2 ~ 8 级戈仑冰人的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/18">
        <TimelineRow>7 级戈仑冰人的升级时间减少。</TimelineRow>
        <TimelineRow>6 ~ 7 级戈仑冰人的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/04/17">
        <TimelineRow>在 16 本新增 8 级戈仑冰人。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>3 ~ 7 级戈仑冰人的升级时间减少。</TimelineRow>
        <TimelineRow>6 级戈仑冰人的升级费用降低。</TimelineRow>
        <TimelineRow>天使治疗戈仑石人、小戈仑石人、戈仑冰人的几率降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>15 本新增 7 级戈仑冰人。</TimelineRow>
        <TimelineRow>4 ~ 5 级戈仑冰人的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>2 ~ 6 级戈仑冰人的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/12/09">
        <TimelineRow>2 ~ 3 级戈仑冰人的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>14 本推出，并在 14 本新增 6 级戈仑冰人。</TimelineRow>
        <TimelineRow>戈仑冰人的训练时间由 360 秒减少到 300 秒。</TimelineRow>
        <TimelineRow>2 ~ 4 级戈仑冰人的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/03/30">
        <TimelineRow>所有等级戈仑冰人防守状态下死亡后的冰冻时间减少 0.5 秒。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/04/02">
        <TimelineRow>12 级大本营新增 5 级戈仑冰人。</TimelineRow>
        <TimelineRow>在防守时，戈仑冰人死亡后的冰冻时间整体减少。</TimelineRow>
        <TimelineRow>戈仑冰人进攻时的冰冻半径增大 36%.</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
