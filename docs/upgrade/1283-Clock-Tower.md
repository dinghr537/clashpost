---
title: "部落冲突 coc 夜世界时光钟楼升级数据"
navTitle: "时光钟楼"
shownTitle: "时光钟楼"
description: "时光钟楼使您基地中的项目运行加快！采集资源、研究和建造的速度加快。"
module: upgrade-bh
imgFolder: bh_buildings/1283
wiki: https://clashofclans.fandom.com/wiki/Clock_Tower
canonical: /upgrade/1283-Clock-Tower
dataSyncedOn: 2026-10-13
---

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Clock_Tower10.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

<SmallTitle>各等级图片</SmallTitle>

<Panel>
    <UnitImgGroup :folder="$frontmatter.imgFolder">
        <UnitImg imgTitle="废墟" imgSrc="Clock_Tower_Ruin.png"/>
        <UnitImg imgTitle="1 级" imgSrc="Clock_Tower1.png"/>
        <UnitImg imgTitle="2 级" imgSrc="Clock_Tower2.png"/>
        <UnitImg imgTitle="3 级" imgSrc="Clock_Tower3.png"/>
        <UnitImg imgTitle="4 级" imgSrc="Clock_Tower4.png"/>
        <UnitImg imgTitle="5 级" imgSrc="Clock_Tower5.png"/>
        <UnitImg imgTitle="6 级" imgSrc="Clock_Tower6.png"/>
        <UnitImg imgTitle="7 级" imgSrc="Clock_Tower7.png"/>
        <UnitImg imgTitle="8 级" imgSrc="Clock_Tower8.png"/>
        <UnitImg imgTitle="9 级" imgSrc="Clock_Tower9.png"/>
        <UnitImg imgTitle="10 级" imgSrc="Clock_Tower10.png"/>
    </UnitImgGroup>
</Panel>

<SmallTitle>建筑数量对照表</SmallTitle>

<BuildingNum>
    <BuildingNumRow title="大本等级" num="1 - 3, 4 - 5, 6 - 10" />
    <BuildingNumRow title="合计" num="0, 1, 1" />
    <BuildingNumRow title="第一区域的建筑数量上限" num="\, \, 1" />
    <BuildingNumRow title="第二区域的建筑数量上限" num="\, \, 0" />
</BuildingNum>

<SmallTitle>属性</SmallTitle>

<UnitProperties>
    <UnitProperty pKey="占地面积" pValue="3×3" />
    <UnitProperty pKey="判定面积" pValue="2×2" :isJudgeSquare="true" />
    <UnitProperty pKey="加速倍数" pValue="10" />
    <UnitProperty pKey="冷却时间" pValue="22 小时" />
</UnitProperties>

<SmallTitle>升级数据</SmallTitle>

<script setup>
const tableExtraInfo = [
    {
        "column": 2,
        "type": "time",
        "gpClass": "building",
        "noGoldPass": true
    },
    {
        "column": 5,
        "type": "cost",
        "gpClass": "building",
        "icon": "Gold2"
    },
    {
        "column": 6,
        "type": "time",
        "gpClass": "building"
    },
    {
        "column": 7,
        "type": "exp",
        "icon": "Exp"
    }
];
</script>

<UnitTable :tableExtraInfo="tableExtraInfo">

| 等级 | 加速时长 | 节省的时间 | 节省的<br>时间比例 | 生命值 | 升级费用 | 升级时间 | 升级后可<br>获得的经验 | 所需夜世界<br>大本营等级 |
|  --- |   ---   |    ---    |        ---        |  ---  |   ---   |    ---   |         ---          |           ---         |
| 1 | 0,0,14,0 | 0,2,6,0 | 9.4% | 650 | 150000 | 0,2,0,0 |  | 4 |
| 2 | 0,0,16,0 | 0,2,24,0 | 10.8% | 800 | 180000 | 0,3,0,0 |  | 4 |
| 3 | 0,0,18,0 | 0,2,42,0 | 12.1% | 975 | 220000 | 0,4,0,0 |  | 4 |
| 4 | 0,0,20,0 | 0,3,0,0 | 13.4% | 1150 | 300000 | 0,6,0,0 |  | 4 |
| 5 | 0,0,22,0 | 0,3,18,0 | 14.8% | 1350 | 700000 | 0,12,0,0 |  | 5 |
| 6 | 0,0,24,0 | 0,3,36,0 | 16.1% | 1600 | 1200000 | 1,0,0,0 |  | 6 |
| 7 | 0,0,26,0 | 0,3,54,0 | 17.4% | 1850 | 1700000 | 2,0,0,0 |  | 7 |
| 8 | 0,0,28,0 | 0,4,12,0 | 18.7% | 2150 | 2200000 | 3,0,0,0 |  | 8 |
| 9 | 0,0,30,0 | 0,4,30,0 | 20.0% | 2450 | 2700000 | 4,0,0,0 |  | 9 |
| 10 | 0,0,32,0 | 0,4,48,0 | 21.3% | 2750 | 3700000 | 5,0,0,0 |  | 10 |
</UnitTable>

<SmallTitle>更新历史</SmallTitle>

<Timeline>
    <TimelineItem date="2023/05/15">
        <TimelineRow>夜世界重做，建筑的数值重新平衡，伤害、生命值等数据有变化。</TimelineRow>
        <TimelineRow>5 ~ 9 级时光钟楼的升级费用增加。</TimelineRow>
        <TimelineRow>夜世界 10 本推出，时光钟楼可升至 10 级。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/05/15">
        <TimelineRow>考虑到部队训练时间和战争机器恢复时间都被移除，更新后，时光钟楼将主要作用于加速建筑和资源生产，具体调整如下：</TimelineRow>
        <TimelineRow>时光钟楼的提速效果从原来的 8 倍提升至 10 倍；</TimelineRow>
        <TimelineRow>时光钟楼提速时长从原来的 3 ~ 11 分钟对应提升至 14 ~ 30 分钟；</TimelineRow>
        <TimelineRow>时光钟楼提速冷却时间从 7 小时延长至 22 小时；</TimelineRow>
        <TimelineRow>跳过时光钟楼提速冷却时间所需的宝石数量减少。</TimelineRow>
    </TimelineItem>
     <TimelineItem date="2019/06/18">
        <TimelineRow>夜世界 9 本推出，时光钟楼可升至 9 级。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>
<p><small>数值核对：2026-10-13 · <a href="https://clashofclans.fandom.com/wiki/Clock_Tower?oldid=622494" target="_blank" rel="noopener noreferrer">部落冲突维基</a>。部分附加字段沿用原记录。</small></p>
