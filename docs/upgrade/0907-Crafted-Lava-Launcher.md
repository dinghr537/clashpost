---
title: "部落冲突 coc 精工熔岩发射器升级数据"
navTitle: "精工熔岩发射器"
shownTitle: "精工熔岩发射器"
module: upgrade-temp
imgFolder: crafted_buildings/0907
wiki: https://clashofclans.fandom.com/wiki/Lava_Launcher/Home_Village
canonical: /upgrade/0907-Crafted-Lava-Launcher
dataSyncedOn: 2026-10-13
---

<script setup>
const tableExtraInfo0 = [
    {
        "column": 2,
        "type": "cost",
        "icon": "Gold",
        "gpClass": "building",
        "noGoldPass": false
    },
    {
        "column": 3,
        "type": "time",
        "gpClass": "building",
        "noGoldPass": false
    }
];
const tableExtraInfo1 = [
    {
        "column": 5,
        "type": "cost",
        "icon": "Dark_Elixir",
        "gpClass": "building",
        "noGoldPass": false
    },
    {
        "column": 6,
        "type": "time",
        "gpClass": "building",
        "noGoldPass": false
    }
];
const tableExtraInfo2 = [
    {
        "column": 2,
        "type": "cost",
        "icon": "Elixir",
        "gpClass": "building",
        "noGoldPass": false
    },
    {
        "column": 3,
        "type": "time",
        "gpClass": "building",
        "noGoldPass": false
    }
];
</script>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Lava_Launcher7_Crafted.png" :imgAlt="$frontmatter.navTitle" :isSmallImg="true" />

<SmallTitle>各等级图片</SmallTitle>

<Panel>
    <UnitImgGroup :folder="$frontmatter.imgFolder">
        <UnitImg imgTitle="7 级" imgSrc="Lava_Launcher7_Crafted.png" />
        <UnitImg imgTitle="1 级" imgSrc="Lava_Launcher1_Crafted.png" />
        <UnitImg imgTitle="2 级" imgSrc="Lava_Launcher2_Crafted.png" />
        <UnitImg imgTitle="3 级" imgSrc="Lava_Launcher3_Crafted.png" />
        <UnitImg imgTitle="4 级" imgSrc="Lava_Launcher4_Crafted.png" />
        <UnitImg imgTitle="5 级" imgSrc="Lava_Launcher5_Crafted.png" />
        <UnitImg imgTitle="6 级" imgSrc="Lava_Launcher6_Crafted.png" />
    </UnitImgGroup>
</Panel>

<SmallTitle>重要说明</SmallTitle>

1. 家乡精工防御，属于 2026 年 4 月 1 日至 7 月 30 日的批次，现已结束；与夜世界同名防御分开记录。

<SmallTitle>建筑数量对照表</SmallTitle>

<BuildingNum>
    <BuildingNumRow title="大本等级" num="1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18" />
    <BuildingNumRow title="建筑数量" num="0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1" />
</BuildingNum>

<SmallTitle>属性</SmallTitle>

<UnitProperties>
    <UnitProperty pKey="占地面积" pValue="3×3" />
</UnitProperties>

<SmallTitle>属性</SmallTitle>

<UnitProperties>
    <UnitProperty pKey="最小射程" pValue="6格" />
    <UnitProperty pKey="攻击间隔" pValue="7秒" />
    <UnitProperty pKey="熔岩持续时间" pValue="20秒" />
    <UnitProperty pKey="灼烧伤害结算间隔" pValue="0.4秒" />
    <UnitProperty pKey="熔岩半径" pValue="2.5格" />
    <UnitProperty pKey="伤害类型" pValue="范围伤害 - 3格" />
    <UnitProperty pKey="攻击目标" pValue="地面" />
</UnitProperties>

<SmallTitle>模组一：生命值</SmallTitle>

<UnitTable :tableExtraInfo="tableExtraInfo0">

