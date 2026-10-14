---
title: "部落冲突 coc 戈仑石人（石头人）升级数据"
navTitle: "戈仑石人"
shownTitle: "戈仑石人（石头人）"
module: upgrade-home
imgFolder: home_tech/0083
wiki: https://clashofclans.fandom.com/wiki/Golem
canonical: /upgrade/0083-Golem
dataSyncedOn: 2026-10-13
description: "戈仑石人乐于吸收伤害。被摧毁时，他们会爆炸并分裂成小戈仑石人。每个小戈仑石人拥有原戈仑石人 1/5 的攻击力和生命值。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0083-Golem.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-11-17'">

<template #introduction>

- *本页面的内容不是戈仑冰人，如想查看戈仑冰人的页面，请访问：[戈仑冰人](/upgrade/0087-Ice-Golem)。*
- *如想查看陨石戈仑，请访问：[陨石戈仑](/upgrade/0012-Meteor-Golem)、[陨石戈仑（临时兵种）](/upgrade/0e1b-Meteor-Golem)。*
- *如想查看都城的高山戈仑，请访问：[都城高山戈仑](/upgrade/200d-Mountain-Golem)。*

<SwitchTabs contentClass="cp-unit-items" :stickyTabs="true" :pageTabs="true">
    <SwitchTab tabId="cp-unit-item-0" :activeTab="true">戈仑石人</SwitchTab>
    <SwitchTab tabId="cp-unit-item-1">小戈仑石人</SwitchTab>
</SwitchTabs>

<SwitchTabGroup id="cp-unit-item-0" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Golem_info.png" imgAlt="戈仑石人"
    description="戈仑石人乐于吸收伤害。被摧毁时，他们会爆炸并分裂成小戈仑石人。每个小戈仑石人拥有原戈仑石人 1/5 的攻击力和生命值。" />

<SmallTitle>重要说明</SmallTitle>

1. 戈仑石人死亡后会分裂成若干小戈仑石人（小石头人）。
2. 根据玩家解安装包的结果，小石头人占用 6 空间，可被 [隐形弹簧](/upgrade/0381-Spring-Trap) 弹飞。
3. 自 2024 年 6 月平衡性调整起，小石头人的生命值不再固定为大石头人的五分之一，但游戏内的介绍还是保留了五分之一这个说法。

</SwitchTabGroup>

<SwitchTabGroup id="cp-unit-item-1" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Golemite_info.png" imgAlt="小戈仑石人"
    description="小戈仑石人是由这个巨大生物孕育的更小的戈仑石人。当戈仑石人被摧毁时，小戈仑石人被赋予生命并继续战斗！" />

<SmallTitle>重要说明</SmallTitle>

1. 戈仑石人死亡后会分裂成若干小戈仑石人（小石头人）。
2. 根据玩家解安装包的结果，小石头人占用 6 空间，可被 [隐形弹簧](/upgrade/0381-Spring-Trap) 弹飞。
3. 自 2024 年 6 月平衡性调整起，小石头人的生命值不再固定为大石头人的五分之一，但游戏内的介绍还是保留了五分之一这个说法。

</SwitchTabGroup>

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/11/17">
        <TimelineRow>14 级戈仑石人的升级时间和升级费用减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/10/06">
        <TimelineRow>3 ~ 13 级戈仑石人的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/27">
        <TimelineRow>部队的训练时间取消，但增加了捐赠费用。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>在 17 本新增 14 级戈仑石人。</TimelineRow>
        <TimelineRow>2、7 ~ 13 级戈仑石人的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/02/10">
        <TimelineRow>戈仑石人的训练时间由 5:00 改为 4:20</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>2 ~ 13 级戈仑石人的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/18">
        <TimelineRow>11 ~ 12 级戈仑石人的升级时间减少。</TimelineRow>
        <TimelineRow>11 ~ 12 级戈仑石人的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/03">
        <TimelineRow>7 ~ 11 级戈仑石人的生命值提升，小戈仑石人的数据没有变化，因此现在小石头人的生命值不再固定为大石头人的五分之一。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>新增 16 本，并在 16 本新增 13 级戈仑石人。</TimelineRow>
        <TimelineRow>4 ~ 12 级戈仑石人的升级时间减少。</TimelineRow>
        <TimelineRow>2 ~ 5、11 级戈仑石人的升级费用降低。</TimelineRow>
        <TimelineRow>天使治疗戈仑石人、小戈仑石人、戈仑冰人的几率降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>8 ~ 10 级戈仑石人的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>新增 15 本，并在 15 本新增 12 级戈仑石人。</TimelineRow>
        <TimelineRow>5 ~ 11 级戈仑石人的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/12/09">
        <TimelineRow>2 ~ 4 级戈仑石人的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/09/27">
        <TimelineRow>14 本新增 11 级戈仑石人。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>2 ~ 6、8 级戈仑石人的升级时间减少。</TimelineRow>
        <TimelineRow>2 ~ 9 级戈仑石人的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/10/12">
        <TimelineRow>2 ~ 8 级戈仑石人的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/06/22">
        <TimelineRow>13 本新增 10 级戈仑石人。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/03/30">
        <TimelineRow>2 ~ 7 级戈仑石人的升级费用降低。</TimelineRow>
        <TimelineRow>天使治疗小戈仑石人的几率降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/09/11">
        <TimelineRow>1 ~ 3 级戈仑石人的伤害降低，5 ~ 9 级戈仑石人的伤害提高。</TimelineRow>
        <TimelineRow>8 ~ 9 级戈仑石人爆炸后分裂的小戈仑石人从 2 个增加至 3 个。</TimelineRow>
        <TimelineRow>1 ~ 3 级小戈仑石人的生命值提高。</TimelineRow>
        <TimelineRow>现在小戈仑石人的每秒伤害固定为戈仑石人的五分之一。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/06/18">
        <TimelineRow>12 本新增 9 级戈仑石人。</TimelineRow>
        <TimelineRow>5 ~ 8 级戈仑石人和小戈仑石人被摧毁时造成的伤害增加。</TimelineRow>
        <TimelineRow>戈仑石人被摧毁时造成伤害的半径从 1.2 格提升至 1.5 格。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/04/02">
        <TimelineRow>包含大量降低发展成本和提高发展速度的调整，其中所有等级戈仑石人的训练费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
