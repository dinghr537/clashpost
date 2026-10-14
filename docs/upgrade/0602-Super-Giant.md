---
title: "部落冲突 coc 超级巨人升级数据"
navTitle: "超级巨人"
shownTitle: "超级巨人"
module: upgrade-home
imgFolder: home_tech/0602
wiki: https://clashofclans.fandom.com/wiki/Super_Giant
canonical: /upgrade/0602-Super-Giant
dataSyncedOn: 2026-10-13
description: "身为普通巨人的大表哥，超级巨人体型更庞大，且擅长砸开城墙，为自己开路。他们的腰带是在村庄每年的大胃王比赛中赢得的。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0602-Super-Giant.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2026-01-12'">

<template #introduction>

- *如想查看该兵种的普通版本，请访问：[巨人](/upgrade/0002-Giant)。*
- *如想查看夜世界的巨人拳击手，请访问：[夜世界巨人拳击手](/upgrade/1002-Boxer-Giant)。*
- *如想查看都城的超级巨人，请访问：[都城超级巨人](/upgrade/2002-Super-Giant)。*
- *如想查看作为临时兵种以及英雄装备派生兵种的巨人终极强化版，请访问：[霸天巨人](/upgrade/0e17-Giant-Giant)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Super_Giant_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

超级巨人的技能（城墙克星）：对 [城墙](/upgrade/0300-Walls) 造成 5 倍伤害。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2026/01/12">
        <TimelineRow>14 级超级巨人的每秒伤害和生命值增加。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/11/17">
        <TimelineRow>18 本推出，并在 18 本新增 14 级巨人，超级部队的等级也相应更新。</TimelineRow>
        <TimelineRow>13 级超级巨人的每秒伤害和生命值增加。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/27">
        <TimelineRow>部队的训练时间取消，但增加了捐赠费用。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>17 本推出，并在 17 本新增 13 级巨人，超级部队的等级也相应更新。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>16 本推出，并在 16 本新增 12 级巨人，超级部队的等级也相应更新。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>15 本推出，并在 15 本新增 11 级巨人，超级部队的等级也相应更新。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>所有等级的超级巨人生命值降低 200。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/12/07">
        <TimelineRow>超级部队的有效时间从 7 天缩短为 3 天。</TimelineRow>
        <TimelineRow>所有部队的强化费用统一调整为 25,000 暗黑重油。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/03/30">
        <TimelineRow>部落冲突新增“超级兵种”玩法，超级巨人是首批推出的超级兵种之一。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
