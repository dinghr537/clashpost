---
title: "部落冲突 coc 夜世界撼地巨石升级数据"
navTitle: "撼地巨石"
shownTitle: "撼地巨石"
module: upgrade-bh
imgFolder: bh_buildings/1105
wiki: https://clashofclans.fandom.com/wiki/Crusher
canonical: /upgrade/1105-Crusher
dataSyncedOn: 2026-10-13
description: "撼地巨石非常在意自己的私人空间。这块巨石会凶狠地砸向入侵的地面部队，将他们碾压！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/1105-Crusher.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-05-15'">

<template #introduction>

- *如想查看都城的撼地巨石，请访问：[都城撼地巨石](/upgrade/220a-Crusher)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Crusher10.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

\* 不同于的其他范围溅射伤害，撼地巨石的溅射中心就在巨石中心，而其他的范围溅射伤害中心以弹药为中心。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/05/15">
        <TimelineRow>夜世界重做，建筑的数值重新平衡，伤害、生命值等数据有变化。</TimelineRow>
        <TimelineRow>6 ~ 9 级撼地巨石的升级时间增加。</TimelineRow>
        <TimelineRow>夜世界 10 本推出，撼地巨石可升至 10 级。</TimelineRow>
    </TimelineItem>
        <TimelineItem date="2020/06/22">
        <TimelineRow>撼地巨石的溅射半径从 3.5 格缩小至 2.8 格，现在它不再那么容易对范围外的单位造成伤害。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/06/18">
        <TimelineRow>夜世界 9 本推出，撼地巨石可升至 9 级。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
