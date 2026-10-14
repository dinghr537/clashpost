---
title: "部落冲突 coc 超级巨石投手（超级蓝胖、超蓝）升级数据"
navTitle: "超级巨石投手"
shownTitle: "超级巨石投手（超级蓝胖、超蓝）"
module: upgrade-home
imgFolder: home_tech/060c
wiki: https://clashofclans.fandom.com/wiki/Super_Bowler
canonical: /upgrade/060c-Super-Bowler
dataSyncedOn: 2026-10-13
description: "如今，超级巨石投手拥有了他想要的一切：一副抓得更稳的手套、更舒服的鞋子，还有很多大到离谱的巨石。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/060c-Super-Bowler.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-11-17'">

<template #introduction>

- *如想查看该兵种的普通版本，请访问：[巨石投手](/upgrade/0086-Bowler)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Super_Bowler.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

超级巨石投手的技能（三重打击）：超级巨石投手扔出的石头可以连续弹跳击中 3 个目标，并能造成额外溅射伤害。

\* 超级巨石投手扔出去的石头落地后可以造成三次伤害。石头的第一个落地距离超级蓝胖 3 格，第二个落点距离蓝胖 6 格，第三个是 9 格。和普通蓝胖类似，超级蓝胖只能看到第一个目标，二次伤害和三次伤害都是顺带的，它并不知道石头会溅到哪儿。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/11/17">
        <TimelineRow>18 本推出，并在 18 本新增 10 级巨石投手，超级部队的等级也相应更新。</TimelineRow>
        <TimelineRow>9 级超级巨石投手的每秒伤害和生命值增加。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/06/30">
        <TimelineRow>7 ~ 9 级超级巨石投手的生命值增加。</TimelineRow>
        <TimelineRow>7 ~ 9 级超级巨石投手的每秒伤害提升。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/27">
        <TimelineRow>部队的训练时间取消，但增加了捐赠费用。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/02/10">
        <TimelineRow>超级巨石投手的训练时间由 5:00 改为 4:10</TimelineRow>
        <TimelineRow>17 本新增 9 级巨石投手，超级部队的等级也相应更新。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/02/27">
        <TimelineRow>16 本新增 8 级巨石投手，超级部队的等级也相应更新。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>15 本新增 7 级巨石投手，超级部队的等级也相应更新。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/09/27">
        <TimelineRow>新超级兵：超级巨石投手。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
