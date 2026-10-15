---
title: "部落冲突 coc 蛋糕投掷器升级数据"
navTitle: "蛋糕投掷器"
shownTitle: "蛋糕投掷器"
englishName: "Cake-A-Pult"
module: upgrade-temp
imgFolder: crafted_buildings/0909
wiki: https://clashofclans.fandom.com/wiki/Cake-A-Pult
canonical: /upgrade/0909-Cake-A-Pult
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

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Cake-A-Pult4.png" :imgAlt="$frontmatter.navTitle" :isSmallImg="true" />

<SmallTitle>各等级图片</SmallTitle>

<Panel>
    <UnitImgGroup :folder="$frontmatter.imgFolder">
        <UnitImg imgTitle="4 级" imgSrc="Cake-A-Pult4.png" />
        <UnitImg imgTitle="1 级" imgSrc="Cake-A-Pult1.png" />
        <UnitImg imgTitle="2 级" imgSrc="Cake-A-Pult2.png" />
        <UnitImg imgTitle="3 级" imgSrc="Cake-A-Pult3.png" />
    </UnitImgGroup>
</Panel>

<SmallTitle>建筑数量对照表</SmallTitle>

<BuildingNum>
    <BuildingNumRow title="大本等级" num="1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18" />
    <BuildingNumRow title="建筑数量" num="0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1" />
</BuildingNum>

<SmallTitle>属性</SmallTitle>

<UnitProperties>
    <UnitProperty pKey="占地面积" pValue="3×3" />
</UnitProperties>

<SmallTitle>属性</SmallTitle>

<UnitProperties>
    <UnitProperty pKey="射程" pValue="3-12格" />
    <UnitProperty pKey="攻击间隔" pValue="3秒" />
    <UnitProperty pKey="伤害类型" pValue="范围伤害 - 2.5格" />
    <UnitProperty pKey="攻击目标" pValue="地面和空中" />
    <UnitProperty pKey="炸弹爆炸半径" pValue="2.5格" />
    <UnitProperty pKey="炸弹引爆延迟" pValue="3秒" />
</UnitProperties>

<SmallTitle>模组一：生命值</SmallTitle>

<UnitTable :tableExtraInfo="tableExtraInfo0">

| 等级 | 生命值 | 升级费用 | 升级时间 | 升级后可<br>获得的经验 | 所需<br>大本等级 |
| --- | --- | --- | --- | --- | --- |
| 1 | 1600 | \ | \ | \ | 11 |
| 2 | 1800 | 3000000 | 0,4,0,0 | 120 | 12 |
| 3 | 2150 | 4000000 | 0,6,0,0 | 146 | 13 |
| 4 | 2500 | 5000000 | 0,8,0,0 | 169 | 14 |
| 5 | 2700 | 6000000 | 0,10,0,0 | 189 | 15 |
| 6 | 3150 | 7000000 | 0,16,0,0 | 240 | 16 |
| 7 | 3800 | 8000000 | 1,16,0,0 | 379 | 17 |
| 8 | 4300 | 9000000 | 3,2,0,0 | 516 | 18 |
| 9 | 4950 | 10000000 | 5,6,0,0 | 673 | 18 |
| 10 | 5800 | 11000000 | 9,0,0,0 | 881 | 18 |
</UnitTable>

<SmallTitle>模组二：伤害</SmallTitle>

<UnitTable :tableExtraInfo="tableExtraInfo1">

| 等级 | 每次伤害 | 升级费用 | 升级时间 | 升级后可<br>获得的经验 | 所需<br>大本等级 |
| --- | --- | --- | --- | --- | --- |
| 1 | 195 | \ | \ | \ | 11 |
| 2 | 210 | 35000 | 0,6,0,0 | 146 | 12 |
| 3 | 225 | 45000 | 0,8,0,0 | 169 | 13 |
| 4 | 246 | 55000 | 0,10,0,0 | 189 | 14 |
| 5 | 264 | 65000 | 0,12,0,0 | 207 | 15 |
| 6 | 285 | 75000 | 0,18,0,0 | 254 | 16 |
| 7 | 315 | 85000 | 1,19,0,0 | 393 | 17 |
| 8 | 333 | 95000 | 3,8,0,0 | 536 | 18 |
| 9 | 354 | 105000 | 5,18,0,0 | 704 | 18 |
| 10 | 375 | 115000 | 9,12,0,0 | 905 | 18 |
</UnitTable>

<SmallTitle>模组三：爆炸伤害</SmallTitle>

<UnitTable :tableExtraInfo="tableExtraInfo2">

| 等级 | 爆炸伤害 | 升级费用 | 升级时间 | 升级后可<br>获得的经验 | 所需<br>大本等级 |
| --- | --- | --- | --- | --- | --- |
| 1 | 400 | \ | \ | \ | 11 |
| 2 | 450 | 4000000 | 0,8,0,0 | 169 | 12 |
| 3 | 480 | 5000000 | 0,10,0,0 | 189 | 13 |
| 4 | 510 | 6000000 | 0,11,0,0 | 198 | 14 |
| 5 | 530 | 7500000 | 0,13,0,0 | 216 | 15 |
| 6 | 550 | 9000000 | 0,19,0,0 | 261 | 16 |
| 7 | 600 | 10500000 | 1,22,0,0 | 406 | 17 |
| 8 | 750 | 12000000 | 3,11,0,0 | 546 | 18 |
| 9 | 900 | 13500000 | 6,4,0,0 | 729 | 18 |
| 10 | 950 | 15000000 | 10,0,0,0 | 929 | 18 |
</UnitTable>

<SmallTitle>更新历史</SmallTitle>

<Timeline>
    <TimelineItem date="2026/08/01">
        <TimelineRow>新增蛋糕投掷器。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2026/07/30">
        <TimelineRow>公布蛋糕投掷器，共30级。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2026/06/16">
        <TimelineRow>已加入游戏文件。</TimelineRow>
    </TimelineItem>
</Timeline>


<p><small>数值核对：2026-10-13 · <a href="https://clashofclans.fandom.com/wiki/Cake-A-Pult?oldid=625029" target="_blank" rel="noopener noreferrer">部落冲突维基</a>。</small></p>
