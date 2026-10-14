---
title: "部落冲突 coc 熔岩气球玩偶装备升级数据"
navTitle: "熔岩气球玩偶"
shownTitle: "熔岩气球玩偶"
module: upgrade-home
imgFolder: home_heroes/0785
wiki: https://clashofclans.fandom.com/wiki/Lavaloon_Puppet
canonical: /upgrade/0785-Lavaloon-Puppet
dataSyncedOn: 2026-10-13
description: "熔岩气球玩偶是大守护者的第二件史诗装备，它在 2024 年 10 月的合体狂热活动中首次开放购买。熔岩气球玩偶装备可以使大守护者在使用技能时召唤几只熔岩气球。除了召唤熔岩气球外，熔岩气球玩偶装备还可以增加大守护者的每秒伤害和生命值。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0785-Lavaloon-Puppet.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2026-01-12'">

<template #introduction>

- *如想查看与装备的派生兵种同名的临时兵种，请访问：[熔岩气球](/upgrade/0e0b-Lavaloon)。*

<SwitchTabs contentClass="cp-unit-items" :stickyTabs="true" :pageTabs="true">
    <SwitchTab tabId="cp-unit-item-0" :activeTab="true">装备</SwitchTab>
    <SwitchTab tabId="cp-unit-item-1">熔岩气球</SwitchTab>
    <SwitchTab tabId="cp-unit-item-2">迷你熔岩气球犬</SwitchTab>
</SwitchTabs>

<SwitchTabGroup id="cp-unit-item-0" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Lavaloon_Puppet_info.png" imgAlt="熔岩气球玩偶" description="召唤可怕的熔岩气球。" />

<SmallTitle>说明</SmallTitle>

1. 熔岩气球玩偶是 [大守护者](/upgrade/0202-Grand-Warden) 的第二件史诗装备，它在 2024 年 10 月的合体狂热活动中首次开放购买。
2. 熔岩气球玩偶装备可以使大守护者在使用技能时召唤几只熔岩气球。
3. 除了召唤熔岩气球外，熔岩气球玩偶装备还可以增加大守护者的每秒伤害和生命值。

注：如果升级费用中有多种资源，则同时需要多种资源才能升级。

</SwitchTabGroup>

<SwitchTabGroup id="cp-unit-item-1" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Lavaloon_info.png" imgAlt="熔岩气球" description="兼具气球兵的强力炸弹和熔岩猎犬的坚硬外壳，熔岩气球能轻松摧毁基地，一炸一个坑！" />

<SmallTitle>重要说明</SmallTitle>

由装备召唤的熔岩气球与与临时兵种 [熔岩气球](/upgrade/0e0b-Lavaloon) 极为相似，比如：

- 两者都以防空火箭作为优先目标，且都有类似于 [熔岩猎犬](/upgrade/0085-Lava-Hound) 和 [寒冰猎犬](/upgrade/060a-Ice-Hound) 的三段式攻击偏好。
- 两者都有爆炸分裂的特殊技能。
- 两者的基本属性（移动速度、攻击速度等）相同，只是升级数据（各个等级的每秒伤害、生命值等）不同。

\* 熔岩气球在到达目标的途中会释放炸弹，每次炸弹爆炸时都会分裂出一只迷你熔岩气球犬。另外，熔岩气球死亡时会额外分裂一些迷你熔岩气球犬。

</SwitchTabGroup>

<SwitchTabGroup id="cp-unit-item-2" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Lavaloon_Pup_info.png" imgAlt="迷你熔岩气球犬" description="这些调皮的绿色小怪物就是为战斗而生的，无论什么情况他们都会接着战斗。" :isSmallImg="true" />

</SwitchTabGroup>

</template>

<template #history>

<Timeline>
    <TimelineItem date="2026/01/12">
        <TimelineRow>21 ~ 27 级熔岩气球玩偶召唤的熔岩气球数量由 2 增加到 3.</TimelineRow>
        <TimelineRow>熔岩气球占据的人口数由 23 减少到 21.</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/10/11">
        <TimelineRow>新装备：熔岩气球玩偶。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
