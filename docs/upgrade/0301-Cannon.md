---
title: "部落冲突 coc 加农炮升级数据"
navTitle: "加农炮"
shownTitle: "加农炮"
description: "加农炮很适合防御单个目标。升级加农炮可以增强火力。注意！防御建筑在升级时不能开火！"
module: upgrade-home
imgFolder: home_buildings/0301
wiki: https://clashofclans.fandom.com/wiki/Cannon
canonical: /upgrade/0301-Cannon
dataSyncedOn: 2026-10-13
---

<script setup>
const tableExtraInfoStandardMode = [
    {
        "column": 4,
        "type": "cost",
        "gpClass": "building",
        "icon": "Gold"
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
const tableExtraInfoGearUpMode = tableExtraInfoStandardMode;
</script>

- *如想查看由两个加农炮合成的跳弹加农炮，请访问：[跳弹加农炮](/upgrade/0313-Ricochet-Cannon)。*
- *如想查看由一个加农炮和一个箭塔合成的建筑，请访问：[复合机械塔](/upgrade/0317-Multi-Gear-Tower)。*
- *如想查看夜世界的加农炮和双管加农炮，请访问：[夜世界加农炮](/upgrade/1100-Cannon)、[夜世界双管加农炮](/upgrade/1101-Double-Cannon)。*
- *如想查看都城的加农炮，请访问：[都城加农炮](/upgrade/2201-Cannon)。*

<SwitchTabs contentClass="cp-unit-items" :stickyTabs="true" :pageTabs="true">
    <SwitchTab tabId="cp-unit-item-0" :activeTab="true">标准模式</SwitchTab>
    <SwitchTab tabId="cp-unit-item-1">连发模式</SwitchTab>
</SwitchTabs>

<!-- ↓↓↓ 标准模式 ↓↓↓ -->
<SwitchTabGroup id="cp-unit-item-0" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Cannon21.png" imgAlt="加农炮（标准模式）"
    :description="$frontmatter.description" :isSmallImg="true" />

<SmallTitle>各等级图片</SmallTitle>

<Panel>
    <UnitImgGroup title="未改装" :folder="$frontmatter.imgFolder">
        <UnitImg imgTitle="1 级" imgSrc="Cannon1.png" />
        <UnitImg imgTitle="2 级" imgSrc="Cannon2.png" />
        <UnitImg imgTitle="3 级" imgSrc="Cannon3.png" />
        <UnitImg imgTitle="4 级" imgSrc="Cannon4.png" />
        <UnitImg imgTitle="5 级" imgSrc="Cannon5.png" />
        <UnitImg imgTitle="6 级" imgSrc="Cannon6.png" />
        <UnitImg imgTitle="7 级" imgSrc="Cannon7.png" />
        <UnitImg imgTitle="8 级" imgSrc="Cannon8.png" />
        <UnitImg imgTitle="9 级" imgSrc="Cannon9.png" />
        <UnitImg imgTitle="10 级" imgSrc="Cannon10.png" />
        <UnitImg imgTitle="11 级" imgSrc="Cannon11.png" />
        <UnitImg imgTitle="12 级" imgSrc="Cannon12.png" />
        <UnitImg imgTitle="13 级" imgSrc="Cannon13.png" />
        <UnitImg imgTitle="14 级" imgSrc="Cannon14.png" />
        <UnitImg imgTitle="15 级" imgSrc="Cannon15.png" />
        <UnitImg imgTitle="16 级" imgSrc="Cannon16.png" />
        <UnitImg imgTitle="17 级" imgSrc="Cannon17.png" />
        <UnitImg imgTitle="18 级" imgSrc="Cannon18.png" />
        <UnitImg imgTitle="19 级" imgSrc="Cannon19.png" />
        <UnitImg imgTitle="20 级" imgSrc="Cannon20.png" />
        <UnitImg imgTitle="21 级" imgSrc="Cannon21.png" />
    </UnitImgGroup>
    <UnitImgGroup title="已改装，处于标准模式" :folder="$frontmatter.imgFolder">
        <UnitImg imgTitle="7 级" imgSrc="Cannon7A.png" />
        <UnitImg imgTitle="8 级" imgSrc="Cannon8A.png" />
        <UnitImg imgTitle="9 级" imgSrc="Cannon9A.png" />
        <UnitImg imgTitle="10 级" imgSrc="Cannon10A.png" />
        <UnitImg imgTitle="11 级" imgSrc="Cannon11A.png" />
        <UnitImg imgTitle="12 级" imgSrc="Cannon12A.png" />
        <UnitImg imgTitle="13 级" imgSrc="Cannon13A.png" />
        <UnitImg imgTitle="14 级" imgSrc="Cannon14A.png" />
        <UnitImg imgTitle="15 级" imgSrc="Cannon15A.png" />
        <UnitImg imgTitle="16 级" imgSrc="Cannon16A.png" />
        <UnitImg imgTitle="17 级" imgSrc="Cannon17A.png" />
        <UnitImg imgTitle="18 级" imgSrc="Cannon18A.png" />
        <UnitImg imgTitle="19 级" imgSrc="Cannon19A.png" />
        <UnitImg imgTitle="20 级" imgSrc="Cannon20A.png" />
        <UnitImg imgTitle="21 级" imgSrc="Cannon21A.png" />
    </UnitImgGroup>
</Panel>

<SmallTitle>各大本等级的加农炮数量</SmallTitle>

<BuildingNum>
    <BuildingNumRow title="大本等级" num="1, 2 - 4, 5 - 6,  7 - 9, 10, 11 - 15, 16, 17 - 18" />
    <BuildingNumRow title="建筑数量" num="1,     2,     3,      5,  6,       7,  3,       0" />
</BuildingNum>

在 16 级大本营，游戏引入合并建筑功能，这里的建筑数量指的是将所有可合并的建筑都合并后的数量。

<SmallTitle>属性</SmallTitle>

<UnitProperties>
    <UnitProperty pKey="占地面积" pValue="3×3" />
    <UnitProperty pKey="判定面积" pValue="2×2" :isJudgeSquare="true" />
    <UnitProperty pKey="伤害类型" pValue="单体伤害" />
    <UnitProperty pKey="攻击的目标" pValue="仅地面目标" />
    <UnitProperty pKey="射程" pValue="9 格" />
    <UnitProperty pKey="攻速" pValue="0.8 秒 1 发<sup>*</sup>" />
    <UnitProperty pKey="改装所需加农炮等级" pValue="7" />
    <UnitProperty pKey="改装所需夜世界双管加农炮等级" pValue="4" />
    <UnitProperty pKey="改装数量" pValue="仅限一个" />
    <UnitProperty pKey="改装时间" pValue="2" :isUpgradeTime="true" gpClass="building" />
    <UnitProperty pKey="改装费用" pValue="1M" :isUpgradeCost="true" resourceType="Gold" gpClass="building" />
</UnitProperties>

\* 加农炮改装前（标准模式）的攻速是 0.8 秒一次，改装后（连发模式）是 2.2 秒一轮。在连发模式下，4 连发期间每发 0.192 秒，之后停顿 1.6 秒。如果目标在加农炮还没打完 4 连发之前死亡， 导致加农炮没有发射全部 4 发炮弹时，每发没有射出去的炮弹会减少 0.2 秒攻击间隔。这里的 2.2 是这么算的：0.192 * (4 - 1) + 1.6 = 2.176 (秒) ≈ 2.2 (秒)。

<SmallTitle>升级数据</SmallTitle>

<UnitTable :tableExtraInfo="tableExtraInfoStandardMode">

| 等级 | 每秒伤害 | 每次伤害 | 生命值 | 升级费用 |   升级时间   |升级后可<br>获得的经验| 所需<br>大本等级 |
| ---- |   ---   |   ---   |   ---  |   ---   |     ---     |        ---          |       ---      |
| 1 | 7 | 5.6 | 300 | 250 | 0,0,0,5 |  | 1 |
| 2 | 10 | 8 | 360 | 1000 | 0,0,0,30 |  | 1 |
| 3 | 13 | 10.4 | 420 | 4000 | 0,0,2,0 |  | 2 |
| 4 | 17 | 13.6 | 500 | 16000 | 0,0,20,0 |  | 3 |
| 5 | 23 | 18.4 | 600 | 50000 | 0,0,30,0 |  | 4 |
| 6 | 30 | 24 | 660 | 60000 | 0,1,0,0 |  | 5 |
| 7 | 40 | 32 | 730 | 100000 | 0,2,0,0 |  | 6 |
| 8 | 48 | 38.4 | 800 | 160000 | 0,3,0,0 |  | 7 |
| 9 | 56 | 44.8 | 880 | 250000 | 0,3,30,0 |  | 8 |
| 10 | 64 | 51.2 | 960 | 330000 | 0,4,0,0 |  | 8 |
| 11 | 74 | 59.2 | 1060 | 500000 | 0,4,30,0 |  | 9 |
| 12 | 85 | 68 | 1160 | 600000 | 0,5,0,0 |  | 10 |
| 13 | 95 | 76 | 1260 | 660000 | 0,6,0,0 |  | 10 |
| 14 | 100 | 80 | 1380 | 1000000 | 0,8,0,0 |  | 11 |
| 15 | 105 | 84 | 1500 | 1200000 | 0,10,0,0 |  | 11 |
| 16 | 110 | 88 | 1620 | 1300000 | 0,11,0,0 |  | 12 |
| 17 | 115 | 92 | 1740 | 1500000 | 0,12,0,0 |  | 12 |
| 18 | 125 | 100 | 1870 | 1800000 | 0,16,0,0 |  | 13 |
| 19 | 135 | 108 | 2000 | 2000000 | 0,20,0,0 |  | 13 |
| 20 | 150 | 120 | 2150 | 2600000 | 1,0,0,0 |  | 14 |
| 21 | 160 | 128 | 2250 | 3000000 | 1,12,0,0 |  | 15 |
</UnitTable>
</SwitchTabGroup>

<!-- ↓↓↓ 连发模式 ↓↓↓ -->
<SwitchTabGroup id="cp-unit-item-1" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Cannon21B.png" imgAlt="加农炮（连发模式）"
    :description="$frontmatter.description" :isSmallImg="true" />

<SmallTitle>各等级图片</SmallTitle>

<Panel>
    <UnitImgGroup title="已改装，处于连发模式" :folder="$frontmatter.imgFolder">
        <UnitImg imgTitle="7 级" imgSrc="Cannon7B.png" />
        <UnitImg imgTitle="8 级" imgSrc="Cannon8B.png" />
        <UnitImg imgTitle="9 级" imgSrc="Cannon9B.png" />
        <UnitImg imgTitle="10 级" imgSrc="Cannon10B.png" />
        <UnitImg imgTitle="11 级" imgSrc="Cannon11B.png" />
        <UnitImg imgTitle="12 级" imgSrc="Cannon12B.png" />
        <UnitImg imgTitle="13 级" imgSrc="Cannon13B.png" />
        <UnitImg imgTitle="14 级" imgSrc="Cannon14B.png" />
        <UnitImg imgTitle="15 级" imgSrc="Cannon15B.png" />
        <UnitImg imgTitle="16 级" imgSrc="Cannon16B.png" />
        <UnitImg imgTitle="17 级" imgSrc="Cannon17B.png" />
        <UnitImg imgTitle="18 级" imgSrc="Cannon18B.png" />
        <UnitImg imgTitle="19 级" imgSrc="Cannon19B.png" />
        <UnitImg imgTitle="20 级" imgSrc="Cannon20B.png" />
        <UnitImg imgTitle="21 级" imgSrc="Cannon21B.png" />
    </UnitImgGroup>
</Panel>

<SmallTitle>各大本等级的加农炮数量</SmallTitle>

<BuildingNum>
    <BuildingNumRow title="大本等级" num="1, 2 - 4, 5 - 6,  7 - 9, 10, 11 - 15, 16, 17 - 18" />
    <BuildingNumRow title="建筑数量" num="1,     2,     3,      5,  6,       7,  3,       0" />
</BuildingNum>

在 16 级大本营，游戏引入合并建筑功能，这里的建筑数量指的是将所有可合并的建筑都合并后的数量。

<SmallTitle>属性</SmallTitle>

<UnitProperties>
    <UnitProperty pKey="占地面积" pValue="3×3" />
    <UnitProperty pKey="判定面积" pValue="2×2" :isJudgeSquare="true" />
    <UnitProperty pKey="伤害类型" pValue="单体伤害" />
    <UnitProperty pKey="攻击的目标" pValue="仅地面目标" />
    <UnitProperty pKey="射程" pValue="7 格 " />
    <UnitProperty pKey="攻速" pValue="2.2 秒 4 发<sup>*</sup>" />
    <UnitProperty pKey="改装所需加农炮等级" pValue="7" />
    <UnitProperty pKey="改装所需夜世界双管加农炮等级" pValue="4" />
    <UnitProperty pKey="改装数量" pValue="仅限一个" />
    <UnitProperty pKey="改装时间" pValue="2" :isUpgradeTime="true" gpClass="building" />
    <UnitProperty pKey="改装费用" pValue="1M" :isUpgradeCost="true" resourceType="Gold" gpClass="building" />
</UnitProperties>

\* 加农炮改装前（标准模式）的攻速是 0.8 秒一次，改装后（连发模式）是 2.2 秒一轮。在连发模式下，4 连发期间每发 0.192 秒，之后停顿 1.6 秒。如果目标在加农炮还没打完 4 连发之前死亡， 导致加农炮没有发射全部 4 发炮弹时，每发没有射出去的炮弹会减少 0.2 秒攻击间隔。这里的 2.2 是这么算的：0.192 * (4 - 1) + 1.6 = 2.176 (秒) ≈ 2.2 (秒)。

<SmallTitle>升级数据</SmallTitle>

<UnitTable :tableExtraInfo="tableExtraInfoGearUpMode">

| 等级 | 每秒伤害 | 每次伤害 | 生命值 | 升级费用 |  升级时间  |升级后可<br>获得的经验| 所需<br>大本等级 |
| ---- |   ---   |   ---   |   ---  |   ---   |    ---    |        ---          |       ---      |
| 7 | 80 | 43.52 | 730 | 100000 | 0,2,0,0 |  | 6 |
| 8 | 95 | 52.22 | 800 | 160000 | 0,3,0,0 |  | 7 |
| 9 | 111 | 60.92 | 880 | 250000 | 0,3,30,0 |  | 8 |
| 10 | 127 | 69.63 | 960 | 330000 | 0,4,0,0 |  | 8 |
| 11 | 147 | 80.51 | 1060 | 500000 | 0,4,30,0 |  | 9 |
| 12 | 170 | 92.48 | 1160 | 600000 | 0,5,0,0 |  | 10 |
| 13 | 190 | 103.36 | 1260 | 660000 | 0,6,0,0 |  | 10 |
| 14 | 200 | 108.8 | 1380 | 1000000 | 0,8,0,0 |  | 11 |
| 15 | 210 | 114.24 | 1500 | 1200000 | 0,10,0,0 |  | 11 |
| 16 | 220 | 119.68 | 1620 | 1300000 | 0,11,0,0 |  | 12 |
| 17 | 230 | 125.12 | 1740 | 1500000 | 0,12,0,0 |  | 12 |
| 18 | 250 | 136 | 1870 | 1800000 | 0,16,0,0 |  | 13 |
| 19 | 270 | 146.88 | 2000 | 2000000 | 0,20,0,0 |  | 13 |
| 20 | 300 | 163.2 | 2150 | 2600000 | 1,0,0,0 |  | 14 |
| 21 | 320 | 174.08 | 2250 | 3000000 | 1,12,0,0 |  | 15 |
</UnitTable>
</SwitchTabGroup>

<!-- ↓↓↓ 公共部分 ↓↓↓ -->
<SmallTitle>更新历史</SmallTitle>

<Timeline>
    <TimelineItem date="2026/02/23">
        <TimelineRow>改装加农炮每秒伤害显示调整： 7级： 54 → 80 8级： 64 → 95 9级： 75 → 111 10级： 86 → 127 11级： 100 → 147 12级： 116 → 170 13级： 129 → 190 14级： 143 → 200 15级： 156 → 210 16级： 162 → 220 17级： 170 → 230 18级： 175 → 250 19级： 189 → 270 20级： 202 → 300 21级： 216 → 320 改装加农炮每次伤害提高36%： 7级： 32 → 43.52 8级： 38.4 → 52.22 9级： 44.8 → 60.92 10级： 51.2 → 69.63 11级： 59.2 → 80.51 12级： 68 → 92.48 13级： 76 → 103.36 14级： 80 → 108.8 15级： 84 → 114.24 16级： 88 → 119.68 17级： 92 → 125.12 18级： 100 → 136 19级： 108 → 146.88 20级： 120 → 163.2 21级： 128 → 174.08</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/10/06">
        <TimelineRow>18 ~ 21 级加农炮的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/06/16">
        <TimelineRow>1 ~ 6 级加农炮的生命值减少。</TimelineRow>
        <TimelineRow>1 ~ 6 级加农炮的每秒伤害降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>1 ~ 9、11 ~ 12、14 ~ 16、18、20 ~ 21 级加农炮的升级时间减少。</TimelineRow>
        <TimelineRow>6 ~ 16、18、20 ~ 21 级加农炮的升级费用降低。</TimelineRow>
        <TimelineRow>加农炮的改装费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/02/10">
        <TimelineRow>2、3、10、13、15、17、19 级加农炮的升级时间减少。</TimelineRow>
        <TimelineRow>13、15、17、19 级加农炮的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>17 本推出，其中 2 个加农炮可以被合并为 1 个跳弹加农炮。</TimelineRow>
        <TimelineRow>8 ~ 9、12 ~ 21 级加农炮的升级时间减少。</TimelineRow>
        <TimelineRow>15 ~ 21 级加农炮的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/18">
        <TimelineRow>14 ~ 21 级加农炮的升级时间减少。</TimelineRow>
        <TimelineRow>16 ~ 21 级加农炮的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/03">
        <TimelineRow>14 ~ 19 级加农炮的每秒伤害降低。</TimelineRow>
        <TimelineRow>自本次更新后，连发模式秒伤 = 1.35 倍快速模式秒伤，标准模式次伤 = 连发模式次伤这两个规律不再成立。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>16 本推出，其中 4 个加农炮可以被合并为 2 个跳弹加农炮。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/09/28">
        <TimelineRow>12 ~ 20 级加农炮的每秒伤害降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>16 ~ 19 级加农炮的升级时间减少。</TimelineRow>
        <TimelineRow>16 ~ 19 级加农炮的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>15 本推出，并在 15 本新增 21 级加农炮。</TimelineRow>
        <TimelineRow>12 ~ 20 级加农炮的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/12/09">
        <TimelineRow>8 ~ 19 级加农炮的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>14 本推出，并在 14 本新增 20 级加农炮。</TimelineRow>
        <TimelineRow>2 ~ 14 级加农炮的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/06/22">
        <TimelineRow>13 本新增 19 级加农炮。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/03/30">
        <TimelineRow>18 级加农炮的生命值由 1860 调整到 1870。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/12/09">
        <TimelineRow>13 本推出，并在 13 本新增 18 级加农炮。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/04/02">
        <TimelineRow>10 ~ 16 级加农炮的升级费用降低。</TimelineRow>
        <TimelineRow>7 ~ 13、16 级加农炮的升级时间减少。</TimelineRow>
        <TimelineRow>12 级大本营新增 17 级加农炮。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/02/22">
        <TimelineRow>10 ~ 16 级加农炮的伤害降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>
<p><small>数值核对：2026-10-13 · <a href="https://clashofclans.fandom.com/wiki/Cannon?oldid=619060" target="_blank" rel="noopener noreferrer">部落冲突维基</a>。部分附加字段沿用原记录。</small></p>
