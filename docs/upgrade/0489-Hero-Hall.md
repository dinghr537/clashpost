---
title: "部落冲突 coc 英雄殿堂升级数据"
navTitle: "英雄殿堂"
shownTitle: "英雄殿堂"
module: upgrade-home
imgFolder: home_buildings/0489
wiki: https://clashofclans.fandom.com/wiki/Hero_Hall
canonical: /upgrade/0489-Hero-Hall
dataSyncedOn: 2026-10-13
description: "这座华丽的殿堂是为了颂扬村庄里最强大的勇士！前往英雄殿堂，查看所有与英雄相关的信息，并升级英雄。升级英雄殿堂可解锁更多英雄！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0489-Hero-Hall.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-11-17'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Hero_Hall12_hd.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

<SmallTitle>重要说明</SmallTitle>

1. 2024 年 11 月更新后，你需要在英雄殿堂升级和管理英雄，不能和以前一样直接在阵型中找到英雄升级。
    - 所谓的管理英雄指的是在英雄殿堂中分配战宠、管理装备、查看皮肤、修改防守英雄等快捷方式。
2. 虽然官方将升级操作整合进了英雄殿堂，但升级英雄仍然需要占用建筑工人。
3. 现在 [大本](/upgrade/0400-Town-Hall) 等级不再是限制英雄升级的参数，能不能升级只看英雄殿堂等级。
4. 随着英雄殿堂推出，游戏引入了英雄栏位的概念。
    - 在进攻时，英雄栏位的数量代表可同时上场的英雄数量。
    - 在防守时，英雄栏位会以战旗的形式放置在阵型中，你可以指派一名英雄保卫战旗附近的区域。

如果你在 **2024 年 11 月更新前** 已经拥有英雄，那么官方会根据你更新时的英雄等级送你相应等级英雄殿堂和亡灵王子，无需从头开始升级。如果更新时你的英雄尚未升级完成，那么官方会帮你直接秒掉这一级英雄。

官方送的英雄/建筑等级就高不就低。比如说更新时你的四王等级为 60/70/51/20，那么更新后你可以获得 8 级英雄殿堂和 50 级亡灵王子。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/11/17">
        <TimelineRow>18 本推出，并在 18 本新增 12 级英雄殿堂。</TimelineRow>
        <TimelineRow>11 级英雄殿堂的升级时间和升级费用减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/10/06">
        <TimelineRow>4 ~ 10 级英雄殿堂的升级时间减少。</TimelineRow>
        <TimelineRow>4 ~ 10 级英雄殿堂的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>3、7 ~ 10 级英雄殿堂的升级时间减少。</TimelineRow>
        <TimelineRow>8 ~ 10 级英雄殿堂的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>17 本推出，新建筑：英雄殿堂。</TimelineRow>
        <TimelineRow>现在你需要在英雄殿堂升级和管理英雄，不能和以前一样直接在阵型中找到英雄升级。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
