---
title: "部落冲突 coc 雷电法术（闪电）升级数据"
navTitle: "雷电法术"
shownTitle: "雷电法术（闪电）"
module: upgrade-home
imgFolder: home_tech/0100
wiki: https://clashofclans.fandom.com/wiki/Lightning_Spell
canonical: /upgrade/0100-Lightning-Spell
dataSyncedOn: 2026-10-13
description: "放出一道闪电攻击敌军！施放雷电法术，击晕小范围内的建筑和部队，并对其造成伤害。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0100-Lightning-Spell.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-11-17'">

<template #introduction>

- *如想查看都城的雷电法术，请访问：[都城雷电法术](/upgrade/2102-Lightning-Spell)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Lightning_Spell.png" :imgAlt="$frontmatter.navTitle"
    description="放出一道闪电攻击敌军！<br>施放雷电法术，击晕小范围内的建筑和部队，并对其造成伤害。"
    :isSmallImg="true" />

<SmallTitle>重要说明</SmallTitle>

1. 对于建筑来说，雷电法术的闪电只需**蹭到建筑边缘**即可对建筑造成完整伤害，参见：新版雷电法术攻击范围示意。
2. 雷电法术对敌方英雄有效，但是要想劈到英雄最好把雷电法术扔在英雄头顶，否则可能劈不到。
3. 雷电法术不能对资源仓库（[储金罐](/upgrade/0404-Gold-Storage)、[圣水瓶](/upgrade/0405-Elixir-Storage) 和 [暗黑重油罐](/upgrade/0406-Dark-Elixir-Storage)）、[大本营](/upgrade/0400-Town-Hall) 和 [部落城堡](/upgrade/0407-Clan-Castle) 造成伤害。

\* 如果玩家升级到 5 级大本营并且解锁了雷电法术，即使玩家没有立即升实验室也可以升级雷电法术。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/11/17">
        <TimelineRow>18 本推出，并在 18 本新增 13 级雷电法术。</TimelineRow>
        <TimelineRow>12 级雷电法术的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/10/06">
        <TimelineRow>10 ~ 11 级雷电法术的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/27">
        <TimelineRow>法术的配置时间取消，但新增了捐赠费用。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>2 ~ 4、6、8 ~ 11 级雷电法术的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>17 本推出，并在 17 本新增 12 级雷电法术。</TimelineRow>
        <TimelineRow>6 ~ 9、11 级雷电法术的升级时间减少。</TimelineRow>
        <TimelineRow>10 ~ 11 级雷电法术的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/18">
        <TimelineRow>10 级雷电法术的升级时间减少。</TimelineRow>
        <TimelineRow>10 级雷电法术的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>16 本推出，并在 16 本新增 11 级雷电法术。</TimelineRow>
        <TimelineRow>6 ~ 10 级雷电法术的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>9 级雷电法术的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>15 本推出，并在 15 本新增 10 级雷电法术。</TimelineRow>
        <TimelineRow>7 ~ 9 级雷电法术的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/12/09">
        <TimelineRow>2 ~ 8 级雷电法术的升级费用降低。</TimelineRow>
        <TimelineRow>2 ~ 7 级雷电法术的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>2 ~ 7 级雷电法术的升级费用降低。</TimelineRow>
        <TimelineRow>2 ~ 8 级雷电法术的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/12/07">
        <TimelineRow>雷电法术不再对部落城堡造成伤害。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/06/22">
        <TimelineRow>雷电法术由 2 空间改为 1 空间。</TimelineRow>
        <TimelineRow>11 本新增 8 级雷电法术，12 本新增 9 级雷电法术。</TimelineRow>
        <TimelineRow>可对目标产生短时间的击晕效果（短暂冰冻），打断目标的攻击并使其攻击重置。</TimelineRow>
        <TimelineRow>所有等级雷电法术的配置费用降低。</TimelineRow>
        <TimelineRow>所有等级雷电法术的伤害减少。</TimelineRow>
        <TimelineRow>更新后雷电的随机半径没了，伤害的范围固定。（5×5 的方格去掉四个角得到的 21 格的区域）</TimelineRow>
        <TimelineRow>更新后雷电法术对大本营无效。</TimelineRow>
        <TimelineRow>7 级雷电法术的升级时间由 10 天降为 9 天。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/03/30">
        <TimelineRow>6 ~ 7 级雷电法术的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/04/02">
        <TimelineRow>包含大量降低发展成本和提高发展速度的调整，其中 6 ~ 7 级雷电法术的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
