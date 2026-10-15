---
title: "部落冲突 coc 火热蜡烛升级数据"
navTitle: "火热蜡烛"
shownTitle: "火热蜡烛"
englishName: "Hot Candle"
module: upgrade-temp
imgFolder: crafted_buildings/090b
wiki: https://clashofclans.fandom.com/wiki/Hot_Candle
canonical: /upgrade/090b-Hot-Candle
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
        "column": 3,
        "type": "cost",
        "icon": "Gold",
        "gpClass": "building",
        "noGoldPass": false
    },
    {
        "column": 4,
        "type": "time",
        "gpClass": "building",
        "noGoldPass": false
    }
];
const tableExtraInfo2 = [
    {
        "column": 4,
        "type": "cost",
        "icon": "Dark_Elixir",
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
</script>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Hot_Candle4-1.png" :imgAlt="$frontmatter.navTitle" :isSmallImg="true" />

<SmallTitle>各等级图片</SmallTitle>

<Panel>
    <UnitImgGroup :folder="$frontmatter.imgFolder">
        <UnitImg imgTitle="4 级（阶段 1）" imgSrc="Hot_Candle4-1.png" />
        <UnitImg imgTitle="1 级（阶段 1）" imgSrc="Hot_Candle1-1.png" />
        <UnitImg imgTitle="2 级（阶段 1）" imgSrc="Hot_Candle2-1.png" />
        <UnitImg imgTitle="3 级（阶段 1）" imgSrc="Hot_Candle3-1.png" />
        <UnitImg imgTitle="1 级（阶段 2）" imgSrc="Hot_Candle1-2.png" />
        <UnitImg imgTitle="2 级（阶段 2）" imgSrc="Hot_Candle2-2.png" />
        <UnitImg imgTitle="3 级（阶段 2）" imgSrc="Hot_Candle3-2.png" />
        <UnitImg imgTitle="4 级（阶段 2）" imgSrc="Hot_Candle4-2.png" />
        <UnitImg imgTitle="1 级（阶段 3）" imgSrc="Hot_Candle1-3.png" />
        <UnitImg imgTitle="2 级（阶段 3）" imgSrc="Hot_Candle2-3.png" />
        <UnitImg imgTitle="3 级（阶段 3）" imgSrc="Hot_Candle3-3.png" />
        <UnitImg imgTitle="4 级（阶段 3）" imgSrc="Hot_Candle4-3.png" />
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
    <UnitProperty pKey="射程" pValue="10.5格" />
    <UnitProperty pKey="攻击间隔" pValue="0.5秒" />
    <UnitProperty pKey="伤害类型" pValue="单体" />
    <UnitProperty pKey="攻击目标" pValue="地面和空中" />
    <UnitProperty pKey="目标数量 / 基础形态" pValue="6" />
    <UnitProperty pKey="目标数量 / 第一次衰减" pValue="4" />
    <UnitProperty pKey="目标数量 / 第二次衰减" pValue="3" />
</UnitProperties>

<SmallTitle>模组一：生命值</SmallTitle>

<UnitTable :tableExtraInfo="tableExtraInfo0">

| 等级 | 生命值 | 升级费用 | 升级时间 | 升级后可<br>获得的经验 | 所需<br>大本等级 |
| --- | --- | --- | --- | --- | --- |
| 1 | 1600 | \ | \ | \ | 11 |
| 2 | 1800 | 3500000 | 0,6,0,0 | 146 | 12 |
| 3 | 2150 | 4500000 | 0,8,0,0 | 169 | 13 |
| 4 | 2500 | 5500000 | 0,10,0,0 | 189 | 14 |
| 5 | 2700 | 6500000 | 0,12,0,0 | 207 | 15 |
| 6 | 3150 | 7500000 | 0,18,0,0 | 254 | 16 |
| 7 | 3900 | 8500000 | 1,19,0,0 | 393 | 17 |
| 8 | 4500 | 10000000 | 3,8,0,0 | 536 | 18 |
| 9 | 5200 | 11500000 | 5,18,0,0 | 704 | 18 |
| 10 | 6000 | 13000000 | 9,12,0,0 | 905 | 18 |
</UnitTable>

<SmallTitle>模组二：伤害</SmallTitle>

<UnitTable :tableExtraInfo="tableExtraInfo1">

| 等级 | 每束火焰每秒伤害 | 每次伤害 | 升级费用 | 升级时间 | 升级后可<br>获得的经验 | 所需<br>大本等级 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 80 | 40 | \ | \ | \ | 11 |
| 2 | 100 | 50 | 4000000 | 0,8,0,0 | 169 | 12 |
| 3 | 120 | 60 | 5000000 | 0,10,0,0 | 189 | 13 |
| 4 | 150 | 75 | 6000000 | 0,11,0,0 | 198 | 14 |
| 5 | 160 | 80 | 7500000 | 0,13,0,0 | 216 | 15 |
| 6 | 180 | 90 | 9000000 | 0,19,0,0 | 261 | 16 |
| 7 | 190 | 95 | 10500000 | 1,22,0,0 | 406 | 17 |
| 8 | 210 | 105 | 12000000 | 3,11,0,0 | 546 | 18 |
| 9 | 230 | 115 | 13500000 | 6,4,0,0 | 729 | 18 |
| 10 | 250 | 125 | 15000000 | 10,0,0,0 | 929 | 18 |
</UnitTable>

<SmallTitle>模组三：生效秒数</SmallTitle>

<UnitTable :tableExtraInfo="tableExtraInfo2">

| 等级 | 总生效时间（秒）<br>基础形态 | 总生效时间（秒）<br>第一次衰减 | 总生效时间（秒）<br>第二次衰减 | 升级费用 | 升级时间 | 升级后可<br>获得的经验 | 所需<br>大本等级 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 59秒 | 60秒 - 94秒 | 95秒+ | \ | \ | \ | 11 |
| 2 | 61秒 | 62秒 - 98秒 | 99秒+ | 30000 | 0,4,0,0 | 120 | 12 |
| 3 | 63秒 | 64秒 - 102秒 | 103秒+ | 40000 | 0,6,0,0 | 146 | 13 |
| 4 | 65秒 | 66秒 - 106秒 | 107秒+ | 50000 | 0,8,0,0 | 169 | 14 |
| 5 | 67秒 | 68秒 - 110秒 | 111秒+ | 60000 | 0,10,0,0 | 189 | 15 |
| 6 | 69秒 | 70秒 - 114秒 | 115秒+ | 70000 | 0,16,0,0 | 240 | 16 |
| 7 | 71秒 | 72秒 - 118秒 | 119秒+ | 80000 | 1,16,0,0 | 379 | 17 |
| 8 | 73秒 | 74秒 - 122秒 | 123秒+ | 90000 | 3,2,0,0 | 516 | 18 |
| 9 | 75秒 | 76秒 - 126秒 | 127秒+ | 100000 | 5,6,0,0 | 673 | 18 |
| 10 | 77秒 | 78秒 - 131秒 | 132秒+ | 110000 | 9,0,0,0 | 881 | 18 |
</UnitTable>

<SmallTitle>更新历史</SmallTitle>

<Timeline>
    <TimelineItem date="2026/08/31">
        <TimelineRow>火热蜡烛的衰减计时改为首次部署部队时开始，恢复原设计机制。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2026/08/01">
        <TimelineRow>新增火热蜡烛。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2026/07/31">
        <TimelineRow>修复火热蜡烛的衰减计时误计入侦察阶段的问题，暂改为建筑被摧毁时开始计时。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2026/07/30">
        <TimelineRow>公布火热蜡烛，共30级。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2026/06/16">
        <TimelineRow>已加入游戏文件。</TimelineRow>
    </TimelineItem>
</Timeline>


<p><small>数值核对：2026-10-13 · <a href="https://clashofclans.fandom.com/wiki/Hot_Candle?oldid=625464" target="_blank" rel="noopener noreferrer">部落冲突维基</a>。</small></p>
