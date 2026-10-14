---
title: "部落冲突 coc 野猪骑士木偶（野猪骑士玩偶）装备升级数据"
navTitle: "野猪骑士木偶"
shownTitle: "野猪骑士木偶（野猪骑士玩偶）"
module: upgrade-home
imgFolder: home_heroes/07c2
wiki: https://clashofclans.fandom.com/wiki/Hog_Rider_Puppet
canonical: /upgrade/07c2-Hog-Rider-Puppet
dataSyncedOn: 2026-10-13
description: "野猪骑士木偶是飞盾战神的一件普通装备。野猪骑士木偶装备可以让飞盾战神使用技能时召唤出一定数量的野猪骑士。带上野猪骑士木偶时，开启技能后，飞盾战神会在短时间内隐形，因此野猪骑士可以为她扛伤害。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/07c2-Hog-Rider-Puppet.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2026-01-12'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Hog_Rider_Puppet_info.png" :imgAlt="$frontmatter.navTitle" description="召唤一群野猪骑士。" />

<SmallTitle>说明</SmallTitle>

1. 野猪骑士木偶是 [飞盾战神](/upgrade/0203-Royal-Champion) 的一件普通装备。
2. 野猪骑士木偶装备可以让飞盾战神使用技能时召唤出一定数量的 [野猪骑士](/upgrade/0081-Hog-Rider)。
   - 召唤出的野猪骑士等级取决于装备等级，而非 [实验室](/upgrade/0483-Laboratory) 中野猪骑士的等级。
3. 带上野猪骑士木偶时，开启技能后，飞盾战神会在短时间内隐形，因此野猪骑士可以为她扛伤害。
4. 除了召唤野猪骑士外，该装备还可以为飞盾战神提供额外的生命值，并且增加技能时恢复的生命值。

注意：如果升级费用中有多种资源，则同时需要多种资源才能升级。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2026/01/12">
        <TimelineRow>1 ~ 18 级野猪骑士木偶装备召唤的野猪骑士数量和等级分别增加 1.</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/09/09">
        <TimelineRow>3 ~ 18 级野猪骑士木偶装备召唤的野猪骑士等级降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/02/27">
        <TimelineRow>在 14 本新增野猪骑士木偶装备。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
