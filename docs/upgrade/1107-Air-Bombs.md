---
title: "部落冲突 coc 夜世界空中炸弹发射器升级数据"
navTitle: "空中炸弹发射器"
shownTitle: "空中炸弹发射器"
description: "要应对繁重的空中防御任务，使用空中炸弹发射器准没错。它能持续不断地向空中发射木桶，木桶会在空中爆炸重创敌军！"
module: upgrade-bh
imgFolder: bh_buildings/1107
wiki: https://clashofclans.fandom.com/wiki/Air_Bombs
canonical: /upgrade/1107-Air-Bombs
dataSyncedOn: 2026-10-13
---

- *如想查看都城的空中炸弹发射器，请访问：[都城空中炸弹发射器](/upgrade/2208-Air-Bombs)。*
- *如想查看家乡的陷阱空中炸弹，请访问：[空中炸弹](/upgrade/0382-Air-Bomb)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Air_Bombs10.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

<SmallTitle>各等级图片</SmallTitle>

<Panel>
    <UnitImgGroup :folder="$frontmatter.imgFolder">
        <UnitImg imgTitle="1 级" imgSrc="Air_Bombs1.png" />
        <UnitImg imgTitle="2 级" imgSrc="Air_Bombs2.png" />
        <UnitImg imgTitle="3 级" imgSrc="Air_Bombs3.png" />
        <UnitImg imgTitle="4 级" imgSrc="Air_Bombs4.png" />
        <UnitImg imgTitle="5 级" imgSrc="Air_Bombs5.png" />
        <UnitImg imgTitle="6 级" imgSrc="Air_Bombs6.png" />
        <UnitImg imgTitle="7 级" imgSrc="Air_Bombs7.png" />
        <UnitImg imgTitle="8 级" imgSrc="Air_Bombs8.png" />
        <UnitImg imgTitle="9 级" imgSrc="Air_Bombs9.png" />
        <UnitImg imgTitle="10 级" imgSrc="Air_Bombs10.png" />
    </UnitImgGroup>
</Panel>

<SmallTitle>建筑数量对照表</SmallTitle>

<BuildingNum>
    <BuildingNumRow title="大本等级" num="1 - 3, 4 - 10" />
    <BuildingNumRow title="建筑数量" num="    0,      1" />
</BuildingNum>

<SmallTitle>属性</SmallTitle>

<UnitProperties>
    <UnitProperty pKey="占地面积" pValue="3×3" />
    <UnitProperty pKey="判定面积" pValue="2×2" :isJudgeSquare="true" />
    <UnitProperty pKey="伤害类型" pValue="范围伤害" />
    <UnitProperty pKey="伤害半径" pValue="1.5 格" />
    <UnitProperty pKey="攻击的目标" pValue="仅空中目标" />
    <UnitProperty pKey="射程" pValue="7.5 格" />
    <UnitProperty pKey="攻速" pValue="3 秒/次" />
</UnitProperties>

<SmallTitle>升级数据</SmallTitle>

<script setup>
const tableExtraInfo = [
    {
        "column": 4,
        "type": "cost",
        "gpClass": "building",
        "icon": "Gold2"
    },
    {
        "column": 5,
        "type": "time",
        "gpClass": "building"
    },
    {
        "column": 6,
        "type": "exp",
        "icon": "Exp"
    }
];
</script>

<UnitTable :tableExtraInfo="tableExtraInfo">

| 等级 | 每秒伤害 | 每次伤害 | 生命值 | 升级费用 | 升级时间 |升级后可<br>获得的经验|所需夜世界<br>大本等级|
|  --- |   ---   |   ---   |  ---   |   ---   |    ---  |         ---         |         ---        |
| 1 | 90 | 270 | 1000 | 300000 | 0,6,0,0 |  | 4 |
| 2 | 99 | 297 | 1100 | 320000 | 0,12,0,0 |  | 4 |
| 3 | 109 | 327 | 1250 | 340000 | 1,0,0,0 |  | 4 |
| 4 | 119 | 357 | 1400 | 360000 | 2,0,0,0 |  | 4 |
| 5 | 131 | 393 | 1600 | 1200000 | 3,0,0,0 |  | 5 |
| 6 | 145 | 435 | 1850 | 1500000 | 5,0,0,0 |  | 6 |
| 7 | 159 | 477 | 2100 | 2400000 | 7,0,0,0 |  | 7 |
| 8 | 175 | 525 | 2350 | 3400000 | 8,0,0,0 |  | 8 |
| 9 | 193 | 579 | 2600 | 4400000 | 10,0,0,0 |  | 9 |
| 10 | 212 | 636 | 2900 | 5400000 | 12,0,0,0 |  | 10 |

</UnitTable>

<SmallTitle>更新历史</SmallTitle>

<Timeline>
    <TimelineItem date="2023/05/15">
        <TimelineRow>夜世界重做，建筑的数值重新平衡，伤害、生命值等数据有变化。</TimelineRow>
        <TimelineRow>5 ~ 9 级空中炸弹发射器的升级时间增加。</TimelineRow>
        <TimelineRow>夜世界 10 本推出，空中炸弹发射器可升至 10 级。</TimelineRow>
        <TimelineRow>为配合更小的地图，空中炸弹发射器的射程由 8 格降低到 7.5 格。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/06/18">
        <TimelineRow>夜世界 9 本推出，空中炸弹发射器可升至 9 级。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>
<p><small>数值核对：2026-10-13 · <a href="https://clashofclans.fandom.com/wiki/Air_Bombs?oldid=622479" target="_blank" rel="noopener noreferrer">部落冲突维基</a>。部分附加字段沿用原记录。</small></p>
