---
title: "部落冲突 coc 女巫戈仑升级数据"
navTitle: "女巫戈仑"
shownTitle: "女巫戈仑"
module: upgrade-temp
imgFolder: temp_troops/0e0c
wiki: https://clashofclans.fandom.com/wiki/Witch_Golem
canonical: /upgrade/0e0c-Witch-Golem
dataSyncedOn: 2026-10-13
description: "戈仑坚如磐石加上女巫神奇的暗黑魔法，这个可怕的合体兵种能轻松摧毁敌方防御！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0e0c-Witch-Golem.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2024-10-11'">

<template #introduction>

<SwitchTabs contentClass="cp-unit-items" :stickyTabs="true" :pageTabs="true">
    <SwitchTab tabId="cp-unit-item-0" :activeTab="true">女巫戈仑</SwitchTab>
    <SwitchTab tabId="cp-unit-item-1">骷髅</SwitchTab>
    <SwitchTab tabId="cp-unit-item-2">大宝宝</SwitchTab>
</SwitchTabs>

<SwitchTabGroup id="cp-unit-item-0" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Witch_Golem_info.png" imgAlt="女巫戈仑"
    description="戈仑坚如磐石加上女巫神奇的暗黑魔法，这个可怕的合体兵种能轻松摧毁敌方防御！" />

<SmallTitle>重要说明</SmallTitle>

女巫戈仑在 2023 年 10 月的合体狂潮活动中首次推出，在活动中获取 55 000 酸腐圣水（任务点数）即可解锁，并在 2024 年 10 月的合体狂热活动中返场，这次只需 3 000 酸腐圣水即可解锁。

\* 每隔几秒会召唤骷髅军团。被击倒时还会召唤多个大宝宝。

\# 女巫戈仑并不是每次召唤都可以召唤出这么多骷髅，当一只女巫戈仑召唤的骷髅达到上表的限制时，除非骷髅兵死亡，否则女巫戈仑不会继续召唤。这个上限指的是每只女巫戈仑召唤的骷髅，如果有两只女巫戈仑，那么场上的最大骷髅数量为 2 倍上限。
</SwitchTabGroup>

<SwitchTabGroup id="cp-unit-item-1" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Skeleton_Witch_Golem_info.png" imgAlt="女巫戈仑召唤的骷髅"
    description="这个不死生物本身并不可怕，但它从不单独作战，因为女巫戈仑可以召唤无数骷髅兵来对付敌人！" />

<SmallTitle>重要说明</SmallTitle>

这个骷髅兵的属性与 [女巫](/upgrade/0084-Witch) 召唤出来的骷髅相同，至少女巫戈仑最后一次推出时是相同的。

</SwitchTabGroup>

<SwitchTabGroup id="cp-unit-item-2" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Big_Boy_Witch_Golem.png" imgAlt="女巫戈仑召唤的大宝宝"
    description="每天一桶奶，养成大骷髅。大宝宝绝对是史上最大的骷髅兵，但别看他样子吓人，其实他还是个离不开妈妈的宝宝。" />

<SmallTitle>重要说明</SmallTitle>

这个骷髅兵的属性与 [超级女巫](/upgrade/0605-Super-Witch) 召唤出来的大宝宝不同，不可套用超级女巫的那个大宝宝的数据。

</SwitchTabGroup>

</template>

<template #history>

<Timeline>
    <TimelineItem date="2024/10/11">
        <TimelineRow>该兵种第 2 次推出，是 2024 年合体狂热活动中的五个临时兵种之一。</TimelineRow>
        <TimelineRow>与 2023 版相比，该兵种新增了第 11 个等级。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/10/20">
        <TimelineRow>所有等级的大宝宝的每秒伤害增加 20%.</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/10/13">
        <TimelineRow>该兵种第 1 次推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
