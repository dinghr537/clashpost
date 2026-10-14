---
title: "部落冲突 coc 超级亡灵（超苍、马云）升级数据"
navTitle: "超级亡灵"
shownTitle: "超级亡灵（超苍、马云）"
module: upgrade-home
imgFolder: home_tech/0608
wiki: https://clashofclans.fandom.com/wiki/Super_Minion
canonical: /upgrade/0608-Super-Minion
dataSyncedOn: 2026-10-13
description: "超级亡灵的大脑门可不光是好看，更代表了智慧！既然体型变大让它无法躲开搜空地雷，那从安全距离远程攻击防御建筑显然非常明智！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0608-Super-Minion.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2026-01-28'">

<template #introduction>

- *如想查看该兵种的普通版本，请访问：[亡灵](/upgrade/0080-Minion)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Super_Minion_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

超级亡灵的技能（远程狙杀）：当超级亡灵作进攻方时，其前 8 次攻击为远距离攻击；作防守方时，其前 3 次攻击为远距离攻击。

\* 4 - 7 级超级亡灵只在 奖章活动 中出现，不能通过常规方式得到。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2026/01/28">
        <TimelineRow>超级亡灵的“远程狙杀”技能在进攻时的远距离攻击次数由 7 次改为 8 次，防守时保持 3 次不变。</TimelineRow>
        <TimelineRow>超级亡灵的“远程狙杀”技能的射程由 10 格提升到 10.25 格。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/11/17">
        <TimelineRow>18 本推出，并在 18 本新增 14 级亡灵，超级部队的等级也相应更新。</TimelineRow>
        <TimelineRow>13 级超级亡灵的每秒伤害和生命值增加。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/06/30">
        <TimelineRow>超级亡灵的“远程狙杀”技能在进攻时的远距离攻击次数由 6 次改为 7 次，防守时保持 3 次不变。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/27">
        <TimelineRow>部队的训练时间取消，但增加了捐赠费用。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/02/10">
        <TimelineRow>超级亡灵的训练时间由 1:48 改为 1:36</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>17 本推出，并在 17 本新增 13 级亡灵，超级部队的等级也相应更新。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/02/27">
        <TimelineRow>16 本新增 12 级亡灵，超级部队的等级也相应更新。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/01/23">
        <TimelineRow>超级亡灵在进攻时，其技能“远程狙杀”的效果从前 5 次为远距离攻击调整为前 6 次。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>参加防守的超级亡灵现在只有前 3 次攻击为远距离攻击。</TimelineRow>
        <TimelineRow>15 本推出，并在 15 本新增 11 级亡灵，超级部队的等级也相应更新。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/05/02">
        <TimelineRow>家乡所有空军的攻击距离减少 0.5 格（超级飞龙除外，这玩意削了 1 格）。</TimelineRow>
        <TimelineRow>超级亡灵的远程狙杀技能的攻击距离减少 0.5 格。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>14 本推出，并在 14 本新增 10 级亡灵，超级部队的等级也相应更新。</TimelineRow>
        <TimelineRow>超级亡灵每秒伤害值降低 50，生命值提高 100。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/12/07">
        <TimelineRow>超级部队的有效时间从 7 天缩短为 3 天。</TimelineRow>
        <TimelineRow>所有部队的强化费用统一调整为 25,000 暗黑重油。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/10/23">
        <TimelineRow>超级亡灵远距离攻击时不再有额外伤害（维护前有 65 的额外伤害）。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/10/12">
        <TimelineRow>新的超级兵种：超级亡灵。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
