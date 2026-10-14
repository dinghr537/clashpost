---
title: "部落冲突 coc 派对法师升级数据"
navTitle: "派对法师"
shownTitle: "派对法师"
module: upgrade-temp
imgFolder: temp_troops/0e06
wiki: https://clashofclans.fandom.com/wiki/Party_Wizard
canonical: /upgrade/0e06-Party-Wizard
dataSyncedOn: 2026-10-13
description: "听见远处架子鼓的声音了吗？派对法师华丽登场！他脚踩节奏，手扔火球，绝对是庆功派对的灵魂人物。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0e06-Party-Wizard.json";
</script>

<SyncedUnitData :data="unitData">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Party_Wizard_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

派对法师一般在部落冲突生日（8 月 2 日）前后推出，他比 [普通法师](/upgrade/0006-Wizard) 的移动速度更快，伤害也更高，但生命值更少。

\* 游戏内部确实规定了 1 级派对法师的属性，但是派对法师 5 本才会解锁，这时候系统会自动把派对法师升到 2 级，所以 1 级派对法师实际上不会出现。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/08">
        <TimelineRow>该兵种第 4 次推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/08">
        <TimelineRow>该兵种第 3 次推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/08">
        <TimelineRow>该兵种第 2 次推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/08">
        <TimelineRow>该兵种第 1 次推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
