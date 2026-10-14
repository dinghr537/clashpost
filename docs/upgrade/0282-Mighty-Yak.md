---
title: "部落冲突 coc 大牦（牛）升级数据"
navTitle: "大牦"
shownTitle: "大牦（牛）"
module: upgrade-home
imgFolder: home_heroes/0282
wiki: https://clashofclans.fandom.com/wiki/Mighty_Yak
canonical: /upgrade/0282-Mighty-Yak
dataSyncedOn: 2026-10-13
description: "大牦像攻城机器一样坚实，有着不撞倒城墙不罢休的毅力。大牦会在跟随的英雄被击倒时陷入狂怒。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0282-Mighty-Yak.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-03-24'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Mighty_Yak_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

1. 大牦的技能（破墙专家）：大牦可对 [城墙](/upgrade/0300-Walls) 造成额外伤害。
2. 如果主人被召回或者阵亡，大牦会变成一个自由单位，此时没有偏好。
3. 主人阵亡时，大牦会获得几秒的狂暴效果。如果狂暴期间被 [回溯法术](/upgrade/0107-Recall-Spell) 召回，狂暴效果不会暂停。
4. 大牦是所有战宠中唯一不能跳墙的，不过凭借其对墙的 20 倍伤害加成，一般的城墙不能对大牦的路线造成太大的影响。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/03/24">
        <TimelineRow>2 ~ 15 级大牦的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>2 ~ 15 级大牦的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/18">
        <TimelineRow>2 ~ 13 级大牦的升级时间减少。</TimelineRow>
        <TimelineRow>2 ~ 15 级大牦的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>4 ~ 10 级大牦的升级时间减少。</TimelineRow>
        <TimelineRow>2 ~ 15 级大牦的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>15 本新增 11 ~ 15 级大牦。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/09/27">
        <TimelineRow>移除了大牦攻击时的溅射伤害。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>部落冲突推出战宠，其中莱希、闪枭、大牦、独角是第一批推出的。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
