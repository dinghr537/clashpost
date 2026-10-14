---
title: "部落冲突 coc 超级法师（超法）升级数据"
navTitle: "超级法师"
shownTitle: "超级法师（超法）"
module: upgrade-home
imgFolder: home_tech/0609
wiki: https://clashofclans.fandom.com/wiki/Super_Wizard
canonical: /upgrade/0609-Super-Wizard
dataSyncedOn: 2026-10-13
description: "超级法师全身充满了魔法能量！他可能是实验室里最聪明的人，但也有可能会把实验室炸上天。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0609-Super-Wizard.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2026-01-28'">

<template #introduction>

- *如想查看该兵种的普通版本，请访问：[法师](/upgrade/0006-Wizard)。*
- *如想查看夜世界的电火法师，请访问：[夜世界电火法师](/upgrade/100b-Electrofire-Wizard)。*
- *如想查看都城的超级法师，请访问：[都城超级法师](/upgrade/2005-Super-Wizard)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Super_Wizard_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

1. 超级法师的技能（链式魔法）：超级法师的链式魔法攻击可以弹射伤害多个目标，只要这些目标在他初始目标的溅射范围内。它就可以同时对多个目标造成伤害。
2. 超级法师的闪电链和 [雷电飞龙](/upgrade/000c-Electro-Dragon) 不同，雷电飞龙的每次连锁有一定延迟，而超级法师除了正在攻击的目标之外，其他目标是一起掉血的。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2026/01/28">
        <TimelineRow>所有等级超级法师的生命值提升。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/11/17">
        <TimelineRow>18 本推出，并在 18 本新增 14 级法师，超级部队的等级也相应更新。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/06/30">
        <TimelineRow>11 ~ 13 级超级法师的每秒伤害提升。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/27">
        <TimelineRow>部队的训练时间取消，但增加了捐赠费用。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>17 本推出，并在 17 本新增 13 级法师，超级部队的等级也相应更新。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>16 本推出，并在 16 本新增 12 级法师，超级部队的等级也相应更新。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>15 本推出，并在 15 本新增 11 级法师，超级部队的等级也相应更新。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/01/20">
    <TimelineRow>超级法师连锁后的伤害由 60% 降低到 40%.</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/12/07">
    <TimelineRow>新超级兵：超级法师。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
