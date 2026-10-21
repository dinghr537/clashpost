---
title: "部落冲突 coc 烈焰之心装备升级数据"
navTitle: "烈焰之心"
shownTitle: "烈焰之心"
description: "烈焰之心是飞龙公爵的两件初始装备之一，另一件是助燃器。烈焰之心装备的死亡爆炸效果只会在飞龙公爵第一次死亡时触发。如果他被凤凰复活后再次死亡，则不会再触发爆炸效果。除死亡爆炸外，烈焰之心装备还可以增加飞龙公爵的生命值并持续回血。"
module: upgrade-home
imgFolder: home_heroes/07e0
wiki: https://clashofclans.fandom.com/wiki/Fire_Heart
canonical: /upgrade/07e0-Fire-Heart
dataSyncedOn: 2026-10-13
dataBalanceUpdatedOn: 2026-10-20
---

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Fire_Heart_info.png" :imgAlt="$frontmatter.navTitle" description="缓慢恢复飞龙公爵的生命值，当他倒下时，会爆发出灼伤敌人的烈焰。" />

<SmallTitle>说明</SmallTitle>

1. 烈焰之心是 [飞龙公爵](/upgrade/0205-Dragon-Duke) 的两件初始装备之一，另一件是 [助燃器](/upgrade/07e1-Flame-Blower)。
2. 烈焰之心装备的死亡爆炸效果只会在飞龙公爵第一次死亡时触发。如果他被 [凤凰](/upgrade/0287-Phoenix) 复活或 [复苏法术](/upgrade/0108-Revive-Spell) 复苏后再次死亡，则不会再触发爆炸效果。
3. 除死亡爆炸外，烈焰之心装备还可以增加飞龙公爵的生命值并持续回血。

<SmallTitle>属性</SmallTitle>

<UnitProperties>
    <UnitProperty pKey="技能类型" pValue="被动技能" />
    <UnitProperty pKey="装备稀有度" pValue="普通" />
    <UnitProperty pKey="解锁条件" pValue="有飞龙公爵即可" />
    <UnitProperty pKey="死亡爆炸半径" pValue="4 格" />
</UnitProperties>

<SmallTitle>升级数据</SmallTitle>

<script setup>
const tableExtraInfo = [
    {
        "column": 5,
        "type": "cost",
        "icon": "Shiny_Ore",
        "noGoldPass": true
    },
    {
        "column": 6,
        "type": "cost",
        "icon": "Glowy_Ore",
        "noGoldPass": true
    }
];
</script>

<UnitTable :tableExtraInfo="tableExtraInfo">

| 等级 |死亡爆炸<br>伤害|每秒恢复<br>血量|每秒<br>伤害提升|生命值增加|升级费用|升级费用|所需<br>铁匠铺等级|所需<br>大本等级|
| ---- |      ---     |       ---     |      ---      |    ---  |  ---  |  ---  |       ---       |       ---      |
| 1 | 1000 | 50 | 0 | 830 | \ | \ | \ | \ |
| 2 | 1000 | 50 | 0 | 1100 | 120 | \ | 1 | 8 |
| 3 | 1350 | 70 | 0 | 1350 | 240 | 20 | 1 | 8 |
| 4 | 1350 | 70 | 0 | 1600 | 400 | \ | 1 | 8 |
| 5 | 1350 | 70 | 0 | 1850 | 600 | \ | 1 | 8 |
| 6 | 1700 | 90 | 0 | 2100 | 840 | 100 | 1 | 8 |
| 7 | 1700 | 90 | 0 | 2400 | 1120 | \ | 1 | 8 |
| 8 | 1700 | 90 | 0 | 2600 | 1440 | \ | 1 | 8 |
| 9 | 2000 | 110 | 0 | 2900 | 1800 | 200 | 1 | 8 |
| 10 | 2000 | 110 | 0 | 3150 | 1900 | \ | 3 | 10 |
| 11 | 2000 | 110 | 0 | 3400 | 2000 | \ | 3 | 10 |
| 12 | 2350 | 120 | 0 | 3700 | 2100 | 400 | 3 | 10 |
| 13 | 2350 | 120 | 0 | 3900 | 2200 | \ | 5 | 12 |
| 14 | 2350 | 120 | 0 | 4200 | 2300 | \ | 5 | 12 |
| 15 | 2700 | 130 | 0 | 4400 | 2400 | 600 | 5 | 12 |
| 16 | 2700 | 130 | 0 | 4700 | 2500 | \ | 7 | 14 |
| 17 | 2700 | 130 | 0 | 5000 | 2600 | \ | 7 | 14 |
| 18 | 3000 | 140 | 0 | 5150 | 2700 | 600 | 7 | 14 |
</UnitTable>

注意：如果升级费用中有多种资源，则同时需要多种资源才能升级。

<SmallTitle>更新历史</SmallTitle>

<Timeline>
    <TimelineItem date="2026/10/20">
        <TimelineRow>移除所有等级的每秒伤害加成；各等级生命值加成降低，18 级由 5600 降至 5150。</TimelineRow>
        <TimelineRow>每秒恢复血量降低：12–14 级由 130 降至 120，15–17 级由 140 降至 130，18 级由 150 降至 140。</TimelineRow>
        <TimelineRow><a href="https://supercell.com/en/games/clashofclans/blog/news/balance-changes-incoming-october-2026/" target="_blank" rel="noopener noreferrer">官方公告</a>（10/17 发布） · <a href="https://clashfox.com/blog/balance-changes-before-town-hall-19-fire-heart-and-ruin-witch-nerfed-hogs-and-p-e-k-k-a-bu" target="_blank" rel="noopener noreferrer">数值参考</a> · <a href="https://x.com/ClashofClans/status/2112450159326179560" target="_blank" rel="noopener noreferrer">10/20 维护完成</a>；维护后已在游戏内确认调整生效。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2026/05/26">
        <TimelineRow>调整15至18级的每秒自我治疗量： 15-17级： 155 → 140 18级： 175 → 150 调整2至18级的每秒伤害： 2级： 12 → 10 3级： 14 → 12 4级： 16 → 12 5级： 18 → 12 6级： 20 → 14 7级： 22 → 14 8级： 24 → 14 9级： 26 → 16 10级： 28 → 16 11级： 30 → 16 12级： 32 → 18 13级： 34 → 18 14级： 36 → 18 15级： 38 → 20 16级： 40 → 20 17级： 42 → 20 18级： 45 → 23</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2026/02/27">
        <TimelineRow>公布烈焰之心的技能机制。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2026/02/23">
        <TimelineRow>新装备：烈焰之心。</TimelineRow>
        <TimelineRow>此时仅加入游戏，飞龙公爵仍被囚禁，装备暂时无法获取。 <a href="https://clashofclans.fandom.com/wiki/Fire_Heart#History" target="_blank" rel="noopener noreferrer">来源</a></TimelineRow>
    </TimelineItem>
    <TimelineItem date="2026/02/22">
        <TimelineRow>飞龙公爵公布时展示烈焰之心。 <a href="https://clashofclans.fandom.com/wiki/Fire_Heart#History" target="_blank" rel="noopener noreferrer">来源</a></TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>
<p><small>数值核对：2026-10-13 · <a href="https://clashofclans.fandom.com/wiki/Fire_Heart?oldid=625389" target="_blank" rel="noopener noreferrer">部落冲突维基</a>。部分附加字段沿用原记录。</small></p>
