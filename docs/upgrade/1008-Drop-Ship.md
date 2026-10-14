---
title: "部落冲突 coc 夜世界骷髅气球升级数据"
navTitle: "骷髅气球"
shownTitle: "骷髅气球"
module: upgrade-bh
imgFolder: bh_tech/1008
wiki: https://clashofclans.fandom.com/wiki/Drop_Ship
canonical: /upgrade/1008-Drop-Ship
dataSyncedOn: 2026-10-13
description: "里面挤满的不是炸弹，而是骷髅兵，骷髅兵从气球里直接跳到敌军旁边发动攻击！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/1008-Drop-Ship.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2024-02-27'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Drop_Ship_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

骷髅上限：每个骷髅气球召唤的骷髅最多能有 9 个在场上存在。

技能描述：骷髅轰炸：使用技能时，骷髅气球会朝正下方丢下炸弹，造成范围伤害并对城墙造成额外伤害。此外，爆炸效果还会召唤出骷髅兵进行后续的地面攻击。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2024/02/27">
        <TimelineRow>骷髅气球的攻击距离从 0 格（建筑头顶）修改为 0.5 格。</TimelineRow>
        <TimelineRow>骷髅轰炸技能的爆炸半径从 3 格减少到 2.25 格。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/10/09">
        <TimelineRow>现在骷髅气球优先攻击防御建筑而不是攻击距离最近的建筑。</TimelineRow>
        <TimelineRow>骷髅气球的生命值增加 21%.</TimelineRow>
        <TimelineRow>骷髅气球的技能半径增加 0.5 格（原文就是这个意思，实际上好像没改任何半径/距离相关的属性）。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/05/15">
        <TimelineRow>新增 19 - 20 级骷髅气球。</TimelineRow>
        <TimelineRow>由于夜世界重做，部队的伤害、生命值等数据都有变化。</TimelineRow>
        <TimelineRow>现在骷髅气球多了一个一次性技能“骷髅轰炸”，启用后骷髅气球会朝正下方丢炸弹，并召唤一群骷髅继续战斗。</TimelineRow>
        <TimelineRow>现在骷髅气球一解锁就是 11 级，你不需要从 1 级开始升了。如果更新前部队高于 11 级，更新后等级不会重置。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/05/02">
        <TimelineRow>现在骷髅气球必须走到建筑头顶才能投放骷髅了，不像以前有 0.5 格的间隔。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/06/15">
        <TimelineRow>提升了骷髅气球在 10-11 级和 14-15 级的死亡附加伤害，以修复其特殊技能信息和实际死亡附加伤害不一致的问题。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/06/18">
        <TimelineRow>夜世界 9 本开放，所有兵种可升至 18 级。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
