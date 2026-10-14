---
title: "部落冲突 coc 终极炸弹升级数据"
navTitle: "终极炸弹"
shownTitle: "终极炸弹"
module: upgrade-home
imgFolder: home_buildings/0387
wiki: https://clashofclans.fandom.com/wiki/Giga_Bomb
canonical: /upgrade/0387-Giga-Bomb
dataSyncedOn: 2026-10-13
description: "村民们不想把这么危险的武器放在大本营里，所以把它搬了出来！终极炸弹会将敌人击退，并造成巨大伤害。这个陷阱的威力足够大，所以没必要藏起来！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0387-Giga-Bomb.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2026-02-23'">

<template #introduction>

- 游戏中还存在另一种大炸弹，详见：[巨型炸弹](/upgrade/0383-Giant-Bomb)。

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Giga_Bomb4.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

<SmallTitle>重要说明</SmallTitle>

1. 根据游戏设定，从 17 级 [大本营](/upgrade/0400-Town-Hall) 开始，大本营内的炸弹被拆分成了一个单独的陷阱：终极炸弹，因此 17 级大本营被摧毁后不再爆炸。
    - 和 16 本被摧毁后引爆的炸弹相比，终极炸弹的爆炸半径保持不变，多出了击退效果，但不再释放毒雾（无减速和持续伤害效果）。
2. 和其他陷阱不同，终极炸弹对进攻方可见。
3. 只有当触发范围内至少有 18 单位的部队时，终极炸弹才会触发。
4. 和 [隐形炸弹](/upgrade/0380-Bomb)、[巨型炸弹](/upgrade/0383-Giant-Bomb) 一样，法术和 [大守护者](/upgrade/0202-Grand-Warden) 的 [永恒书卷](/upgrade/0780-Eternal-Tome) 装备无法延缓或阻止爆炸。
5. 终极炸弹的爆炸效果可以击退高生命值单位以及弹飞低生命值单位，它的范围伤害对空中单位也有效。
6. 被终极炸弹波及到且仍然存活的部队会重新选择进攻目标。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2026/02/23">
        <TimelineRow>在 18 本推出 4 级终极炸弹。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/11/17">
        <TimelineRow>2 ~ 3 级终极炸弹的升级时间和升级费用减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>17 本推出，新陷阱：终极炸弹。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
