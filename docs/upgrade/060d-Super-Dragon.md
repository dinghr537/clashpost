---
title: "部落冲突 coc 超级飞龙（金龙）升级数据"
navTitle: "超级飞龙"
shownTitle: "超级飞龙（金龙）"
module: upgrade-home
imgFolder: home_tech/060d
wiki: https://clashofclans.fandom.com/wiki/Super_Dragon
canonical: /upgrade/060d-Super-Dragon
dataSyncedOn: 2026-10-13
description: "体内有火不算什么，超级飞龙内外都冒火！只要开始战斗，他全身每一处都能迸发出熊熊烈焰。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/060d-Super-Dragon.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-03-27'">

<template #introduction>

- *如想查看该兵种的普通版本，请访问：[飞龙](/upgrade/0008-Dragon)。*
- *如想查看都城的超级飞龙，请访问：[都城超级飞龙](/upgrade/200c-Super-Dragon)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Super_Dragon_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

1. 超级飞龙的技能（炙热龙息）：超级飞龙攻击时可以溅射至周围目标，对它们造成持续伤害。
2. 超级飞龙的攻击机制：先以极快的速度（0.192 秒/次）打完 10 发子弹，休息 1.8 秒后再发射 10 发子弹。超级飞龙的溅射是带有一定随机性的，每次溅射到的建筑不一定相同。

\* 超级飞龙在攻击时没有首选目标，但如果自己被敌方援军、英雄或骷髅攻击，或附近的友军被这些单位攻击，超级飞龙都会转移目标去攻击这些单位。当这些单位都消灭干净之后才会继续攻击附近建筑。

\* 3 - 6 级超级飞龙只在 奖章活动 中出现，不能通过常规方式得到。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/03/27">
        <TimelineRow>部队的训练时间取消，但增加了捐赠费用。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/02/10">
        <TimelineRow>超级飞龙的训练时间由 6:00 改为 5:40</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>17 本推出，并在 17 本新增 12 级飞龙，超级部队的等级也相应更新。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/02/27">
        <TimelineRow>10 ~ 11 级超级飞龙的生命值提升。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>16 本推出，并在 16 本新增 11 级飞龙，超级部队的等级也相应更新。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>15 本新增 10 级飞龙，超级部队的等级也相应更新。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/05/02">
        <TimelineRow>8/9 级超级飞龙的每秒伤害值从 414/448 降低至 405/429。</TimelineRow>
        <TimelineRow>超级飞龙的射程降低 1 格（官方写的削 0.5 格，实际上就是削了 1 格）。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/01/20">
        <TimelineRow>所有等级超级飞龙的生命值减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/12/09">
        <TimelineRow>新超级兵：超级飞龙。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
