---
title: "部落冲突 coc 夜世界战斗直升机升级数据"
navTitle: "战斗直升机"
shownTitle: "战斗直升机"
module: upgrade-bh
imgFolder: bh_tech/10f1
wiki: https://clashofclans.fandom.com/wiki/Battle_Copter
canonical: /upgrade/10f1-Battle-Copter
dataSyncedOn: 2026-10-13
description: "快上直升机！建筑大师厌倦了锤城墙，于是他发明了可以飞跃城墙的新一代飞行器。战斗直升机可从远处发射威力巨大的炮弹，也可以使用爆弹冲锋技能靠近目标发动奇袭。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/10f1-Battle-Copter.json";
</script>

<SyncedUnitData :data="unitData">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Battle_Copter_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

\* 爆弹冲锋：向地面投掷一颗炸弹，并恢复部分生命值。

<SwitchTabs contentClass="cp-upgrade-skill">
    <SwitchTab tabId="cp-upgrade-skill-bar-1" :activeTab="true">1 级能量条</SwitchTab>
    <SwitchTab tabId="cp-upgrade-skill-bar-2">2 级能量条</SwitchTab>
    <SwitchTab tabId="cp-upgrade-skill-bar-3">3 级能量条</SwitchTab>
</SwitchTabs>

<SwitchTabGroup id="cp-upgrade-skill-bar-1" class="cp-upgrade-skill">

</SwitchTabGroup>

<SwitchTabGroup id="cp-upgrade-skill-bar-2" class="cp-upgrade-skill">

</SwitchTabGroup>

<SwitchTabGroup id="cp-upgrade-skill-bar-3" class="cp-upgrade-skill">

</SwitchTabGroup>

</template>

</SyncedUnitData>
