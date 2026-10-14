---
title: "部落冲突 coc 隐形药水瓶装备升级数据"
navTitle: "隐形药水瓶"
shownTitle: "隐形药水瓶"
module: upgrade-home
imgFolder: home_heroes/0741
wiki: https://clashofclans.fandom.com/wiki/Invisibility_Vial
canonical: /upgrade/0741-Invisibility-Vial
dataSyncedOn: 2026-10-13
description: "隐形药水瓶是弓箭女皇的两件初始装备之一。隐形药水瓶可以使弓箭女皇在技能生效期间短暂隐形。在技能生效期间，弓箭女皇的每次射击伤害会大幅增加。此外，隐形药水瓶还可以为女王提供额外生命值。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0741-Invisibility-Vial.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2024-11-25'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Invisibility_Vial_info.png" :imgAlt="$frontmatter.navTitle" description="使弓箭女皇隐身并强化其攻击。" />

<SmallTitle>说明</SmallTitle>

1. 隐形药水瓶是 [弓箭女皇](/upgrade/0201-Archer-Queen) 的两件初始装备之一，另一件是 [弓箭手木偶](/upgrade/0740-Archer-Puppet)。
2. 隐形药水瓶可以使弓箭女皇在技能生效期间短暂隐形。在技能生效期间，弓箭女皇的每次射击伤害会大幅增加。
3. 此外，隐形药水瓶还可以为女王提供额外生命值。
4. 和 [隐形法术](/upgrade/0106-Invisibility-Spell) 类似，隐形药水瓶的隐形效果只是不会被建筑锁定，并非无敌。隐形期间女王仍然会被隐形前已经打出去的子弹打中，也会受到溅射伤害。
   - 如果 [天鹰火炮](/upgrade/030b-Eagle-Artillery) 在隐形前就瞄准了女王，即使使用了隐形药水瓶，女王仍然会被天鹰火炮打中，只有在开火前使用隐形药水瓶才能让天鹰火炮转移目标。
5. 隐形药水瓶生效期间的射击伤害加成可以与 [狂暴法术](/upgrade/0102-Rage-Spell) 叠加。在较高的装备等级下，女王可以迅速摧毁建筑物。

注意：如果升级费用中有多种资源，则同时需要多种资源才能升级。

在 2023 年 12 月装备系统发布时，已解锁弓箭女皇的玩家会有一个初始的装备等级，并且不需要解锁铁匠铺。装备等级与玩家的英雄等级相关，具体如下表。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2024/11/25">
        <TimelineRow>现在 8 本就可以解锁弓箭女皇了，该页面的部分信息需要同步更改。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>游戏新增装备系统，隐形药水瓶是第一批推出的装备。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
