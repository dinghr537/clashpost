---
title: "部落冲突 coc 骷髅陷阱升级数据"
navTitle: "骷髅陷阱"
shownTitle: "骷髅陷阱"
module: upgrade-home
imgFolder: home_buildings/0385
wiki: https://clashofclans.fandom.com/wiki/Skeleton_Trap
canonical: /upgrade/0385-Skeleton-Trap
dataSyncedOn: 2026-10-13
description: "骷髅兵虽然脆弱，但异常狡猾，他们出其不意地伏击毫无戒备的敌军部队，并分散敌军注意力！您可以将骷髅陷阱的目标设置为地面部队或空中部队。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0385-Skeleton-Trap.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-11-17'">

<template #introduction>

- 本页内容不是空中炸弹，如想查看空中炸弹的数据，请访问：[空中炸弹](/upgrade/0382-Air-Bomb)。

<SwitchTabs contentClass="cp-unit-items" :stickyTabs="true" :pageTabs="true">
    <SwitchTab tabId="cp-unit-item-0" :activeTab="true">骷髅陷阱</SwitchTab>
    <SwitchTab tabId="cp-unit-item-1">骷髅</SwitchTab>
</SwitchTabs>

<SwitchTabGroup id="cp-unit-item-0" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Skeleton_Trap_info.png" imgAlt="骷髅陷阱"
    description="骷髅兵虽然脆弱，但异常狡猾，他们出其不意地伏击毫无戒备的敌军部队，并分散敌军注意力！您可以将骷髅陷阱的目标设置为地面部队或空中部队。" :isSmallImg="true" />

</SwitchTabGroup>

<SwitchTabGroup id="cp-unit-item-1" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Skeleton_info.png" imgAlt="骷髅"
    description="这些不死生物本身不构成太大的威胁，但它们从来不单独作战，因为女巫会不断召唤成群的骷髅兵来对抗您的敌人！" :isSmallImg="true" />

</SwitchTabGroup>

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/11/17">
        <TimelineRow>18 本推出，并在 18 本新增 5 级骷髅陷阱。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>3 ~ 4 级骷髅陷阱的升级时间减少。</TimelineRow>
        <TimelineRow>2 ~ 4 级骷髅陷阱的升级费用降低。</TimelineRow>
        <TimelineRow>对地模式的骷髅陷阱召唤出的骷髅占用的人口数由 2 调整为 1，现在对空和对地骷髅的人口数统一为 1 了。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>所有等级骷髅陷阱的升级费用降低。</TimelineRow>
        <TimelineRow>3 ~ 4级骷髅陷阱的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/12/09">
        <TimelineRow>3 ~ 4 级骷髅陷阱的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>14 本推出，并在 14 本新解锁一个骷髅陷阱。</TimelineRow>
        <TimelineRow>2 ~ 4 级骷髅陷阱的升级时间减少。</TimelineRow>
        <TimelineRow>2 ~ 3 级骷髅陷阱的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/12/09">
        <TimelineRow>13 本推出，并在 13 本新增 4 级搜空地雷。</TimelineRow>
        <TimelineRow>13 本新解锁一个搜空地雷。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/04/02">
        <TimelineRow>玩家上线后，所有的陷阱将自动被重新布置，重新布置不再需要花费金币。然而，如果玩家不上线，陷阱就不会被重新布置，所以你仍然可以攻击到陷阱失效的村庄。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
