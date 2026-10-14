---
title: "部落冲突 coc 蝙蝠法术升级数据"
navTitle: "蝙蝠法术"
shownTitle: "蝙蝠法术"
module: upgrade-home
imgFolder: home_tech/0184
wiki: https://clashofclans.fandom.com/wiki/Bat_Spell
canonical: /upgrade/0184-Bat-Spell
dataSyncedOn: 2026-10-13
description: "在战场上任意地点召唤一群蝙蝠大军！在您最需要空中支援时施放蝙蝠法术。蝙蝠不会触发陷阱。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0184-Bat-Spell.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-11-17'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Bat_Spell.png" :imgAlt="$frontmatter.navTitle"
    description="在战场上任意地点召唤一群蝙蝠大军！<br>在您最需要空中支援时施放蝙蝠法术。蝙蝠不会触发陷阱。"
    :isSmallImg="true" />

<SmallTitle>重要说明</SmallTitle>

1. 蝙蝠的第一次出手在到达防御建筑之后的 1.5 秒，而 [法师塔](/upgrade/0305-Wizard-Tower) 的攻速为 1.3 秒/次，故蝙蝠怕法师塔。
2. 蝙蝠对 [大本营](/upgrade/0400-Town-Hall) 和资源罐的伤害为对其他建筑的 15%.
3. 蝙蝠无法触发城堡内的援兵。
4. 虽然蝙蝠本身无法触发陷阱，但是被其他空军触发的陷阱还是有可能攻击蝙蝠。

\* 第一次生成 2 个蝙蝠，之后每 0.6 秒生成一个。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/11/17">
        <TimelineRow>18 本推出，并在 18 本新增 8 级蝙蝠法术。</TimelineRow>
        <TimelineRow>7 级蝙蝠法术的升级时间和升级费用减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/10/06">
        <TimelineRow>6 级蝙蝠法术的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/27">
        <TimelineRow>法术的配置时间取消，但新增了捐赠费用。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>17 本新增 7 级蝙蝠法术。</TimelineRow>
        <TimelineRow>2 ~ 6 级蝙蝠法术的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>2 ~ 6 级蝙蝠法术的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/18">
        <TimelineRow>3 级和 6 级蝙蝠法术的升级时间减少。</TimelineRow>
        <TimelineRow>6 级蝙蝠法术的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>6 级蝙蝠法术的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>5 级蝙蝠法术的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>15 本推出，并在 15 本新增 6 级蝙蝠法术。</TimelineRow>
        <TimelineRow>2 ~ 5 级蝙蝠法术的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/12/09">
        <TimelineRow>4 ~ 5 级蝙蝠法术的升级费用降低。</TimelineRow>
        <TimelineRow>2 ~ 3 级蝙蝠法术的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>2 ~ 3 级蝙蝠法术的升级费用降低。</TimelineRow>
        <TimelineRow>2 ~ 4 级蝙蝠法术的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
