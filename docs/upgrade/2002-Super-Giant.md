---
title: "部落冲突 coc 都城超级巨人升级数据"
navTitle: "超级巨人"
shownTitle: "超级巨人"
module: upgrade-capital
imgFolder: capital_tech/2002
wiki: https://clashofclans.fandom.com/wiki/Super_Giant/Clan_Capital
canonical: /upgrade/2002-Super-Giant
dataSyncedOn: 2026-10-13
description: "身为普通巨人的大表哥，超级巨人体型更庞大，且擅长砸开城墙，为自己开路。他们的腰带是在村庄每年的大胃王比赛中赢得的。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/2002-Super-Giant.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-09-14'">

<template #introduction>

- *如想查看家乡的超级巨人，请访问：[超级巨人](/upgrade/0602-Super-Giant)。*
- *如想查看夜世界的巨人拳击手，请访问：[夜世界巨人拳击手](/upgrade/1002-Boxer-Giant)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Super_Giant_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

1. 超级巨人的解锁条件是建造 [超级巨人训练营](/upgrade/2342-Super-Giant-Barracks)，而这需要部落解锁野蛮人兵营，并且 [都城大本营](/upgrade/2400-Capital-Hall) 达到 2 级。
2. 超级巨人的技能（城墙克星）：对 [城墙](/upgrade/2200-Walls) 造成 5 倍伤害。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/09/14">
        <TimelineRow>4 ~ 5 级超级巨人的生命值由 3900/4200 增加到 4000/4400.</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/05/02">
        <TimelineRow>超级巨人随着部落都城玩法一同推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
