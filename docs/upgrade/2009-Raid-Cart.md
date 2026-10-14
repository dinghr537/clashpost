---
title: "部落冲突 coc 都城突袭炮车升级数据"
navTitle: "突袭炮车"
shownTitle: "突袭炮车"
module: upgrade-capital
imgFolder: capital_tech/2009
wiki: https://clashofclans.fandom.com/wiki/Raid_Cart
canonical: /upgrade/2009-Raid-Cart
dataSyncedOn: 2026-10-13
description: "又是一个带轮子的加农炮？可能没什么新意，但一些大块头的加入弥补了这点遗憾。现在它火力更强，还有不好惹的野蛮人一路护送！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/2009-Raid-Cart.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-09-14'">

<template #introduction>

- *如想查看夜世界的加农炮战车，请访问：[夜世界加农炮战车](/upgrade/1006-Cannon-Cart)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Raid_Cart_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

1. 突袭炮车的解锁条件是建造 [突袭炮车训练营](/upgrade/2349-Raid-Cart-Barracks)，而这需要部落解锁建筑工人工坊，并且 [都城大本营](/upgrade/2400-Capital-Hall) 达到 5 级。
2. 攻城炮车类似于夜世界的 [加农炮战车](/upgrade/1006-Cannon-Cart)，只不过血量更高，攻速更慢。
3. 加农炮战车还可以作为防守部队驻扎在 [突袭炮车岗哨](/upgrade/2211-Raid-Cart-Post) 附近。
4. 加农炮战车的技能（奋战到底）：被摧毁后获得一些临时生命值。
5. 突袭炮车在部署之前是一个整体，你不能把攻城炮车和 [野蛮人](/upgrade/20c0-Barbarian) 分开部署。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/09/14">
        <TimelineRow>攻击新目标的速度加快了 0.2 秒。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/06/30">
        <TimelineRow>将突袭炮车的第一次攻击减慢 0.7 秒。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/06/27">
        <TimelineRow>更新后，疗伤法术对被摧毁的攻城炮车无效。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/05/02">
        <TimelineRow>突袭炮车随着部落都城玩法一同推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
