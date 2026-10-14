---
title: "部落冲突 coc 都城超级野蛮人升级数据"
navTitle: "超级野蛮人"
shownTitle: "超级野蛮人"
module: upgrade-capital
imgFolder: capital_tech/2000
wiki: https://clashofclans.fandom.com/wiki/Super_Barbarian/Clan_Capital
canonical: /upgrade/2000-Super-Barbarian
dataSyncedOn: 2026-10-13
description: "生命值更高、力量更强、速度更快，最重要的是秀发更浓密。成为超级野蛮人是每个普通野蛮人的梦想！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/2000-Super-Barbarian.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-09-14'">

<template #introduction>

- *如想查看家乡的超级野蛮人，请访问：[超级野蛮人](/upgrade/0600-Super-Barbarian)。*
- *如想查看夜世界的狂暴野蛮人，请访问：[夜世界狂暴野蛮人](/upgrade/1000-Raged-Barbarian)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Super_Barbarian_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

1. 当部落解锁野蛮人兵营时，系统会自动建造 [超级野蛮人训练营](/upgrade/2340-Super-Barbarian-Barracks)，也就是说超级野蛮人在 [都城大本营](/upgrade/2400-Capital-Hall) 达到 2 级后可解锁。
2. 超级野蛮人的技能（狂暴）：部署 8 秒内狂暴。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/09/14">
        <TimelineRow>4 ~ 5 级超级野蛮人的生命值由 1100/1200 增加到 1120/1240.</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/05/02">
        <TimelineRow>超级野蛮人随着部落都城玩法一同推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
