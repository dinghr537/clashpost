---
title: "部落冲突 coc 大本营升级数据"
navTitle: "大本营"
shownTitle: "大本营"
module: upgrade-home
imgFolder: home_buildings/0400
wiki: https://clashofclans.fandom.com/wiki/Town_Hall
canonical: /upgrade/0400-Town-Hall
dataSyncedOn: 2026-10-13
description: "大本营是村庄的核心。升级大本营，可解锁新的防御、建筑、陷阱和更多内容。在战斗中摧毁敌军大本营，您将获得一颗星。把大本营建在村庄中心，并在其周围建造城墙、陷阱以及其他防御是最安全的举措。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0400-Town-Hall.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-11-17'">

<template #introduction>

- *如想查看大本营的自带武器，请访问：[巨型特斯拉电磁塔](/upgrade/030c-Giga-Tesla)、[巨型地狱之塔](/upgrade/030d-Giga-Inferno)、[地狱火炮](/upgrade/0315-Inferno-Artillery)。*
- *如想查看夜世界的大本营，请访问：[建筑大师大本营](/upgrade/1200-Builder-Hall)、[夜世界奥仔哨站](/upgrade/1240-O.T.T.O's-Outpost)。*
- *如想查看都城的大本营，请访问：[都城大本营](/upgrade/2400-Capital-Hall)、[子城大本营](/upgrade/2401-District-Hall)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Town_Hall18_hd.png" :imgAlt="$frontmatter.navTitle"
    description="大本营是村庄的核心。升级大本营，可解锁新的防御、建筑、陷阱和更多内容。<br>在战斗中摧毁敌军大本营，您将获得一颗星。<br>把大本营建在村庄中心，并在其周围建造城墙、陷阱以及其他防御是最安全的举措。" />

<SmallTitle>重要说明</SmallTitle>

[雷电法术](/upgrade/0100-Lightning-Spell) 不能对大本营造成伤害，[地震法术](/upgrade/0181-Earthquake-Spell) 可以。

**\* 关于建筑数量和陷阱数量的说明：**

1. 这里的建筑数量包含大本营本身以及 5 个 [建筑工人小屋](/upgrade/0500-Builders-Hut)，在 10 级及以上大本营还包含 [小博木屋](/upgrade/0501-B.O.Bs-Hut)。
2. 理论上来说，[部落城堡](/upgrade/0407-Clan-Castle) 在 2 级大本营也有可能解锁，但这种情况过于刁钻，为了让数据更具普遍性，这里将城堡视为 3 级大本营解锁。
3. 当商店里的所有建筑都已建造，且所有可以合并的建筑都已经合并时，建筑数量才会等于表格中的数字。
4. 战旗 不视为建筑。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/11/17">
        <TimelineRow>游戏新增 18 级大本营。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/10/06">
        <TimelineRow>同步游戏内大本营的文字描述。</TimelineRow>
        <TimelineRow>16 级大本营的升级费用降低。</TimelineRow>
        <TimelineRow>13 ~ 17 级大本营的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/06/16">
        <TimelineRow>1 ~ 4 级大本营的生命值减少。</TimelineRow>
        <TimelineRow>由于精制台的推出，17 级大本营的建筑数量加一。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>6、9、14 ~ 17 级大本营的升级费用降低。</TimelineRow>
        <TimelineRow>10 ~ 12 级大本营的升级时间增加。</TimelineRow>
        <TimelineRow>15 ~ 17 级大本营的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/02/10">
        <TimelineRow>游戏推出了新的合并建筑，17 本的建筑数量有变。</TimelineRow>
        <TimelineRow>3 级大本营的升级时间减少。</TimelineRow>
        <TimelineRow>14 ~ 17 级大本营可存储的资源量增加。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>游戏新增 17 级大本营。</TimelineRow>
        <TimelineRow>15 ~ 16 级大本营的升级费用降低。</TimelineRow>
        <TimelineRow>14 ~ 16 级大本营的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>游戏新增 16 级大本营。</TimelineRow>
        <TimelineRow>15 级大本营的升级时间由 15 天减少至 13 天 12 小时。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>更新后训练营和暗黑训练营各保留一个，多余的全部删除，所以各个大本的最大建筑数量改变。</TimelineRow>
        <TimelineRow>游戏新增 15 级大本营。</TimelineRow>
        <TimelineRow>10 ~ 14 级大本营的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/12/09">
        <TimelineRow>1 ~ 13 级大本营的升级费用降低。</TimelineRow>
        <TimelineRow>4 ~ 14 级大本营的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/29">
        <TimelineRow>14 级大本营爆炸后毒药的伤害增长更快。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>14 级大本营推出。</TimelineRow>
        <TimelineRow>7、10、11 级大本营的升级费用降低。</TimelineRow>
        <TimelineRow>2 级大本营可存储的金币和圣水由 1000 增加到 2500。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/12/09">
        <TimelineRow>13 级大本营推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/04/02">
        <TimelineRow>包含大量降低发展成本和提高发展速度的调整，其中 4 ~ 10 级大本营的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
