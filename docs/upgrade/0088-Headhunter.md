---
title: "部落冲突 coc 英雄猎手（头号杀手）升级数据"
navTitle: "英雄猎手"
shownTitle: "英雄猎手（头号杀手）"
description: "英雄猎手在战场上只有一个任务：消灭敌方英雄。此外，她还在村庄药剂师那儿兼职。身体轻盈的她能轻松跳过城墙，而且她的兵器可以减缓目标的移动速度和攻击速度。"
module: upgrade-home
imgFolder: home_tech/0088
wiki: https://clashofclans.fandom.com/wiki/Headhunter
canonical: /upgrade/0088-Headhunter
dataSyncedOn: 2026-10-13
---

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Headhunter_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>各等级图片</SmallTitle>

<Panel>
    <UnitImgGroup :folder="$frontmatter.imgFolder">
        <UnitImg imgTitle="1 级" imgSrc="Headhunter1.png" />
        <UnitImg imgTitle="2 级" imgSrc="Headhunter2.png" />
        <UnitImg imgTitle="3 级" imgSrc="Headhunter3.png" />
            <UnitImg imgTitle="4 级" imgSrc="Headhunter4.png" />
</UnitImgGroup>
</Panel>

<SmallTitle>重要说明</SmallTitle>

1. 英雄猎手的技能：攻击时有毒药效果，可以减缓敌军的移动速度和攻击速度。此外，英雄猎手还可以跳墙。
2. 英雄猎手的毒药效果只对部队、英雄和攻城机器有效，它不能对建筑造成伤害，也不能减缓建筑的攻击速度。
3. 英雄猎手的毒药效果和其他具有毒药效果的单位（如 [猛蜥](/upgrade/0286-Poison-Lizard)、[毒药法术](/upgrade/0180-Poison-Spell)）同时作用时，减速效果取较强的一种。英雄猎手的普通攻击对英雄造成 4 倍伤害。
4. 英雄猎手的攻击附带短暂的毒药伤害和减速效果。单名英雄猎手造成的毒药伤害通常较低，多名英雄猎手连续攻击同一目标时毒药效果可以累积。

<SmallTitle>属性</SmallTitle>

<UnitProperties>
    <UnitProperty pKey="部队类型" pValue="地面远程单位" />
    <UnitProperty pKey="攻击偏好" pValue="英雄 (4 倍伤害)" />
    <UnitProperty pKey="伤害类型" pValue="单体伤害" />
    <UnitProperty pKey="攻击的目标" pValue="地面和空中目标" />
    <UnitProperty pKey="占据人口" pValue="6" />
    <UnitProperty pKey="移动速度" pValue="24（游戏内数值）" />
    <UnitProperty pKey="攻击速度" pValue="0.6 秒/次" />
    <UnitProperty pKey="攻击距离" pValue="3 格" />
    <UnitProperty pKey="所需暗黑训练营等级" pValue="9" />
    <UnitProperty pKey="所需大本等级" pValue="12" />
    <UnitProperty pKey="训练时间" pValue="无" trainingSystem="2025" />
    <UnitProperty pKey="捐赠费用" pValue="3,3,135,Dark_Elixir" :isDonationCost="true" />
</UnitProperties>

<p><small>移动速度采用玩家提供的游戏内数值 24；<a href="https://clashofclans.fandom.com/wiki/Headhunter#Statistics" target="_blank" rel="noopener noreferrer">Wiki 单位页</a>记为 32，与游戏内数值不同。</small></p>

<SmallTitle>升级数据</SmallTitle>

<script setup>
const tableExtraInfo = [
    {
        "column": 7,
        "type": "cost",
        "gpClass": "research",
        "icon": "Dark_Elixir"
    },
    {
        "column": 8,
        "type": "time",
        "gpClass": "research"
    }
];
</script>

<UnitTable :tableExtraInfo="tableExtraInfo">

| 等级 |  每秒伤害 | 每次伤害 |每秒伤害<br>(对英雄)|每次伤害<br>(对英雄)|毒药法术<br>效果<sup>*</sup>| 生命值 | 升级花费| 升级时间 |所需<br>实验室等级|所需<br>大本等级|
| ---- |   ----   |   ----  |        ---        |        ---        |            ----           |  ---- |  ----  |   ----   |       ----     |      ----     |
| 1 | 105 | 63 | 420 | 252 | 40% / 55% | 360 | \ | \ | 1 | 12 |
| 2 | 115 | 69 | 460 | 276 | 42% / 60% | 400 | 57500 | 5,0,0,0 | 10 | 12 |
| 3 | 125 | 75 | 500 | 300 | 44% / 65% | 440 | 90000 | 7,0,0,0 | 11 | 13 |
| 4 | 135 | 81 | 540 | 324 | 46% / 68% | 500 | 370000 | 15,12,0,0 | 16 | 18 |
</UnitTable>

\* 毒药法术效果：移动速度降低 / 攻击速度降低。

<SmallTitle>更新历史</SmallTitle>

<Timeline>
    <TimelineItem date="2026/04/27">
        <TimelineRow>新增 4 级英雄猎手。 <a href="https://clashofclans.fandom.com/wiki/Headhunter#History" target="_blank" rel="noopener noreferrer">来源</a></TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/27">
        <TimelineRow>部队的训练时间取消，但增加了捐赠费用。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>2 ~ 3 级英雄猎手的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/02/10">
        <TimelineRow>英雄猎手的训练时间由 1:00 改为 0:50</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>2 ~ 3 级英雄猎手的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>2 ~ 3 级英雄猎手的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>2 ~ 3 级英雄猎手的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/29">
        <TimelineRow>1 ~ 3 级英雄猎手的每秒伤害从 108/120/132 降至 105/115/125。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
    <TimelineRow>修复了英雄猎手的淬毒效果持续时间计时不太准确的问题。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/06/22">
        <TimelineRow>12 本可解锁新兵种：英雄猎手。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>
<p><small>数值核对：2026-10-13 · <a href="https://clashofclans.fandom.com/wiki/Headhunter?oldid=625334" target="_blank" rel="noopener noreferrer">部落冲突维基</a>。部分附加字段沿用原记录。</small></p>
