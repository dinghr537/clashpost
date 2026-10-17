---
title: "部落冲突 coc 迫击炮升级数据"
navTitle: "迫击炮"
shownTitle: "迫击炮"
description: "迫击炮可以发出威力无比的炮弹，其造成的溅射伤害可以击败大群敌军。注意，要防止敌军过于接近迫击炮！"
module: upgrade-home
imgFolder: home_buildings/0303
wiki: https://clashofclans.fandom.com/wiki/Mortar
canonical: /upgrade/0303-Mortar
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
const tableExtraInfoFastMode = tableExtraInfoStandardMode;
</script>

- *如想查看夜世界的多管迫击炮，请访问 [夜世界多管迫击炮](/upgrade/1108-Multi-Mortar)。*
- *如想查看都城的多管迫击炮，请访问：[都城多管迫击炮](/upgrade/2206-Multi-Mortar)。*

<SwitchTabs contentClass="cp-unit-items" :stickyTabs="true" :pageTabs="true">
    <SwitchTab tabId="cp-unit-item-0" :activeTab="true">标准模式</SwitchTab>
    <SwitchTab tabId="cp-unit-item-1">快速模式</SwitchTab>
</SwitchTabs>

<!-- ↓↓↓ 标准模式 ↓↓↓ -->
<SwitchTabGroup id="cp-unit-item-0" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Mortar18.png" imgAlt="迫击炮（标准模式）"
    :description="$frontmatter.description" :isSmallImg="true" />

<SmallTitle>各等级图片</SmallTitle>

<Panel>
    <UnitImgGroup title="未改装" :folder="$frontmatter.imgFolder">
        <UnitImg imgTitle="1 级" imgSrc="Mortar1.png" />
        <UnitImg imgTitle="2 级" imgSrc="Mortar2.png" />
        <UnitImg imgTitle="3 级" imgSrc="Mortar3.png" />
        <UnitImg imgTitle="4 级" imgSrc="Mortar4.png" />
        <UnitImg imgTitle="5 级" imgSrc="Mortar5.png" />
        <UnitImg imgTitle="6 级" imgSrc="Mortar6.png" />
        <UnitImg imgTitle="7 级" imgSrc="Mortar7.png" />
        <UnitImg imgTitle="8 级" imgSrc="Mortar8.png" />
        <UnitImg imgTitle="9 级" imgSrc="Mortar9.png" />
        <UnitImg imgTitle="10 级" imgSrc="Mortar10.png" />
        <UnitImg imgTitle="11 级" imgSrc="Mortar11.png" />
        <UnitImg imgTitle="12 级" imgSrc="Mortar12.png" />
        <UnitImg imgTitle="13 级" imgSrc="Mortar13.png" />
        <UnitImg imgTitle="14 级" imgSrc="Mortar14.png" />
        <UnitImg imgTitle="15 级" imgSrc="Mortar15.png" />
        <UnitImg imgTitle="16 级" imgSrc="Mortar16.png" />
        <UnitImg imgTitle="17 级" imgSrc="Mortar17.png" />
        <UnitImg imgTitle="17 级" imgSrc="Mortar18.png" />
    </UnitImgGroup>
    <UnitImgGroup title="已改装，处于标准模式" :folder="$frontmatter.imgFolder">
        <UnitImg imgTitle="8 级" imgSrc="Mortar8A.png" />
        <UnitImg imgTitle="9 级" imgSrc="Mortar9A.png" />
        <UnitImg imgTitle="10 级" imgSrc="Mortar10A.png" />
        <UnitImg imgTitle="11 级" imgSrc="Mortar11A.png" />
        <UnitImg imgTitle="12 级" imgSrc="Mortar12A.png" />
        <UnitImg imgTitle="13 级" imgSrc="Mortar13A.png" />
        <UnitImg imgTitle="14 级" imgSrc="Mortar14A.png" />
        <UnitImg imgTitle="15 级" imgSrc="Mortar15A.png" />
        <UnitImg imgTitle="16 级" imgSrc="Mortar16A.png" />
        <UnitImg imgTitle="17 级" imgSrc="Mortar17A.png" />
        <UnitImg imgTitle="17 级" imgSrc="Mortar18A.png" />
            <UnitImg imgTitle="18 级（改装）" imgSrc="Mortar18G.png" />
</UnitImgGroup>
</Panel>

<SmallTitle>各大本等级的迫击炮数量</SmallTitle>

