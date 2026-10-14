---
title: "部落冲突 coc 雷电飞龙升级数据"
navTitle: "雷电飞龙"
shownTitle: "雷电飞龙"
module: upgrade-home
imgFolder: home_tech/000c
wiki: https://clashofclans.fandom.com/wiki/Electro_Dragon
canonical: /upgrade/000c-Electro-Dragon
dataSyncedOn: 2026-10-13
description: "雷电飞龙拥有钢铁般坚硬的鳞片，还能从高空中喷吐雷电。它最喜欢从空中对敌方实施毁灭性打击。被消灭时，雷电飞龙还会释放雷电再次劈向敌方！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/000c-Electro-Dragon.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2026-01-12'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Electro_Dragon_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

1. 雷电飞龙会对 3 格以内 (不含 3 格) 的兵种或建筑造成连锁伤害，闪电的下次连锁伤害为上次的 80%，伤害比例为 100%、80%、64%、51.2%、41%，连锁延迟为 0.128 秒。
2. 雷电飞龙死亡后会对附近目标造成 6 次闪电伤害。
3. 雷电飞龙死亡后，正在连锁的雷电会消失。
4. 雷龙背后的背鳍是蓄能标志，共 5 个。当第 4 个亮起的时候已经蓄能完毕，就算部队或英雄隐身也会被打到，第 5 个亮起只是攻击时顺带的动画。

<Pic src="/upgrade/description/Electro_Dragon_Example.jpg" caption="雷电飞龙背鳍示意图" maxWidth="25rem" :lazyLoading="false" width="443" height="260" />

5. 雷龙的闪电优先连锁最近目标，距离一样时优先弹射至生命值最高的目标，生命值一样时按照建筑内部 ID 以及建造先后顺序判断。注意：这里的“生命值”指的是建筑满血时的生命值，就算残血也按满血算。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2026/01/12">
        <TimelineRow>1 ~ 9 级雷电飞龙的每秒伤害和生命值增加。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/11/17">
        <TimelineRow>18 本推出，并在 18 本新增 9 级雷电飞龙。</TimelineRow>
        <TimelineRow>8 级雷电飞龙的升级时间和升级费用减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/10/06">
        <TimelineRow>2、3、6、7 级雷电飞龙的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/27">
        <TimelineRow>部队的训练时间取消，但增加了捐赠费用。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>2、4 ~ 7 级雷电飞龙的升级时间减少。</TimelineRow>
        <TimelineRow>2、6 ~ 7 级雷电飞龙的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/02/10">
        <TimelineRow>雷电飞龙的训练时间由 6:00 改为 4:20</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>17 本推出，并在 17 本新增 8 级雷电飞龙。</TimelineRow>
        <TimelineRow>5 ~ 7 级雷电飞龙的升级时间减少。</TimelineRow>
        <TimelineRow>4 ~ 7 级雷电飞龙的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/18">
        <TimelineRow>6 级雷电飞龙的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/02/27">
        <TimelineRow>6 ~ 7 级雷电飞龙的生命值提升。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>16 本推出，同时在 16 本新增 7 级雷电飞龙。</TimelineRow>
        <TimelineRow>2 ~ 6 级雷电飞龙的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>3 ~ 4 级雷电飞龙的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>15 本推出，并在 15 本新增 6 级雷电飞龙。</TimelineRow>
        <TimelineRow>2 ~ 5 级雷电飞龙的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/05/02">
        <TimelineRow>家乡所有空军的攻击距离减少 0.5 格（超级飞龙除外，这玩意削了 1 格）。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/02/15">
        <TimelineRow>雷电飞龙的移动速度从每秒 1.5 格改为每秒 1.6 格（12 改为 12.8，游戏内四舍五入到 13 了）。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/12/09">
        <TimelineRow>2 级雷电飞龙的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/06/15">
        <TimelineRow>14 本新增 5 级雷电飞龙。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/10/12">
        <TimelineRow>如果弹射范围内有多个等距离目标，雷电飞龙的闪电链会优先弹射至生命值最高的目标。注意：这里的“生命值”指的是建筑满血时的生命值，就算残血也按满血算。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/12/09">
        <TimelineRow>13 本开放，新增 4 级雷电飞龙。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/04/02">
        <TimelineRow>包含大量降低发展成本和提高发展速度的调整，其中所有等级的雷电飞龙训练费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
