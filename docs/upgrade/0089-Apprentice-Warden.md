---
title: "部落冲突 coc 守护者学徒（小咏王）升级数据"
navTitle: "守护者学徒"
shownTitle: "守护者学徒（小咏王）"
module: upgrade-home
imgFolder: home_tech/0089
wiki: https://clashofclans.fandom.com/wiki/Apprentice_Warden
canonical: /upgrade/0089-Apprentice-Warden
dataSyncedOn: 2026-10-13
description: "虽然守护者学徒雄心勃勃，但他只是一位学徒，所以他只能使用神奇的生命光环和没那么神奇的弹弓助部队一臂之力。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0089-Apprentice-Warden.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-10-06'">

<template #introduction>

- *如想查看大守护者，请访问：[大守护者（咏王）](/upgrade/0202-Grand-Warden)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Apprentice_Warden_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

1. 守护者学徒拥有和 [大守护者](/upgrade/0202-Grand-Warden)<sup>*</sup> 类似的生命光环效果，这个光环效果可以为周围的部队提供生命值加成。
   - \* 这里指带上 [生命宝石](/upgrade/0781-Life-Gem) 这个初始装备后的大守护者，下同。
2. 和大守护者类似，守护者学徒的光环对自己无效，但对附近的其他守护者学徒有效。如果使用多个守护者学徒，他们可以互相加血。
3. 守护者学徒的光环对英雄有效。
4. 守护者学徒的光环加成没有上限，4 级守护者学徒能实实在在地给 95 级 [蛮王](/upgrade/0200-Barbarian-King) 加 2900 多血，而大守护者由于上限的存在，只能给加 575 血。
5. 虽然守护者学徒能给高血量兵种加的血比大守护者多，但是它的光环效果会被大守护者覆盖，因为大守护者的光环加成比例是更高的，只是那个上限影响了大守护者的发挥。
6. 守护者学徒没有类似大守护者的飞行模式，但它拥有大守护者的跳墙能力。
7. 虽然从纸面上来说守护者学徒攻击时没有首选目标，但他更愿意跟随附近的部队，并与大部队一起攻击同样的目标，只要这些部队数量够多。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/10/06">
        <TimelineRow>4 级守护者学徒的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/27">
        <TimelineRow>部队的训练时间取消，但增加了捐赠费用。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>2 ~ 4 级守护者学徒的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/02/10">
        <TimelineRow>守护者学徒的训练时间由 4:00 改为 2:50</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>2 ~ 4 级守护者学徒的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/18">
        <TimelineRow>3 ~ 4 级守护者学徒的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/03/26">
        <TimelineRow>所有等级守护者学徒的光环加血比例减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>3 ~ 4 级守护者学徒的升级时间减少。</TimelineRow>
    <TimelineRow>3 级守护者学徒的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>13 本可解锁新兵种：守护者学徒。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
