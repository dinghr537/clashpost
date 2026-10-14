---
title: "部落冲突 coc 都城高山戈仑升级数据"
navTitle: "高山戈仑"
shownTitle: "高山戈仑"
module: upgrade-capital
imgFolder: capital_tech/200d
wiki: https://clashofclans.fandom.com/wiki/Mountain_Golem
canonical: /upgrade/200d-Mountain-Golem
dataSyncedOn: 2026-10-13
description: "这座高山可能移动起来慢得像蜗牛，但不要小瞧了它那矿化之后的石手。高山戈仑能轻松碾压敌人，这就是......呃......高山的力量，就这么简单。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/200d-Mountain-Golem.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-09-14'">

<template #introduction>

- *如想查看家乡的戈仑石人，请访问：[戈仑石人](/upgrade/0083-Golem)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Mountain_Golem_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

1. 高山戈仑的解锁条件是建造 [ 高山戈仑石场](/upgrade/234d-Mountain-Golem-Quarry)，而这需要部落解锁戈仑石厂，且 [都城大本营](/upgrade/2400-Capital-Hall) 达到 7 级。
2. 高山戈仑可以越过宽度 2 格以内的河流。
3. 高山戈仑的技能（一碰就倒）：轻轻一碰就可以推倒城墙。另外，高山戈仑无法通过弹跳法术获得跳墙能力（直接推倒了还需要跳吗）。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/09/14">
        <TimelineRow>高山戈仑的移动速度从每秒 0.6 格增加到每秒 0.8 格，游戏内显示是从 4 到 6.</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>移除高山戈仑选择目标时的随机性。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/06/30">
        <TimelineRow>伤害半径从 0.75 增加到 0.9 格。</TimelineRow>
        <TimelineRow>1 ~ 4 级高山戈仑的生命值由 2.8万/3.2万/3.6万/4万 增加到 3万/3.35万/3.7万/4.05万。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/05/02">
        <TimelineRow>高山戈仑随着部落都城玩法一同推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
