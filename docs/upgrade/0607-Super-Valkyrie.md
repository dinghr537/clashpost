---
title: "部落冲突 coc 超级瓦基丽武神升级数据"
navTitle: "超级瓦基丽武神"
shownTitle: "超级瓦基丽武神"
module: upgrade-home
imgFolder: home_tech/0607
wiki: https://clashofclans.fandom.com/wiki/Super_Valkyrie
canonical: /upgrade/0607-Super-Valkyrie
dataSyncedOn: 2026-10-13
description: "比起普通的瓦基丽武神，超级瓦基丽武神无论在哪一方面都更加优秀，而且她们也暴躁得多！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0607-Super-Valkyrie.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-03-27'">

<template #introduction>

- *如想查看该兵种的普通版本，请访问：[瓦基丽武神](/upgrade/0082-Valkyrie)。*
- *如想查看作为临时兵种推出的超级强化版本，请访问：[铁臂终结者](/upgrade/0e19-The-Disarmer)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Super_Valkyrie_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

超级武神的技能（临别赠礼）：死亡时丢下一个狂暴法术。

\* 这里的 8 点移动速度等于 1 格/秒，26 点移动速度就是 3.25 格/秒。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/03/27">
        <TimelineRow>部队的训练时间取消，但增加了捐赠费用。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/02/10">
        <TimelineRow>超级瓦基丽武神的训练时间由 3:45 改为 2:55</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>16 本推出，并在 16 本新增 11 级瓦基丽武神，超级部队的等级也相应更新。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>15 本新增 10 级瓦基丽武神，超级部队的等级也相应更新。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/06/27">
        <TimelineRow>攻击速度：从 1.8 秒缩短至 1.1 秒。</TimelineRow>
        <TimelineRow>移动速度：从每秒 3.5 格降低至每秒 3 格。</TimelineRow>
        <TimelineRow>狂暴法术范围：从 3.5 格提升至 4 格。</TimelineRow>
        <TimelineRow>所有等级超级瓦基丽武神的生命值提升。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>14 本推出，并在 14 本新增 9 级瓦基丽武神，超级部队的等级也相应更新。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/12/07">
        <TimelineRow>超级部队的有效时间从 7 天缩短为 3 天。</TimelineRow>
        <TimelineRow>所有部队的强化费用统一调整为 25,000 暗黑重油。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/10/12">
        <TimelineRow>新超级兵：超级瓦基丽武神。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
