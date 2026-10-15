---
title: "部落冲突 coc 夜世界巨型地雷升级数据"
navTitle: "巨型地雷"
shownTitle: "巨型地雷"
description: "一个隐藏的强力爆炸陷阱。可选择对地或对空！"
module: upgrade-bh
imgFolder: bh_buildings/1183
wiki: https://clashofclans.fandom.com/wiki/Mega_Mine
canonical: /upgrade/1183-Mega-Mine
dataSyncedOn: 2026-10-13
---

- 如想查看夜世界的地雷，请访问：[夜世界地雷](/upgrade/1182-Mine)。
- 如想查看都城的巨型地雷，请访问：[都城巨型地雷](/upgrade/2281-Mega-Mine)。

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Mega_Mine10.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

<SmallTitle>各等级图片</SmallTitle>

<Panel>
    <UnitImgGroup title="对地"  :folder="$frontmatter.imgFolder">
        <UnitImg imgTitle="1 级" imgSrc="Mega_Mine1.png"/>
        <UnitImg imgTitle="2 级" imgSrc="Mega_Mine2.png"/>
        <UnitImg imgTitle="3 级" imgSrc="Mega_Mine3.png"/>
        <UnitImg imgTitle="4 级" imgSrc="Mega_Mine4.png"/>
        <UnitImg imgTitle="5 级" imgSrc="Mega_Mine5.png"/>
        <UnitImg imgTitle="6 级" imgSrc="Mega_Mine6.png"/>
        <UnitImg imgTitle="7 级" imgSrc="Mega_Mine7.png"/>
        <UnitImg imgTitle="8 级" imgSrc="Mega_Mine8.png"/>
        <UnitImg imgTitle="9 级" imgSrc="Mega_Mine9.png"/>
        <UnitImg imgTitle="10 级" imgSrc="Mega_Mine10.png"/>
    </UnitImgGroup>
    <UnitImgGroup title="对空"  :folder="$frontmatter.imgFolder">
        <UnitImg imgTitle="1 级" imgSrc="Mega_Mine1_Air.png"/>
        <UnitImg imgTitle="2 级" imgSrc="Mega_Mine2_Air.png"/>
        <UnitImg imgTitle="3 级" imgSrc="Mega_Mine3_Air.png"/>
        <UnitImg imgTitle="4 级" imgSrc="Mega_Mine4_Air.png"/>
        <UnitImg imgTitle="5 级" imgSrc="Mega_Mine5_Air.png"/>
        <UnitImg imgTitle="6 级" imgSrc="Mega_Mine6_Air.png"/>
        <UnitImg imgTitle="7 级" imgSrc="Mega_Mine7_Air.png"/>
        <UnitImg imgTitle="8 级" imgSrc="Mega_Mine8_Air.png"/>
        <UnitImg imgTitle="9 级" imgSrc="Mega_Mine9_Air.png"/>
        <UnitImg imgTitle="10 级" imgSrc="Mega_Mine10_Air.png"/>
    </UnitImgGroup>
</Panel>

<SmallTitle>建筑数量对照表</SmallTitle>

<BuildingNum>
    <BuildingNumRow title="大本等级" num="1-3, 4-5, 6-7, 8, 9-10" />
    <BuildingNumRow title="建筑数量" num=" 0,   1,   2,  3,  4" />
</BuildingNum>

<SmallTitle>属性</SmallTitle>

<UnitProperties>
    <UnitProperty pKey="占地面积" pValue="2×2" />
    <UnitProperty pKey="作用类型" pValue="爆炸" />
    <UnitProperty pKey="作用目标" pValue="可调对地和对空" />
    <UnitProperty pKey="触发半径" pValue="3 格" />
    <UnitProperty pKey="爆炸半径" pValue="4 格" />
</UnitProperties>

<SmallTitle>升级数据</SmallTitle>

<script setup>
const tableExtraInfo = [
    {
        "column": 2,
        "type": "cost",
        "gpClass": "building",
        "icon": "Gold2"
    },
    {
        "column": 3,
        "type": "time",
        "gpClass": "building"
    },
    {
        "column": 4,
        "type": "exp",
        "icon": "Exp"
    }
];
</script>

<UnitTable :tableExtraInfo="tableExtraInfo">

| 等级 | 爆炸伤害 | 升级费用 | 升级时间 |升级后可<br>获得的经验|所需夜世界<br>大本营等级|
|  --- |   ---   |   ---   |   ---   |         ---         |         ---          |
| 1 | 250 | 30000 | \ |  | 4 |
| 2 | 275 | 40000 | 0,1,0,0 |  | 4 |
| 3 | 300 | 50000 | 0,3,0,0 |  | 4 |
| 4 | 330 | 80000 | 0,6,0,0 |  | 4 |
| 5 | 360 | 120000 | 0,12,0,0 |  | 5 |
| 6 | 395 | 300000 | 1,0,0,0 |  | 6 |
| 7 | 430 | 600000 | 1,12,0,0 |  | 7 |
| 8 | 470 | 1000000 | 2,0,0,0 |  | 8 |
| 9 | 510 | 1400000 | 3,0,0,0 |  | 9 |
| 10 | 550 | 2500000 | 4,0,0,0 |  | 10 |
</UnitTable>

<SmallTitle>更新历史</SmallTitle>

<Timeline>
    <TimelineItem date="2023/10/20">
        <TimelineRow>3 ~ 10 级巨型地雷的爆炸伤害降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/05/15">
        <TimelineRow>夜世界重做，建筑的数值重新平衡，伤害、生命值等数据有变化。</TimelineRow>
        <TimelineRow>所有等级巨型地雷的爆炸伤害增加。</TimelineRow>
        <TimelineRow>所有等级巨型地雷的升级费用增加。</TimelineRow>
        <TimelineRow>触发巨型地雷的最低兵种重量调整为 3，这意味着骷髅兵不能触发巨型地雷了。</TimelineRow>
        <TimelineRow>夜世界 10 本推出，巨型地雷可升至 10 级。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/06/18">
        <TimelineRow>夜世界 9 本推出，巨型地雷可升至 9 级。</TimelineRow>
        <TimelineRow>9 本新增一个巨型地雷。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>
<p><small>数值核对：2026-10-13 · <a href="https://clashofclans.fandom.com/wiki/Mega_Mine?oldid=592217" target="_blank" rel="noopener noreferrer">部落冲突维基</a>。部分附加字段沿用原记录。</small></p>
