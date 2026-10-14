---
title: "部落冲突 coc 超级矿工（超矿）升级数据"
navTitle: "超级矿工"
shownTitle: "超级矿工（超矿）"
module: upgrade-home
imgFolder: home_tech/060e
wiki: https://clashofclans.fandom.com/wiki/Super_Miner
canonical: /upgrade/060e-Super-Miner
dataSyncedOn: 2026-10-13
description: "拿着大钻机，留着拉风的胡子，这位超级矿工随时准备暗中破坏敌方防御！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/060e-Super-Miner.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-11-17'">

<template #introduction>

- *如想查看该兵种的普通版本，请访问：[掘地矿工](/upgrade/000b-Miner)。*
- *如想查看都城的超级矿工，请访问：[都城超级矿工](/upgrade/200f-Super-Miner)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Super_Miner_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

1. 超级矿工的技能（终极大爆炸）：被消灭时丢下一个炸药桶。
2. 超级矿工使用钻机进行攻击，攻击时间越长伤害越高，类似于 [地狱飞龙](/upgrade/0604-Inferno-Dragon)。
3. 超级矿工能免疫 [飓风陷阱](/upgrade/0386-Tornado-Trap) 的转圈效果。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/11/17">
        <TimelineRow>18 本推出，并在 18 本新增 12 级掘地矿工，超级部队的等级也相应更新。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/06/30">
        <TimelineRow>7 ~ 11 级超级矿工的生命值增加。</TimelineRow>
        <TimelineRow>9 ~ 11 级超级矿工的每秒伤害提升。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/27">
        <TimelineRow>部队的训练时间取消，但增加了捐赠费用。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/02/10">
        <TimelineRow>17 本新增 11 级掘地矿工，超级部队的等级也相应更新。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>16 本推出，并在 16 本新增 10 级掘地矿工，超级部队的等级也相应更新。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>9 级超级矿工的生命值由 3200 提升到 3500。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/12/12">
        <TimelineRow>新超级兵：超级矿工。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
