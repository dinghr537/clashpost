---
title: "部落冲突 coc 空中战车升级数据"
navTitle: "空中战车"
shownTitle: "空中战车"
module: upgrade-home
imgFolder: home_tech/0248
wiki: https://clashofclans.fandom.com/wiki/Sky_Wagon
canonical: /upgrade/0248-Sky-Wagon
dataSyncedOn: 2026-10-13
description: "空中战车会在空中投放装有援军的木桶，木桶落地后会造成少量伤害并放出部队。它能飞行、会自己解体，而且法术对它无效。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0248-Sky-Wagon.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2026-04-27'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Sky_Wagon_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>说明</SmallTitle>

1. 空中战车会在空中飞行，并把装有援军的木桶投向目标。每个木桶落地时都会造成少量伤害，同时放出 [亡灵](/upgrade/0005-Minions)、[气球兵](/upgrade/0003-Balloon)、[飞龙宝宝](/upgrade/000a-Baby-Dragon) 和 1 个部落城堡援军（如果有）。
   - 空中战车的运作方式和 [部队发射器](/upgrade/0247-Troop-Launcher) 类似，但它可以独立移动并自行寻找目标，而不是只对某一区域投放援军。
2. 木桶里的部队部署顺序遵循常规规则：先按人口从低到高，再按内部顺序；同类兵种则按等级从低到高部署。
3. 空中战车自带的部队等级取决于空中战车自身等级，而不是实验室里已经研究到的等级。
4. 空中战车的木桶数量有限，投完后会自动解体；如果它在投完前被摧毁，剩余木桶会消失，但它携带的部落城堡援军仍会在其被摧毁的位置释放出来。

\* 空中战车的面板里不会直接显示平均每秒伤害，这个伤害值实际上使用与等级相同的值。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2026/04/27">
        <TimelineRow>新增攻城机器：空中战车。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
