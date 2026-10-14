---
title: "部落冲突 coc 超级野猪骑士升级数据"
navTitle: "超级野猪骑士"
shownTitle: "超级野猪骑士"
module: upgrade-home
imgFolder: home_tech/060f
wiki: https://clashofclans.fandom.com/wiki/Super_Hog_Rider
canonical: /upgrade/060f-Super-Hog-Rider
dataSyncedOn: 2026-10-13
description: "野猪和骑士这对可怕的组合如今实力更加强劲。他们既可一起冲锋陷阵，也能分开行动，继续并肩作战。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/060f-Super-Hog-Rider.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2026-02-23'">

<template #introduction>

- *如想查看该兵种的普通版本，请访问：[野猪骑士](/upgrade/0081-Hog-Rider)。*

<SwitchTabs contentClass="cp-unit-items" :stickyTabs="true" :pageTabs="true">
    <SwitchTab tabId="cp-unit-item-0" :activeTab="true">超级野猪骑士</SwitchTab>
    <SwitchTab tabId="cp-unit-item-1">超级野猪</SwitchTab>
    <SwitchTab tabId="cp-unit-item-2">超级骑士</SwitchTab>
</SwitchTabs>

<SwitchTabGroup id="cp-unit-item-0" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Super_Hog_Rider_info.png" imgAlt="超级野猪骑士"
    description="野猪和骑士这对可怕的组合如今实力更加强劲。他们既可一起冲锋陷阵，也能分开行动，继续并肩作战。" />

<SmallTitle>重要说明</SmallTitle>

超级野猪骑士的技能（分头作战）：被击倒后，野猪和骑士会分开，成为相互独立的部队。

</SwitchTabGroup>

<SwitchTabGroup id="cp-unit-item-1" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Super_Hog_info.png" imgAlt="超级野猪"
    description="没有骑士的野猪也能跃过城墙、攻击防御建筑。所以骑士一开始存在的意义是什么？" />

</SwitchTabGroup>

<SwitchTabGroup id="cp-unit-item-2" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Super_Rider_info.png" imgAlt="超级骑士"
    description="没有野猪的骑士依旧势不可挡，他会抡起锤子攻击所有周围的目标。" />

<SmallTitle>重要说明</SmallTitle>

超级骑士对城墙有两倍伤害，不过超级骑士没有攻击偏好。

</SwitchTabGroup>

</template>

<template #history>

<Timeline>
    <TimelineItem date="2026/02/23">
        <TimelineRow>18 本新增 15 级野猪骑士，超级部队的等级也相应更新。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/06/30">
        <TimelineRow>12 ~ 14 级超级野猪骑士的生命值增加。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/27">
        <TimelineRow>部队的训练时间取消，但增加了捐赠费用。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>17 本新增 14 级野猪骑士，超级部队的等级也相应更新。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/02/10">
        <TimelineRow>超级野猪骑士的训练时间由 1:50 改为 1:41</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/02/27">
        <TimelineRow>16 本新增 13 级野猪骑士，超级部队的等级也相应更新。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>新超级兵：超级野猪骑士。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
