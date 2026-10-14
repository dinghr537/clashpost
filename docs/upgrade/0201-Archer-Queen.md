---
title: "部落冲突 coc 弓箭女皇（女王）升级数据"
navTitle: "弓箭女皇"
shownTitle: "弓箭女皇（女王）"
module: upgrade-home
imgFolder: home_heroes/0201
wiki: https://clashofclans.fandom.com/wiki/Archer_Queen
canonical: /upgrade/0201-Archer-Queen
dataSyncedOn: 2026-10-13
description: "这位优雅的女猎手掌握着毁灭性的力量，实力碾压其他所有弓箭手。虽然生命值不高，但她能用威力十足的十字连弩从远处攻击目标。在防守时她会拼尽全力守卫村庄。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0201-Archer-Queen.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-11-17'">

<template #introduction>

- *如想查看弓箭女皇的创作原型，请访问：[弓箭手](/upgrade/0001-Archer)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Archer_Queen_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

1. 下方的数据均为不含装备的数据。
2. 英雄在防守时没有装备。

搜索半径：如果敌军进入这个范围，英雄会奔向敌军，并进行反击。<br>
巡逻半径：在没有敌人的情况下，英雄也会走动，而这个走动的范围叫巡逻半径。<br>

下表中的生命值恢复量是基础属性，与装备无关。即使没有装备，开技能也会回血。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/11/17">
        <TimelineRow>18 本推出，并在 18 本新增 101 ~ 105 级弓箭女皇。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/10/06">
        <TimelineRow>现在 14 级大本营即可解锁 81 ~ 85 级弓箭女皇。</TimelineRow>
        <TimelineRow>25、31 ~ 95 级弓箭女皇的升级时间减少。</TimelineRow>
        <TimelineRow>51 ~ 95 级弓箭女皇的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/27">
        <TimelineRow>取消英雄的恢复时间，现在英雄可以像战宠一样瞬间恢复。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>英雄的升级操作被整合进英雄殿堂，取消王座，同时引入英雄栏位和战旗的概念。</TimelineRow>
        <TimelineRow>英雄不再拥有警戒半径，遇到敌人后头顶不会冒问号，而是直接反击。</TimelineRow>
        <TimelineRow>现在 8 本就可以解锁 1 ~ 10 级弓箭女皇了。</TimelineRow>
        <TimelineRow>在 17 本新增 96 - 100 级弓箭女皇。</TimelineRow>
        <TimelineRow>2 ~ 3、17 ~ 40、46 级弓箭女皇的升级时间减少。</TimelineRow>
        <TimelineRow>1 ~ 95 级弓箭女皇的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>16 本推出，同时在 16 本新增 91 ~ 95 级弓箭女皇。</TimelineRow>
        <TimelineRow>所有等级弓箭女皇的每秒伤害和生命值降低。</TimelineRow>
        <TimelineRow>所有等级的升级时间和升级成本降低。</TimelineRow>
        <TimelineRow>废除原来的技能系统，用装备系统代替。</TimelineRow>
        <TimelineRow>现在所有英雄开启技能后都会回血了。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>15 本新增 86 ~ 90 级弓箭女皇。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>15 本推出，并在 15 本新增 81 ~ 85 级弓箭女皇。</TimelineRow>
        <TimelineRow>33 ~ 80 级弓箭女皇的升级费用降低。</TimelineRow>
        <TimelineRow>35 ~ 75 级弓箭女皇的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/02/15">
        <TimelineRow>英雄引入额外生命值概念，战斗时先消耗额外生命值再消耗本身的生命值，也就是说你可以连续打两场。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/12/09">
        <TimelineRow>26 ~ 64 级弓箭女皇的升级花费降低。</TimelineRow>
        <TimelineRow>20 ~ 29 级弓箭女皇的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>现在英雄可以搭配战宠了。</TimelineRow>
        <TimelineRow>14 本推出，并在 14 本新增 76 ~ 80 级弓箭女皇。</TimelineRow>
        <TimelineRow>优化弓箭女皇的寻路系统，这将改善她的 AI，比如她现在会优先往有城墙缺口的方向移动。</TimelineRow>
        <TimelineRow>1 ~ 50 级弓箭女皇的升级花费降低。</TimelineRow>
        <TimelineRow>2 ~ 50 级弓箭女皇的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/12/07">
        <TimelineRow>战斗结束时，如果英雄的技能尚未使用，英雄会自动恢复一部分生命值（数值等于他们使用技能时可恢复的生命值）。这样就缩短了英雄的冷却时间，让他们可以更快投入下一场战斗！</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/10/12">
        <TimelineRow>更新后，英雄会一直处于防御状态，而且在进行防御后会自动恢复为满血状态。“正在防御”和“正在休息”两种模式间的切换功能已被移除。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/06/22">
        <TimelineRow>13 本新增 71 ~ 75 级弓箭女皇。</TimelineRow>
        <TimelineRow>所有等级弓箭女皇的恢复时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/03/30">
        <TimelineRow>2 ~ 40 级弓箭女皇的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/12/09">
        <TimelineRow>13 本推出，并且在 13 本新增 66 ~ 70 级弓箭女皇。</TimelineRow>
        <TimelineRow>进攻时，如果英雄技能一直没有被手动开启，英雄在即将被击败时会自动开启英雄技能进行自救。该功能可以在“设置>更多设置”中关闭。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/06/18">
        <TimelineRow>12 本新增 61 ~ 65 级弓箭女皇。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/04/02">
        <TimelineRow>为了让英雄能穿上皮肤，英雄的模型被更改。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
