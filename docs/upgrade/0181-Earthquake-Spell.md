---
title: "部落冲突 coc 地震法术升级数据"
navTitle: "地震法术"
shownTitle: "地震法术"
module: upgrade-home
imgFolder: home_tech/0181
wiki: https://clashofclans.fandom.com/wiki/Earthquake_Spell
canonical: /upgrade/0181-Earthquake-Spell
dataSyncedOn: 2026-10-13
description: "用强烈的地震摧毁地面目标吧！地震法术造成的伤害受建筑最大生命值影响。对同一目标重复施放地震法术，造成的伤害将会递减。但是，没有任何城墙能抵抗四次地震法术！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0181-Earthquake-Spell.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2026-02-23'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Earthquake_Spell.png" :imgAlt="$frontmatter.navTitle"
    description="用强烈的地震摧毁地面目标吧！<br>地震法术造成的伤害受建筑最大生命值影响。对同一目标重复施放地震法术，造成的伤害将会递减。但是，没有任何城墙能抵抗四次地震法术！"
    :isSmallImg="true" />

<SmallTitle>重要说明</SmallTitle>

1. 4 瓶地震可以摧毁任何等级的 [城墙](/upgrade/0300-Walls)。
2. 从 6 级开始，地震法术可以对地面部队造成伤害。
3. 如果玩家操作得当，地震法术实际震开的范围会大于理论数据，参见『部落冲突』科普向之地震法术。
4. 地震法术不能对 [储金罐](/upgrade/0404-Gold-Storage)、[圣水瓶](/upgrade/0405-Elixir-Storage) 和 [暗黑重油罐](/upgrade/0406-Dark-Elixir-Storage) 造成伤害。
5. 当多瓶地震法术同时使用时，其伤害会有所不同。总体上来说，多个地震攻击建筑的伤害递减，对城墙递增。为方便起见，我们称第一瓶地震法术造成的伤害为**基准伤害**。如果你对具体公式感兴趣，那就展开看看吧！

14.5%：1 级地震对建筑的基准伤害是 14.5%，但游戏内显示 14%.<br>
14.5%：8 级地震对部队的基准伤害是 14.5%，但游戏内显示 14%.

</template>

<template #history>

<Timeline>
    <TimelineItem date="2026/02/23">
        <TimelineRow>现在地震法术可以对部队造成伤害了。</TimelineRow>
        <TimelineRow>推出 6 ~ 8 级地震法术。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/27">
        <TimelineRow>法术的配置时间取消，但新增了捐赠费用。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>2 ~ 5 级地震法术的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>5 级地震法术的升级时间减少。</TimelineRow>
        <TimelineRow>2 ~ 5 级地震法术的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/18">
        <TimelineRow>5 级地震法术的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>2 ~ 3 级地震法术的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>4 ~ 5 级地震法术的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/12/09">
        <TimelineRow>2 ~ 4 级地震法术的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>2 ~ 4 级地震法术的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/06/18">
        <TimelineRow>11 本新增 5 级地震法术。</TimelineRow>
        <TimelineRow>更新后，地震等级越高，作用范围越大，之前固定为 4 格半径。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
