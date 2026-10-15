---
title: "部落冲突 coc 精工炙热熔炉升级数据"
navTitle: "精工炙热熔炉"
shownTitle: "精工炙热熔炉"
module: upgrade-temp
imgFolder: crafted_buildings/0908
wiki: https://clashofclans.fandom.com/wiki/Roaster/Home_Village
canonical: /upgrade/0908-Crafted-Roaster
dataSyncedOn: 2026-10-13
---

<script setup>
const tableExtraInfo0 = [
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
const tableExtraInfo1 = [
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
const tableExtraInfo2 = [
    {
        "column": 2,
        "type": "cost",
        "icon": "Dark_Elixir",
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

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Roaster10_Crafted.png" :imgAlt="$frontmatter.navTitle" :isSmallImg="true" />

<SmallTitle>各等级图片</SmallTitle>

<Panel>
    <UnitImgGroup :folder="$frontmatter.imgFolder">
        <UnitImg imgTitle="10 级" imgSrc="Roaster10_Crafted.png" />
        <UnitImg imgTitle="1 级" imgSrc="Roaster1_Crafted.png" />
        <UnitImg imgTitle="2 级" imgSrc="Roaster2_Crafted.png" />
        <UnitImg imgTitle="3 级" imgSrc="Roaster3_Crafted.png" />
        <UnitImg imgTitle="4 级" imgSrc="Roaster4_Crafted.png" />
        <UnitImg imgTitle="5 级" imgSrc="Roaster5_Crafted.png" />
        <UnitImg imgTitle="6 级" imgSrc="Roaster6_Crafted.png" />
        <UnitImg imgTitle="7 级" imgSrc="Roaster7_Crafted.png" />
        <UnitImg imgTitle="8 级" imgSrc="Roaster8_Crafted.png" />
        <UnitImg imgTitle="9 级" imgSrc="Roaster9_Crafted.png" />
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
    <UnitProperty pKey="射程" pValue="10格" />
    <UnitProperty pKey="攻击间隔" pValue="0.25?s" />
    <UnitProperty pKey="连发间隔" pValue="1.5秒" />
    <UnitProperty pKey="伤害类型" pValue="范围伤害 - 1.5格" />
    <UnitProperty pKey="攻击目标" pValue="地面和空中" />
</UnitProperties>

<SmallTitle>模组一：生命值</SmallTitle>

<UnitTable :tableExtraInfo="tableExtraInfo0">

| 等级 | 生命值 | 升级费用 | 升级时间 | 升级后可<br>获得的经验 |
| --- | --- | --- | --- | --- |
| 1 | 960 | \ | \ | \ |
| 2 | 1500 | 3500000 | 0,6,0,0 | 146 |
| 3 | 2000 | 4500000 | 0,8,0,0 | 169 |
| 4 | 2500 | 5500000 | 0,10,0,0 | 189 |
| 5 | 3000 | 6500000 | 0,12,0,0 | 207 |
| 6 | 3500 | 7500000 | 0,14,0,0 | 224 |
| 7 | 4000 | 8500000 | 1,2,0,0 | 305 |
| 8 | 4500 | 10000000 | 2,4,0,0 | 432 |
| 9 | 5200 | 11500000 | 4,6,0,0 | 605 |
| 10 | 6000 | 13000000 | 8,12,0,0 | 856 |
</UnitTable>

<SmallTitle>模组二：伤害</SmallTitle>

<UnitTable :tableExtraInfo="tableExtraInfo1">

| 等级 | 每次伤害 | 升级费用 | 升级时间 | 升级后可<br>获得的经验 |
| --- | --- | --- | --- | --- |
| 1 | 85 | \ | \ | \ |
| 2 | 90 | 4000000 | 0,8,0,0 | 169 |
| 3 | 95 | 5000000 | 0,10,0,0 | 189 |
| 4 | 100 | 6000000 | 0,11,0,0 | 198 |
| 5 | 105 | 7500000 | 0,13,0,0 | 216 |
| 6 | 110 | 9000000 | 0,15,0,0 | 232 |
| 7 | 115 | 10500000 | 1,3,0,0 | 311 |
| 8 | 120 | 12000000 | 2,6,0,0 | 440 |
| 9 | 125 | 13500000 | 4,12,0,0 | 623 |
| 10 | 135 | 15000000 | 9,0,0,0 | 881 |
</UnitTable>

<SmallTitle>模组三：连发次数</SmallTitle>

<UnitTable :tableExtraInfo="tableExtraInfo2">

| 等级 | 连发次数 | 升级费用 | 升级时间 | 升级后可<br>获得的经验 |
| --- | --- | --- | --- | --- |
| 1 | 8 | \ | \ | \ |
| 2 | 9 | 30000 | 0,4,0,0 | 120 |
| 3 | 10 | 40000 | 0,6,0,0 | 146 |
| 4 | 11 | 50000 | 0,8,0,0 | 169 |
| 5 | 12 | 60000 | 0,10,0,0 | 189 |
| 6 | 13 | 70000 | 0,12,0,0 | 207 |
| 7 | 14 | 80000 | 1,0,0,0 | 293 |
| 8 | 15 | 90000 | 2,0,0,0 | 415 |
| 9 | 16 | 100000 | 4,0,0,0 | 587 |
| 10 | 17 | 110000 | 8,0,0,0 | 831 |
</UnitTable>

<SmallTitle>更新历史</SmallTitle>

<Timeline>
    <TimelineItem date="2026/07/31">
        <TimelineRow>本批熔岩火炮停止开放。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2026/05/26">
        <TimelineRow>精工炙热熔炉连发间隔1.80秒→1.50秒，伤害半径1.2格→1.5格；每次伤害：1级50→85，2级54→90，3级58→95，4级62→100，5级66→105，6级70→110，7级75→115，8级80→120，9级87→125，10级95→135；全部等级连发次数增加2次。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2026/04/01">
        <TimelineRow>新增熔岩火炮。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2026/03/30">
        <TimelineRow>公布熔岩火炮，共30级。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2026/03/27">
        <TimelineRow>调整2至9级的生命值： 2级： 1,520 → 1,500 3级： 2,080 → 2,000 4级： 2,640 → 2,500 5级： 3,200 → 3,000 6级： 3,760 → 3,500 7级： 4,320 → 4,000 8级： 4,880 → 4,500 9级： 5,440 → 5,200 调整2至9级的每次伤害： 2级： 55 → 54 3级： 60 → 58 4级： 65 → 62 5级： 70 → 66 6级： 75 → 70 7级： 80 → 75 8级： 85 → 80 9级： 90 → 87 调整全部模组的升级费用： 模组1（生命值）： 2级： 4,000,000 → 3,500,000 圣水 3级： 5,000,000 → 4,500,000 圣水 4级： 6,000,000 → 5,500,000 圣水 5级： 7,000,000 → 6,500,000 圣水 6级： 8,000,000 → 7,500,000 圣水 7级： 9,000,000 → 8,500,000 圣水 9级： 11,000,000 → 11,500,000 圣水 10级： 12,000,000 → 13,000,000 圣水 模组2（伤害）： 2级： 5,000,000 → 4,000,000 金币 3级： 6,500,000 → 5,000,000 金币 4级： 8,000,000 → 6,000,000 金币 5级： 9,500,000 → 7,500,000 金币 6级： 10,000,000 → 9,000,000 金币 8级： 11,000,000 → 12,000,000 金币 9级： 11,500,000 → 13,500,000 金币 10级： 12,000,000 → 15,000,000 金币 模组3（连发次数）： 2级： 25,000 → 30,000 暗黑重油 3级： 30,000 → 40,000 暗黑重油 4级： 35,000 → 50,000 暗黑重油 5级： 40,000 → 60,000 暗黑重油 6级： 55,000 → 70,000 暗黑重油 7级： 70,000 → 80,000 暗黑重油 8级： 85,000 → 90,000 暗黑重油 10级： 115,000 → 110,000 暗黑重油 调整全部模组的升级时间： 模组1（生命值）： 2级： 1天 → 6小时 3级： 1天 6小时 → 8小时 4级： 1天 12小时 → 10小时 5级： 1天 18小时 → 12小时 6级： 2天 → 14小时 7级： 2天 6小时 → 1天 2小时 8级： 2天 12小时 → 2天 4小时 9级： 2天 18小时 → 4天 6小时 10级： 3天 → 8天 12小时 模组2（伤害）： 2级： 12小时 → 8小时 3级： 16小时 → 10小时 4级： 20小时 → 11小时 5级： 1天 → 13小时 6级： 1天 6小时 → 15小时 7级： 1天 12小时 → 1天 3小时 8级： 2天 → 2天 6小时 9级： 2天 12小时 → 4天 12小时 10级： 3天 → 9天 模组3（连发次数）： 2级： 1天 12小时 → 4小时 3级： 2天 → 6小时 4级： 2天 12小时 → 8小时 5级： 2天 14小时 → 10小时 6级： 2天 16小时 → 12小时 7级： 2天 18小时 → 1天 8级： 2天 20小时 → 2天 9级： 2天 22小时 → 4天 10级： 3天 → 8天</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2026/02/23">
        <TimelineRow>已加入游戏文件。</TimelineRow>
    </TimelineItem>
</Timeline>


<p><small>数值核对：2026-10-13 · <a href="https://clashofclans.fandom.com/wiki/Roaster/Home_Village?oldid=624970" target="_blank" rel="noopener noreferrer">部落冲突维基</a>。</small></p>
