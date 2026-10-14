---
title: "部落冲突 coc 隐形弹簧升级数据"
navTitle: "隐形弹簧"
shownTitle: "隐形弹簧"
module: upgrade-home
imgFolder: home_buildings/0381
wiki: https://clashofclans.fandom.com/wiki/Spring_Trap
canonical: /upgrade/0381-Spring-Trap
dataSyncedOn: 2026-10-13
description: "曾经有一个精妙的弹簧摆在我的面前，我没有看见，然后，就没有然后了！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0381-Spring-Trap.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-11-17'">

<template #introduction>

- 如想查看夜世界的隐形弹簧，请访问：[夜世界隐形弹簧](/upgrade/1181-Spring-Trap)。

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Spring_Trap_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

<SmallTitle>重要说明</SmallTitle>

2025/10 更新后，隐形弹簧重做。当前版本隐形弹簧的机制比较复杂，具体如下：

1. 隐形弹簧只会锁定作用范围内占用人口最大的单个地面部队。
2. 隐形弹簧对部队的作用机制如下：
    - 如果部队的占用人口数**未超出**弹簧弹射能力，无论该部队的剩余生命值是多少，都会被直接弹飞；
    - 如果部队的占用人口数**超出了**弹簧弹射能力，且部队的**剩余生命值足够**，可以承受弹簧的高额伤害，则该部队会被击晕并受到高额伤害；
    - 如果部队的占用人口数**超出了**弹簧弹射能力，且部队的**剩余生命值过低**，无法承受弹簧的高额伤害，则该部队会被直接弹飞；
3. 隐形弹簧对英雄、战宠和攻城机器的作用机制与部队类似，但它们不会被弹出地图，而是会播放常规的死亡动画。
    - 隐形弹簧可以对英雄、战宠和攻城机器造成**一半伤害**。
4. 如果同一部队在同一位置多次触发隐形弹簧，伤害不会叠加。
5. [大守护者](/upgrade/0202-Grand-Warden) 的 [永恒书卷](/upgrade/0780-Eternal-Tome) 装备无法阻止小单位部队被隐形弹簧弹飞，也无法使部队免疫弹簧的击退效果，但可以免疫大单位部队受到的伤害。
6. 现在隐形弹簧的反应比 [哥布林](/upgrade/0003-Goblin) 和 [超级炸弹人](/upgrade/0603-Super-Wall-Breaker) 都快，即使哥布林或超级炸弹人在移动，弹簧也可以弹飞它们。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/11/17">
        <TimelineRow>18 本推出，并在 18 本新增 13 级隐形弹簧。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/10/06">
        <TimelineRow>隐形弹簧重做，现在弹簧有 12 个等级了。</TimelineRow>
        <TimelineRow>5 级隐形弹簧的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>2 ~ 5 级隐形弹簧的升级时间减少。</TimelineRow>
        <TimelineRow>2 ~ 4 级隐形弹簧的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>4 级隐形弹簧的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/18">
        <TimelineRow>5 级隐形弹簧的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>2 ~ 5 级隐形弹簧的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>5 级隐形弹簧的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/12/09">
        <TimelineRow>4 ~ 5 级隐形弹簧的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>2 ~ 4 级隐形弹簧的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/06/22">
        <TimelineRow>13 本新增一个隐形弹簧。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/03/30">
        <TimelineRow>3 ~ 5 级隐形弹簧的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/02/28">
        <TimelineRow>隐形弹簧的触发半径由 0.7 格调整为 0.8 格。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/12/09">
        <TimelineRow>所有等级隐形弹簧可以弹飞的人口数减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/04/02">
        <TimelineRow>玩家上线后，所有的陷阱将自动被重新布置，重新布置不再需要花费金币。然而，如果玩家不上线，陷阱就不会被重新布置，所以你仍然可以攻击到陷阱失效的村庄。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