| 等级 | 生命值 | 升级费用 | 升级时间 | 升级后可<br>获得的经验 |
| --- | --- | --- | --- | --- |
| 1 | 450 | \ | \ | \ |
| 2 | 800 | 3000000 | 0,4,0,0 | 120 |
| 3 | 1200 | 4000000 | 0,6,0,0 | 146 |
| 4 | 1600 | 5000000 | 0,8,0,0 | 169 |
| 5 | 2100 | 6000000 | 0,10,0,0 | 189 |
| 6 | 2600 | 7000000 | 0,12,0,0 | 207 |
| 7 | 3100 | 8000000 | 1,0,0,0 | 293 |
| 8 | 3600 | 9000000 | 2,0,0,0 | 415 |
| 9 | 4200 | 10000000 | 4,0,0,0 | 587 |
| 10 | 4900 | 11000000 | 8,0,0,0 | 831 |
</UnitTable>

<SmallTitle>模组二：伤害</SmallTitle>

<UnitTable :tableExtraInfo="tableExtraInfo1">

| 等级 | 每秒伤害 | 每次伤害 | 灼烧总伤害 | 每次灼烧伤害 | 升级费用 | 升级时间 | 升级后可<br>获得的经验 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 72 | 504 | 1050 | 21 | \ | \ | \ |
| 2 | 75 | 525 | 1100 | 22 | 35000 | 0,6,0,0 | 146 |
| 3 | 80 | 560 | 1150 | 23 | 45000 | 0,8,0,0 | 169 |
| 4 | 85 | 595 | 1200 | 24 | 55000 | 0,10,0,0 | 189 |
| 5 | 90 | 630 | 1250 | 25 | 65000 | 0,12,0,0 | 207 |
| 6 | 95 | 665 | 1300 | 26 | 75000 | 0,14,0,0 | 224 |
| 7 | 100 | 700 | 1350 | 27 | 85000 | 1,2,0,0 | 305 |
| 8 | 105 | 735 | 1450 | 29 | 95000 | 2,4,0,0 | 432 |
| 9 | 110 | 770 | 1500 | 30 | 105000 | 4,6,0,0 | 605 |
| 10 | 115 | 805 | 1600 | 32 | 115000 | 8,12,0,0 | 856 |
</UnitTable>

<SmallTitle>模组三：射程</SmallTitle>

<UnitTable :tableExtraInfo="tableExtraInfo2">

| 等级 | 最大射程 | 升级费用 | 升级时间 | 升级后可<br>获得的经验 |
| --- | --- | --- | --- | --- |
| 1 | 11 | \ | \ | \ |
| 2 | 11.5 | 4000000 | 0,8,0,0 | 169 |
| 3 | 12 | 5000000 | 0,10,0,0 | 189 |
| 4 | 12.5 | 6000000 | 0,11,0,0 | 198 |
| 5 | 13 | 7500000 | 0,13,0,0 | 216 |
| 6 | 13.5 | 9000000 | 0,15,0,0 | 232 |
| 7 | 14 | 10500000 | 1,3,0,0 | 311 |
| 8 | 14.5 | 12000000 | 2,6,0,0 | 440 |
| 9 | 15 | 13500000 | 4,12,0,0 | 623 |
| 10 | 16 | 15000000 | 9,0,0,0 | 881 |
</UnitTable>

<SmallTitle>更新历史</SmallTitle>

