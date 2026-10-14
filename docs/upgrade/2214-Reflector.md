---
title: "部落冲突 coc 都城反弹机升级数据"
navTitle: "反弹机"
shownTitle: "反弹机"
module: upgrade-capital
imgFolder: capital_buildings/2214
wiki: https://clashofclans.fandom.com/wiki/Reflector
canonical: /upgrade/2214-Reflector
dataSyncedOn: 2026-10-13
description: "会旋转、带护盾、还能反弹敌人的进攻？这种奇特的装置想都没想过......但反弹机全都做到了！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/2214-Reflector.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2022-10-09'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Reflector4.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

<SmallTitle>重要说明</SmallTitle>

1. 反弹机不会主动寻找单位进行攻击，只会反击对其造成伤害的单位。
2. 当部队的攻速慢于反弹机的最快攻速时，反弹机会以和部队相同的攻速进行反击；当部队的攻速快于或等于反弹机的最快攻速时，反弹机会以最快攻速进行反击。
3. 反弹机会反击隐形的单位，如隐秘弓箭手。
4. 反弹机会对间接伤害进行反击，比如说如果它被超级飞龙溅射到，那么也会进行反击。但是这里有一个例外，反弹机不会反击超级法师的链式伤害。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2022/10/09">
        <TimelineRow>都城新防御：反弹机。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
