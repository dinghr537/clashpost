---
title: "部落冲突 coc 夜世界电火法师升级数据"
navTitle: "电火法师"
shownTitle: "电火法师"
module: upgrade-bh
imgFolder: bh_tech/100b
wiki: https://clashofclans.fandom.com/wiki/Electrofire_Wizard
canonical: /upgrade/100b-Electrofire-Wizard
dataSyncedOn: 2026-10-13
description: "作为精通魔法的时尚达人，电火法师既可释放烈火焚烧单一目标，也可使用超强电流电击多重目标。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/100b-Electrofire-Wizard.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-05-15'">

<template #introduction>

- *如想查看家乡的超级法师，请访问：[超级法师](/upgrade/0609-Super-Wizard)。*
- *如想查看都城的超级法师，请访问：[都城超级法师](/upgrade/2005-Super-Wizard)。*

<SwitchTabs contentClass="cp-unit-items" :stickyTabs="true" :pageTabs="true">
    <SwitchTab tabId="cp-unit-item-0" :activeTab="true">烈火模式</SwitchTab>
    <SwitchTab tabId="cp-unit-item-1">电击模式</SwitchTab>
</SwitchTabs>

<SwitchTabGroup id="cp-unit-item-0" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Electrofire_Wizard_Fire_info.png" imgAlt="电火法师（烈火模式）" :description="$frontmatter.description" />

\* 烈火模式（默认）：射出随时间增加伤害的烈焰射线。电击模式：发射蓄能缓慢但可在多个目标间弹跳的雷电攻击。

</SwitchTabGroup>

<SwitchTabGroup id="cp-unit-item-1" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Electrofire_Wizard_Electro_info.png" imgAlt="电火法师（电击模式）" :description="$frontmatter.description" />

\* 烈火模式（默认）：射出随时间增加伤害的烈焰射线。电击模式：发射蓄能缓慢但可在多个目标间弹跳的雷电攻击。

</SwitchTabGroup>

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/05/15">
        <TimelineRow>夜世界 10 本新兵种：电火法师。该兵种一解锁就是 17 级，你不需要从 1 级开始升。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
