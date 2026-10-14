---
title: "部落冲突 coc 攻城烈焰车（投石车）升级数据"
navTitle: "攻城烈焰车"
shownTitle: "攻城烈焰车（投石车）"
module: upgrade-home
imgFolder: home_tech/0245
wiki: https://clashofclans.fandom.com/wiki/Flame_Flinger
canonical: /upgrade/0245-Flame-Flinger
dataSyncedOn: 2026-10-13
description: "这架可爱的攻城机器能投掷出多个烈焰精灵，不仅会给敌方村庄造成重击，还会留下一片持续燃烧的区域。攻城烈焰车的攻击范围很远，足以让自己在攻击时远离危险，但要小心攻击范围更远的防御建筑和陷阱！法术对攻城烈焰车无效。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0245-Flame-Flinger.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-03-27'">

<template #introduction>

- *玩家所说的投石车指的是攻城烈焰车，而不是投石炮，投石炮的数据请参考：[投石炮](/upgrade/030e-Scattershot)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Flame_Flinger.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

1. 攻城烈焰车部署后会投掷烈焰精灵，对敌方建筑造成持续伤害。
2. 攻城烈焰车的伤害机制比较复杂，我们只能得出定性结论，具体伤害无法计算。目前已经确定的是，攻城烈焰车有 3 种伤害：直接高额伤害、直接溅射伤害、后续持续伤害。由于这几种伤害的大小不一样，伤害范围也不是完全重叠，所以实战中烈焰范围内的建筑可能不是同时被摧毁的。
3. 烈焰精灵命中目标后的那一下攻击对墙有 8 倍伤害，但烈焰精灵的灼烧效果对 [城墙](/upgrade/0300-Walls) 没有额外伤害。
4. 攻城烈焰车部署后不能移动，即使没有受到伤害也会自动掉血。[大守护者](/upgrade/0202-Grand-Warden) 的 [永恒书卷](/upgrade/0780-Eternal-Tome) 装备无法阻止它自动掉血。
5. 当攻城烈焰车的血量清零时，攻城烈焰车就会自动解体并释放部落城堡内的部队。

攻击速度：目前的公开资料显示攻城烈焰车的攻速是 5 秒每次，但根据我们的测试，攻城烈焰车的实际攻速约为 5.4 秒每次。<br>
首次进攻时机：这是我们团队内部的测试值，仅供参考。<br>
掉血速度：这是烈焰车不受到伤害时的掉血速度。

熔岩的最大伤害：攻城烈焰车发射出的熔岩伤害类似于 [毒药法术](/upgrade/0180-Poison-Spell)，也就是前期伤害低，兵种或建筑待在熔岩里的时间越长瞬时伤害越高。<br>
最大存活时间：攻城烈焰车和 [攻城训练营](/upgrade/0243-Siege-Barracks) 及 [滚木车](/upgrade/0244-Log-Launcher) 一样会自己掉血，这个最大存活时间指的是未受到伤害时的存活时间。同样，[大守护者](/upgrade/0202-Grand-Warden) 的 [永恒书卷](/upgrade/0780-Eternal-Tome) 装备无法阻止烈焰车自身掉血。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/03/27">
        <TimelineRow>攻城机器的建造时间被取消。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>2 ~ 5 级攻城烈焰车的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/18">
        <TimelineRow>2 ~ 4 级攻城烈焰车的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/04/17">
        <TimelineRow>在 16 本新增 5 级攻城烈焰车。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>2 ~ 4 级攻城烈焰车的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>2 ~ 4 级攻城烈焰车的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/06/27">
        <TimelineRow>攻城烈焰车击中目标后燃烧伤害的范围缩小。</TimelineRow>
        <TimelineRow>击中后燃烧伤害的持续时间从 20 秒延长至 30 秒。</TimelineRow>
        <TimelineRow>所有等级攻城烈焰车的每秒燃烧伤害降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/02/15">
        <TimelineRow>攻击效果将从原本一次投掷 3 个烈焰精灵组成的单一炮弹调整为投掷 3 个单独的烈焰精灵。</TimelineRow>
        <TimelineRow>各等级攻城烈焰车的每次攻击伤害值从 675/725/775/825 提升至 675/750/825/900。</TimelineRow>
        <TimelineRow>间接攻击造成的溅射伤害降低。</TimelineRow>
        <TimelineRow>各等级攻城烈焰车的燃烧最高每秒伤害值从 180/200/220/240 降低至 120/140/160/180。</TimelineRow>
        <TimelineRow>燃烧伤害递增的速度大幅增加。</TimelineRow>
        <TimelineRow>燃烧持续时间略微缩短。</TimelineRow>
        <TimelineRow>攻城烈焰车 AI 优化，变得更加稳定。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/12/09">
        <TimelineRow>14 本可解锁新攻城机器：攻城烈焰车。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
