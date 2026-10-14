---
title: "部落冲突 coc 复仇之塔升级数据"
navTitle: "复仇之塔"
shownTitle: "复仇之塔"
module: upgrade-home
imgFolder: home_buildings/0319
wiki: https://clashofclans.fandom.com/wiki/Revenge_Tower
canonical: /upgrade/0319-Revenge-Tower
dataSyncedOn: 2026-10-13
description: "如果你摧毁了它的建筑伙伴，复仇之塔就会锁定你、追踪你，然后狠狠惩罚你。随着周围建筑被摧毁，它会变得更强大、更愤怒！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0319-Revenge-Tower.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2026-01-28'">

<template #introduction>

<SwitchTabs contentClass="cp-unit-items" :stickyTabs="true" :pageTabs="true">
    <SwitchTab tabId="cp-unit-item-0" :activeTab="true">休眠状态</SwitchTab>
    <SwitchTab tabId="cp-unit-item-1">一阶段</SwitchTab>
    <SwitchTab tabId="cp-unit-item-2">二阶段</SwitchTab>
    <SwitchTab tabId="cp-unit-item-3">三阶段</SwitchTab>
</SwitchTabs>

<SwitchTabGroup id="cp-unit-item-0" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Revenge_Tower2_Dormant.png" imgAlt="复仇之塔（休眠状态）" :description="$frontmatter.description" :isSmallImg="true" />

<SmallTitle>重要说明</SmallTitle>

1. 复仇之塔随着建筑被摧毁的数量增加而增强。
    - 游戏开始时，它处于休眠状态，不会主动攻击。
    - 当 5 座建筑物被摧毁时，它会进入一阶段。一阶段的复仇之塔会以较慢的速度向地面和空中单位发射高伤害的弹丸。
    - 当 25 座建筑物被摧毁时，它会进入二阶段。此时复仇之塔每次造成的伤害减半，但射速翻倍，并且可以像 [跳弹加农炮](/upgrade/0313-Ricochet-Cannon) 一样将弹丸反弹到其他目标，不过只能反弹一次。
    - 当 50 座建筑物被摧毁时，它会进入三阶段，也就是最终阶段。此时复仇之塔每次造成的伤害不变，射速再次翻倍，且可以反弹两次。
2. 即使复仇之塔处于休眠状态，它仍被视为防御建筑，这意味着 [巨人](/upgrade/0002-Giant)、[气球兵](/upgrade/0005-Balloon) 等以防御为目标的单位会优先攻击它。

</SwitchTabGroup>

<SwitchTabGroup id="cp-unit-item-1" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Revenge_Tower2_Stage1.png" imgAlt="复仇之塔（一阶段）" :description="$frontmatter.description" :isSmallImg="true" />

</SwitchTabGroup>

<SwitchTabGroup id="cp-unit-item-2" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Revenge_Tower2_Stage2.png" imgAlt="复仇之塔（二阶段）" :description="$frontmatter.description" :isSmallImg="true" />

</SwitchTabGroup>

<SwitchTabGroup id="cp-unit-item-3" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Revenge_Tower2_Stage3.png" imgAlt="复仇之塔（三阶段）" :description="$frontmatter.description" :isSmallImg="true" />

\* 弹射伤害一栏中，135 / 81 代表弹丸弹射到第一个目标时的伤害为 135，弹射到第二个目标时为 81.
</SwitchTabGroup>

</template>

<template #history>

<Timeline>
    <TimelineItem date="2026/01/28">
        <TimelineRow>复仇之塔最后一个阶段的攻速由 0.3 秒/次 降低到 0.35 秒/次。</TimelineRow>
        <TimelineRow>复仇之塔二阶段的触发条件改为 25 座建筑被摧毁（之前是 20 座）。</TimelineRow>
        <TimelineRow>复仇之塔三阶段的触发条件改为 50 座建筑被摧毁（之前是 40 座）。</TimelineRow>
        <TimelineRow>复仇之塔三阶段的每秒伤害降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/11/17">
        <TimelineRow>18 本推出，并在 18 本新增建筑：复仇之塔，共设两个等级。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
