---
title: "部落冲突 coc 都城空中炸弹发射器升级数据"
navTitle: "空中炸弹发射器"
shownTitle: "空中炸弹发射器"
module: upgrade-capital
imgFolder: capital_buildings/2208
wiki: https://clashofclans.fandom.com/wiki/Air_Bombs/Clan_Capital
canonical: /upgrade/2208-Air-Bombs
dataSyncedOn: 2026-10-13
description: "要应对繁重的空中防御任务，使用空中炸弹发射器准没错。它能持续不断地向空中发射木桶，木桶会在空中爆炸重创敌军！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/2208-Air-Bombs.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2022-05-02'">

<template #introduction>

- *如想查看家乡的陷阱空中炸弹，请访问：[空中炸弹](/upgrade/0382-Air-Bomb)。*
- *如想查看夜世界的建筑空中炸弹发射器，请访问：[夜世界空中炸弹发射器](/upgrade/1107-Air-Bombs)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Air_Bombs5.png" :imgAlt="$frontmatter.navTitle"
    description="要应对繁重的空中防御任务，使用空中炸弹发射器准没错。<br>它能持续不断地向空中发射木桶，木桶会在空中爆炸重创敌军！"
    :isSmallImg="true" />

</template>

<template #history>

<Timeline>
    <TimelineItem date="2022/05/02">
        <TimelineRow>空中炸弹发射器随着部落都城玩法一同推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
