---
title: "部落冲突 coc 废墟女巫升级数据"
navTitle: "废墟女巫"
shownTitle: "废墟女巫"
englishName: "Ruin Witch"
module: upgrade-home
imgFolder: home_tech/0013
wiki: https://clashofclans.fandom.com/wiki/Ruin_Witch
canonical: /upgrade/0013-Ruin-Witch
dataSyncedOn: 2026-10-13
---

<script setup>
const tableExtraInfo0 = [
    {
        "column": 6,
        "type": "cost",
        "icon": "Dark_Elixir",
        "gpClass": "research",
        "noGoldPass": false
    },
    {
        "column": 7,
        "type": "time",
        "gpClass": "research",
        "noGoldPass": false
    }
];
</script>

<SwitchTabs contentClass="cp-unit-items" :stickyTabs="true" :pageTabs="true">
    <SwitchTab tabId="cp-unit-item-0" :activeTab="true">废墟女巫</SwitchTab>
    <SwitchTab tabId="cp-unit-item-1">废墟骑士</SwitchTab>
</SwitchTabs>

<SwitchTabGroup id="cp-unit-item-0" class="cp-unit-items">

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Ruin_Witch1.png" :imgAlt="$frontmatter.navTitle" :isSmallImg="true" />

<SmallTitle>各等级图片</SmallTitle>

<Panel>
    <UnitImgGroup :folder="$frontmatter.imgFolder">
        <UnitImg imgTitle="1 级" imgSrc="Ruin_Witch1.png" />
        <UnitImg imgTitle="2 级" imgSrc="Ruin_Witch2.png" />
        <UnitImg imgTitle="3 级" imgSrc="Ruin_Witch3.png" />
        <UnitImg imgTitle="4 级" imgSrc="Ruin_Witch4.png" />
    </UnitImgGroup>
</Panel>

<SmallTitle>重要说明</SmallTitle>

1. 解锁条件：13级暗黑训练营、16级大本营。

2. 召唤物废墟骑士的等级随废墟女巫变化，不能单独训练或升级。

<SmallTitle>属性</SmallTitle>

<UnitProperties>
    <UnitProperty pKey="攻击偏好" pValue="建筑残骸" />
    <UnitProperty pKey="占据人口" pValue="26" />
    <UnitProperty pKey="移动速度" pValue="1.5 格/秒" />
    <UnitProperty pKey="所需暗黑训练营等级" pValue="13" />
    <UnitProperty pKey="射程" pValue="0.8格" />
</UnitProperties>

<SmallTitle>升级数据</SmallTitle>

<UnitTable :tableExtraInfo="tableExtraInfo0">

| 等级 | 召唤骑士等级 | 最多召唤骑士数 | 生命值 | 每秒伤害 | 每次伤害 | 升级花费 | 升级时间 | 所需<br>实验室等级 | 所需<br>大本等级 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 | 10 | 2300 | 25 | 50 | \ | \ | 14 | 16 |
| 2 | 2 | 10 | 2550 | 26 | 52 | 220000 | 11,0,0,0 | 14 | 16 |
| 3 | 3 | 10 | 2800 | 27 | 54 | 300000 | 12,0,0,0 | 15 | 17 |
| 4 | 4 | 10 | 3050 | 28 | 56 | 380000 | 15,12,0,0 | 16 | 18 |
</UnitTable>

<SmallTitle>更新历史</SmallTitle>

<Timeline>
    <TimelineItem date="2026/08/31">
        <TimelineRow>全部等级的废墟骑士召唤上限从8提高到10。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2026/06/16">
        <TimelineRow>废墟女巫已加入游戏，共4级。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2026/06/13">
        <TimelineRow>公布废墟女巫。</TimelineRow>
    </TimelineItem>
</Timeline>


<p><small>数值核对：2026-10-13 · <a href="https://clashofclans.fandom.com/wiki/Ruin_Witch?oldid=625328" target="_blank" rel="noopener noreferrer">部落冲突维基</a>。</small></p>

</SwitchTabGroup>

<SwitchTabGroup id="cp-unit-item-1" class="cp-unit-items">

<!--@include: ./0014-Ruin-Knight.md#ruin-knight-->

</SwitchTabGroup>
