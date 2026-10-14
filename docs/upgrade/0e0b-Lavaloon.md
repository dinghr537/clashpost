---
title: "部落冲突 coc 熔岩气球升级数据"
navTitle: "熔岩气球"
shownTitle: "熔岩气球"
module: upgrade-temp
imgFolder: temp_troops/0e0b
wiki: https://clashofclans.fandom.com/wiki/Lavaloon
canonical: /upgrade/0e0b-Lavaloon
dataSyncedOn: 2026-10-13
description: "兼具气球兵的强力炸弹和熔岩猎犬的坚硬外壳，熔岩气球能轻松摧毁基地，一炸一个坑！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0e0b-Lavaloon.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-10-10'">

<template #introduction>

- *如想查看熔岩气球玩偶装备派生出来的同名兵种，请访问：[熔岩气球玩偶](/upgrade/0785-Lavaloon-Puppet)。*

<SwitchTabs contentClass="cp-unit-items" :stickyTabs="true" :pageTabs="true">
    <SwitchTab tabId="cp-unit-item-0" :activeTab="true">熔岩气球</SwitchTab>
    <SwitchTab tabId="cp-unit-item-1">迷你熔岩气球犬</SwitchTab>
</SwitchTabs>

<SwitchTabGroup id="cp-unit-item-0" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Lavaloon_info.png" imgAlt="熔岩气球"
    description="兼具气球兵的强力炸弹和熔岩猎犬的坚硬外壳，熔岩气球能轻松摧毁基地，一炸一个坑！" />

<SmallTitle>重要说明</SmallTitle>

1. 熔岩气球在 2023 年 10 月的合体狂潮活动中首次推出，在活动中获取 35 000 酸腐圣水（任务点数）即可解锁，并在 2024 年 10 月的合体狂热活动中返场，这次只需 100 酸腐圣水即可解锁。
2. 熔岩气球的 AI 类似于 [熔岩猎犬](/upgrade/0085-Lava-Hound) 和 [寒冰猎犬](/upgrade/060a-Ice-Hound)，同样以防空火箭为优先攻击目标，同样有分裂功能。

\* 熔岩气球在到达目标的途中会释放炸弹，每次炸弹爆炸时都会分裂出一只迷你熔岩气球犬。另外，熔岩气球死亡时会额外分裂一些迷你熔岩气球犬。

</SwitchTabGroup>

<SwitchTabGroup id="cp-unit-item-1" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Lavaloon_Pup_info.png" imgAlt="迷你熔岩气球犬"
    description="这些调皮的绿色小怪物就是为战斗而生的，无论什么情况他们都会接着战斗。" />

</SwitchTabGroup>

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/10/10">
        <TimelineRow>该兵种第 3 次推出，有效期至 2025/11/01.</TimelineRow>
        <TimelineRow>熔岩气球占用的人口数由 23 调整为 35.</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>迷你熔岩猎犬、迷你寒冰猎犬和迷你熔岩气球犬占用的人口数由 2 调整为 1.</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/10/11">
        <TimelineRow>该兵种第 2 次推出，是 2024 年合体狂热活动中的五个临时兵种之一。</TimelineRow>
        <TimelineRow>与 2023 版相比，该兵种新增了第 11 个等级，但 10 级的伤害和生命值降低了。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/10/20">
        <TimelineRow>所有等级的熔岩气球的生命值减少 10%.</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/10/13">
        <TimelineRow>该兵种第 1 次推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
