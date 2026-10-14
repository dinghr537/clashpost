---
title: "部落冲突 coc 雷电獠牙装备升级数据"
navTitle: "雷电獠牙"
shownTitle: "雷电獠牙"
module: upgrade-home
imgFolder: home_heroes/07e4
wiki: https://clashofclans.fandom.com/wiki/Electro_Fangs
canonical: /upgrade/07e4-Electro-Fangs
dataSyncedOn: 2026-10-13
description: "雷电獠牙是飞龙公爵的普通装备。带上它后，飞龙公爵的攻击会附带连锁闪电，能对初始目标附近的单位造成递减伤害，同时还会提高飞龙公爵的生命值。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/07e4-Electro-Fangs.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2026-04-27'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Electro_Fangs_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>说明</SmallTitle>

1. 雷电獠牙是 [飞龙公爵](/upgrade/0205-Dragon-Duke) 的一件普通装备，在 [铁匠铺](/upgrade/0488-Blacksmith) 10 级时解锁，需要 17 本。
2. 带上雷电獠牙装备后，飞龙公爵的攻击会附带连锁闪电效果，对初始目标附近的单位造成伤害；后续目标会依次承受更低的伤害，每跳减少 20%。
   - 第一个被连锁击中的目标会承受完整伤害，原本的初始目标不会额外吃到这段连锁伤害。
   - 如果附近没有可连锁的目标，连锁闪电不会触发。
3. 这个连锁闪电伤害属于直接技能伤害，不会被 [狂暴法术](/upgrade/0102-Rage-Spell) 等加成伤害的效果强化，也不会受到难度修正影响。
4. 除了连锁闪电外，该装备还会为飞龙公爵提供额外生命值。

注意：
5. 如果升级费用中有多种资源，则同时需要多种资源才能升级。
6. 连锁闪电的伤害会逐跳衰减，最终伤害取决于目标数量和站位。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2026/04/27">
        <TimelineRow>新装备：雷电獠牙。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
