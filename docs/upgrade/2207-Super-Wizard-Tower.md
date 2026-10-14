---
title: "部落冲突 coc 都城超级法师塔升级数据"
navTitle: "超级法师塔"
shownTitle: "超级法师塔"
module: upgrade-capital
imgFolder: capital_buildings/2207
wiki: https://clashofclans.fandom.com/wiki/Super_Wizard_Tower
canonical: /upgrade/2207-Super-Wizard-Tower
dataSyncedOn: 2026-10-13
description: "超级法师电力十足，在对付大批来犯之敌时能发挥巨大作用，因为他们的攻击可以弹射到初始目标附近的其他敌人。。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/2207-Super-Wizard-Tower.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2022-05-02'">

<template #introduction>

- *如想查看家乡的法师塔，请访问：[法师塔](/upgrade/0305-Wizard-Tower)。*
- *如想查看家乡的超级法师塔，请移步：[超级法师塔](/upgrade/0318-Super-Wizard-Tower)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Super_Wizard_Tower5.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2022/05/02">
        <TimelineRow>超级法师塔随着部落都城玩法一同推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
