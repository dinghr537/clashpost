---
title: "部落冲突 coc 治疗书卷装备升级数据"
navTitle: "治疗书卷"
shownTitle: "治疗书卷"
module: upgrade-home
imgFolder: home_heroes/0783
wiki: https://clashofclans.fandom.com/wiki/Healing_Tome
canonical: /upgrade/0783-Healing-Tome
dataSyncedOn: 2026-10-13
description: "治疗书卷是大守护者的一件普通装备。治疗书卷装备可以在大守护者技能生效期间使周围的部队获得疗伤法术的效果。在治疗书卷的范围内，英雄可以获得全额治疗效果，攻城机器不能获得治疗效果。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0783-Healing-Tome.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2024-09-09'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Healing_Tome_info.png" :imgAlt="$frontmatter.navTitle" description="治疗大守护者和所有附近友军单位。" />

<SmallTitle>说明</SmallTitle>

1. 治疗书卷是 [大守护者](/upgrade/0202-Grand-Warden) 的一件普通装备。
2. 治疗书卷装备可以在大守护者技能生效期间使周围的部队获得 [疗伤法术](/upgrade/0101-Healing-Spell) 的效果。
3. 与疗伤法术不同的是，治疗书卷的范围会随着大守护者的位置变化而变化，大守护者是治疗圈的圆心。
4. 在治疗书卷的范围内，英雄可以获得全额治疗效果，攻城机器不能获得治疗效果。
5. 除了释放疗伤法术外，治疗书卷装备还可以增加大守护者的生命值，也可以增加他使用技能使恢复的生命值。

注：如果升级费用中有多种资源，则同时需要多种资源才能升级。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2024/09/09">
        <TimelineRow>所有等级治疗书卷装备的治疗效果持续时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>游戏新增装备系统，治疗书卷是第一批推出的装备。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
