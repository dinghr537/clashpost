---
title: "部落冲突 coc 哥布林升级数据"
navTitle: "哥布林"
shownTitle: "哥布林"
module: upgrade-home
imgFolder: home_tech/0003
wiki: https://clashofclans.fandom.com/wiki/Goblin
canonical: /upgrade/0003-Goblin
dataSyncedOn: 2026-10-13
description: "这些麻烦的小家伙眼里只有一件事：资源！他们的反应比隐形弹簧更快，会无休止地取得资源。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0003-Goblin.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-10-06'">

<template #introduction>

- *如想查看该兵种的强化版本，请访问：[隐秘哥布林（超哥）](/upgrade/0601-Sneaky-Goblin)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Goblin_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

1. 哥布林攻击资源类建筑时，其伤害翻倍。
2. [铁匠铺](/upgrade/0488-Blacksmith) 免疫 [雷电法术](/upgrade/0100-Lightning-Spell) 伤害，理论上属于资源类建筑，但不被哥布林优先攻击，哥布林的攻击伤害也不会翻倍。
3. 2025/10 更新后，哥布林的反应已经没有隐形弹簧快了，但游戏内仍然保留了“他们的反应比隐形弹簧更快”这段介绍。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/10/06">
        <TimelineRow>8 ~ 9 级哥布林的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/27">
        <TimelineRow>部队的训练时间取消，但增加了捐赠费用。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>2 ~ 9 级哥布林的升级时间减少。</TimelineRow>
        <TimelineRow>5 ~ 9 级哥布林的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>2 ~ 3、6 ~ 9 级哥布林的升级时间减少。</TimelineRow>
        <TimelineRow>3、8、9 级哥布林的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/18">
        <TimelineRow>7 ~ 9 级哥布林的升级时间减少。</TimelineRow>
        <TimelineRow>9 级哥布林的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>7 ~ 9 级哥布林的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>15 本新增 9 级哥布林。</TimelineRow>
    <TimelineRow>8 级哥布林的升级时间减少。</TimelineRow>
        <TimelineRow>8 级哥布林的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>7 ~ 8 级哥布林的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/12/09">
        <TimelineRow>2 ~ 4，6 ~ 8 级哥布林的升级费用降低。</TimelineRow>
        <TimelineRow>2 ~ 7 级哥布林的升级时间减少。</TimelineRow>
        <TimelineRow>4 ~ 7 级哥布林的生命值提升。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>3 ~ 8 级的哥布林的升级费用降低。</TimelineRow>
        <TimelineRow>3 ~ 7 级哥布林的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020-03-30">
        <TimelineRow>5 ~ 7 级哥布林的升级费用降低。</TimelineRow>
    <TimelineRow>12 本新增 8 级哥布林。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019-04-02">
        <TimelineRow>包含大量降低发展成本和提高发展速度的调整，其中 5 ~ 7 级哥布林的升级时间下调。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019-02-22">
        <TimelineRow>4 ~ 7 级哥布林的生命值提高。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