<Timeline>
    <TimelineItem date="2026/07/31">
        <TimelineRow>本批熔岩发射器停止开放。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2026/05/26">
        <TimelineRow>调整全部等级的每秒伤害： 1级： 80 → 72 2级： 83 → 75 3级： 87 → 80 4级： 91 → 85 5级： 95 → 90 6级： 100 → 95 7级： 105 → 100 8级： 111 → 105 9级： 118 → 110 10级： 125 → 115 调整全部等级的每次灼烧伤害： 1级： 26 → 21 2级： 27 → 22 3级： 29 → 23 4级： 30 → 24 5级： 31 → 25 6级： 33 → 26 7级： 34 → 27 8级： 36 → 29 9级： 38 → 30 10级： 40 → 32 调整2至10级的攻击范围： 2级： 12 → 11.5 射程 3级： 13 → 12 射程 4级： 14 → 12.5 射程 5级： 15 → 13 射程 6级： 16 → 13.5 射程 7级： 17 → 14 射程 8级： 18 → 14.5 射程 9级： 19 → 15 射程 10级： 20 → 16 射程</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2026/04/01">
        <TimelineRow>新增熔岩发射器。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2026/03/30">
        <TimelineRow>公布熔岩发射器，共30级。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2026/03/27">
        <TimelineRow>调整2至9级的生命值： 2级： 900 → 800 3级： 1,400 → 1,200 4级： 1,900 → 1,600 5级： 2,400 → 2,100 6级： 2,900 → 2,600 7级： 3,400 → 3,100 8级： 3,900 → 3,600 9级： 4,400 → 4,200 调整2至9级的每秒伤害： 2级： 85 → 83 3级： 90 → 87 4级： 95 → 91 5级： 100 → 95 6级： 105 → 100 7级： 110 → 105 8级： 115 → 111 9级： 120 → 118 调整模组1和3的升级费用： 模组1（生命值）： 3级： 3,500,000 → 4,000,000 金币 4级： 4,000,000 → 5,000,000 金币 5级： 4,500,000 → 6,000,000 金币 6级： 6,000,000 → 7,000,000 金币 7级： 7,500,000 → 8,000,000 金币 7级： 9,000,000 → 9,000,000 金币 9级： 10,500,000 → 10,000,000 金币 10级： 12,000,000 → 11,000,000 金币 模组3（射程）： 2级： 6,000,000 → 4,000,000 圣水 3级： 6,500,000 → 5,000,000 圣水 4级： 8,000,000 → 6,000,000 圣水 5级： 9,500,000 → 7,500,000 圣水 6级： 10,000,000 → 9,000,000 圣水 8级： 11,000,000 → 12,000,000 圣水 9级： 11,500,000 → 13,500,000 圣水 10级： 12,000,000 → 15,000,000 圣水 调整全部模组的升级时间： 模组1（生命值）： 2级： 1天 12小时 → 4小时 3级： 2天 → 6小时 4级： 2天 12小时 → 8小时 5级： 2天 14小时 → 10小时 6级： 2天 16小时 → 12小时 7级： 2天 18小时 → 1天 8级： 2天 20小时 → 2天 9级： 2天 22小时 → 4天 10级： 3天 → 8天 模组2（伤害）： 2级： 1天 → 6小时 3级： 1天 6小时 → 8小时 4级： 1天 12小时 → 10小时 5级： 1天 18小时 → 12小时 6级： 2天 → 14小时 7级： 2天 6小时 → 1天 2小时 8级： 2天 12小时 → 2天 4小时 9级： 2天 18小时 → 4天 6小时 10级： 3天 → 8天 12小时 模组3（射程）： 2级： 12小时 → 8小时 3级： 16小时 → 10小时 4级： 20小时 → 11小时 5级： 1天 → 13小时 6级： 1天 6小时 → 15小时 7级： 1天 12小时 → 1天 3小时 8级： 2天 → 2天 6小时 9级： 2天 12小时 → 4天 12小时 10级： 3天 → 9天</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2026/02/23">
        <TimelineRow>已加入游戏文件。</TimelineRow>
    </TimelineItem>
</Timeline>


<p><small>数值核对：2026-10-13 · <a href="https://clashofclans.fandom.com/wiki/Lava_Launcher/Home_Village?oldid=625570" target="_blank" rel="noopener noreferrer">部落冲突维基</a>。</small></p>
