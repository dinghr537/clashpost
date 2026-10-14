---
title: "部落冲突 coc 超级女巫升级数据"
navTitle: "超级女巫"
shownTitle: "超级女巫"
module: upgrade-home
imgFolder: home_tech/0605
wiki: https://clashofclans.fandom.com/wiki/Super_Witch
canonical: /upgrade/0605-Super-Witch
dataSyncedOn: 2026-10-13
description: "凝聚魔法，召唤强大力量。超级女巫召唤的不是成群的小骷髅兵，而是一个骨骼密度惊人的超大骷髅兵。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0605-Super-Witch.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2026-02-23'">

<template #introduction>

- *如想查看该兵种的普通版本，请访问：[女巫](/upgrade/0084-Witch)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Super_Witch_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

超级女巫的技能（大宝宝）：超级女巫会召唤一个体型超大的骷髅兵。

\* 第一个大骷髅在部署后 5 秒召唤，之后每 30 秒召唤一个。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2026/02/23">
        <TimelineRow>在 18 本新增 8 级女巫，超级部队的等级也相应更新。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2026/01/12">
        <TimelineRow>7 级超级女巫的每秒伤害和生命值增加。</TimelineRow>
        <TimelineRow>大宝宝占用的人口数由 10 调整为 20.</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/27">
        <TimelineRow>部队的训练时间取消，但增加了捐赠费用。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>大宝宝（超级女巫的骷髅巨人）占用的人口数由 20 调整为 10，这意味着它现在可以被隐形弹簧弹飞了。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/02/10">
        <TimelineRow>超级女巫的训练时间由 6:40 改为 5:33。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>16 本推出，并在 16 本新增 7 级女巫，超级部队的等级也相应更新。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>15 本推出，并在 15 本新增 6 级女巫，超级部队的等级也相应更新。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>超级女巫的训练时间由 1200 秒减少到 800 秒。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/12/07">
        <TimelineRow>超级部队的有效时间从 7 天缩短为 3 天。</TimelineRow>
        <TimelineRow>所有部队的强化费用统一调整为 25,000 暗黑重油。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/06/22">
        <TimelineRow>新超级兵：超级女巫。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
