---
title: "部落冲突 coc 都城飞行堡垒（空中堡垒）升级数据"
navTitle: "飞行堡垒"
shownTitle: "飞行堡垒（空中堡垒）"
module: upgrade-capital
imgFolder: capital_tech/2008
wiki: https://clashofclans.fandom.com/wiki/Flying_Fortress
canonical: /upgrade/2008-Flying-Fortress
dataSyncedOn: 2026-10-13
description: "你可能觉得堡垒插上翅膀会很危险，但飞行堡垒不存在这个问题。搭载着骷髅飞骑的飞行堡垒能对敌方实施可怕的轰炸。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/2008-Flying-Fortress.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-06-12'">

<template #introduction>

- *如想查看攻击方式与飞行堡垒类似的都城兵种，请访问该页面后切换到野猪飞骑：[都城野猪突袭队](/upgrade/200b-Hog-Raiders)。*

<SwitchTabs contentClass="cp-unit-items" :stickyTabs="true" :pageTabs="true">
    <SwitchTab tabId="cp-unit-item-0" :activeTab="true">飞行堡垒</SwitchTab>
    <SwitchTab tabId="cp-unit-item-1">骷髅飞骑</SwitchTab>
</SwitchTabs>

<SwitchTabGroup id="cp-unit-item-0" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Flying_Fortress_info.png" imgAlt="飞行堡垒"
    description="你可能觉得堡垒插上翅膀会很危险，但飞行堡垒不存在这个问题。搭载着骷髅飞骑的飞行堡垒能对敌方实施可怕的轰炸。" />

<SmallTitle>重要说明</SmallTitle>

1. 飞行堡垒的解锁条件是建造 [飞行堡垒工坊](/upgrade/2348-Flying-Fortress-Yard)，而这需要气球环礁这个子城升到 2 本，并且 [都城大本营](/upgrade/2400-Capital-Hall) 达到 4 级。
2. 飞行堡垒的技能（空降骷髅）：受到伤害后生成骷髅飞骑，骷髅飞骑死亡后生成大量 [骷髅](/upgrade/20c1-Skeleton)。

</SwitchTabGroup>

<SwitchTabGroup id="cp-unit-item-1" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Skeleton_Glider_info.png" imgAlt="骷髅飞骑"
    description="骷髅兵身材矮小，很难越过城墙。好在骨头和滑翔翼足够轻巧，让它能轻松飞过去！" />

<SmallTitle>重要说明</SmallTitle>

1. 飞行堡垒的解锁条件是建造 [飞行堡垒工坊](/upgrade/2348-Flying-Fortress-Yard)，而这需要气球环礁这个子城升到 2 本，并且 [都城大本营](/upgrade/2400-Capital-Hall) 达到 4 级。
2. 飞行堡垒的技能（空降骷髅）：受到伤害后生成骷髅飞骑，骷髅飞骑死亡后生成大量 [骷髅](/upgrade/20c1-Skeleton)。

</SwitchTabGroup>

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/06/12">
        <TimelineRow>移除飞行堡垒选择目标时的随机性。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/12/09">
        <TimelineRow>1 ~ 4 级飞行堡垒的生命值从 10000/12000/14000/16000 提高到 12000/13500/15000/16500.</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/05/02">
        <TimelineRow>飞行堡垒随着部落都城玩法一同推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
