---
title: "部落冲突 coc 实验助手（实验室助理）升级数据"
navTitle: "实验助手"
shownTitle: "实验助手（实验室助理）"
module: upgrade-home
imgFolder: home_tech/0800
wiki: https://clashofclans.fandom.com/wiki/Lab_Assistant
canonical: /upgrade/0800-Lab-Assistant
dataSyncedOn: 2026-10-13
description: "实验助手可以加快研究速度。您每天可以指派他一次，升级实验助手还会提升其工作速度！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0800-Lab-Assistant.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2024-11-25'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Lab_Assistant_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

1. 实验助手在家乡 [大本营](/upgrade/0400-Town-Hall) 达到 9 级后可以解锁。
2. 解锁后，实验助手可被指派到实验室正在进行的部队、法术、攻城机器升级，从而缩短整体研究时间。
   - 实验助手每天可以工作 1 小时，冷却时间为 23 小时。
   - 实验助手无法独自完成任务，如果任务在实验助手的工作期间完成，则他会提前停止工作，并且在冷却时间结束之前无法给他分配其他任务。
   - 实验助手只能在家乡的实验室工作，无法前往 [战宠小屋](/upgrade/0487-Pet-House)、[英雄殿堂](/upgrade/0489-Hero-Hall) 以及夜世界 [星空实验室](/upgrade/1282-Star-Laboratory) 工作。
3. 升级实验助手可提高其工作效率，从而节省更多时间。
   - 升级实验助手无需花费时间，但需要花费宝石。
   - 你不能在实验助手工作期间升级他。
4. 研究药水对实验助手无效。
5. 黄金令牌的建造加成不能减少升级实验助手所需的宝石。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2024/11/25">
        <TimelineRow>新角色：实验助手，9 本可解锁。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
