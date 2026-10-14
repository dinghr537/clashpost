---
title: "部落冲突 coc 熔岩猎犬（狗）升级数据"
navTitle: "熔岩猎犬"
shownTitle: "熔岩猎犬（狗）"
module: upgrade-home
imgFolder: home_tech/0085
wiki: https://clashofclans.fandom.com/wiki/Lava_Hound
canonical: /upgrade/0085-Lava-Hound
dataSyncedOn: 2026-10-13
description: "这些暴躁的猛兽会不由自主地寻找防空火箭，为其他部队提供绝佳的保护。被摧毁后，它们会分裂成多个体型和威胁都更小的迷你熔岩犬。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0085-Lava-Hound.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2026-02-23'">

<template #introduction>

- *如想查看该兵种的强化版本，请访问：[寒冰猎犬](/upgrade/060a-Ice-Hound)。*
- *游戏中有一个战宠也常常被玩家称作狗，详见：[莱希](/upgrade/0280-L.A.S.S.I)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Lava_Hound_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

1. 熔岩猎犬死亡后可以分裂出若干迷你熔岩犬（小狗）。
2. 小狗可以攻击空中目标，但分裂之前的大狗不行。

\* 熔岩猎犬有三段攻击偏好。场上有防空火箭时攻击 [防空火箭](/upgrade/0304-Air-Defense)，没有防空火箭时攻击其他防御建筑，没有防御建筑时攻击非防御建筑。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2026/02/23">
        <TimelineRow>在 18 本新增 8 级熔岩猎犬。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/06/16">
        <TimelineRow>在 16 本新增 7 级熔岩猎犬。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/27">
        <TimelineRow>部队的训练时间取消，但增加了捐赠费用。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>3 ~ 6 级熔岩猎犬的升级时间减少。</TimelineRow>
        <TimelineRow>迷你熔岩猎犬、迷你寒冰猎犬和迷你熔岩气球犬占用的人口数由 2 调整为 1.</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/02/10">
        <TimelineRow>熔岩猎犬的训练时间由 5:00 改为 4:20</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>2 ~ 5 级熔岩猎犬的升级时间减少。</TimelineRow>
        <TimelineRow>2 ~ 6 级熔岩猎犬的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/18">
        <TimelineRow>3 ~ 4 级熔岩猎犬的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>3、5 ~ 6 级熔岩猎犬的升级时间减少。</TimelineRow>
        <TimelineRow>2 ~ 3 级熔岩猎犬的升级费用降低。</TimelineRow>
        <TimelineRow>2 ~ 6 级熔岩猎犬防守时分裂出的小狗数量减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>5 ~ 6 级熔岩猎犬的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/05/15">
        <TimelineRow>修复远程地面部队在试图瞄准防御中且飞出游戏地图的迷你熔岩猎犬时，偶尔会卡住的问题。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>3 ~ 6 级熔岩猎犬的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/05/02">
        <TimelineRow>家乡所有空军的攻击距离减少 0.5 格（超级飞龙除外，这玩意削了 1 格）。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>如果熔岩猎犬和寒冰猎犬在选择目标时，场上剩余的防空火箭都被隐形了，它们不会忘记锁定之前没有看到的防空火箭。</TimelineRow>
        <TimelineRow>2 ~ 5 级熔岩猎犬的升级费用降低。</TimelineRow>
        <TimelineRow>2 ~ 3 级熔岩猎犬的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/10/12">
        <TimelineRow>2 ~ 4 级熔岩猎犬的升级时间减少。</TimelineRow>
        <TimelineRow>2 级和 4 级熔岩猎犬的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/06/22">
        <TimelineRow>13 本新增 6 级熔岩猎犬。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/12/09">
        <TimelineRow>熔岩猎犬死亡后的爆炸半径从 5 格减少到 3.5 格。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
