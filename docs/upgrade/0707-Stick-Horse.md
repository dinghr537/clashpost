---
title: "部落冲突 coc 木棍马驹装备升级数据"
navTitle: "木棍马驹"
shownTitle: "木棍马驹"
module: upgrade-home
imgFolder: home_heroes/0707
wiki: https://clashofclans.fandom.com/wiki/Stick_Horse
canonical: /upgrade/0707-Stick-Horse
dataSyncedOn: 2026-10-13
description: "木棍马驹是野蛮人之王的第四件史诗装备，它在 2026 年 2 月的智慧勇士活动中首次开放购买。带上木棍马驹装备后，野蛮人之王可直接跃过城墙，且移动速度与攻击速度加快、伤害和生命值提高，这些加成与蛮王是否开启技能无关。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0707-Stick-Horse.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2026-02-09'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Stick_Horse_info.png" :imgAlt="$frontmatter.navTitle" description="部署后可直接跃过城墙，同时移动速度与攻击速度加快。" />

<SmallTitle>说明</SmallTitle>

1. 木棍马驹是 [野蛮人之王](/upgrade/0200-Barbarian-King) 的第四件史诗装备，它在 2026 年 2 月的智慧勇士活动中首次开放购买。
2. 带上木棍马驹装备后，野蛮人之王**可直接跃过城墙**，且移动速度与攻击速度加快、伤害和生命值提高。这些加成与蛮王是否开启技能无关。

注意：
3. 上表的 8 点移动速度代表 1 格/秒。
4. 如果升级费用中有多种资源，则同时需要多种资源才能升级。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2026/02/09">
        <TimelineRow>新装备：木棍马驹。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
