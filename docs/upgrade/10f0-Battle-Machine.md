---
title: "部落冲突 coc 夜世界战争机器升级数据"
navTitle: "战争机器"
shownTitle: "战争机器"
module: upgrade-bh
imgFolder: bh_tech/10f0
wiki: https://clashofclans.fandom.com/wiki/Battle_Machine
canonical: /upgrade/10f0-Battle-Machine
dataSyncedOn: 2026-10-13
description: "建筑大师的获奖发明，可以粉碎敌方建筑。只有它才能证明谁是这里最好的建筑工人！解锁电磁战锤技能，狠狠地击打敌人！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/10f0-Battle-Machine.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-10-20'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Battle_Machine_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

\* 电磁战锤：在接下来的几次攻击造成额外伤害，并恢复部分生命值。如果启用技能时能量条达到 2 级，则接下来的几次攻击含有连锁效果。

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

<template #history>

<Timeline>
    <TimelineItem date="2023/10/20">
        <TimelineRow>将技能的生效时间恢复为三次攻击。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/10/09">
        <TimelineRow>将技能的生效时间更改为两次攻击。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/05/15">
        <TimelineRow>新增 31 - 35 级战争机器。</TimelineRow>
        <TimelineRow>现在夜世界英雄的技能强度分成了三个充能等级，充能等级越高，技能越强。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/06/22">
        <TimelineRow>提升了 21 至 30 级战争机器的每秒伤害值。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/03/30">
        <TimelineRow>移除战争的恢复时间。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/06/18">
        <TimelineRow>夜世界 9 本开放，战争机器可升至 30 级。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/04/02">
        <TimelineRow>巨型加农炮不再对战争机器造成多倍伤害。</TimelineRow>
        <TimelineRow>所有等级战争机器的恢复时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2018/03/05">
        <TimelineRow>夜世界 8 本开放，战争机器可升至 25 级。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2017/09/27">
        <TimelineRow>夜世界 7 本开放，战争机器可升至 20 级。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2017/06/27">
        <TimelineRow>夜世界 6 本开放，战争机器可升至 10 级。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
