---
title: "部落冲突 coc 夜世界炸弹兵升级数据"
navTitle: "炸弹兵"
shownTitle: "炸弹兵"
module: upgrade-bh
imgFolder: bh_tech/1004
wiki: https://clashofclans.fandom.com/wiki/Bomber
canonical: /upgrade/1004-Bomber
dataSyncedOn: 2026-10-13
description: "炸弹兵渴望毁灭、追求高质特效，他会炸毁看到的一切东西，对城墙可造成额外伤害！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/1004-Bomber.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-05-15'">

<template #introduction>

- 如想查看家乡的炸弹人，请访问：[炸弹人](/upgrade/0004-Wall-Breaker)。

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Bomber_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

\* 弹跳炸弹：使用技能时，炸弹兵的下一次攻击会弹跳 2 次，产生巨大爆炸并对城墙造成高额伤害。该技能在冷却时间结束后可以重复使用。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/05/15">
        <TimelineRow>新增 19 - 20 级炸弹兵。</TimelineRow>
        <TimelineRow>由于夜世界重做，部队的伤害、生命值等数据都有变化。</TimelineRow>
        <TimelineRow>炸弹兵的技能改为“弹跳炸弹”，启用后炸弹兵的下一次攻击会弹跳两次。</TimelineRow>
        <TimelineRow>炸弹兵的移动速度由 16（2 格/秒） 提升至 19.2（2.4 格/秒）。</TimelineRow>
        <TimelineRow>现在炸弹兵一解锁就是 5 级，你不需要从 1 级开始升了。如果更新前部队高于 5 级，更新后等级不会重置。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/06/22">
        <TimelineRow>炸弹兵的兵种重量从 2 提升至 4。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/06/18">
        <TimelineRow>夜世界 9 本开放，所有兵种可升至 18 级。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
