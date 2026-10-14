---
title: "部落冲突 coc 都城亡灵大军升级数据"
navTitle: "亡灵大军"
shownTitle: "亡灵大军"
module: upgrade-capital
imgFolder: capital_tech/2004
wiki: https://clashofclans.fandom.com/wiki/Minion_Horde
canonical: /upgrade/2004-Minion-Horder
dataSyncedOn: 2026-10-13
description: "六个行动迅速、无护甲保护的飞行战士。三人为伍，六人成军！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/2004-Minion-Horde.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2022-06-30'">

<template #introduction>

- *如想查看家乡的亡灵，请访问：[亡灵](/upgrade/0080-Minion)。*
- *如想查看夜世界的异变亡灵，请访问：[夜世界异变亡灵](/upgrade/1003-Beta-Minion)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Minion_Horde_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

1. 亡灵大军的解锁条件是建造 [亡灵训练营](/upgrade/2344-Minion-Barracks)，而这需要野蛮人兵营这个子城升到 2 本，并且 [都城大本营](/upgrade/2400-Capital-Hall) 达到 3 级。
2. 在都城中，亡灵只能以 6 个一组的形式部署。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2022/06/30">
        <TimelineRow>亡灵的每秒伤害从 38/46/54/62/70 提升到 56/62/68/74/80</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/05/02">
        <TimelineRow>亡灵大军随着部落都城玩法一同推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