<BuildingNum>
    <BuildingNumRow title="大本等级" num="1 - 2, 3 - 5, 6, 7, 8 - 18" />
    <BuildingNumRow title="建筑数量" num="    0,     1, 2, 3,      4" />
</BuildingNum>

<SmallTitle>属性</SmallTitle>

<UnitProperties>
    <UnitProperty pKey="占地面积" pValue="3×3" />
    <UnitProperty pKey="判定面积" pValue="2×2" :isJudgeSquare="true" />
    <UnitProperty pKey="伤害类型" pValue="范围伤害" />
    <UnitProperty pKey="伤害半径" pValue="1.5 格" />
    <UnitProperty pKey="攻击的目标" pValue="仅地面目标" />
    <UnitProperty pKey="射程" pValue="4 ~ 11 格" />
    <UnitProperty pKey="攻速" pValue="5 秒 1 发 (标准)" />
    <UnitProperty pKey="改装所需迫击炮等级" pValue="8" />
    <UnitProperty pKey="改装所需夜世界迫击炮等级" pValue="8" />
    <UnitProperty pKey="改装数量" pValue="仅限一个" />
    <UnitProperty pKey="改装时间" pValue="14" :isUpgradeTime="true" gpClass="building" />
    <UnitProperty pKey="改装费用" pValue="6M" :isUpgradeCost="true" resourceType="Gold" gpClass="building" />
</UnitProperties>

<SmallTitle>升级数据</SmallTitle>

<UnitTable :tableExtraInfo="tableExtraInfoStandardMode">

| 等级 | 每秒伤害 | 每次伤害 | 生命值 | 升级费用 |  升级时间  |升级后可<br>获得的经验| 所需<br>大本等级 |
| ---- |   ---   |   ---   |   ---  |   ---   |    ---    |        ---          |       ---      |
| 1 | 4 | 20 | 400 | 5000 | 0,0,30,0 |  | 3 |
| 2 | 5 | 25 | 450 | 25000 | 0,1,0,0 |  | 4 |
| 3 | 6 | 30 | 500 | 90000 | 0,2,0,0 |  | 5 |
| 4 | 7 | 35 | 550 | 180000 | 0,3,0,0 |  | 6 |
| 5 | 9 | 45 | 600 | 300000 | 0,6,0,0 |  | 7 |
| 6 | 11 | 55 | 650 | 500000 | 0,8,0,0 |  | 8 |
| 7 | 15 | 75 | 700 | 900000 | 0,12,0,0 |  | 9 |
| 8 | 20 | 100 | 800 | 1200000 | 0,18,0,0 |  | 10 |
| 9 | 25 | 125 | 950 | 1600000 | 0,20,0,0 |  | 11 |
| 10 | 30 | 150 | 1100 | 1800000 | 1,0,0,0 |  | 11 |
| 11 | 35 | 175 | 1300 | 2300000 | 1,6,0,0 |  | 12 |
| 12 | 38 | 190 | 1500 | 2400000 | 1,12,0,0 |  | 12 |
| 13 | 42 | 210 | 1700 | 2800000 | 2,0,0,0 |  | 13 |
| 14 | 48 | 240 | 1950 | 4300000 | 2,12,0,0 |  | 14 |
| 15 | 54 | 270 | 2150 | 5000000 | 3,0,0,0 |  | 15 |
| 16 | 60 | 300 | 2300 | 7000000 | 4,0,0,0 |  | 16 |
| 17 | 66 | 330 | 2450 | 13000000 | 5,0,0,0 |  | 17 |
| 18 | 72 | 360 | 2550 | 21000000 | 12,12,0,0 |  | 18 |

</UnitTable>
</SwitchTabGroup>

<!-- ↓↓↓ 快速模式 ↓↓↓ -->
<SwitchTabGroup id="cp-unit-item-1" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Mortar18B.png" imgAlt="迫击炮（快速模式）"
    :description="$frontmatter.description" :isSmallImg="true" />

<SmallTitle>各等级图片</SmallTitle>

