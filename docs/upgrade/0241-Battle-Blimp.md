---
title: "部落冲突 coc 攻城飞艇升级数据"
navTitle: "攻城飞艇"
shownTitle: "攻城飞艇"
module: upgrade-home
imgFolder: home_tech/0241
wiki: https://clashofclans.fandom.com/wiki/Battle_Blimp
canonical: /upgrade/0241-Battle-Blimp
dataSyncedOn: 2026-10-13
description: "攻城飞艇可以无视地面障碍，并将您的部落援军直接运送至敌军村庄中心，在飞行途中还会不断投放炸弹。由于外壳不够结实，它很容易被敌军击落。法术对攻城飞艇无效。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0241-Battle-Blimp.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-06-16'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Battle_Blimp_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

1. 攻城飞艇部署后会直线前往 [大本营](/upgrade/0400-Town-Hall) 方向，并在路线上投掷炸弹。
2. 当攻城飞艇的血量清零或到达大本营时，攻城飞艇就会解体并释放里面的援军。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/06/16">
        <TimelineRow>在 15 本新增 5 级攻城飞艇。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/27">
        <TimelineRow>攻城机器的建造时间被取消。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>2 ~ 4 级攻城飞艇的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>2 ~ 4 级攻城飞艇的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>2 ~ 4 级攻城飞艇的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>2 ~ 4 级攻城飞艇的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/05/02">
        <TimelineRow>现在攻城飞艇的下落位置距离大本营只有 1.5 格，以前是 2 格。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/02/15">
        <TimelineRow>各等级攻城飞艇被摧毁时的爆炸伤害从 1000/1200/1400/1600 降低至 700/800/900/1000。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/10/12">
        <TimelineRow>如果您没有部署攻城机器，当其他军队都被消灭后，战斗不再会自动结束。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/06/22">
        <TimelineRow>13 本新增 4 级攻城飞艇。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/12/09">
        <TimelineRow>所有等级攻城飞艇的死亡伤害提高。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/06/18">
        <TimelineRow>所有等级攻城飞艇的生命值增加。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
