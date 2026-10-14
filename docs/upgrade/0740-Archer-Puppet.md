---
title: "部落冲突 coc 弓箭手木偶（弓箭手玩偶）装备升级数据"
navTitle: "弓箭手木偶"
shownTitle: "弓箭手木偶（弓箭手玩偶）"
module: upgrade-home
imgFolder: home_heroes/0740
wiki: https://clashofclans.fandom.com/wiki/Archer_Puppet
canonical: /upgrade/0740-Archer-Puppet
dataSyncedOn: 2026-10-13
description: "弓箭手木偶是弓箭女皇的两件初始装备之一。弓箭手木偶装备可以让弓箭女皇使用技能时召唤出一定数量的弓箭手。召唤出的弓箭手等级与实验室中弓箭手的等级相同。除了召唤弓箭手外，该装备还可以为弓箭女皇提供额外的每秒伤害，并且增加技能时恢复的生命值。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0740-Archer-Puppet.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-02-10'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Archer_Puppet_info.png" :imgAlt="$frontmatter.navTitle" description="召唤一群隐形弓箭手。" />

<SmallTitle>说明</SmallTitle>

1. 弓箭手木偶是 [弓箭女皇](/upgrade/0201-Archer-Queen) 的两件初始装备之一，另一件是 [隐形药水瓶](/upgrade/0741-Invisibility-Vial)。
2. 弓箭手木偶装备可以让弓箭女皇使用技能时召唤出一定数量的 [弓箭手](/upgrade/0001-Archer)。
    - 装备召唤出的弓箭手有隐身效果，持续时间随装备等级增加而增加。
    - 弓箭手木偶的召唤速度为每秒 5 个弓箭手。
    - 召唤出的弓箭手等级与 [实验室](/upgrade/0483-Laboratory) 中弓箭手的等级相同。
3. 除了召唤弓箭手外，该装备还可以为弓箭女皇提供额外的每秒伤害，并且增加开技能时恢复的生命值。

注意：如果升级费用中有多种资源，则同时需要多种资源才能升级。

在 2023 年 12 月装备系统发布时，已解锁弓箭女皇的玩家会有一个初始的装备等级，并且不需要解锁铁匠铺。装备等级与玩家的英雄等级相关，具体如下表。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/02/10">
        <TimelineRow>所有等级弓箭手木偶的每秒伤害增加值和开启技能后生命值恢复加成提高。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>现在 8 本就可以解锁弓箭女皇了，该页面的部分信息需要同步更改。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/09/09">
        <TimelineRow>现在弓箭手木偶装备召唤出的弓箭手有隐身效果了。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>游戏新增装备系统，弓箭手木偶是第一批推出的装备。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
