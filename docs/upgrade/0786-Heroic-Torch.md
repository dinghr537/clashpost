---
title: "部落冲突 coc 英雄火炬装备升级数据"
navTitle: "英雄火炬"
shownTitle: "英雄火炬"
module: upgrade-home
imgFolder: home_heroes/0786
wiki: https://clashofclans.fandom.com/wiki/Heroic_Torch
canonical: /upgrade/0786-Heroic-Torch
dataSyncedOn: 2026-10-13
description: "英雄火炬是大守护者的第三件史诗装备，它在 2025 年 8 月的水花大赛活动中首次开放购买。2. 技能持续期间，英雄火炬能为光环内的单位提供弹跳法术的效果，同时提升单位的移动速度，减少他们受到的伤害。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0786-Heroic-Torch.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2026-01-12'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Heroic_Torch.png" :imgAlt="$frontmatter.navTitle" description="激发附近部队的斗志，让他们能够穿过城墙、加速移动，并降低所受伤害" :isSmallImg="true" />

<SmallTitle>说明</SmallTitle>

1. 英雄火炬是 [大守护者](/upgrade/0202-Grand-Warden) 的第三件史诗装备，它在 2025 年 8 月的水花大赛活动中首次开放购买。
2. 技能持续期间，英雄火炬能为光环内的单位提供弹跳法术的效果，同时提升单位的移动速度，减少他们受到的伤害。
    - 英雄火炬对攻城机器无效。
    - 大守护者自身可以享受到英雄火炬的加成效果。
    - 其他英雄只能获得一半的加速效果，但其他效果不受影响。
3. 和 [永恒书卷](/upgrade/0780-Eternal-Tome) 类似，弹跳、减伤等效果只对光环内的单位有效，离开光环 1 秒后的部队就会失去英雄火炬的效果。在技能生效期间，进入光环或在光环内生成的单位亦可获得英雄火炬的效果。
4. 此外，英雄火炬可以提高大守护者的生命值和每秒伤害属性，以及增加开启技能时恢复的生命值。
5. 关于英雄火炬的减伤效果能否和 [冰障法术](/upgrade/0780-Eternal-Tome)、[永恒书卷](/upgrade/0780-Eternal-Tome) 叠加的问题，目前没有人测试，根据我们多年的经验，大概率是不能直接叠加，取效果最强的那个。

注意：
6. 上表的 8 点移动速度代表 1 格/秒。
7. 如果升级费用中有多种资源，则同时需要多种资源才能升级。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2026/01/12">
        <TimelineRow>1 ~ 27 级英雄火炬的持续时间、减伤比例、英雄回血增加值、英雄每秒伤害增加值、英雄生命值增加值提升。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/10/06">
        <TimelineRow>现在大守护者自身可以享受到英雄火炬的全部加成效果了。在此之前，大守护者只能享受到装备的减伤效果，不能享受其加速效果。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/08/08">
        <TimelineRow>新装备：英雄火炬。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
