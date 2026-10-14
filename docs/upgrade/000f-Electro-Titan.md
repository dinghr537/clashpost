---
title: "部落冲突 coc 雷霆泰坦（雷电泰坦）升级数据"
navTitle: "雷霆泰坦"
shownTitle: "雷霆泰坦（雷电泰坦）"
module: upgrade-home
imgFolder: home_tech/000f
wiki: https://clashofclans.fandom.com/wiki/Electro_Titan
canonical: /upgrade/000f-Electro-Titan
dataSyncedOn: 2026-10-13
description: "雷霆泰坦从不控制自己与生俱来的魔力，在战场上，她就是无比强大的存在。她将自己的一部分魔力转化为一条威力十足的电鞭，而剩下的魔力则围绕在她身边，破坏周遭的一切。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/000f-Electro-Titan.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2026-02-23'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Electro_Titan_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

1. 雷霆泰坦光环范围内的敌方兵种、英雄和建筑会持续掉血。
2. 只要光环覆盖到建筑的判定面积就可以对建筑造成持续伤害。
3. 雷霆泰坦的光环无法对 [城墙](/upgrade/0300-Walls) 造成伤害。
4. 雷霆泰坦的光环对英雄的伤害只有普通兵种的 25%.
5. 雷霆泰坦的光环可以对隐形状态下的部队和建筑造成伤害。
6. [狂暴法术](/upgrade/0102-Rage-Spell) 只能提升雷霆泰坦的普通攻击，不能提升雷霆泰坦的光环伤害。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2026/02/23">
        <TimelineRow>在 18 本新增了 5 级雷霆泰坦。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2026/01/28">
        <TimelineRow>4 级雷霆泰坦的生命值由 8400 提升到 8700.</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/10/06">
        <TimelineRow>3 ~ 4 级雷霆泰坦的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/27">
        <TimelineRow>部队的训练时间取消，但增加了捐赠费用。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>2 ~ 4 级雷霆泰坦的升级时间减少。</TimelineRow>
        <TimelineRow>3 级雷霆泰坦的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/02/10">
        <TimelineRow>雷霆泰坦的训练时间由 6:00 改为 4:30</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>2 ~ 4 级雷霆泰坦的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/04/17">
        <TimelineRow>在 16 本新增 4 级雷霆泰坦。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>2 ~ 3 级雷霆泰坦的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/05/15">
        <TimelineRow>增加雷霆泰坦的「大守护者权重」，让大守护者更有可能跟随他们。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>15 本推出，并在 14 本新增新兵种：雷霆泰坦。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
