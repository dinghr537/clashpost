---
title: "部落冲突 coc 夜世界雷霆皮卡（威能皮卡、超级皮卡）升级数据"
navTitle: "雷霆皮卡"
shownTitle: "雷霆皮卡（威能皮卡、超级皮卡）"
module: upgrade-bh
imgFolder: bh_tech/1009
wiki: https://clashofclans.fandom.com/wiki/Power_P.E.K.K.A
canonical: /upgrade/1009-Power-P.E.K.K.A
dataSyncedOn: 2026-10-13
description: "这件强大的暗黑盔甲不断辐射出不稳定的能量，这些能量随时都可能挣脱盔甲的束缚！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/1009-Power-P.E.K.K.A.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-05-15'">

<template #introduction>

- *如想查看都城的雷霆皮卡（原超级皮卡），请访问：[都城雷霆皮卡](/upgrade/200a-Power-P.E.K.K.A)。*
- *如想查看家乡的皮卡超人，请访问：[皮卡超人](/upgrade/0009-P.E.K.K.A)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Power_P.E.K.K.A_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

\* 能量过载：激活时会造成大爆炸，造成一定伤害。这个技能可以由玩家手动触发，如果手动触发了，死亡时就不会再有爆炸效果。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/05/15">
        <TimelineRow>“超级皮卡”更名为“雷霆皮卡”。</TimelineRow>
        <TimelineRow>新增 19 - 20 级雷霆皮卡。</TimelineRow>
        <TimelineRow>由于夜世界重做，部队的伤害、生命值等数据都有变化。</TimelineRow>
        <TimelineRow>现在雷霆皮卡的“能量过载”技能可以由玩家手动触发了，不过手动触发的话死亡时就没有爆炸效果了。</TimelineRow>
        <TimelineRow>雷霆皮卡的兵种重量由 25 减少到 22。</TimelineRow>
        <TimelineRow>雷霆皮卡的移动速度由 19（2.375 格/秒） 减少到 16（2 格/秒）。</TimelineRow>
        <TimelineRow>现在雷霆皮卡一解锁就是 13 级，你不需要从 1 级开始升了。如果更新前部队高于 13 级，更新后等级不会重置。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/06/18">
        <TimelineRow>夜世界 9 本开放，所有兵种可升至 18 级。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
