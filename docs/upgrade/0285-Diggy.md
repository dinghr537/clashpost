---
title: "部落冲突 coc 地兽（挖挖）升级数据"
navTitle: "地兽"
shownTitle: "地兽（挖挖）"
module: upgrade-home
imgFolder: home_heroes/0285
wiki: https://clashofclans.fandom.com/wiki/Diggy
canonical: /upgrade/0285-Diggy
dataSyncedOn: 2026-10-13
description: "地兽生性腼腆，大部分时候都躲在地下。但在战斗中，它还是会做好自己分内的事：破土而出攻击建筑，助英雄一臂之力。地兽跟随的英雄被击倒后，它会寻找另一位英雄为其提供帮助。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0285-Diggy.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-10-06'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Diggy_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

1. 地兽的技能（地下惊喜）：虽然大部分时间都躲在地底，但地兽也会钻出地面瘫痪并摧毁敌方防御建筑。
2. 地兽不仅可以瘫痪防御建筑，还可以瘫痪部队和英雄了。
3. 只有当前主人阵亡时，地兽才会变更主人。跟随新主人的机制与跟随原主人的机制相同。如果没有找到新主人，地兽也会变成独立单位。
4. 如果地兽当前主人或新主人被召回，地兽会认为主人并未阵亡，因此不寻找新主人，而是暂时变成自由单位。
5. 当主人阵亡时，地兽会寻找场上最近的英雄作为新主人。地兽并不能看见被召回的英雄。
6. 在地兽没有主人时，正常部署或使用 [回溯法术](/upgrade/0107-Recall-Spell) 部署一个英雄，地兽会立即以该英雄作为新主人。
7. 地兽能免疫 [飓风陷阱](/upgrade/0386-Tornado-Trap) 的转圈效果。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/10/06">
        <TimelineRow>8 级地兽的升级费用降低。</TimelineRow>
        <TimelineRow>现在地兽不仅可以瘫痪防御建筑，还可以瘫痪部队和英雄了（更新前只能瘫痪防御建筑）。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>2 ~ 10 级地兽的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>2 ~ 10 级地兽的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>2 ~ 10 级地兽的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>15 本推出，可解锁四个新宠物，地兽是其中之一。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