<Panel>
    <UnitImgGroup title="已改装，处于连发模式" :folder="$frontmatter.imgFolder">
        <UnitImg imgTitle="8 级" imgSrc="Mortar8B.png" />
        <UnitImg imgTitle="9 级" imgSrc="Mortar9B.png" />
        <UnitImg imgTitle="10 级" imgSrc="Mortar10B.png" />
        <UnitImg imgTitle="11 级" imgSrc="Mortar11B.png" />
        <UnitImg imgTitle="12 级" imgSrc="Mortar12B.png" />
        <UnitImg imgTitle="13 级" imgSrc="Mortar13B.png" />
        <UnitImg imgTitle="14 级" imgSrc="Mortar14B.png" />
        <UnitImg imgTitle="15 级" imgSrc="Mortar15B.png" />
        <UnitImg imgTitle="16 级" imgSrc="Mortar16B.png" />
        <UnitImg imgTitle="17 级" imgSrc="Mortar17B.png" />
        <UnitImg imgTitle="18 级" imgSrc="Mortar18B.png" />
    </UnitImgGroup>
</Panel>

<SmallTitle>各大本等级的迫击炮数量</SmallTitle>

<BuildingNum>
    <BuildingNumRow title="大本等级" num="1 - 2, 3 - 5, 6, 7, 8 - 18" />
    <BuildingNumRow title="建筑数量" num="    0,     1, 2, 3,      4" />
</BuildingNum>

<SmallTitle>属性</SmallTitle>

<UnitProperties>
    <UnitProperty pKey="占地面积" pValue="3×3" />
    <UnitProperty pKey="判定面积" pValue="2×2" :isJudgeSquare="true" />
    <UnitProperty pKey="伤害类型" pValue="范围伤害" />
    <UnitProperty pKey="伤害半径" pValue="1.5 格" />
    <UnitProperty pKey="攻击的目标" pValue="仅地面目标" />
    <UnitProperty pKey="射程" pValue="4 ~ 11 格" />
    <UnitProperty pKey="攻速" pValue="5 秒 3 发 (改装)<sup>*</sup>" />
    <UnitProperty pKey="改装所需迫击炮等级" pValue="8" />
    <UnitProperty pKey="改装所需夜世界迫击炮等级" pValue="8" />
    <UnitProperty pKey="改装数量" pValue="仅限一个" />
    <UnitProperty pKey="改装时间" pValue="14" :isUpgradeTime="true" gpClass="building" />
    <UnitProperty pKey="改装费用" pValue="6M" :isUpgradeCost="true" resourceType="Gold" gpClass="building" />
</UnitProperties>

\* 多管迫击炮的攻击间隔是：3 连发期间每发 0.5 秒，之后停顿 4 秒。如果目标在多管还没打完 3 连发之前死亡，导致多管没有发射全部3发炮弹时，每发没有射出去的炮弹会减少 0.5 秒攻击间隔。上述的 5 秒指的是一整个周期的时间，0.5 * (3 - 1) + 4 = 5 (秒)

<SmallTitle>升级数据</SmallTitle>

<UnitTable :tableExtraInfo="tableExtraInfoFastMode">

| 等级 | 每秒伤害 | 每次伤害 | 生命值 | 升级费用 |  升级时间  |升级后可<br>获得的经验| 所需<br>大本等级 |
| ---- |   ---   |   ---   |   ---  |   ---   |    ---    |        ---          |       ---      |
| 8 | 25 | 41.6 | 800 | 1200000 | 0,18,0,0 |  | 10 |
| 9 | 30 | 51.58 | 950 | 1600000 | 0,20,0,0 |  | 11 |
| 10 | 37 | 63.23 | 1100 | 1800000 | 1,0,0,0 |  | 11 |
| 11 | 42 | 71.55 | 1300 | 2300000 | 1,6,0,0 |  | 12 |
| 12 | 46 | 78.2 | 1500 | 2400000 | 1,12,0,0 |  | 12 |
| 13 | 51 | 86.52 | 1700 | 2800000 | 2,0,0,0 |  | 13 |
| 14 | 58 | 98.17 | 1950 | 4300000 | 2,12,0,0 |  | 14 |
| 15 | 65 | 109.82 | 2150 | 5000000 | 3,0,0,0 |  | 15 |
| 16 | 73 | 123.13 | 2300 | 7000000 | 4,0,0,0 |  | 16 |
| 17 | 80 | 134.78 | 2450 | 13000000 | 5,0,0,0 |  | 17 |
| 18 | 88 | 148.09 | 2550 | 21000000 | 12,12,0,0 |  | 18 |
</UnitTable>
</SwitchTabGroup>

<!-- ↓↓↓ 公共部分 ↓↓↓ -->
注：迫击炮改装后每秒伤害会略微提高。

<SmallTitle>更新历史</SmallTitle>

