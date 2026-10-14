---
title: "部落冲突 coc 凤凰升级数据"
navTitle: "凤凰"
shownTitle: "凤凰"
module: upgrade-home
imgFolder: home_heroes/0287
wiki: https://clashofclans.fandom.com/wiki/Phoenix
canonical: /upgrade/0287-Phoenix
dataSyncedOn: 2026-10-13
description: "真正的朋友会在你遇到困难时及时出手相助。战斗开始时，凤凰只是一颗蛋，帮不上什么忙。但当它跟随的英雄可能被击倒时，它会破壳而出，愤怒地攻击附近的敌人，还能让英雄暂时免疫伤害。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0287-Phoenix.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-10-06'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Phoenix_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

1. 凤凰的技能（浴火重生）：在跟随的英雄快被击倒时，凤凰会破壳而出，让英雄暂时免疫伤害。
2. 凤凰在主人阵亡前是一颗蛋，不会攻击，不会受伤，也不能提供任何帮助。当主人阵亡时，凤凰会复活主人并使其无敌几秒钟。时间过后，英雄会强制阵亡。
3. 当凤凰没有破壳而出的时候，它的人口数为零，这个数据主要用于计算 [回溯法术](/upgrade/0107-Recall-Spell) 的召回。特别地，如果召回凤凰的主人，即使凤凰蛋不在回溯法术范围内，也会被强制跟随英雄一起被召回。
4. 被凤凰复活的英雄不能以任何方式回复血量，不会被 [天使](/upgrade/0007-Healer) 锁定，[大守护者](/upgrade/0202-Grand-Warden) 的 [永恒书卷](/upgrade/0780-Eternal-Tome) 装备也无法延长其复活时间。一旦复活时间结束，英雄必定会阵亡，凤凰会继续战斗。
5. 凤凰和主人都可以被单独召回，主人被召回后无敌时间会暂停，而凤凰的无敌时间不会暂停。
6. 如果主人被召回或阵亡，凤凰会变成一个自由单位，此时没有偏好目标。
7. 在凤凰的无敌效果结束后，你可以对该英雄使用 [复苏法术](/upgrade/0108-Revive-Spell)。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/10/06">
        <TimelineRow>8 级凤凰的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>2 ~ 10 级凤凰的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>2 ~ 10 级凤凰的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>2 ~ 10 级凤凰的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/05/15">
        <TimelineRow>修复使用战宠凤凰的英雄有时不会触发特斯拉电磁塔的问题。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>15 本推出，可解锁四个新宠物，凤凰是其中之一。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
