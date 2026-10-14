---
title: "部落冲突 coc 烈焰之心装备升级数据"
navTitle: "烈焰之心"
shownTitle: "烈焰之心"
module: upgrade-home
imgFolder: home_heroes/07e0
wiki: https://clashofclans.fandom.com/wiki/Fire_Heart
canonical: /upgrade/07e0-Fire-Heart
dataSyncedOn: 2026-10-13
description: "烈焰之心是飞龙公爵的两件初始装备之一，另一件是助燃器。烈焰之心装备的死亡爆炸效果只会在飞龙公爵第一次死亡时触发。如果他被凤凰复活后再次死亡，则不会再触发爆炸效果。除死亡爆炸外，烈焰之心装备还可以增加飞龙公爵的生命值和攻击力。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/07e0-Fire-Heart.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2026-02-23'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Fire_Heart_info.png" :imgAlt="$frontmatter.navTitle" description="缓慢恢复飞龙公爵的生命值，当他倒下时，会爆发出灼伤敌人的烈焰。" />

<SmallTitle>说明</SmallTitle>

1. 烈焰之心是 [飞龙公爵](/upgrade/0205-Dragon-Duke) 的两件初始装备之一，另一件是 [助燃器](/upgrade/07e1-Flame-Blower)。
2. 烈焰之心装备的死亡爆炸效果只会在飞龙公爵第一次死亡时触发。如果他被 [凤凰](/upgrade/0287-Phoenix) 复活或 [复苏法术](/upgrade/0108-Revive-Spell) 复苏后再次死亡，则不会再触发爆炸效果。
3. 除死亡爆炸外，烈焰之心装备还可以增加飞龙公爵的伤害和生命值。

注意：如果升级费用中有多种资源，则同时需要多种资源才能升级。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2026/02/23">
        <TimelineRow>新装备：烈焰之心。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
