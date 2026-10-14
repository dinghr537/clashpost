---
title: "部落冲突 coc 女巫升级数据"
navTitle: "女巫"
shownTitle: "女巫"
module: upgrade-home
imgFolder: home_tech/0084
wiki: https://clashofclans.fandom.com/wiki/Witch
canonical: /upgrade/0084-Witch
dataSyncedOn: 2026-10-13
description: "女巫从来不是一个人在战斗，她能不断召唤骷髅兵发起攻击。升级您的女巫，让她每次可以召唤更多骷髅兵。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0084-Witch.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2026-02-23'">

<template #introduction>

- *如想查看该兵种的强化版本，请访问：[超级女巫](/upgrade/0605-Super-Witch)。*
- *如想查看夜世界的暗夜女巫，请访问：[夜世界暗夜女巫](/upgrade/1007-Night-Witch)。*

<SwitchTabs contentClass="cp-unit-items" :stickyTabs="true" :pageTabs="true">
    <SwitchTab tabId="cp-unit-item-0" :activeTab="true">女巫</SwitchTab>
    <SwitchTab tabId="cp-unit-item-1">骷髅</SwitchTab>
</SwitchTabs>

<SwitchTabGroup id="cp-unit-item-0" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Witch_info.png" imgAlt="女巫"
    description="女巫从来不是一个人在战斗，她能不断召唤骷髅兵发起攻击。升级您的女巫，让她每次可以召唤更多骷髅兵。" />

\* 女巫并不是每次召唤都可以召唤出这么多骷髅，当一只女巫召唤的骷髅达到上表的限制时，除非骷髅兵死亡，否则女巫不会继续召唤。这个上限指的是每只女巫召唤的骷髅，如果有两只女巫，那么场上的最大骷髅数量为 2 倍上限。
</SwitchTabGroup>

<SwitchTabGroup id="cp-unit-item-1" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Skeleton_info.png" imgAlt="女巫召唤的骷髅"
    description="这些不死生物本身不构成太大的威胁，但它们从来不单独作战，因为女巫会不断召唤成群的骷髅兵来对抗您的敌人！" />

</SwitchTabGroup>

</template>

<template #history>

<Timeline>
    <TimelineItem date="2026/02/23">
        <TimelineRow>在 18 本添加了 8 级女巫。</TimelineRow>
        <TimelineRow>添加了 2 级骷髅。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/10/06">
        <TimelineRow>4 ~ 7 级女巫的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/27">
        <TimelineRow>部队的训练时间取消，但增加了捐赠费用。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>2 ~ 7 级女巫的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/02/10">
        <TimelineRow>女巫的训练时间由 2:00 改为 1:40</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>2 ~ 7 级女巫的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/18">
        <TimelineRow>6 级女巫的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/03">
        <TimelineRow>4 ~ 5 级女巫的每秒伤害提升。</TimelineRow>
        <TimelineRow>4 ~ 6 级女巫的生命值提升。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>新增 16 本，并在 16 本新增 7 级女巫。</TimelineRow>
        <TimelineRow>5 ~ 6 级女巫的升级时间减少。</TimelineRow>
        <TimelineRow>2 ~ 3 级女巫的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>5 级女巫的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>新增 15 本，并在 15 本新增 6 级女巫。</TimelineRow>
        <TimelineRow>3 ~ 5 级女巫的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/12/09">
        <TimelineRow>2 ~ 3 级女巫的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>女巫的训练时间由 360 秒减少到 240 秒。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/10/12">
        <TimelineRow>2 ~ 4 级女巫的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/04/02">
        <TimelineRow>2 ~ 4 级女巫的升级时间减少。</TimelineRow>
        <TimelineRow>1 ~ 4 级女巫的训练费用降低。</TimelineRow>
        <TimelineRow>3 ~ 4 级女巫的升级费用降低。</TimelineRow>
        <TimelineRow>12 本新增 5 级女巫，4 级女巫下放到 11 本，3 级下放到 10 本。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
