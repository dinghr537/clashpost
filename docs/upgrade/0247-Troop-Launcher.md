---
title: "部落冲突 coc 部队发射器升级数据"
navTitle: "部队发射器"
shownTitle: "部队发射器"
module: upgrade-home
imgFolder: home_tech/0247
wiki: https://clashofclans.fandom.com/wiki/Troop_Launcher
canonical: /upgrade/0247-Troop-Launcher
dataSyncedOn: 2026-10-13
description: "这是一台无法移动的机器，它会向友军发射装满部队和部落城堡援军的飞桶，为他们提供支援。每个飞桶可容纳多个单位，包括一个部落城堡援军。飞桶数量有限，一定要充分发挥它们的作用！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0247-Troop-Launcher.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-11-17'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Troop_Launcher_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

1. 部队发射器部署后会向我方部队发射一桶一桶的部队。
    - 部队发射器发射部队时会同时发射自带部队和城堡内的援军，每次发射的配置为 [巨人](/upgrade/0002-Giant)、[野蛮人](/upgrade/0000-Barbarian)、[弓箭手](/upgrade/0001-Archer)、[炸弹人](/upgrade/0004-Wall-Breaker) 和 一个 [部落城堡](/upgrade/0407-Clan-Castle) 内的部队，其中巨人最先出来。
2. 部队发射器部署后不能移动，即使没有受到伤害也会自动掉血。[大守护者](/upgrade/0202-Grand-Warden) 的 [永恒书卷](/upgrade/0780-Eternal-Tome) 装备无法阻止部队发射器自身掉血。
3. 部队发射器中的部队等级取决于部队发射器的等级，而非玩家在 [实验室](/upgrade/0483-Laboratory) 中的部队等级。
4. 当部队发射器的血量清零，或发射完所有自带部队时，部队发射器就会自动解体并释放部落城堡内的部队。部队发射器解体后，只有尚未发射的自带部队会消失，援军会正常出来。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/11/17">
        <TimelineRow>4 级部队发射器的升级时间和升级费用减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/27">
        <TimelineRow>攻城机器的建造时间被取消。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/02/10">
        <TimelineRow>在 16 本新增攻城机器：部队发射器。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
