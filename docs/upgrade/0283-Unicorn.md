---
title: "部落冲突 coc 独角（马）升级数据"
navTitle: "独角"
shownTitle: "独角（马）"
module: upgrade-home
imgFolder: home_heroes/0283
wiki: https://clashofclans.fandom.com/wiki/Unicorn
canonical: /upgrade/0283-Unicorn
dataSyncedOn: 2026-10-13
description: "独角不轻易相信他人，但它绝对值得您付出爱心和耐心与它建立信任，因为它会像天使一样治愈所有伤痛！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0283-Unicorn.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-10-06'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Unicorn_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

1. 独角的技能（专属天使）：独角会跟随搭档英雄并提供治疗。
2. 独角是主人的专属天使，只要主人在场，独角的治疗目标永远都是主人。如果主人被召回或者阵亡，独角会像天使那样去辅助其他部队。主人被重新部署后，独角会立即调头回来找主人。
3. 天使不会主动帮独角补血，但当天使的奶溅射到独角时它是可以回血的。
4. 独角可以给空中部队补血，如空中模式的 [大守护者](/upgrade/0202-Grand-Warden)，但天使不行。
5. 当多个治疗单位治疗同一目标时，治疗量会衰减。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/10/06">
        <TimelineRow>8 级独角的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>在 17 本新增 11 ~ 15 级独角。</TimelineRow>
        <TimelineRow>2 ~ 10 级独角的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>2 ~ 10 级独角的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>4 ~ 10 级独角的升级时间减少。</TimelineRow>
        <TimelineRow>2 ~ 10 级独角的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/05/02">
        <TimelineRow>4 ~ 10 级独角的每秒恢复值从 59/62/65/68/71/74/77 降低至 58/60/62/64/66/68/70。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>部落冲突推出战宠，其中莱希、闪枭、大牦、独角是第一批推出的。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
