---
title: "部落冲突 coc 夜世界兵营升级数据"
navTitle: "兵营"
shownTitle: "兵营"
module: upgrade-bh
imgFolder: bh_buildings/1281
wiki: https://clashofclans.fandom.com/wiki/Army_Camp/Builder_Base
canonical: /upgrade/1281-Army-Camp
dataSyncedOn: 2026-10-13
description: "您的部队驻扎在兵营，每个兵营一次只能容纳一种兵。升级某些兵种可以提高兵营容纳该兵种的数量。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/1281-Army-Camp.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-05-15'">

<template #introduction>

- *如想查看夜世界的预备营，请访问：[夜世界预备营](/upgrade/1285-Reinforcement-Camp)。*
- *如想查看家乡的兵营，请访问：[兵营](/upgrade/0480-Army-Camp)。*
- *如想查看都城的兵营，请访问：[都城兵营](/upgrade/2300-Army-Camp)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Army_Camp.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

<SmallTitle>重要说明</SmallTitle>

夜世界的兵营与家乡有些许不同，这里列举一些夜世界兵营的一些独有特性：

1. 在夜世界，每个兵营只能放一种兵，每个兵营可存放的部队数量取决于兵种的种类和等级；
2. 夜世界的兵营不能升级，兵营的建造费用取决于你已有的兵营数量；
3. 匹配对手不需要消耗金币，而且下兵之前可以临时换兵；
4. 夜世界造兵不需要时间，造兵可以瞬间完成。（在 2020 年 3 月 30 日更新之前，填满每个兵营需要的时间固定为 1 分钟）

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/05/15">
        <TimelineRow>5 ~ 6 级兵营的升级费用增加。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
