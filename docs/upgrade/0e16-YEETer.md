---
title: "部落冲突 coc 战吼狂人升级数据"
navTitle: "战吼狂人"
shownTitle: "战吼狂人"
module: upgrade-temp
imgFolder: temp_troops/0e16
wiki: https://clashofclans.fandom.com/wiki/YEETer
canonical: /upgrade/0e16-YEETer
dataSyncedOn: 2026-10-13
description: "战吼狂人的攻击范围超远，战斗一开始他会投出 4 名忠诚的部族成员，攻击一切目标！之后，他会投掷自己最擅长的巨矛。现在，大声喊出来——咦哈！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0e16-YEETer.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-04-01'">

<template #introduction>

<SwitchTabs contentClass="cp-unit-items" :stickyTabs="true" :pageTabs="true">
    <SwitchTab tabId="cp-unit-item-0" :activeTab="true">战吼狂人</SwitchTab>
    <SwitchTab tabId="cp-unit-item-1">部族小队</SwitchTab>
</SwitchTabs>

<SwitchTabGroup id="cp-unit-item-0" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="YEETer_info.png" imgAlt="战吼狂人"
    description="战吼狂人的攻击范围超远，战斗一开始他会投出 4 名忠诚的部族成员，攻击一切目标！之后，他会投掷自己最擅长的巨矛。现在，大声喊出来——咦哈！" />

<SmallTitle>重要说明</SmallTitle>

1. 战吼狂人在 2025 年 4 月的部落狂热活动中作为临时兵种推出。
2. 战吼狂人扔部族成员时，攻击距离为 7 格；扔长矛时，攻击距离为 6 格。
3. 战吼狂人扔部族成员和扔长矛都可造成伤害，且伤害值是一样的。

</SwitchTabGroup>

<SwitchTabGroup id="cp-unit-item-1" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="YEETer_info.png" imgAlt="战吼狂人"
    description="数量占优时，体型便不再重要！战吼狂人登场时，会将这个四人小队投掷到战场上——他们擅长近战，会用迷你但强大的双手猛击一切目标！" />

</SwitchTabGroup>

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/04/01">
        <TimelineRow>该兵种第 1 次推出，有效期至 2025/05/01.</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
