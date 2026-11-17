---
title: "部落冲突 烟花炮手塔升级数据"
navTitle: "烟花炮手塔"
shownTitle: "烟花炮手塔"
englishName: "Firecracker Tower"
description: "烟花炮手塔的属性、解锁条件和升级数据。"
module: upgrade-home
wiki: https://clashofclans.fandom.com/wiki/Firecracker_Tower
canonical: /upgrade/031b-Firecracker-Tower
dataVersionUpdatedOn: 2026-11-16
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

19 本可将 21 级箭塔和 7 级投石炮合并成烟花炮手塔，最多合并 2 座。其火箭能攻击地面和空中目标，在命中点及目标后方造成范围伤害，射程 10 格。

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


<small>资料参考：[Supercell 更新公告](https://supercell.com/en/games/clashofclans/blog/release-notes/the-clash-of-titans-update-is-rolling-out/)、[COC Wiki 19 本指南](https://cocwiki.com/guides/town-hall-19)、[Clash of Clans Wiki](https://clashofclans.fandom.com/wiki/Firecracker_Tower)；费用和时间另参考 [ClashKing Assets](https://github.com/ClashKingInc/ClashKingAssets/blob/fa40345986d5c862480e6fa34aa5100ab8eee345/assets/static_data.json)。部分中文名称为便于查询的暂译。COC Wiki 引用的 Wiki 资料依 CC BY-SA 3.0 整理，改编资料按 [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) 分享。</small>
