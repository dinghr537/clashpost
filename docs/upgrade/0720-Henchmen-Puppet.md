---
title: "部落冲突 coc 护卫玩偶装备升级数据"
navTitle: "护卫玩偶"
shownTitle: "护卫玩偶"
module: upgrade-home
imgFolder: home_heroes/0720
wiki: https://clashofclans.fandom.com/wiki/Henchmen_Puppet
canonical: /upgrade/0720-Henchmen-Puppet
dataSyncedOn: 2026-10-13
description: "护卫玩偶是亡灵王子的两件初始装备之一，另一件是暗黑魔球。护卫玩偶装备可以让亡灵王子使用技能时召唤出两个空中护卫。激活技能后，亡灵王子会短暂隐身，此时空中护卫的作用就是替英雄扛伤害。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0720-Henchmen-Puppet.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-11-17'">

<template #introduction>

<SwitchTabs contentClass="cp-unit-items" :stickyTabs="true" :pageTabs="true">
    <SwitchTab tabId="cp-unit-item-0" :activeTab="true">护卫玩偶</SwitchTab>
    <SwitchTab tabId="cp-unit-item-1">空中护卫</SwitchTab>
</SwitchTabs>

<SwitchTabGroup id="cp-unit-item-0" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Henchmen_Puppet_info.png" imgAlt="护卫玩偶" description="召唤空中护卫来增援亡灵王子" />

<SmallTitle>说明</SmallTitle>

1. 护卫玩偶是 [亡灵王子](/upgrade/0204-Minion-Prince) 的两件初始装备之一，另一件是 [暗黑魔球](/upgrade/0721-Dark-Orb)。
2. 护卫玩偶装备可以让亡灵王子使用技能时召唤出两个空中护卫。激活技能后，亡灵王子会短暂隐身，此时空中护卫的作用就是替英雄扛伤害。
3. 除了召唤空中护卫外，该装备还拥有以下功能：
    - 提供额外的每秒伤害；
    - 增加生命值（与是否开技能无关）；
    - 增加开技能时恢复的生命值。

注意：

4. 如果升级费用中有多种资源，则同时需要多种资源才能升级。
5. 如果玩家升级到了 9 本并解锁了亡灵王子，即使玩家没有马上升 [铁匠铺](/upgrade/0488-Blacksmith) 也可以升级护卫玩偶装备。
</SwitchTabGroup>

<SwitchTabGroup id="cp-unit-item-1" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Henchmen_info.png" imgAlt="护卫玩偶装备的空中护卫"
    description="亡灵王子可以召唤这些邪恶的兄弟姐妹与他并肩作战！他们会吸收伤害并攻击防御建筑。" />

<SmallTitle>说明</SmallTitle>

空中护卫不能在 [训练营](/upgrade/0481-Barracks) 或 [暗黑训练营](/upgrade/0482-Dark-Barracks) 中直接训练，只能通过护卫玩偶装备召唤。

</SwitchTabGroup>

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/11/17">
        <TimelineRow>现在亡灵王子的所有装备都提供 500 生命值加成。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>亡灵王子的初始装备随英雄的推出而同步推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
