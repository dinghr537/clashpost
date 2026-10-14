---
title: "部落冲突 coc 烈焰熔炉升级数据"
navTitle: "烈焰熔炉"
shownTitle: "烈焰熔炉"
module: upgrade-home
imgFolder: home_tech/008b
wiki: https://clashofclans.fandom.com/wiki/Furnace
canonical: /upgrade/008b-Furnace
dataSyncedOn: 2026-10-13
description: "烈焰熔炉无法移动，但会随时间召唤小火怪攻击建筑。这些好奇的小家伙所到之处都会留下火焰！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/008b-Furnace.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-03-27'">

<template #introduction>

<SwitchTabs contentClass="cp-unit-items" :stickyTabs="true" :pageTabs="true">
    <SwitchTab tabId="cp-unit-item-0" :activeTab="true">烈焰熔炉</SwitchTab>
    <SwitchTab tabId="cp-unit-item-1">小火怪</SwitchTab>
</SwitchTabs>

<SwitchTabGroup id="cp-unit-item-0" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Furnace_info.png" imgAlt="烈焰熔炉"
    description="烈焰熔炉无法移动，但会随时间召唤小火怪攻击建筑。这些好奇的小家伙所到之处都会留下火焰！" />

<SmallTitle>重要说明</SmallTitle>

1. 和 [攻城训练营](/upgrade/0243-Siege-Barracks) 等攻城机器类似，烈焰熔炉部署后无法移动，并且会随时间推移自动掉血。[大守护者](/upgrade/0202-Grand-Warden) 的 [永恒书卷](/upgrade/0780-Eternal-Tome) 装备无法阻止它自动掉血。
2. 和 [大雪怪](/upgrade/000d-Yeti) 不同，烈焰熔炉释放小火怪的速度是固定的，与烈焰熔炉受到的伤害值和剩余生命值均无关。
3. 如果烈焰熔炉被摧毁时仍有未释放完的小火怪，则未释放出的小火怪会直接消失。
4. 当烈焰熔炉作为进攻部队时，即使场上没有目标供小火怪攻击，烈焰熔炉也不会停止释放小火怪，此时烈焰熔炉释放出的小火怪会停留在生成地。
5. 当烈焰熔炉作为防守部队时，如果场上没有目标供小火怪攻击，烈焰熔炉会停止释放小火怪，此时烈焰熔炉仍然会自动掉血。如果这种无目标状态持续足够久，就会出现烈焰熔炉解体时都没有释放完全部小火怪的现象。
6. 烈焰熔炉可以被治疗单位治愈，但 [天使](/upgrade/0007-Healer) 和 [独角](/upgrade/0283-Unicorn) 都不会将它定为治疗目标。由于 [部队发射器](/upgrade/0247-Troop-Launcher) 有跟天使类似的 AI，部队发射器也不会向它发射部队。

\* 这是烈焰熔炉未受到伤害时的存活时间。

</SwitchTabGroup>

<SwitchTabGroup id="cp-unit-item-1" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Firemite_info.png" imgAlt="小火怪"
    description="这些小家伙速度快、好奇心强，生命值较低，对探索建筑有着炽热的渴望！它们只想找个温暖的地方藏起来，所到之处都会留下火焰，对目标造成持续伤害。" />

<SmallTitle>重要说明</SmallTitle>

1. 和小雪怪类似，小火怪攻击时会先接近目标建筑，然后在短暂停顿后跳到建筑身上并造成伤害。在跳跃状态下，小火怪是无敌的，且不能被其他单位锁定。
2. 和小雪怪类似，小火怪可以跳过城墙。
3. 小火怪攻击后会留下一个火坑，并对目标造成持续伤害。
4. 和 [毒药法术](/upgrade/0180-Poison-Spell) 类似，这个火坑的伤害是递增的，多个火坑不能叠加伤害，但能更快到达最高伤害。
5. 小火怪攻击一次后就会死亡，[大守护者](/upgrade/0202-Grand-Warden) 的 [永恒书卷](/upgrade/0780-Eternal-Tome) 装备也无法阻止。

占据人口：在考虑小火怪与 [隐形弹簧](/upgrade/0381-Spring-Trap)、[镜像法术](/upgrade/0105-Clone-Spell) 或 [回溯法术](/upgrade/0107-Recall-Spell) 的相互作用时，小火怪应被视为 1 人口。<br>
攻击时机：根据解析安装包的结果，小火怪的攻击速度是一秒一次，但实际上小火怪的首次攻击时机为到达目标后 0.5 秒，且攻击一次后就会死亡，因此其攻速值无意义。

</SwitchTabGroup>

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/03/27">
        <TimelineRow>部队的训练时间取消，但增加了捐赠费用。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>新兵种：烈焰熔炉，15 本可解锁。</TimelineRow>
    </TimelineItem>
</Timeline>

</template>

</SyncedUnitData>
