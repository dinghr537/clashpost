---
title: "部落冲突 coc 都城野猪突袭队（野猪特攻队）升级数据"
navTitle: "野猪突袭队"
shownTitle: "野猪突袭队（野猪特攻队）"
module: upgrade-capital
imgFolder: capital_tech/200b
wiki: https://clashofclans.fandom.com/wiki/Hog_Raiders
canonical: /upgrade/200b-Hog-Raiders
dataSyncedOn: 2026-10-13
description: "野猪骑士和野猪飞骑的完美结合，掀起一场野猪突袭派对！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/200b-Hog-Raiders.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2022-05-02'">

<template #introduction>

- *如想查看家乡的野猪骑士，请访问：[野猪骑士](/upgrade/0081-Hog-Rider)。*
- *如想查看夜世界的野猪飞骑，请访问：[夜世界野猪飞骑](/upgrade/100a-Hog-Glider)。*
- *如想查看飞行堡垒的派生兵种骷髅飞骑，请访问该页面后切换到骷髅飞骑：[都城骷髅飞骑](/upgrade/2008-Flying-Fortress)。*

<SwitchTabs contentClass="cp-unit-items" :stickyTabs="true" :pageTabs="true">
    <SwitchTab tabId="cp-unit-item-0" :activeTab="true">野猪突袭队</SwitchTab>
    <SwitchTab tabId="cp-unit-item-1">野猪飞骑</SwitchTab>
    <SwitchTab tabId="cp-unit-item-2">野猪骑士</SwitchTab>
</SwitchTabs>

<SwitchTabGroup id="cp-unit-item-0" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Hog_Raiders_info.png" imgAlt="野猪突袭队"
    description="野猪骑士和野猪飞骑的完美结合，掀起一场野猪突袭派对！" />

<SmallTitle>重要说明</SmallTitle>

1. 野猪突袭队的解锁条件是建造 [野猪突袭队训练营](/upgrade/234b-Hog-Raider-Barracks)，而这需要部落解锁飞龙悬崖，且 [都城大本营](/upgrade/2400-Capital-Hall) 达到 6 级。
2. 野猪突袭队在部署之前是一个整体，你不能把野猪飞骑和野猪骑士分开部署。

</SwitchTabGroup>

<SwitchTabGroup id="cp-unit-item-1" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Hog_Glider_info.png" imgAlt="野猪飞骑"
    description="当之无愧的空中骑士！他们是翻越城墙的专家，但不太擅长平稳着陆，容易撞上建筑。" />

<SmallTitle>重要说明</SmallTitle>

1. 野猪飞骑的技能（奇袭俯冲）：野猪飞骑的首次攻击将使被击中的敌方防御建筑瘫痪一段时间，然后他将跳下滑翔翼，变回普通的野猪骑士。
2. 如果野猪飞骑在攻击目标建筑前被击落，他将失去飞行能力，变回普通野猪骑士。

</SwitchTabGroup>

<SwitchTabGroup id="cp-unit-item-2" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Hog_Rider_info.png" imgAlt="野猪骑士"
    description="滑翔翼被摧毁后，战场上将出现一人一猪两位勇士，他们可以轻松跃过城墙，继续为您战斗。" />

<SmallTitle>重要说明</SmallTitle>

和家乡的 [野猪骑士](/upgrade/0081-Hog-Rider) 一样，都城的野猪其实也可以敏捷地跃过城墙，优先攻击敌方的防御建筑。

</SwitchTabGroup>

</template>

<template #history>

<Timeline>
    <TimelineItem date="2022/05/02">
        <TimelineRow>野猪突袭队随着部落都城玩法一同推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
