---
title: "部落冲突 coc 建筑工人小屋升级数据"
navTitle: "建筑工人小屋"
shownTitle: "建筑工人小屋"
module: upgrade-home
imgFolder: home_buildings/0500
wiki: https://clashofclans.fandom.com/wiki/Builder%27s_Hut
canonical: /upgrade/0500-Builders-Hut
dataSyncedOn: 2026-10-13
description: "没有建筑工人一切都免谈！您可以雇佣多个建筑工人同时开始多个项目的建造或升级，或者使用宝石加快施工速度。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0500-Builders-Hut.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2026-01-28'">

<template #introduction>

- *如想查看村庄内类似于建筑工人小屋的另一种建筑，请访问：[小博木屋（巴布小屋）](/upgrade/0501-B.O.Bs-Hut)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Builders_Hut7_hd.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

1. 建筑工人小屋的建造不限制大本营等级，也就是说你可以在刚注册游戏账号时就买够 5 个建筑工人。
2. 2021 年 4 月更新后，建筑工人小屋可以升级了。升级后，建筑工人小屋自带武器，可以反击了，同时建筑工人会在战斗过程中围绕受损的建筑敲敲打打，尽力修复建筑。
3. **激活后的建筑工人小屋属于防御建筑**，[气球兵](/upgrade/0005-Balloon)、[野猪骑士](/upgrade/0081-Hog-Rider) 等兵种会优先攻击它。
4. 尽管建筑工人在战场上不会有生命危险，也不能被进攻方的部队锁定为目标，但是**法术可以对他造成影响。**[毒药法术](/upgrade/0180-Poison-Spell) 会减缓他修复建筑的速度，[冰冻法术](/upgrade/0104-Freeze-Spell)
   会暂停他的修复行为。[雷电法术](/upgrade/0100-Lightning-Spell) 会让他重置修复的目标。
5. 建筑工人小屋被摧毁后，建筑工人将停止修复建筑。
6. **多个建筑工人可以同时修复一个建筑**，同时修复时效率会降低，衰减机制同 治疗单位的衰减。
7. 建筑工人会优先修复自己的小屋，其次修复离自己最近的建筑。如果你想玩闪震，但是你要打的建筑旁边有工人小屋，那么你需要先放 [地震](/upgrade/0181-Earthquake-Spell)
   再放闪电。因为放了地震之后工人小屋残血了，建筑工人会先修自己的房子，这时候你就有充足的时间放闪电了。
8. 即使工人正在升级建筑，战斗过程中他仍然会修复建筑。
9. 当你解锁第 6 个工人后，村庄内会多出一个类似于建筑工人小屋的建筑，但那实际上是 [小博木屋](/upgrade/0501-B.O.Bs-Hut)。战斗过程中，小博**不会**像其他建筑工人一样修复建筑。解锁第 6 个工人的条件见 [波仔控制室](/upgrade/1284-B.O.B-Control)。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2026/01/28">
        <TimelineRow>建筑工人的移动速度由 3.5 格/秒 降低到 2.5 格/秒。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/11/17">
        <TimelineRow>7 级建筑工人小屋的升级时间和升级费用减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/10/06">
        <TimelineRow>2 ~ 6 级建筑工人小屋的升级时间减少。</TimelineRow>
        <TimelineRow>2 ~ 6 级建筑工人小屋的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>17 本新增 7 级建筑工人小屋。</TimelineRow>
        <TimelineRow>2 ~ 6 级建筑工人小屋的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/02/10">
        <TimelineRow>建筑工人小屋的充能时间和充能费用减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>2 ~ 6 级建筑工人小屋的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/09/09">
        <TimelineRow>超级充能推出，建筑工人小屋是第一批可以充能的建筑之一。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/18">
        <TimelineRow>2 ~ 5 级建筑工人小屋的升级时间减少。</TimelineRow>
        <TimelineRow>5 级建筑工人小屋的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/04/17">
        <TimelineRow>16 本新增 6 级建筑工人小屋。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>2 ~ 4 级建筑工人小屋的升级费用减少。</TimelineRow>
        <TimelineRow>5 级建筑工人小屋的升级时间 14 天 12 小时 减少至 14 天 6 小时。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>15 本新增 5 级建筑工人小屋。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>2 ~ 4 级建筑工人小屋的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/05/02">
        <TimelineRow>3/4 级的建筑工人小屋加入防守时，建筑工人的每秒修复值从 55/60 提升至 60/70。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/29">
        <TimelineRow>建筑工人小屋的攻击半径从 6 格增加到 7 格。</TimelineRow>
        <TimelineRow>防守状态下，建筑工人的移动速度从 24 提升到 28。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>从 14 本开始，建筑工人小屋可以升级了，升级后建筑工人会在战斗时修复建筑。此外，升级后建筑工人小屋将变成防御建筑，气球兵、野猪骑士等兵种会优先攻击它。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
