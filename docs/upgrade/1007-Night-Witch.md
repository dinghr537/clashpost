---
title: "部落冲突 coc 夜世界暗夜女巫升级数据"
navTitle: "暗夜女巫"
shownTitle: "暗夜女巫"
module: upgrade-bh
imgFolder: bh_tech/1007
wiki: https://clashofclans.fandom.com/wiki/Night_Witch
canonical: /upgrade/1007-Night-Witch
dataSyncedOn: 2026-10-13
description: "从容地召唤出成群的飞行生物，和她的妹妹不同，她可不会破坏草皮。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/1007-Night-Witch.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2024-02-27'">

<template #introduction>

- *如想查看家乡的女巫，请访问：[女巫](/upgrade/0084-Witch)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Night_Witch_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

每次召唤数量：暗夜女巫并不是每次都会召唤 3 到 4 个蝙蝠，当一只暗夜女巫召唤的蝙蝠达到上表的限制时，除非蝙蝠死亡，否则不会继续召唤。这个上限指的是每只暗夜女巫召唤的蝙蝠，如果有两只暗夜女巫，那么场上的最大蝙蝠数量为 2 倍上限。<br>
开启技能后的召唤数量：开启技能后暗夜女巫会额外召唤一批蝙蝠，注意是额外召唤的，不受上限影响。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2024/02/27">
        <TimelineRow>所有等级暗夜女巫的生命值增加。</TimelineRow>
        <TimelineRow>所有等级暗夜女巫开启技能后召唤出的蝙蝠数量增加。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/10/20">
        <TimelineRow>暗夜女巫的生命值增加 6%.</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/10/09">
        <TimelineRow>暗夜女巫的生命值增加 11%.</TimelineRow>
        <TimelineRow>暗夜女巫召唤蝙蝠的冷却时间减少 0.8 秒。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/05/15">
        <TimelineRow>新增 19 - 20 级暗夜女巫。</TimelineRow>
        <TimelineRow>由于夜世界重做，部队的伤害、生命值等数据都有变化。</TimelineRow>
        <TimelineRow>现在暗夜女巫多了个一次性技能“蝙蝠召唤”，可以额外召唤一群蝙蝠，以前的召唤功能还在。</TimelineRow>
        <TimelineRow>暗夜女巫的兵种重量从 12 提升至 14。</TimelineRow>
        <TimelineRow>现在暗夜女巫一解锁就是 9 级，你不需要从 1 级开始升了。如果更新前部队高于 9 级，更新后等级不会重置。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/06/18">
        <TimelineRow>夜世界 9 本开放，所有兵种可升至 18 级。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
