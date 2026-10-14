---
title: "部落冲突 coc 夜世界飞龙宝宝升级数据"
navTitle: "飞龙宝宝"
shownTitle: "飞龙宝宝"
module: upgrade-bh
imgFolder: bh_tech/1005
wiki: https://clashofclans.fandom.com/wiki/Baby_Dragon/Builder_Base
canonical: /upgrade/1005-Baby-Dragon
dataSyncedOn: 2026-10-13
description: "飞龙宝宝可爱又温暖，一发脾气就喜欢喷射火焰。没有哪个爱搞破坏的家伙能有它这么可爱。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/1005-Baby-Dragon.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-10-09'">

<template #introduction>

- *如想查看家乡的飞龙宝宝，请访问：[飞龙宝宝](/upgrade/000a-Baby-Dragon)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Baby_Dragon_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

技能描述：火冒三丈：周围没有其他空中部队时，飞龙宝宝的伤害会提升。<br>
技能描述：烈焰喷嚏：飞龙宝宝喷出锥形范围的火焰，对前方的敌人造成伤害。

烈焰喷嚏的额外伤害：2023 年 10 月更新后，烈焰喷嚏造成的额外伤害不再固定。根据与敌人距离的不同，伤害最大可衰减 20%.

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/10/09">
        <TimelineRow>飞龙宝宝的烈焰喷嚏伤害不再固定，根据到目标的距离缩减 0 ~ 20%.</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/05/15">
        <TimelineRow>新增 19 - 20 级飞龙宝宝。</TimelineRow>
        <TimelineRow>由于夜世界重做，部队的伤害、生命值等数据都有变化。</TimelineRow>
        <TimelineRow>飞龙宝宝现在有两个技能了，本次更新在原有“火冒三丈”技能的基础上加了个一次性技能“烈焰喷嚏”。</TimelineRow>
        <TimelineRow>现在飞龙宝宝一解锁就是 5 级，你不需要从 1 级开始升了。如果更新前部队高于 5 级，更新后等级不会重置。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/05/02">
        <TimelineRow>夜世界所有空军的攻击距离减少 0.5 格（蝙蝠除外）。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/06/18">
        <TimelineRow>夜世界 9 本开放，所有兵种可升至 18 级。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
