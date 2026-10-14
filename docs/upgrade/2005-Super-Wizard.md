---
title: "部落冲突 coc 都城超级法师升级数据"
navTitle: "超级法师"
shownTitle: "超级法师"
module: upgrade-capital
imgFolder: capital_tech/2005
wiki: https://clashofclans.fandom.com/wiki/Super_Wizard/Clan_Capital
canonical: /upgrade/2005-Super-Wizard
dataSyncedOn: 2026-10-13
description: "超级法师全身充满了魔法能量！他可能是实验室里最聪明的人，但也有可能会把实验室炸上天。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/2005-Super-Wizard.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2022-06-30'">

<template #introduction>

- *如想查看家乡的超级法师，请访问：[超级法师](/upgrade/0609-Super-Wizard)。*
- *如想查看夜世界的电火法师，请访问：[夜世界电火法师](/upgrade/100b-Electrofire-Wizard)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Super_Wizard_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

1. 超级法师的解锁条件是建造 [超级法师训练营](/upgrade/2345-Super-Wizard-Barracks)，而这需要部落解锁法师山谷，并且 [都城大本营](/upgrade/2400-Capital-Hall) 达到 3 级。
2. 超级法师的技能（链式魔法）：超级法师的链式魔法攻击可以弹射伤害多个目标，只要这些目标在他初始目标的溅射范围内。它就可以同时对多个目标造成伤害。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2022/06/30">
        <TimelineRow>所有等级超级法师的生命值增加 200 点.</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/05/02">
        <TimelineRow>超级法师随着部落都城玩法一同推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
