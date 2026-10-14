---
title: "部落冲突 coc 夜世界建筑大师训练营升级数据"
navTitle: "建筑大师训练营"
shownTitle: "建筑大师训练营"
module: upgrade-bh
imgFolder: bh_buildings/1280
wiki: https://clashofclans.fandom.com/wiki/Builder_Barracks
canonical: /upgrade/1280-Builder-Barracks
dataSyncedOn: 2026-10-13
description: "建筑大师训练营为建筑大师基地战斗训练部队！您还可以在发动进攻前快速更换部队。升级建筑大师训练营以解锁更多兵种！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/1280-Builder-Barracks.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-05-15'">

<template #introduction>

- *如想查看家乡的训练营，请访问：[训练营](/upgrade/0481-Barracks)。*
- *都城的训练营比较多，这里就不放链接了，如有需求请自行前往相关页面查看。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Builder_Barracks12.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

<SmallTitle>重要说明</SmallTitle>

夜世界的训练营与家乡有些许不同，这里列举一些夜世界训练营的一些独有特性：
1. 在夜世界，训练部队不需要消耗圣水；
2. 在你用掉兵营中的部队后，训练营可以自动训练你上次使用的配置。
3. 夜世界造兵不需要时间，造兵可以瞬间完成。（在 2020 年 3 月 30 日更新之前，填满每个兵营需要的时间固定为 1 分钟）

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/05/15">
        <TimelineRow>夜世界重做，建筑的数值重新平衡，伤害、生命值等数据有变化。</TimelineRow>
        <TimelineRow>7 ~ 11 级建筑大师训练营的升级费用增加。</TimelineRow>
        <TimelineRow>夜世界 10 本推出，建筑大师训练营可升至 12 级，新增兵种: 电火法师。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/10/16">
        <TimelineRow>夜世界造兵不需要时间了，造兵可以瞬间完成。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/06/18">
        <TimelineRow>夜世界 9 本推出，建筑大师训练营可升至 11 级，新增兵种野猪飞骑。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
