---
title: "部落冲突 coc 都城超级矿工升级数据"
navTitle: "超级矿工"
shownTitle: "超级矿工"
module: upgrade-capital
imgFolder: capital_tech/200f
wiki: https://clashofclans.fandom.com/wiki/Super_Miner/Clan_Capital
canonical: /upgrade/200f-Super-Miner
dataSyncedOn: 2026-10-13
description: "拿着大钻机，留着拉风的胡子，这位超级矿工随时准备暗中破坏敌方防御！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/200f-Super-Miner.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2024-02-27'">

<template #introduction>

- *如想查看家乡的超级矿工，请访问：[超级矿工](/upgrade/060e-Super-Miner)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Super_Miner_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

1. 超级矿工的解锁条件是建造 [超级矿工训练营](/upgrade/234f-Super-Miner-Barracks)，而这需要部落解锁哥布林矿井，且 [都城大本营](/upgrade/2400-Capital-Hall) 达到 9 级。
2. 超级矿工可以绕过水和悬崖。
3. 超级矿工专注于一个目标的时间越长，他的钻头每秒造成的伤害就越高，这个机制与 [地狱之塔](/upgrade/030a-Inferno-Tower) 和 [地狱飞龙](/upgrade/0604-Inferno-Dragon) 类似。
4. 超级矿工的技能（终极大爆炸）：超级矿工死亡后会对一个区域内的所有地面单位造成伤害。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2024/02/27">
        <TimelineRow>所有等级超级矿工的生命值减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/11/27">
        <TimelineRow>1 级超级矿工的秒伤由 170-340-510 减少到 160-340-630.</TimelineRow>
        <TimelineRow>2 级超级矿工的秒伤由 190-380-570 减少到 170-370-660.</TimelineRow>
        <TimelineRow>3 级超级矿工的秒伤由 210-420-630 减少到 180-400-690.</TimelineRow>
        <TimelineRow>4 级超级矿工的秒伤由 230-460-690 减少到 190-430-720.</TimelineRow>
        <TimelineRow>2 ~ 4级超级矿工的生命值由 4000/4300/4600 减少到 3900/4100/4300.</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/10/09">
        <TimelineRow>都城新增超级矿工，推出 4 个等级。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
