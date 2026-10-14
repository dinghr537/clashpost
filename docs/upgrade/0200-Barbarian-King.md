---
title: "部落冲突 coc 野蛮人之王（蛮王、男王）升级数据"
navTitle: "野蛮人之王"
shownTitle: "野蛮人之王（蛮王、男王）"
module: upgrade-home
imgFolder: home_heroes/0200
wiki: https://clashofclans.fandom.com/wiki/Barbarian_King
canonical: /upgrade/0200-Barbarian-King
dataSyncedOn: 2026-10-13
description: "所有野蛮人中体型最大、最勇猛的一个。这个大块头能吸收大量伤害，并会用他的剑摧毁所有拦路之物。他在防守时会拼命守护领土。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0200-Barbarian-King.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2026-02-23'">

<template #introduction>

- *如想查看野蛮人之王的创作原型，请访问：[野蛮人](/upgrade/0000-Barbarian)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Barbarian_King_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

1. 下方的数据均为不含装备的数据。
2. 英雄在防守时没有装备。

搜索半径：如果敌军进入这个范围，英雄会奔向敌军，并进行反击。<br>
巡逻半径：在没有敌人的情况下，英雄也会走动，而这个走动的范围叫巡逻半径。<br>

下表中的生命值恢复量是基础属性，与装备无关。即使没有装备，开技能也会回血。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2026/02/23">
        <TimelineRow>71 ~ 95 级野蛮人之王的升级时间减少。</TimelineRow>
        <TimelineRow>82 ~ 90 级野蛮人之王的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/11/17">
        <TimelineRow>18 本推出，并在 18 本新增 101 ~ 105 级野蛮人之王。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/10/06">
        <TimelineRow>现在 14 级大本营即可解锁 81 ~ 85 级野蛮人之王。</TimelineRow>
        <TimelineRow>31 ~ 95 级野蛮人之王的升级时间减少。</TimelineRow>
        <TimelineRow>51 ~ 95 级野蛮人之王的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/27">
        <TimelineRow>取消英雄的恢复时间，现在英雄可以像战宠一样瞬间恢复。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>英雄的升级操作被整合进英雄殿堂，取消王座，同时引入英雄栏位和战旗的概念。</TimelineRow>
        <TimelineRow>英雄不再拥有警戒半径，遇到敌人后头顶不会冒问号，而是直接反击。</TimelineRow>
        <TimelineRow>在 17 本新增 96 - 100 级野蛮人之王。</TimelineRow>
        <TimelineRow>2 ~ 3、17 ~ 25 级野蛮人之王的升级时间减少。</TimelineRow>
        <TimelineRow>1、3 ~ 90 级野蛮人之王的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/18">
        <TimelineRow>20、25 ~ 85 级野蛮人之王的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>16 本推出，同时在 16 本新增 91 ~ 95 级野蛮人之王。</TimelineRow>
        <TimelineRow>所有等级野蛮人之王的每秒伤害和生命值降低。</TimelineRow>
        <TimelineRow>所有等级的升级时间和升级成本降低。</TimelineRow>
        <TimelineRow>废除原来的技能系统，用装备系统代替。</TimelineRow>
        <TimelineRow>现在所有英雄开启技能后都会回血了。</TimelineRow>
        <TimelineRow>6 ~ 10 级蛮王下放到 7 本，11 ~ 20 级蛮王下放到 8 本。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>15 本新增 86 ~ 90 级野蛮人之王。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>15 本推出，并在 15 本新增 81 ~ 85 级野蛮人之王。</TimelineRow>
        <TimelineRow>33 ~ 80 级野蛮人之王的升级费用降低。</TimelineRow>
        <TimelineRow>35 ~ 75 级野蛮人之王的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/02/15">
        <TimelineRow>英雄引入额外生命值概念，战斗时先消耗额外生命值再消耗本身的生命值，也就是说你可以连续打两场。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/12/09">
        <TimelineRow>26 ~ 64 级野蛮人之王的升级花费降低。</TimelineRow>
        <TimelineRow>20 ~ 29 级野蛮人之王的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>现在英雄可以搭配战宠了。</TimelineRow>
        <TimelineRow>14 本推出，并在 14 本新增 76 ~ 80 级野蛮人之王。</TimelineRow>
        <TimelineRow>1 ~ 50 级野蛮人之王的升级花费降低。</TimelineRow>
        <TimelineRow>2 ~ 50 级野蛮人之王的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/12/07">
        <TimelineRow>战斗结束时，如果英雄的技能尚未使用，英雄会自动恢复一部分生命值（数值等于他们使用技能时可恢复的生命值）。这样就缩短了英雄的冷却时间，让他们可以更快投入下一场战斗！</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/10/12">
        <TimelineRow>更新后，英雄会一直处于防御状态，而且在进行防御后会自动恢复为满血状态。“正在防御”和“正在休息”两种模式间的切换功能已被移除。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/06/22">
        <TimelineRow>13 本新增 71 ~ 75 级野蛮人之王。</TimelineRow>
        <TimelineRow>所有等级野蛮人之王的恢复时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/03/30">
        <TimelineRow>2 ~ 40 级野蛮人之王的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/12/09">
        <TimelineRow>13 本推出，并且在 13 本新增 66 ~ 70 级野蛮人之王。</TimelineRow>
        <TimelineRow>进攻时，如果英雄技能一直没有被手动开启，英雄在即将被击败时会自动开启英雄技能进行自救。该功能可以在“设置>更多设置”中关闭。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/06/18">
        <TimelineRow>12 本新增 61 ~ 65 级野蛮人之王。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/04/02">
        <TimelineRow>为了让英雄能穿上皮肤，英雄的模型被更改。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
