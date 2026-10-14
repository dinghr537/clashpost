---
title: "部落冲突 coc 都城雷霆皮卡（威能皮卡、超级皮卡）升级数据"
navTitle: "雷霆皮卡"
shownTitle: "雷霆皮卡（威能皮卡、超级皮卡）"
module: upgrade-capital
imgFolder: capital_tech/200a
wiki: https://clashofclans.fandom.com/wiki/Power_P.E.K.K.A/Clan_Capital
canonical: /upgrade/200a-Power-P.E.K.K.A
dataSyncedOn: 2026-10-13
description: "这件强大的暗黑盔甲不断辐射出不稳定的能量，这些能量随时都可能挣脱盔甲的束缚！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/200a-Power-P.E.K.K.A.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-09-14'">

<template #introduction>

- *如想查看夜世界的雷霆皮卡（原超级皮卡），请访问：[夜世界雷霆皮卡](/upgrade/1009-Power-P.E.K.K.A)。*
- *如想查看家乡的皮卡超人，请访问：[皮卡超人](/upgrade/0009-P.E.K.K.A)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Power_P.E.K.K.A_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

1. 雷霆皮卡的解锁条件是建造 [雷霆皮卡训练营](/upgrade/234a-Power-P.E.K.K.A-Barracks)，而这需要部落将建筑工人工坊这个子城的大本营升到 2 级，并且 [都城大本营](/upgrade/2400-Capital-Hall) 需要达到 6 级。
2. 雷霆皮卡的技能（能量过载）：在死亡时产生巨大的爆炸。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/09/14">
        <TimelineRow>3 ~ 5 级雷霆皮卡的生命值由 8400/9200/10000 增加到 8500/9300/10300.</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/05/15">
        <TimelineRow>“超级皮卡”更名为“雷霆皮卡”.</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/05/02">
        <TimelineRow>超级皮卡随着部落都城玩法一同推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
