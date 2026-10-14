---
title: "部落冲突 coc 超级法师塔升级数据"
navTitle: "超级法师塔"
shownTitle: "超级法师塔"
module: upgrade-home
imgFolder: home_buildings/0318
wiki: https://clashofclans.fandom.com/wiki/Super_Wizard_Tower
canonical: /upgrade/0318-Super-Wizard-Tower
dataSyncedOn: 2026-10-13
description: "超级法师的首次攻击最多可电击附近 15 个敌人，被闪电链命中的目标受到的伤害更低。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0318-Super-Wizard-Tower.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-11-17'">

<template #introduction>

- *如想查看合并前的建筑，请移步：[法师塔](/upgrade/0305-Wizard-Tower)。*
- *如想查看都城的超级法师塔，请移步：[都城超级法师塔](/upgrade/2207-Super-Wizard-Tower)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Super_Wizard_Tower2_hd.png" :imgAlt="$frontmatter.shownTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

1. 超级法师塔不能直接建造，必须由两个 [法师塔](/upgrade/0305-Wizard-Tower) 合并而成，两座用来合并的建筑必须已达到最高等级。
    - 合并一旦开始就无法取消。
    - 合并建筑的操作是永久性的，一旦合并就无法拆开。
    - 升本前必须合并完所有可以合并的建筑。
2. 超级法师塔会向初始目标发射一道闪电，该闪电可连锁初始目标周围的多个目标。
3. 超级法师塔每次攻击最多对 15 个目标造成伤害。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/11/17">
        <TimelineRow>18 本推出，并在 18 本新增建筑：超级法师塔，共设两个等级。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
