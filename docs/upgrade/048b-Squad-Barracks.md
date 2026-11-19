---
title: "部落冲突 小队训练营升级数据"
navTitle: "小队训练营"
shownTitle: "小队训练营"
englishName: "Squad Barracks"
description: "小队训练营的属性、解锁条件和升级数据。"
module: upgrade-home
wiki: https://clashofclans.fandom.com/wiki/Squad_Barracks
canonical: /upgrade/048b-Squad-Barracks
dataVersionUpdatedOn: 2026-11-17
---

<UnitInfo folder="" imgSrc="/images/th19/048b-Squad-Barracks/level_12.webp" :imgAlt="$frontmatter.navTitle" />

<SmallTitle>各等级图片</SmallTitle>

<Panel>
    <UnitImgGroup folder="">
        <UnitImg imgTitle="1 级" imgSrc="/images/th19/048b-Squad-Barracks/level_1.webp" />
        <UnitImg imgTitle="2 级" imgSrc="/images/th19/048b-Squad-Barracks/level_2.webp" />
        <UnitImg imgTitle="3 级" imgSrc="/images/th19/048b-Squad-Barracks/level_3.webp" />
        <UnitImg imgTitle="4 级" imgSrc="/images/th19/048b-Squad-Barracks/level_4.webp" />
        <UnitImg imgTitle="5 级" imgSrc="/images/th19/048b-Squad-Barracks/level_5.webp" />
        <UnitImg imgTitle="6 级" imgSrc="/images/th19/048b-Squad-Barracks/level_6.webp" />
        <UnitImg imgTitle="7 级" imgSrc="/images/th19/048b-Squad-Barracks/level_7.webp" />
        <UnitImg imgTitle="8 级" imgSrc="/images/th19/048b-Squad-Barracks/level_8.webp" />
        <UnitImg imgTitle="9 级" imgSrc="/images/th19/048b-Squad-Barracks/level_9.webp" />
        <UnitImg imgTitle="10 级" imgSrc="/images/th19/048b-Squad-Barracks/level_10.webp" />
        <UnitImg imgTitle="11 级" imgSrc="/images/th19/048b-Squad-Barracks/level_11.webp" />
        <UnitImg imgTitle="12 级" imgSrc="/images/th19/048b-Squad-Barracks/level_12.webp" />
    </UnitImgGroup>
</Panel>

<SmallTitle>建筑数量对照表</SmallTitle>

<BuildingNum>
    <BuildingNumRow title="大本等级" num="1 - 7, 8 - 19" />
    <BuildingNumRow title="建筑数量" num="0, 1" />
</BuildingNum>

<SmallTitle>重要说明</SmallTitle>

8 本可建造小队训练营，之后每升一级训练营就开放一种新小队。出战成员沿用玩家的兵种研究等级，尚未解锁的兵种以 1 级出战。小队只能由自己部署，不能捐赠。到 19 本后可研究小队，升至 2 级即可获得小队能力。

全部 12 种小队可在[升级数据目录](/upgrade/category/home)的“科技”分类中查看。

<SmallTitle>升级数据</SmallTitle>

<script setup>
const tableExtraInfo = [{"column": 2, "type": "cost", "gpClass": "building", "icon": "Elixir"}, {"column": 3, "type": "time", "gpClass": "building"}];
</script>

<UnitTable :tableExtraInfo="tableExtraInfo">

| 等级 | 生命值 | 升级费用 | 升级时间 | 所需大本等级 |
| --- | --- | --- | --- | --- |
| 1 | 500 | 1700000 | 2,0,0,0 | 8 |
| 2 | 560 | 3000000 | 3,0,0,0 | 9 |
| 3 | 620 | 3800000 | 5,0,0,0 | 10 |
| 4 | 680 | 6000000 | 6,0,0,0 | 11 |
| 5 | 740 | 7500000 | 7,0,0,0 | 12 |
| 6 | 800 | 10000000 | 7,12,0,0 | 13 |
| 7 | 860 | 12500000 | 8,0,0,0 | 14 |
| 8 | 920 | 15000000 | 9,12,0,0 | 15 |
| 9 | 980 | 16000000 | 10,0,0,0 | 16 |
| 10 | 1040 | 20000000 | 11,0,0,0 | 17 |
| 11 | 1100 | 26000000 | 13,12,0,0 | 18 |
| 12 | 1160 | 32000000 | 16,0,0,0 | 19 |
</UnitTable>

<small>小队的部署、研究与解锁规则见[Supercell 更新公告](https://supercell.com/en/games/clashofclans/blog/release-notes/the-clash-of-titans-update-is-rolling-out/)。训练营各级生命值、升级费用、时间及大本营要求见[Clash of Clans Wiki](https://clashofclans.fandom.com/wiki/Squad_Barracks?oldid=626398)。</small>
