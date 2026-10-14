---
title: "部落冲突 coc 都城疗伤法术升级数据"
navTitle: "疗伤法术"
shownTitle: "疗伤法术"
module: upgrade-capital
imgFolder: capital_tech/2100
wiki: https://clashofclans.fandom.com/wiki/Healing_Spell/Clan_Capital
canonical: /upgrade/2100-Healing-Spell
dataSyncedOn: 2026-10-13
description: "恢复部队的元气，让他们保持战斗力！施放疗伤法术会产生一个治疗光环，治愈该法术光环之内的部队！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/2100-Healing-Spell.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2022-06-30'">

<template #introduction>

- *如想查看家乡的疗伤法术，请访问：[疗伤法术](/upgrade/0101-Healing-Spell)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Healing_Spell_info.png" :imgAlt="$frontmatter.navTitle"
    description="恢复部队的元气，让他们保持战斗力！<br>施放疗伤法术会产生一个治疗光环，治愈该法术光环之内的部队！"
    :isSmallImg="true" />

<SmallTitle>重要说明</SmallTitle>

当部落重建法师山谷的废墟时，系统会自动建造 [疗伤法术工厂](/upgrade/2380-Heal-Spell-Factory)，重建后即可解锁疗伤法术。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2022/06/30">
        <TimelineRow>1 ~ 5 级疗伤法术的每秒治疗量减少 33.</TimelineRow>
        <TimelineRow>1 ~ 5 级疗伤法术的每秒脉冲治疗量 34/38/42/46/50 减少到 24/28/32/36/40.</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/06/07">
        <TimelineRow>被摧毁的攻城炮车将无法享受到疗伤法术的治疗效果。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/05/02">
        <TimelineRow>疗伤法术随着部落都城玩法一同推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
