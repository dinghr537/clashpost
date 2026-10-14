---
title: "部落冲突 coc 都城雷电法术升级数据"
navTitle: "雷电法术"
shownTitle: "雷电法术"
module: upgrade-capital
imgFolder: capital_tech/2102
wiki: https://clashofclans.fandom.com/wiki/Lightning_Spell/Clan_Capital
canonical: /upgrade/2102-Lightning-Spell
dataSyncedOn: 2026-10-13
description: "放出一道闪电攻击敌军！施放雷电法术，击晕小范围内的建筑和部队，并对其造成伤害。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/2102-Lightning-Spell.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-09-14'">

<template #introduction>

- *如想查看家乡的雷电法术，请访问：[雷电法术](/upgrade/0100-Lightning-Spell)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Lightning_Spell_info.png" :imgAlt="$frontmatter.navTitle"
    description="放出一道闪电攻击敌军！<br>施放雷电法术，击晕小范围内的建筑和部队，并对其造成伤害。"
    :isSmallImg="true" />

<SmallTitle>重要说明</SmallTitle>

当部落解锁雷电法术工厂时，系统会自动建造 [雷电法术工厂](/upgrade/2382-Lightning-Spell-Factory)，而这需要气球环礁这个子城的大本营升到 2 级。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/09/14">
        <TimelineRow>1 ~ 5 级雷电法术的伤害增加 25.</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/05/02">
        <TimelineRow>雷电法术随着部落都城玩法一同推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
