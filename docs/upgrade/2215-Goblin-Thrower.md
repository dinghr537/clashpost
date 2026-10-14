---
title: "部落冲突 coc 都城哥布林发射器升级数据"
navTitle: "哥布林发射器"
shownTitle: "哥布林发射器"
module: upgrade-capital
imgFolder: capital_buildings/2215
wiki: https://clashofclans.fandom.com/wiki/Goblin_Thrower
canonical: /upgrade/2215-Goblin-Thrower
dataSyncedOn: 2026-10-13
description: "这件精美的哥布林手工艺品会朝进攻者快速丢出装满哥布林的飞桶，而这些哥布林会向进攻者丢出尖锐的长矛。那长矛又会丢出什么呢？"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/2215-Goblin-Thrower.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-10-09'">

<template #introduction>

<SwitchTabs contentClass="cp-unit-items" :stickyTabs="true" :pageTabs="true">
    <SwitchTab tabId="cp-unit-item-0" :activeTab="true">哥布林发射器</SwitchTab>
    <SwitchTab tabId="cp-unit-item-1">哥布林投矛手</SwitchTab>
</SwitchTabs>

<SwitchTabGroup id="cp-unit-item-0" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Goblin_Thrower4.png" imgAlt="哥布林发射器"
    description="这件精美的哥布林手工艺品会朝进攻者快速丢出装满哥布林的飞桶，而这些哥布林会向进攻者丢出尖锐的长矛。那长矛又会丢出什么呢？"
    :isSmallImg="true" />

<SmallTitle>重要说明</SmallTitle>

1. 哥布林发射器在一次战斗中一共可以发射 5 个飞桶，每个飞桶内装有 3 只哥布林投矛手。
2. 哥布林发射器一旦发射完所有飞桶则不会继续攻击。
3. 如果哥布林发射器的飞桶在未消耗完毕时即被摧毁，则剩余的飞桶会立即释放。

</SwitchTabGroup>

<SwitchTabGroup id="cp-unit-item-1" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Spear_Goblin_info.png" imgAlt="哥布林投矛手"
    description="是谁想出了这么个馊主意，教哥布林扔长矛？这些长矛又是从哪里来的？不过话说回来，不管是对地面还是空中的进攻者，他们的威慑力真的很大。"
    :isSmallImg="true" />

</SwitchTabGroup>

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/10/09">
        <TimelineRow>都城新防御：哥布林发射器。哥布林投矛手是它的派生兵种。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
