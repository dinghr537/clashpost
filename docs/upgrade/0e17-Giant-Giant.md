---
title: "部落冲突 coc 霸天巨人升级数据"
navTitle: "霸天巨人"
shownTitle: "霸天巨人"
module: upgrade-temp
imgFolder: temp_troops/0e17
wiki: https://clashofclans.fandom.com/wiki/Giant_Giant
canonical: /upgrade/0e17-Giant-Giant
dataSyncedOn: 2026-10-13
description: "霸天巨人的力量堪比十个普通巨人，他能对防御建筑造成巨大的溅射伤害。糟糕！如果他的生命值降至一半，则会进入狂暴状态，速度和力量大幅提升。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0e17-Giant-Giant.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2026-01-28'">

<template #introduction>

- *如想查看普通巨人，请访问：[巨人](/upgrade/0002-Giant)。*
- *如想查看巨人的强化版本，请访问：[超级巨人](/upgrade/0602-Super-Giant)。*
- *如想查看夜世界的巨人拳击手，请访问：[夜世界巨人拳击手](/upgrade/1002-Boxer-Giant)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Giant_Giant_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

1. 霸天巨人在 2025 年 4 月的是敌是友活动中首次作为临时兵种推出，玩家获得 100 活动门票（任务点数）后即可解锁。
2. 霸天巨人对 [城墙](/upgrade/0300-Walls) 有 2 倍伤害。
3. 当霸天巨人的生命值下降到一半时会进入狂暴状态，狂暴状态下霸天巨人的伤害和移动速度均有提升。狂暴效果持续 20 秒。
4. [弓箭女皇](/upgrade/0201-Archer-Queen) 的 [动作人偶](/upgrade/0746-Action-Figure) 装备召唤的兵种就是霸天巨人，其属性和本页中的霸天巨人相同。

\* 1 - 3 级的霸天巨人不能直接训练，需要在活动期间摧毁对手的兵营或者使用弓箭女皇的动作人偶装备才能获得。<br>
\# 11 - 15 级霸天巨人只能在活动期间训练。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2026/01/28">
        <TimelineRow>该兵种第 2 次推出，有效期至 2026/02/02.</TimelineRow>
        <TimelineRow>与上次推出时相比，大守护者对霸天巨人的跟随权重降低，天鹰火炮对霸天巨人的攻击权重降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/04/14">
        <TimelineRow>14 ~ 15 级霸天巨人的每秒伤害和生命值降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/04/08">
        <TimelineRow>该兵种第 1 次推出，有效期至 2025/04/29.</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
