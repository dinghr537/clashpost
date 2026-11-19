---
title: "部落冲突 烟花炮手塔升级数据"
navTitle: "烟花炮手塔"
shownTitle: "烟花炮手塔"
englishName: "Firecracker Tower"
description: "烟花炮手塔的属性、解锁条件和升级数据。"
module: upgrade-home
wiki: https://clashofclans.fandom.com/wiki/Firecracker_Tower
canonical: /upgrade/031b-Firecracker-Tower
dataVersionUpdatedOn: 2026-11-17
---

<UnitInfo folder="" imgSrc="/images/th19/031b-Firecracker-Tower/level_2.webp" :imgAlt="$frontmatter.navTitle" />

<SmallTitle>各等级图片</SmallTitle>

<Panel>
    <UnitImgGroup folder="">
        <UnitImg imgTitle="1 级" imgSrc="/images/th19/031b-Firecracker-Tower/level_1.webp" />
        <UnitImg imgTitle="2 级" imgSrc="/images/th19/031b-Firecracker-Tower/level_2.webp" />
    </UnitImgGroup>
</Panel>

<SmallTitle>建筑数量对照表</SmallTitle>

<BuildingNum>
    <BuildingNumRow title="大本等级" num="1 - 18, 19" />
    <BuildingNumRow title="建筑数量" num="0, 2" />
</BuildingNum>

<SmallTitle>重要说明</SmallTitle>

每座烟花炮手塔由一座 21 级箭塔和一座 7 级投石炮合并而成，19 本最多拥有两座。火箭可命中 10 格内的地面或空中目标。命中时先造成范围伤害，然后向目标后方散射火花。

<SmallTitle>升级数据</SmallTitle>

<script setup>
const tableExtraInfo = [{"column": 5, "type": "cost", "gpClass": "building", "icon": "Gold"}, {"column": 6, "type": "time", "gpClass": "building"}];
</script>

<UnitTable :tableExtraInfo="tableExtraInfo">

| 等级 | 每秒伤害 | 火箭每次伤害 | 火花伤害范围 | 生命值 | 升级费用 | 升级时间 | 所需大本等级 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 270 | 365–483.84 | 190–365 | 6500 | 31000000 | 14,12,0,0 | 19 |
| 2 | 280 | 385–501.76 | 200–385 | 6700 | 32000000 | 15,0,0,0 | 19 |
</UnitTable>

<small>合并条件和攻击方式见[Supercell 更新公告](https://supercell.com/en/games/clashofclans/blog/release-notes/the-clash-of-titans-update-is-rolling-out/)。各级伤害范围、生命值、费用和时间见[Clash of Clans Wiki](https://clashofclans.fandom.com/wiki/Firecracker_Tower?oldid=626491)。</small>
