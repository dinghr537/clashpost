---
title: "部落冲突 coc 都城永恒急速法术升级数据"
navTitle: "永恒急速法术"
shownTitle: "永恒急速法术"
module: upgrade-capital
imgFolder: capital_tech/2106
wiki: https://clashofclans.fandom.com/wiki/Endless_Haste_Spell
canonical: /upgrade/2106-Endless-Haste-Spell
dataSyncedOn: 2026-10-13
description: "永久提速部队的速度！施放该法术产生一个急速光环，穿过该光环的单位会获得加速效果，一直持续当场战斗结束！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/2106-Endless-Haste-Spell.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-10-02'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Endless_Haste_Spell_info.png" :imgAlt="$frontmatter.navTitle"
    description="永久提速部队的速度！<br>施放该法术产生一个急速光环，穿过该光环的单位会获得加速效果，一直持续当场战斗结束！"
    :isSmallImg="true" />

<SmallTitle>重要说明</SmallTitle>

1. 当哥布林矿井这个子城的大本营升到 2 级，且都城之巅的大本营等级 9 级后，系统会自动建造 [永恒急速法术工厂](/upgrade/2386-Endless-Haste-Spell-Factory)，建造完成后即解锁永恒急速法术。
2. 部署后，进入永恒急速法术影响范围的单位将获得小幅但永久的速度提升，即使部队离开法术半径后，提速效果仍然持续。
3. 多个永恒急速法术的效果不会叠加。
4. 永恒急速法术的提速效果可以暂时被 [狂暴法术](/upgrade/2104-Rage-Spell) 覆盖，因为狂暴法术具有更高的速度提升属性。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/10/02">
        <TimelineRow>新法术：永恒急速法术。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
