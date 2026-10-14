---
title: "部落冲突 coc 炸弹人升级数据"
navTitle: "炸弹人"
shownTitle: "炸弹人"
module: upgrade-home
imgFolder: home_tech/0004
wiki: https://clashofclans.fandom.com/wiki/Wall_Breaker
canonical: /upgrade/0004-Wall-Breaker
dataSyncedOn: 2026-10-13
description: "只有轰塌一面面城墙才能让炸弹人那颗冰冷的心得到些许温暖。“砰”的一声巨响，他们为您的地面部队开道！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0004-Wall-Breaker.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-11-17'">

<template #introduction>

- *如想查看该兵种的强化版本，请访问：[超级炸弹人（超炸）](/upgrade/0603-Super-Wall-Breaker)。*
- *如想查看夜世界的炸弹兵，请访问：[夜世界炸弹兵](/upgrade/1004-Bomber)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Wall_Breaker_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

1. 不要把两层墙挨着摆，炸弹人可以炸到。下图中画出来的所有城墙都可以受到伤害。

<Pic src="/upgrade/description/Breaking_Walls_2.jpg" caption="炸弹人的伤害范围" :lazyLoading="false" maxWidth="10rem" width="284" height="228" />

2. 根据解析安装包的结果，炸弹人的攻速是一秒一次，也即每秒伤害等于每次伤害。但实际上它引爆炸弹后自身也会死亡，所以这个兵种不讨论攻速。下方所说的攻击伤害均为每次伤害。
3. 2020 年 10 月更新后，炸弹人的伤害分为主动伤害和死亡伤害，和 [超级炸弹人](/upgrade/0603-Super-Wall-Breaker) 一样。如果炸弹人成功爆破，则建筑受到炸弹人的主动伤害加死亡伤害；如果在爆破之前被打死了，并且死亡伤害波及到了建筑，则建筑受到炸弹人的死亡伤害。
4. 即使炸弹人被 [弹簧](/upgrade/0381-Spring-Trap) 弹飞，炸弹仍然会爆炸。
5. [狂暴法术](/upgrade/0102-Rage-Spell) 只会影响主动伤害，而不会影响死亡伤害。
6. [大守护者](/upgrade/0202-Grand-Warden) 的 [永恒书卷](/upgrade/0780-Eternal-Tome) 装备无法让炸弹人攻击后存活。
7. 2020 年 10 月更新后，对炸弹人而言，[弹跳法术](/upgrade/0103-Jump-Spell) 覆盖的城墙，等价于城墙消失。
8. 部分高本玩家会用“炸弹人”指代超级炸弹人，而非普通炸弹人，在看解说视频的时候需要注意一下。

9. 上方的“面板伤害”解释："10/9" 表示主动伤害为 10，死亡伤害为 9.
10. 上方的“中途死亡”指的是炸弹人中途死亡的爆炸伤害，“成功爆破”指的是炸弹人成功自爆的伤害。成功爆破的伤害是两个面板伤害加起来，再算上对城墙的 40 倍伤害。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/11/17">
        <TimelineRow>18 本推出，并在 18 本新增 14 级炸弹人。</TimelineRow>
        <TimelineRow>13 级炸弹人的升级时间和升级费用减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/10/06">
        <TimelineRow>7 ~ 12 级炸弹人的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/06/16">
        <TimelineRow>1 ~ 4 级炸弹人的主动伤害提升（死亡伤害不变）。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/27">
        <TimelineRow>部队的训练时间取消，但增加了捐赠费用。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>2 ~ 5、9 ~ 12 级炸弹人的升级时间减少。</TimelineRow>
        <TimelineRow>2 ~ 9、11 ~ 12 级炸弹人的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>17 本推出，并在 17 本新增 13 级炸弹人。</TimelineRow>
        <TimelineRow>3 ~ 7、9 ~ 12 级炸弹人的升级时间减少。</TimelineRow>
        <TimelineRow>7 ~ 12 级炸弹人的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/18">
        <TimelineRow>8、10 ~ 11 级炸弹人的升级时间减少。</TimelineRow>
        <TimelineRow>10 ~ 11 级炸弹人的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>16 本推出，同时在 16 本新增 12 级炸弹人。</TimelineRow>
        <TimelineRow>6 ~ 11 级炸弹人的升级时间减少。</TimelineRow>
        <TimelineRow>10 级炸弹人的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>8 ~ 9 级炸弹人的升级时间减少。</TimelineRow>
        <TimelineRow>8 ~ 9 级炸弹人的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>15 本推出，并在 15 本新增 11 级炸弹人。</TimelineRow>
        <TimelineRow>6 ~ 10 级炸弹人的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/12/09">
        <TimelineRow>4 ~ 9 级炸弹人的升级费用降低。</TimelineRow>
        <TimelineRow>2 ~ 9 级炸弹人的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>14 本推出，并在 14 本新增 10 级炸弹人。</TimelineRow>
        <TimelineRow>6 ~ 8 级的炸弹人的升级费用降低。</TimelineRow>
        <TimelineRow>3 ~ 8 级炸弹人的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/10/23">
        <TimelineRow>炸弹人的爆炸半径由 1.2 格提升到 1.5 格。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/10/12">
        <TimelineRow>炸弹人现在会使用弹跳法术跳过城墙。</TimelineRow>
        <TimelineRow>优化了炸弹人的 AI，让它们能更集中地锁定同一块城墙，降低它们被部署后分散攻击不同城墙的几率。假设你的炸弹人和城墙已升至你目前大本营所支持的最高等级：<br>
        - 1 个享受狂暴法术加成的炸弹人可以摧毁 1 块城墙。<br>
        - 9 级大本营及以下：2 个炸弹人最高可以摧毁 1 块 9 级城墙。<br>
        - 9 级大本营及以上：3 个炸弹人可以摧毁 1 块 10 级及以上的城墙。<br>
        - 9 级大本营及以上：6 个炸弹人的死亡附加伤害可以摧毁 1 块 10 级及以上的城墙。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020-03-30">
        <TimelineRow>5 ~ 6 级炸弹人的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019-12-09">
        <TimelineRow>13 本推出，并在 13 本新增 9 级炸弹人。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019-04-02">
        <TimelineRow>5 ~ 6 级炸弹人的升级时间减少。</TimelineRow>
        <TimelineRow>所有等级炸弹人的训练费用降低。</TimelineRow>
        <TimelineRow>5 ~ 8 级炸弹人的生命值提高。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
