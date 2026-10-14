---
title: "部落冲突 coc 亡灵王子（苍蝇王、大苍蝇）升级数据"
navTitle: "亡灵王子"
shownTitle: "亡灵王子（苍蝇王、大苍蝇）"
module: upgrade-home
imgFolder: home_heroes/0204
wiki: https://clashofclans.fandom.com/wiki/Minion_Prince
canonical: /upgrade/0204-Minion-Prince
dataSyncedOn: 2026-10-13
description: "这个自称暗黑王子的家伙是个狠角色！亡灵王子会在空中发射暗黑粘液，对防御建筑和部队造成伤害！防守时，他会在自己的英雄战旗附近盘旋。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0204-Minion-Prince.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2026-02-23'">

<template #introduction>

- *如想查看亡灵王子的创作原型，请访问：[亡灵](/upgrade/0080-Minion)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Minion_Prince_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

1. 下方的数据均为不含装备的数据。
2. 英雄在防守时没有装备。

搜索半径：如果敌军进入这个范围，英雄会奔向敌军，并进行反击。<br>
巡逻半径：在没有敌人的情况下，英雄也会走动，而这个走动的范围叫巡逻半径。

下表中的生命值恢复量是基础属性，与装备无关。即使没有装备，开技能也会回血。

如果你在 2024 年 11 月更新前已经拥有英雄，那么官方会根据你更新时的英雄等级送你相应等级英雄殿堂和亡灵王子，无需从头开始升级。如果更新时你的英雄尚未升级完成，那么官方会帮你直接秒掉这一级英雄。

数据表格见 [英雄殿堂](/upgrade/0489-Hero-Hall) 页面，这里不再重复列出。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2026/02/23">
        <TimelineRow>36 ~ 75 级亡灵王子的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/11/17">
        <TimelineRow>18 本推出，并在 18 本新增 91 ~ 95 级亡灵王子。</TimelineRow>
        <TimelineRow>1 ~ 90 级亡灵王子的生命值减少 1000，但所有装备提供 500 生命值加成。也就是说亡灵王子的进攻强度不变，防守强度降低了。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/10/06">
        <TimelineRow>26 ~ 80 级亡灵王子的升级时间减少。</TimelineRow>
        <TimelineRow>31 ~ 74 级亡灵王子的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/27">
        <TimelineRow>取消英雄的恢复时间，现在英雄可以像战宠一样瞬间恢复。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>在 9 本推出新英雄：亡灵王子。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
