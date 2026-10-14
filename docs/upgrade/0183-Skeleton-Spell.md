---
title: "部落冲突 coc 骷髅法术升级数据"
navTitle: "骷髅法术"
shownTitle: "骷髅法术"
module: upgrade-home
imgFolder: home_tech/0183
wiki: https://clashofclans.fandom.com/wiki/Skeleton_Spell
canonical: /upgrade/0183-Skeleton-Spell
dataSyncedOn: 2026-10-13
description: "在战场任意位置召唤一群骷髅兵！必要的时候，在关键位置召唤出一群骷髅兵补上那么几刀可解燃眉之急。骷髅兵不会触发陷阱。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0183-Skeleton-Spell.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-10-06'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Skeleton_Spell.png" :imgAlt="$frontmatter.navTitle"
    description="在战场任意位置召唤一群骷髅兵！<br>必要的时候，在关键位置召唤出一群骷髅兵补上那么几刀可解燃眉之急。骷髅兵不会触发陷阱。"
    :isSmallImg="true" />

<SmallTitle>重要说明</SmallTitle>

1. 骷髅法术召唤出的骷髅兵会带有盔甲。也就是说，兵种至少需要攻击两次才能击杀骷髅兵（第一次打掉盔甲，第二次打死没有盔甲的骷髅兵）。
2. 骷髅对 [大本营](/upgrade/0400-Town-Hall) 和资源罐的伤害为对其他建筑的 15%.
3. 骷髅无法触发城堡内的援兵。
4. 虽然骷髅本身无法触发陷阱，但是被其他地面单位触发的陷阱还是有可能攻击骷髅。

\* 第一次生成 4 个骷髅，之后每秒生成一个。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/10/06">
        <TimelineRow>4 ~ 8 级骷髅法术的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/27">
        <TimelineRow>法术的配置时间取消，但新增了捐赠费用。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>3 ~ 5、8 级骷髅法术的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>2 ~ 8 级骷髅法术的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/18">
        <TimelineRow>8 级骷髅法术的升级时间减少。</TimelineRow>
        <TimelineRow>8 级骷髅法术的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>4 ~ 8 级骷髅法术的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>15 本新增 8 级骷髅法术。</TimelineRow>
        <TimelineRow>5 ~ 7 级骷髅法术的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>2 ~ 7 级骷髅法术的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/06/27">
        <TimelineRow>1 ~ 6 级骷髅法术可召唤的骷髅数量增加。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/12/09">
        <TimelineRow>2 ~ 4 级骷髅法术的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>2 ~ 4 级骷髅法术的升级费用降低。</TimelineRow>
        <TimelineRow>2 ~ 6 级骷髅法术的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/10/12">
        <TimelineRow>所有等级的骷髅法术可召唤的骷髅兵数量增加 1 个。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/05/20">
        <TimelineRow>7 级骷髅法术召唤的骷髅兵数量从 16 个增加至 17 个。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/03/30">
        <TimelineRow>2 ~ 3 级骷髅法术的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/12/09">
        <TimelineRow>13 本新增 7 级骷髅法术。</TimelineRow>
        <TimelineRow>骷髅生成频率改为每秒 1 个（经测试，这是平均值）。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/06/18">
        <TimelineRow>12 本新增 6 级骷髅法术。</TimelineRow>
        <TimelineRow>更新后，骷髅法术召唤出的骷髅兵会带有盔甲。也就是说，兵种至少需要攻击两次才能击杀骷髅兵。（第一次打掉盔甲，第二次打死没有盔甲的骷髅兵）</TimelineRow>
        <TimelineRow>骷髅法术召唤出的骷髅兵数量减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
