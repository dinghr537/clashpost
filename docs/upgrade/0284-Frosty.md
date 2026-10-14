---
title: "部落冲突 coc 冰牙（霜牙）升级数据"
navTitle: "冰牙"
shownTitle: "冰牙（霜牙）"
module: upgrade-home
imgFolder: home_heroes/0284
wiki: https://clashofclans.fandom.com/wiki/Frosty
canonical: /upgrade/0284-Frosty
dataSyncedOn: 2026-10-13
description: "冰牙是最冷酷的战宠......又冷又酷。它不仅能呼出冰冷的气息减缓敌人的速度，还能释放出一群小冰怪，进一步减缓敌方防御建筑的攻击速度，帮助它的英雄驰骋战场。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0284-Frosty.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-10-06'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Frosty_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

1. 冰牙的技能（冷酷伙伴）：冰牙每隔一段时间都会生成小冰怪攻击附近的防御建筑。
2. 冰牙和小冰怪的攻击可以减缓敌方防御建筑、部队、英雄的攻速。
3. 冰牙和小冰怪攻击时的减速效果不能叠加。
4. 冰牙和小冰怪的减速效果可以延后单一目标模式的 [地狱塔](/upgrade/030a-Inferno-Tower) 和 [地狱飞龙](/upgrade/0604-Inferno-Dragon) 达到最高伤害的时间。
5. 如果主人被召回或者阵亡，冰牙会变成一个自由单位，不再拥有攻击偏好。
6. 小冰怪攻击一次后就会死亡，[大守护者](/upgrade/0202-Grand-Warden) 的 [永恒书卷](/upgrade/0780-Eternal-Tome) 装备也无法阻止。

\* 根据解析安装包的结果，小冰怪的攻击速度是一秒一次，但实际上小冰怪的首次攻击时机为到达目标后 0.5 秒，且攻击一次后就会死亡，因此其攻速值无意义。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/10/06">
        <TimelineRow>8 级冰牙的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/06/16">
        <TimelineRow>在 17 本新增 11 ~ 15 级冰牙。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>2 ~ 9 级冰牙的升级费用降低。</TimelineRow>
        <TimelineRow>小雪怪和小冰怪占据的人口数由 3 调整为 1.</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>2 ~ 10 级冰牙的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/18">
        <TimelineRow>2、4 ~ 10 级冰牙的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>2 ~ 10 级冰牙的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>15 本推出，可解锁四个新宠物，冰牙是其中之一。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
