---
title: "部落冲突 coc 冰封箭矢（寒冰箭）装备升级数据"
navTitle: "冰封箭矢"
shownTitle: "冰封箭矢（寒冰箭）"
description: "冰封箭矢是弓箭女皇的第一件史诗装备，它在 2024 年 2 月的龙年佳节活动中首次开放购买。带上冰封箭矢装备后，被女王打中的目标在一段时间内移动速度和攻击速度会变慢。另外，冰封箭矢还能增加女王的每秒伤害。"
module: upgrade-home
imgFolder: home_heroes/0744
wiki: https://clashofclans.fandom.com/wiki/Frozen_Arrow
canonical: /upgrade/0744-Frozen-Arrow
dataSyncedOn: 2026-10-13
dataBalanceUpdatedOn: 2026-10-20
---

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Frozen_Arrow_info.png" :imgAlt="$frontmatter.navTitle" description="冰封箭矢会减缓被命中目标的速度。" />

<SmallTitle>说明</SmallTitle>

1. 冰封箭矢是 [弓箭女皇](/upgrade/0201-Archer-Queen) 的第一件史诗装备，它在 2024 年 2 月的龙年佳节活动中首次开放购买。
2. 带上冰封箭矢装备后，被女王打中的目标在一段时间内移动速度和攻击速度会变慢。
3. 另外，冰封箭矢还能增加女王的每秒伤害。

<SmallTitle>属性</SmallTitle>

<UnitProperties>
    <UnitProperty pKey="技能类型" pValue="被动技能" />
    <UnitProperty pKey="装备稀有度" pValue="史诗" />
</UnitProperties>

<SmallTitle>升级数据</SmallTitle>

<script setup>
const tableExtraInfo = [
    {
        "column": 4,
        "type": "cost",
        "icon": "Shiny_Ore",
        "noGoldPass": true
    },
    {
        "column": 5,
        "type": "cost",
        "icon": "Glowy_Ore",
        "noGoldPass": true
    },
    {
        "column": 6,
        "type": "cost",
        "icon": "Starry_Ore",
        "noGoldPass": true
    }
];
</script>

<UnitTable :tableExtraInfo="tableExtraInfo">

| 等级 |减速比例<sup>#</sup>|减速<br>持续时间|每秒伤害<br>增加|升级费用|升级费用|升级费用|所需<br>铁匠铺等级|所需<br>大本等级|
| ---- |        ---        |      ---      |      ---     |   ---  |   ---  |  ---  |       ---       |      ---      |
| 1 | 30% | 0.75秒 | 35 | \ | \ | \ | 1 | 8 |
| 2 | 30% | 1.00秒 | 40 | 120 | \ | \ | 1 | 8 |
| 3 | 35% | 1.00秒 | 45 | 240 | 20 | \ | 1 | 8 |
| 4 | 35% | 1.00秒 | 50 | 400 | \ | \ | 1 | 8 |
| 5 | 35% | 1.25秒 | 55 | 600 | \ | \ | 1 | 8 |
| 6 | 40% | 1.25秒 | 60 | 840 | 100 | \ | 1 | 8 |
| 7 | 40% | 1.25秒 | 66 | 1120 | \ | \ | 1 | 8 |
| 8 | 40% | 1.50秒 | 72 | 1440 | \ | \ | 1 | 8 |
| 9 | 42% | 1.50秒 | 78 | 1800 | 200 | 10 | 1 | 8 |
| 10 | 42% | 1.50秒 | 85 | 1900 | \ | \ | 1 | 8 |
| 11 | 42% | 1.75秒 | 92 | 2000 | \ | \ | 1 | 8 |
| 12 | 45% | 1.75秒 | 99 | 2100 | 400 | 20 | 1 | 8 |
| 13 | 45% | 1.75秒 | 105 | 2200 | \ | \ | 3 | 10 |
| 14 | 45% | 2.00秒 | 111 | 2300 | \ | \ | 3 | 10 |
| 15 | 50% | 2.00秒 | 117 | 2400 | 600 | 30 | 3 | 10 |
| 16 | 50% | 2.00秒 | 122 | 2500 | \ | \ | 5 | 12 |
| 17 | 50% | 2.25秒 | 127 | 2600 | \ | \ | 5 | 12 |
| 18 | 55% | 2.25秒 | 132 | 2700 | 600 | 50 | 5 | 12 |
| 19 | 55% | 2.25秒 | 136 | 2800 | \ | \ | 7 | 14 |
| 20 | 55% | 2.50秒 | 140 | 2900 | \ | \ | 7 | 14 |
| 21 | 60% | 2.50秒 | 145 | 3000 | 600 | 100 | 7 | 14 |
| 22 | 60% | 2.50秒 | 150 | 3100 | \ | \ | 8 | 15 |
| 23 | 60% | 2.75秒 | 155 | 3200 | \ | \ | 8 | 15 |
| 24 | 65% | 2.75秒 | 160 | 3300 | 600 | 120 | 8 | 15 |
| 25 | 65% | 2.75秒 | 165 | 3400 | \ | \ | 9 | 16 |
| 26 | 65% | 3.00秒 | 170 | 3500 | \ | \ | 9 | 16 |
| 27 | 70% | 3.00秒 | 175 | 3600 | 600 | 150 | 9 | 16 |
</UnitTable>

\# 攻击速度和移动速度的减速比例相同。

注意：如果升级费用中有多种资源，则同时需要多种资源才能升级。

<SmallTitle>推出记录</SmallTitle>

<UnitTable>

| 推出时间 |  活动名称  |     价格      | 购买渠道 |
|   ---   |    ---    |      ---      |    ---   |
| 2024/02 |  龙年佳节  | 3 100 神龙奖章 |   商人   |
| 2024/12 | 大闹玩具店 | 3 100 玩具奖章 |   商人   |
| 2025/10 |  宇宙摇滚  | 3 100 摇滚奖章 |   商人   |
</UnitTable>

<SmallTitle>更新历史</SmallTitle>

<Timeline>
    <TimelineItem date="2026/10/20">
        <TimelineRow>所有等级减速比例提高 5 个百分点，1–2 级由 25% 提高至 30%，27 级由 65% 提高至 70%。</TimelineRow>
        <TimelineRow>提高 21–27 级每秒伤害加成：144→145、148→150、152→155、156→160、160→165、164→170、168→175（依等级顺序）。</TimelineRow>
        <TimelineRow><a href="https://supercell.com/en/games/clashofclans/blog/news/balance-changes-incoming-october-2026/" target="_blank" rel="noopener noreferrer">官方公告</a>（10/17 发布） · <a href="https://clashfox.com/blog/balance-changes-before-town-hall-19-fire-heart-and-ruin-witch-nerfed-hogs-and-p-e-k-k-a-bu" target="_blank" rel="noopener noreferrer">数值参考</a> · <a href="https://x.com/ClashofClans/status/2112450159326179560" target="_blank" rel="noopener noreferrer">10/20 维护完成</a>。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>现在 8 本就可以解锁弓箭女皇了，该页面的部分信息需要同步更改。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/09/09">
        <TimelineRow>所有等级冰封箭矢击中目标后的减速效果变弱（减速比例降低）。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/02/08">
        <TimelineRow>新装备：冰封箭矢。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

<p><small>数值核对：2026-10-13 · <a href="https://clashofclans.fandom.com/wiki/Frozen_Arrow?oldid=621294" target="_blank" rel="noopener noreferrer">部落冲突维基</a>。部分附加字段沿用原记录。</small></p>
