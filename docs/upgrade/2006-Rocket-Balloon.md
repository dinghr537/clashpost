---
title: "部落冲突 coc 都城火箭气球兵（超球）升级数据"
navTitle: "火箭气球兵"
shownTitle: "火箭气球兵（超球）"
module: upgrade-capital
imgFolder: capital_tech/2006
wiki: https://clashofclans.fandom.com/wiki/Rocket_Balloon/Clan_Capital
canonical: /upgrade/2006-Rocket-Balloon
dataSyncedOn: 2026-10-13
description: "地面进攻受阻怎么办？一排火箭气球兵应该能帮你搞定......如果它们的助推器还有燃料。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/2006-Rocket-Balloon.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2022-05-02'">

<template #introduction>

- *如想查看家乡的火箭气球兵，请访问：[火箭气球兵](/upgrade/060b-Rocket-Balloon)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Rocket_Balloon_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

1. 火箭气球兵的解锁条件是建造 [火箭气球兵训练营](/upgrade/2346-Rocket-Balloon-Barracks)，而这需要部落解锁气球环礁，并且 [都城大本营](/upgrade/2400-Capital-Hall) 达到 4 级。
2. 火箭气球兵的技能（急速飞行）：在部署后的 4 秒内提升移动速度。加速状态下火箭气球兵的移动速度是 60.8，即 7.6 格/秒。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2022/05/02">
        <TimelineRow>火箭气球兵随着部落都城玩法一同推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
