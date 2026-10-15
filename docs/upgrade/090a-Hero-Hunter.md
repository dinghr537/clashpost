---
title: "部落冲突 coc 英雄猎台升级数据"
navTitle: "英雄猎台"
shownTitle: "英雄猎台"
englishName: "Hero Hunter"
module: upgrade-temp
imgFolder: crafted_buildings/090a
wiki: https://clashofclans.fandom.com/wiki/Hero_Hunter
canonical: /upgrade/090a-Hero-Hunter
dataSyncedOn: 2026-10-13
---

<script setup>
const tableExtraInfo0 = [
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
const tableExtraInfo1 = [
    {
        "column": 4,
        "type": "cost",
        "icon": "Elixir",
        "gpClass": "building",
        "noGoldPass": false
    },
    {
        "column": 5,
        "type": "time",
        "gpClass": "building",
        "noGoldPass": false
    }
];
const tableExtraInfo2 = [
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
</script>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Hero_Hunter4.png" :imgAlt="$frontmatter.navTitle" :isSmallImg="true" />

<SmallTitle>各等级图片</SmallTitle>

<Panel>
    <UnitImgGroup :folder="$frontmatter.imgFolder">
        <UnitImg imgTitle="4 级" imgSrc="Hero_Hunter4.png" />
        <UnitImg imgTitle="1 级" imgSrc="Hero_Hunter1.png" />
        <UnitImg imgTitle="2 级" imgSrc="Hero_Hunter2.png" />
        <UnitImg imgTitle="3 级" imgSrc="Hero_Hunter3.png" />
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
    <UnitProperty pKey="射程" pValue="9.5格" />
    <UnitProperty pKey="攻击间隔" pValue="0.6秒" />
    <UnitProperty pKey="伤害类型" pValue="单体" />
    <UnitProperty pKey="攻击目标" pValue="地面和空中" />
    <UnitProperty pKey="攻击偏好" pValue="英雄 (2倍 伤害)" />
    <UnitProperty pKey="毒药持续时间" pValue="3秒" />
</UnitProperties>

<SmallTitle>模组一：生命值</SmallTitle>

<UnitTable :tableExtraInfo="tableExtraInfo0">

| 等级 | 生命值 | 升级费用 | 升级时间 | 升级后可<br>获得的经验 | 所需<br>大本等级 |
| --- | --- | --- | --- | --- | --- |
| 1 | 1600 | \ | \ | \ | 11 |
| 2 | 1800 | 40000 | 0,8,0,0 | 169 | 12 |
| 3 | 2150 | 50000 | 0,10,0,0 | 189 | 13 |
| 4 | 2500 | 60000 | 0,11,0,0 | 198 | 14 |
| 5 | 2700 | 70000 | 0,13,0,0 | 216 | 15 |
| 6 | 3150 | 80000 | 0,19,0,0 | 261 | 16 |
| 7 | 3900 | 90000 | 1,22,0,0 | 406 | 17 |
| 8 | 4400 | 100000 | 3,11,0,0 | 546 | 18 |
| 9 | 5200 | 110000 | 6,4,0,0 | 729 | 18 |
| 10 | 6000 | 120000 | 10,0,0,0 | 929 | 18 |
</UnitTable>

<SmallTitle>模组二：伤害</SmallTitle>

<UnitTable :tableExtraInfo="tableExtraInfo1">

| 等级 | 每秒伤害 | 每次伤害 | 每秒伤害<br>(对英雄) | 升级费用 | 升级时间 | 升级后可<br>获得的经验 | 所需<br>大本等级 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 145 | 87 | 290 | \ | \ | \ | 11 |
| 2 | 155 | 93 | 310 | 3000000 | 0,4,0,0 | 120 | 12 |
| 3 | 170 | 102 | 340 | 4000000 | 0,6,0,0 | 146 | 13 |
| 4 | 185 | 111 | 370 | 5000000 | 0,8,0,0 | 169 | 14 |
| 5 | 195 | 117 | 390 | 6000000 | 0,10,0,0 | 189 | 15 |
| 6 | 210 | 126 | 420 | 7000000 | 0,16,0,0 | 240 | 16 |
| 7 | 260 | 156 | 520 | 8000000 | 1,16,0,0 | 379 | 17 |
| 8 | 325 | 195 | 650 | 9000000 | 3,2,0,0 | 516 | 18 |
| 9 | 350 | 210 | 700 | 10000000 | 5,6,0,0 | 673 | 18 |
| 10 | 385 | 231 | 770 | 11000000 | 9,0,0,0 | 881 | 18 |
</UnitTable>

<SmallTitle>模组三：毒药等级</SmallTitle>

<UnitTable :tableExtraInfo="tableExtraInfo2">

| 等级 | 毒药法术等级 | 升级费用 | 升级时间 | 升级后可<br>获得的经验 | 所需<br>大本等级 |
| --- | --- | --- | --- | --- | --- |
| 1 | 3 | \ | \ | \ | 11 |
| 2 | 4 | 3500000 | 0,6,0,0 | 146 | 12 |
| 3 | 5 | 4500000 | 0,8,0,0 | 169 | 13 |
| 4 | 6 | 5500000 | 0,10,0,0 | 189 | 14 |
| 5 | 7 | 6500000 | 0,12,0,0 | 207 | 15 |
| 6 | 8 | 7500000 | 0,18,0,0 | 254 | 16 |
| 7 | 9 | 8500000 | 1,19,0,0 | 393 | 17 |
| 8 | 10 | 10000000 | 3,8,0,0 | 536 | 18 |
| 9 | 11 | 11500000 | 5,18,0,0 | 704 | 18 |
| 10 | 12 | 13000000 | 9,12,0,0 | 905 | 18 |
</UnitTable>

<SmallTitle>更新历史</SmallTitle>

<Timeline>
    <TimelineItem date="2026/08/01">
        <TimelineRow>新增英雄猎台。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2026/07/30">
        <TimelineRow>公布英雄猎台，共30级。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2026/06/16">
        <TimelineRow>已加入游戏文件。</TimelineRow>
    </TimelineItem>
</Timeline>


<p><small>数值核对：2026-10-13 · <a href="https://clashofclans.fandom.com/wiki/Hero_Hunter?oldid=625573" target="_blank" rel="noopener noreferrer">部落冲突维基</a>。</small></p>