<Timeline>
    <TimelineItem date="2026/04/27">
        <TimelineRow>为 18 级迫击炮新增两级超级充能。<a href="https://supercell.com/en/games/clashofclans/blog/release-notes/the-sound-of-clash-update/" target="_blank" rel="noopener noreferrer">来源：Supercell 官方更新公告</a>。</TimelineRow>
        <TimelineRow>改装后的多管迫击炮首次连发增加 0.5 秒延迟，修复原先立即开火的时序。 <a href="https://supercell.com/en/games/clashofclans/blog/release-notes/the-sound-of-clash-update/" target="_blank" rel="noopener noreferrer">官方公告</a></TimelineRow>
    </TimelineItem>
    <TimelineItem date="2026/02/23">
        <TimelineRow>添加了 18 级迫击炮。</TimelineRow>
        <TimelineRow>移除了 17 级迫击炮的超级充能。</TimelineRow>
        <TimelineRow>更改了多管迫击炮在游戏面板中显示的伤害值（实际伤害没变，只是更改了显示算法）。</TimelineRow>
        <TimelineRow>多管模式每秒伤害显示值：8—17 级分别由 22、28、33、38、41、51、52、59、65、72 改为 24、30、37、42、46、51、58、66、73、81；每次伤害显示值：9 级 47→46，15 级 99→98，17 级 121→120。 <a href="https://clashofclans.fandom.com/wiki/Mortar#History" target="_blank" rel="noopener noreferrer">来源</a></TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/11/17">
        <TimelineRow>17 级及两个充能等级的迫击炮的升级时间和升级费用减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/10/06">
        <TimelineRow>15 ~ 16 级迫击炮的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>1 ~ 9、11、13 ~ 16 级迫击炮的升级时间减少。</TimelineRow>
        <TimelineRow>3 ~ 4、6 ~ 16 级迫击炮的升级费用降低。</TimelineRow>
        <TimelineRow>迫击炮的改装费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/02/10">
        <TimelineRow>在 17 本新增 17 级迫击炮。</TimelineRow>
        <TimelineRow>10、12 级迫击炮的升级时间减少。</TimelineRow>
        <TimelineRow>10、12 级迫击炮的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>9 ~ 16 级迫击炮的升级时间减少。</TimelineRow>
        <TimelineRow>11 ~ 16 级迫击炮的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/09/09">
        <TimelineRow>超级充能推出，迫击炮是第一批可以充能的建筑之一。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/18">
        <TimelineRow>1 ~ 15 级迫击炮的升级时间减少。</TimelineRow>
        <TimelineRow>14 ~ 15 级迫击炮的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>4 ~ 15 级迫击炮的升级时间减少。</TimelineRow>
        <TimelineRow>5 ~ 6、8 ~ 14 级迫击炮的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>11 ~ 13 级迫击炮的升级时间减少。</TimelineRow>
        <TimelineRow>11 ~ 13 级迫击炮的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>15 本推出，并在 15 本新增 15 级迫击炮。</TimelineRow>
        <TimelineRow>8 ~ 14 级迫击炮的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/06/27">
        <TimelineRow>9 ~ 14 级迫击炮的生命值增加。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/01/20">
        <TimelineRow>修复了改装后的迫击炮首发箭矢射出位置不合理的问题。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/12/09">
        <TimelineRow>4 ~ 13 级迫击炮的升级费用降低。</TimelineRow>
    </TimelineItem>
        <TimelineItem date="2021/09/27">
        <TimelineRow>14 本新增 14 级迫击炮。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>1 ~ 11 级迫击炮的升级费用降低。</TimelineRow>
        <TimelineRow>2 ~ 10 级迫击炮的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/03/30">
        <TimelineRow>13 本新增 13 级迫击炮。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/12/09">
        <TimelineRow>所有等级多管迫击炮的伤害提高 10%.</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/09/11">
        <TimelineRow>12 级迫击炮的生命值由 950 提升至 980。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/06/18">
        <TimelineRow>12 本新增 12 级迫击炮。</TimelineRow>
    </TimelineItem>
        <TimelineItem date="2019/04/02">
        <TimelineRow>1 级迫击炮的新建时间减少。</TimelineRow>
    </TimelineItem>
        <TimelineItem date="2019/02/22">
        <TimelineRow>5 ~ 12 级迫击炮的伤害提高。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>
<p><small>数值核对：2026-10-13 · <a href="https://clashofclans.fandom.com/wiki/Mortar?oldid=625094" target="_blank" rel="noopener noreferrer">部落冲突维基</a>。部分附加字段沿用原记录。</small></p>
