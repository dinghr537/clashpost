---
title: "部落冲突 coc 攻城滚木车升级数据"
navTitle: "攻城滚木车"
shownTitle: "攻城滚木车"
module: upgrade-home
imgFolder: home_tech/0244
wiki: https://clashofclans.fandom.com/wiki/Log_Launcher
canonical: /upgrade/0244-Log-Launcher
dataSyncedOn: 2026-10-13
description: "虽然攻城滚木车不是最快也不是最牢固的，但它绝对会让人疲于应付。攻城滚木车会不断抛出滚木，碾平路径上的一切，扫清通往敌军大本营的道路。法术对攻城滚木车无效。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0244-Log-Launcher.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-03-27'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Log_Launcher.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

1. 部署攻城滚木车后，它会对准 [大本营](/upgrade/0400-Town-Hall) 前进，并不断释放滚木，对前进路线上的建筑造成伤害。
2. 攻城滚木车的攻击距离是 20 格或者 4 个建筑。在命中第 4 个建筑时滚木会消失，不会攻击至 20 格距离。
3. 攻城滚木车部署后，即使没有受到伤害也会自动掉血。[大守护者](/upgrade/0202-Grand-Warden) 的 [永恒书卷](/upgrade/0780-Eternal-Tome) 装备无法阻止它自动掉血。
4. 当攻城滚木车的血量清零或到达大本营时，攻城滚木车就会自动解体并释放部落城堡内的部队。

\* 这是滚木车不受到伤害时的掉血速度。

\# 攻城滚木车会对近距离（具体几格不知道）的建筑造成额外伤害，我们将其称为“贴脸伤害”，而且“贴脸伤害”对 [城墙](/upgrade/0300-Walls) 仍然有 4 倍伤害。在近距离下，滚木车造成的伤害 = 每次伤害 + 贴脸伤害。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/03/27">
        <TimelineRow>攻城机器的建造时间被取消。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>2 ~ 4 级攻城滚木车的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/02/27">
        <TimelineRow>16 本新增 5 级攻城滚木车。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>2 ~ 4 级攻城滚木车的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>2 ~ 4 级攻城滚木车的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>2 ~ 4 级攻城滚木车的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/12/07">
        <TimelineRow>13 本可解锁新攻城机器：攻城滚木车。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
