---
title: "部落冲突 coc 火箭气球兵（超球）升级数据"
navTitle: "火箭气球兵"
shownTitle: "火箭气球兵（超球）"
module: upgrade-home
imgFolder: home_tech/060b
wiki: https://clashofclans.fandom.com/wiki/Rocket_Balloon
canonical: /upgrade/060b-Rocket-Balloon
dataSyncedOn: 2026-10-13
description: "气球兵重装升级为火箭气球兵，最新配备的两个火箭助推器都已通过严格的安全检查，助力气球快速飞入战场！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/060b-Rocket-Balloon.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-06-16'">

<template #introduction>

- *如想查看该兵种的普通版本，请访问：[气球兵](/upgrade/0005-Balloon)。*
- *如想查看都城的火箭气球兵，请访问：[都城火箭气球兵](/upgrade/2006-Rocket-Balloon)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Rocket_Balloon_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

火箭气球兵的技能（急速飞行）：在部署后的 4 秒内提升移动速度。加速状态下火箭气球兵的移动速度是 64，即 8 格/秒。

\* 5 - 7 级火箭气球兵只在 奖章活动 中出现，不能通过常规方式得到。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/06/16">
        <TimelineRow>在 17 本新增 12 级气球兵，超级部队的等级也相应更新。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/27">
        <TimelineRow>部队的训练时间取消，但增加了捐赠费用。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/04/09">
        <TimelineRow>8 ~ 10 级火箭气球兵的每秒伤害提升。</TimelineRow>
        <TimelineRow>8 ~ 10 级火箭气球兵的死亡伤害提升。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>16 本推出，并在 16 本新增 11 级气球兵，超级部队的等级也相应更新。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/05/02">
        <TimelineRow>家乡所有空军的攻击距离减少 0.5 格（超级飞龙除外，这玩意削了 1 格）。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/06/15">
        <TimelineRow>新超级兵：火箭气球兵。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
