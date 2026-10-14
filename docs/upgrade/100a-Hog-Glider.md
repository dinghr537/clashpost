---
title: "部落冲突 coc 夜世界野猪飞骑（飞猪骑士）升级数据"
navTitle: "野猪飞骑"
shownTitle: "野猪飞骑（飞猪骑士）"
module: upgrade-bh
imgFolder: bh_tech/100a
wiki: https://clashofclans.fandom.com/wiki/Hog_Glider
canonical: /upgrade/100a-Hog-Glider
dataSyncedOn: 2026-10-13
description: "当之无愧的空中骑士！他们是翻越城墙的专家，但不太擅长平稳着陆，容易撞上建筑。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/100a-Hog-Glider.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-05-15'">

<template #introduction>

- *如想查看家乡的野猪骑士，请访问：[野猪骑士](/upgrade/0081-Hog-Rider)。*
- *如想查看都城的野猪突袭队，请访问：[都城野猪突袭队](/upgrade/200b-Hog-Raiders)。*

<SwitchTabs contentClass="cp-unit-items" :stickyTabs="true" :pageTabs="true">
    <SwitchTab tabId="cp-unit-item-0" :activeTab="true">野猪飞骑</SwitchTab>
    <SwitchTab tabId="cp-unit-item-1">野猪骑士</SwitchTab>
</SwitchTabs>

<SwitchTabGroup id="cp-unit-item-0" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Hog_Glider_info.png" imgAlt="野猪飞骑"
    description="当之无愧的空中骑士！他们是翻越城墙的专家，但不太擅长平稳着陆，容易撞上建筑。" />

</SwitchTabGroup>

<SwitchTabGroup id="cp-unit-item-1" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Hog_Rider_info.png" imgAlt="野猪骑士"
    description="滑翔翼被摧毁后，战场上将出现一人一猪两位勇士，他们可以轻松跃过城墙，继续为您战斗。" />

</SwitchTabGroup>

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/05/15">
        <TimelineRow>新增 19 - 20 级野猪飞骑。</TimelineRow>
        <TimelineRow>由于夜世界重做，部队的伤害、生命值等数据都有变化。</TimelineRow>
        <TimelineRow>现在野猪飞骑一解锁就是 15 级，你不需要从 1 级开始升了。如果更新前部队高于 15 级，更新后等级不会重置。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/05/02">
        <TimelineRow>夜世界所有空军的攻击距离减少 0.5 格（蝙蝠除外）。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/09/11">
        <TimelineRow>18 级野猪飞骑分裂后的野猪骑士的生命值降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/06/18">
        <TimelineRow>夜世界 9 本开放，新兵种：野猪飞骑。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
