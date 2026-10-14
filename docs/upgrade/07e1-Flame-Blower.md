---
title: "部落冲突 coc 助燃器装备升级数据"
navTitle: "助燃器"
shownTitle: "助燃器"
module: upgrade-home
imgFolder: home_heroes/07e1
wiki: https://clashofclans.fandom.com/wiki/Flame_Blower
canonical: /upgrade/07e1-Flame-Blower
dataSyncedOn: 2026-10-13
description: "助燃器是飞龙公爵的两件初始装备之一，另一件是烈焰之心。使用时，助燃器在飞龙公爵面前喷出锥形的火焰造成大量伤害。烈焰之心装备还可以增加飞龙公爵生命值以及技能状态下的生命值恢复量。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/07e1-Flame-Blower.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2026-02-23'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Flame_Blower_info.png" :imgAlt="$frontmatter.navTitle" description="吹出炽热烈焰，灼烧敌人和建筑。" />

<SmallTitle>说明</SmallTitle>

1. 助燃器是 [飞龙公爵](/upgrade/0205-Dragon-Duke) 的两件初始装备之一，另一件是 [烈焰之心](/upgrade/07e0-Fire-Heart)。
2. 开启技能后，飞龙公爵面前会喷出锥形火焰，可造成大量伤害。
3. 烈焰之心装备还可以增加飞龙公爵生命值以及技能状态下的生命值恢复量。

注意：如果升级费用中有多种资源，则同时需要多种资源才能升级。<br>

</template>

<template #history>

<Timeline>
    <TimelineItem date="2026/02/23">
        <TimelineRow>新装备：助燃器。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
