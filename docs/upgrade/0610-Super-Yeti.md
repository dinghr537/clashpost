---
title: "部落冲突 coc 超级大雪怪升级数据"
navTitle: "超级大雪怪"
shownTitle: "超级大雪怪"
module: upgrade-home
imgFolder: home_tech/0610
wiki: https://clashofclans.fandom.com/wiki/Super_Yeti
canonical: /upgrade/0610-Super-Yeti
dataSyncedOn: 2026-10-13
description: "这个神秘的蒙面大雪怪蓄势待发！每当他受到伤害，都会召唤出电力十足的小雪怪，电击最近的建筑，引发毁灭性的连锁反应！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0610-Super-Yeti.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-05-12'">

<template #introduction>

- *如想查看该兵种的普通版本，请访问：[大雪怪](/upgrade/000d-Yeti)。*

<SwitchTabs contentClass="cp-unit-items" :stickyTabs="true" :pageTabs="true">
    <SwitchTab tabId="cp-unit-item-0" :activeTab="true">超级大雪怪</SwitchTab>
    <SwitchTab tabId="cp-unit-item-1">雷电小雪怪</SwitchTab>
</SwitchTabs>

<SwitchTabGroup id="cp-unit-item-0" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Super_Yeti_info.png" imgAlt="超级大雪怪"
    description="这个神秘的蒙面大雪怪蓄势待发！每当他受到伤害，都会召唤出电力十足的小雪怪，电击最近的建筑，引发毁灭性的连锁反应！" />

<SmallTitle>重要说明</SmallTitle>

超级大雪怪的技能（闪电狂袭）：超级大雪怪受伤时会分裂出雷电小雪怪，具体来说是每受到 400 点伤害分裂一个，分裂完为止。

\* 1 - 2 级超级大雪怪只在 奖章活动 中出现，不能通过常规方式得到。

</SwitchTabGroup>

<SwitchTabGroup id="cp-unit-item-1" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Electromite_info.png" imgAlt="雷电小雪怪"
    description="超级大雪怪受伤时，这些带电的小家伙会立刻行动，电击最近的建筑，引发惊人的连锁反应！"
    :isSmallImg="true" />

<SmallTitle>重要说明</SmallTitle>

1. 雷电小雪怪可以跳过城墙。
2. 雷电小雪怪攻击一次后就会死亡，[大守护者](/upgrade/0202-Grand-Warden) 的 [永恒书卷](/upgrade/0780-Eternal-Tome) 装备也无法阻止。

攻击偏好：雷电小雪怪优先攻击建筑（注意并不一定是防御建筑），如果有城堡部队或英雄攻击它，它可以反击，反击完后继续攻击建筑。如果所有的建筑均被 [隐形法术](/upgrade/0106-Invisibility-Spell) 隐形，或被 [蔓生法术](/upgrade/0185-Overgrowth-Spell) 缠绕，则雷电小雪怪会攻击最近的目标。<br>
占据人口：在考虑雷电小雪怪与 [隐形弹簧](/upgrade/0381-Spring-Trap)、[镜像法术](/upgrade/0105-Clone-Spell) 或 [回溯法术](/upgrade/0107-Recall-Spell) 的相互作用时，雷电小雪怪应被视为 3 人口。<br>
攻击时机：根据解析安装包的结果，雷电小雪怪的攻击速度是一秒一次，但实际上雷电小雪怪的首次攻击时机为到达目标后 0.5 秒，且攻击一次后就会死亡，因此其攻速值无意义。

\* 1 - 2 级雷电小雪怪只在 奖章活动 中出现，不能通过常规方式得到。
</SwitchTabGroup>

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/05/12">
        <TimelineRow>超级大雪怪于 2025 年 5 月的“迷你大舞台”活动中正式推出，并作为永久兵种加入游戏。</TimelineRow>
        <TimelineRow>与之前相比，6 - 7 级超级大雪怪可分裂出的雷电小雪怪数量略微减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/27">
        <TimelineRow>官方确认之前添加超级大雪怪并非有意为之，并移除了该兵种。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>新增超级大雪怪。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
