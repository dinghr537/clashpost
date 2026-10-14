---
title: "部落冲突 coc 飞盾战神（神盾勇者、闰土）升级数据"
navTitle: "飞盾战神"
shownTitle: "飞盾战神（神盾勇者、闰土）"
module: upgrade-home
imgFolder: home_heroes/0203
wiki: https://clashofclans.fandom.com/wiki/Royal_Champion
canonical: /upgrade/0203-Royal-Champion
dataSyncedOn: 2026-10-13
description: "翻越城墙，无往不利！飞盾战神一生只怕四件事，但敌军不在其列。她的近距离攻击非常适合用来摧毁近处的防御建筑。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0203-Royal-Champion.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-11-17'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Royal_Champion_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

1. 下方的数据均为不含装备的数据。
2. 英雄在防守时没有装备。

搜索半径：如果敌军进入这个范围，英雄会奔向敌军，并进行反击。<br>
巡逻半径：在没有敌人的情况下，英雄也会走动，而这个走动的范围叫巡逻半径。

下表中的生命值恢复量是基础属性，与装备无关。即使没有装备，开技能也会回血。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/11/17">
        <TimelineRow>18 本推出，并在 18 本新增 51 ~ 55 级飞盾战神。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/10/06">
        <TimelineRow>2 ~ 4、7 ~ 45 级飞盾战神的升级时间减少。</TimelineRow>
        <TimelineRow>11 ~ 45 级飞盾战神的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/27">
        <TimelineRow>取消英雄的恢复时间，现在英雄可以像战宠一样瞬间恢复。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>2 ~ 44 级飞盾战神的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>英雄的升级操作被整合进英雄殿堂，取消王座，同时引入英雄栏位和战旗的概念。</TimelineRow>
        <TimelineRow>英雄不再拥有警戒半径，遇到敌人后头顶不会冒问号，而是直接反击。</TimelineRow>
        <TimelineRow>在 17 本新增 46 - 50 级飞盾战神。</TimelineRow>
        <TimelineRow>8 ~ 30 级飞盾战神的升级时间减少。</TimelineRow>
        <TimelineRow>1 ~ 45 级飞盾战神的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/18">
        <TimelineRow>6 ~ 40 级飞盾战神的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>16 本推出，同时在 16 本新增 41 ~ 45 级飞盾战神。</TimelineRow>
        <TimelineRow>所有等级飞盾战神的每秒伤害和生命值降低。</TimelineRow>
        <TimelineRow>所有等级的升级时间和升级成本降低。</TimelineRow>
        <TimelineRow>废除原来的技能系统，用装备系统代替。</TimelineRow>
        <TimelineRow>现在所有英雄开启技能后都会回血了。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>15 本新增 36 ~ 40 级飞盾战神。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>15 本推出，并在 15 本新增 31 ~ 35 级飞盾战神。</TimelineRow>
        <TimelineRow>2 ~ 30 级飞盾战神的升级费用降低。</TimelineRow>
        <TimelineRow>4 ~ 25 级飞盾战神的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/09/13">
        <TimelineRow>从 25 级开始，飞盾战神开技能之后恢复的血量减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/02/15">
        <TimelineRow>英雄引入额外生命值概念，战斗时先消耗额外生命值再消耗本身的生命值，也就是说你可以连续打两场。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/12/09">
        <TimelineRow>1 ~ 6 级飞盾战神的升级花费降低。</TimelineRow>
        <TimelineRow>2 ~ 5 级飞盾战神的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>现在英雄可以搭配战宠了。</TimelineRow>
        <TimelineRow>14 本推出，并在 14 本新增 26 ~ 30 级飞盾战神。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/12/07">
        <TimelineRow>战斗结束时，如果英雄的技能尚未使用，英雄会自动恢复一部分生命值（数值等于他们使用技能时可恢复的生命值）。这样就缩短了英雄的冷却时间，让他们可以更快投入下一场战斗！</TimelineRow>
        <TimelineRow>13 本新增 21 ~ 25 级飞盾战神。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/10/12">
        <TimelineRow>更新后，英雄会一直处于防御状态，而且在进行防御后会自动恢复为满血状态。“正在防御”和“正在休息”两种模式间的切换功能已被移除。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/06/22">
        <TimelineRow>所有等级飞盾战神的恢复时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/12/09">
        <TimelineRow>新增 13 级大本营，新英雄：飞盾战神。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
