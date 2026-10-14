---
title: "部落冲突 coc 闪枭（鸟）升级数据"
navTitle: "闪枭"
shownTitle: "闪枭（鸟）"
module: upgrade-home
imgFolder: home_heroes/0281
wiki: https://clashofclans.fandom.com/wiki/Electro_Owl
canonical: /upgrade/0281-Electro-Owl
dataSyncedOn: 2026-10-13
description: "闪枭可以从相当远的距离发动电击，重创敌军！但它几乎全身都是羽毛，要好好保护它哦！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0281-Electro-Owl.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-10-06'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Electro_Owl_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

1. 闪枭的技能（电击高手）：闪枭的电击会弹射到附近的另一个目标。
2. 闪枭攻击目标时，闪电可以往附近的目标弹射一次，弹射规律跟 [雷龙](/upgrade/000c-Electro-Dragon) 一样，只不过闪枭只能弹一次。如想了解闪枭的闪电弹射规律，请参考：闪电传递大揭秘——雷龙、闪枭、超法的闪电链机制讲解{target="_blank"}。
3. 如果主人被召回或者阵亡，闪枭会变成一个自由单位，此时没有偏好。
4. 闪枭自身不触发陷阱，但其他部队触发的陷阱可能会误伤到它。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/10/06">
        <TimelineRow>8 级闪枭的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>2 ~ 14 级闪枭的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>2 ~ 11 级闪枭的升级时间减少。</TimelineRow>
        <TimelineRow>2 ~ 15 级闪枭的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/02/27">
        <TimelineRow>16 本新增 11 ~ 15 级闪枭。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>4 ~ 10 级闪枭的升级时间减少。</TimelineRow>
        <TimelineRow>2 ~ 15 级闪枭的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/05/02">
        <TimelineRow>家乡所有空军的攻击距离减少 0.5 格（超级飞龙除外，这玩意削了 1 格）。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>部落冲突推出战宠，其中莱希、闪枭、大牦、独角是第一批推出的。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
