---
title: "部落冲突 coc 大雪怪升级数据"
navTitle: "大雪怪"
shownTitle: "大雪怪"
module: upgrade-home
imgFolder: home_tech/000d
wiki: https://clashofclans.fandom.com/wiki/Yeti
canonical: /upgrade/000d-Yeti
dataSyncedOn: 2026-10-13
description: "这个毛茸茸的家伙力气很大，他喜欢极寒天气，对自己的小雪怪们情有独钟。千万不要伤害大雪怪，否则小雪怪们会要你好看。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/000d-Yeti.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-11-17'">

<template #introduction>

- *如想查看该兵种的强化版本，请访问：[超级大雪怪](/upgrade/0610-Super-Yeti)。*

<SwitchTabs contentClass="cp-unit-items" :stickyTabs="true" :pageTabs="true">
    <SwitchTab tabId="cp-unit-item-0" :activeTab="true">大雪怪</SwitchTab>
    <SwitchTab tabId="cp-unit-item-1">小雪怪</SwitchTab>
</SwitchTabs>

<SwitchTabGroup id="cp-unit-item-0" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Yeti_info.png" imgAlt="大雪怪"
    description="这个毛茸茸的家伙力气很大，他喜欢极寒天气，对自己的小雪怪们情有独钟。千万不要伤害大雪怪，否则小雪怪们会要你好看。" />

<SmallTitle>重要说明</SmallTitle>

每受到 600 伤害，大雪怪就会释放一个小雪怪，大雪怪死亡后会释放剩余的全部小雪怪。

</SwitchTabGroup>

<SwitchTabGroup id="cp-unit-item-1" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Yetimite_info.png" imgAlt="小雪怪"
    description="这些小家伙看上去很可爱，但如果大雪怪受伤，他们会变得无比焦虑。如果大雪怪被伤到了一定程度，他们会义无反顾地涌向最近的防御建筑。" />

<SmallTitle>重要说明</SmallTitle>

1. 小雪怪本身不会触发陷阱，但是大雪怪踩中的 [大炸弹](/upgrade/0383-Giant-Bomb) 等陷阱可能会伤害到小雪怪。
2. 小雪怪对防御建筑的伤害是 4 倍，对带有武器的 [大本营](/upgrade/0400-Town-Hall) 是 2 倍，对不带武器的大本以及其他资源建筑为二分之一。
    - 大本营的武器在升级时应视为不带武器的大本。
    - 此处我们**不**将 [铁匠铺](/upgrade/0488-Blacksmith) 视为资源建筑。
3. 小雪怪攻击时会先接近目标建筑，然后在短暂停顿后跳到建筑身上并造成伤害。在跳跃状态下，小雪怪是无敌的，且不能被其他单位锁定。
4. 小雪怪攻击一次后就会死亡，[大守护者](/upgrade/0202-Grand-Warden) 的 [永恒书卷](/upgrade/0780-Eternal-Tome) 装备也无法阻止。

占据人口：在考虑小雪怪与 [隐形弹簧](/upgrade/0381-Spring-Trap)、[镜像法术](/upgrade/0105-Clone-Spell) 或 [回溯法术](/upgrade/0107-Recall-Spell) 的相互作用时，小雪怪应被视为 2 人口。<br>
攻击时机：根据解析安装包的结果，小雪怪的攻击速度是一秒一次，但实际上小雪怪的首次攻击时机为到达目标后 0.5 秒，且攻击一次后就会死亡，因此其攻速值无意义。

</SwitchTabGroup>

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/11/17">
        <TimelineRow>7 级大雪怪的升级时间和升级费用减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/10/06">
        <TimelineRow>2 ~ 6 级大雪怪的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/04/14">
        <TimelineRow>小雪怪占据的人口数由 1 调整为 2.</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/27">
        <TimelineRow>部队的训练时间取消，但增加了捐赠费用。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>在 17 本新增 7 级大雪怪。</TimelineRow>
        <TimelineRow>2 ~ 6 级大雪怪的升级时间减少。</TimelineRow>
        <TimelineRow>2 ~ 3、5 ~ 6 级大雪怪的升级费用降低。</TimelineRow>
        <TimelineRow>小雪怪和小冰怪占据的人口数由 3 调整为 1.</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/02/10">
        <TimelineRow>大雪怪的训练时间由 3:00 改为 2:30</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>2 ~ 6 级大雪怪的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/18">
        <TimelineRow>4 ~ 5 级大雪怪的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/04/17">
        <TimelineRow>在 16 本新增 6 级大雪怪。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>2 ~ 5 级大雪怪的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>15 本新增 5 级大雪怪。</TimelineRow>
        <TimelineRow>2 ~ 3 级大雪怪的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>2 ~ 4 级大雪怪的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/12/09">
        <TimelineRow>2 级大雪怪的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/09/27">
        <TimelineRow>14 本新增 4 级大雪怪。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/03/30">
        <TimelineRow>小雪怪对防御建筑的伤害仍然是 4 倍，但对带有武器的大本削弱为 2 倍，资源建筑削弱为二分之一。</TimelineRow>
        <TimelineRow>大守护者不再跟随小雪怪。</TimelineRow>
        <TimelineRow>天鹰火炮不再将小雪怪作为目标。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/01/16">
        <TimelineRow>小雪怪不再触发陷阱。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/12/09">
        <TimelineRow>12 本可解锁新兵种：大雪怪。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
