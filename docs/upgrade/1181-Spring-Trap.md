---
title: "部落冲突 coc 夜世界隐形弹簧升级数据"
navTitle: "隐形弹簧"
shownTitle: "隐形弹簧"
module: upgrade-bh
imgFolder: bh_buildings/1181
wiki: https://clashofclans.fandom.com/wiki/Spring_Trap/Builder_Base
canonical: /upgrade/1181-Spring-Trap
dataSyncedOn: 2026-10-13
description: "曾经有一个精妙的弹簧摆在我的面前，我没有看见，然后，就没有然后了！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/1181-Spring-Trap.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-10-06'">

<template #introduction>

- 如想查看家乡的隐形弹簧，请访问：[隐形弹簧](/upgrade/0381-Spring-Trap)。

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Spring_Trap_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

<SmallTitle>重要说明</SmallTitle>

2025/10 更新后，夜世界的隐形弹簧重做，其机制与家乡的隐形弹簧类似，详见家乡的 [隐形弹簧](/upgrade/0381-Spring-Trap)
页面。这里只强调一个不同点，夜世界的隐形弹簧可以弹飞的部队人口数固定为 4，不能随升级改变。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/10/06">
        <TimelineRow>夜世界的隐形弹簧重做，其机制与家乡的隐形弹簧类似。</TimelineRow>
        <TimelineRow>在夜世界 10 本推出 5 级隐形弹簧。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/05/15">
        <TimelineRow>夜世界重做，建筑的数值重新平衡，伤害、生命值等数据有变化。</TimelineRow>
        <TimelineRow>所有等级隐形弹簧可以弹飞的兵种重量降低。</TimelineRow>
        <TimelineRow>3 ~ 4 级隐形弹簧的升级费用增加。</TimelineRow>
        <TimelineRow>所有等级隐形弹簧可以弹飞的兵种重量降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/06/18">
        <TimelineRow>夜世界 9 本推出，9 本新增一个隐形弹簧。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
