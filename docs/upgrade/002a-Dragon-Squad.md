---
title: "部落冲突 飞龙小队升级数据"
navTitle: "飞龙小队"
shownTitle: "飞龙小队"
englishName: "Dragons Squad"
description: "飞龙小队的属性、解锁条件和升级数据。"
module: upgrade-home
wiki: https://clashofclans.fandom.com/wiki/Dragon_Squad
canonical: /upgrade/002a-Dragon-Squad
dataVersionUpdatedOn: 2026-11-16
---

<UnitInfo folder="" imgSrc="/images/th19/002a-Dragon-Squad/icon.webp" :imgAlt="$frontmatter.navTitle" />

<SmallTitle>重要说明</SmallTitle>

小队组成：2 个飞龙、2 个龙骑士。通过 11 级[小队训练营](/upgrade/048b-Squad-Barracks)解锁。一次部署整个小队；成员的兵种等级跟随玩家研究进度。小队不能捐赠，小队自身升级在 19 本开放。

<SmallTitle>升级数据</SmallTitle>

<script setup>
const tableExtraInfo = [{"column": 3, "type": "cost", "gpClass": "research", "icon": "Elixir"}, {"column": 4, "type": "time", "gpClass": "research"}];
</script>

<UnitTable :tableExtraInfo="tableExtraInfo">

| 小队等级 | 占用人口 | 小队能力 | 升级花费 | 升级时间 | 所需实验室等级 | 所需大本等级 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 85 | 无 | — | — | — | 18 |
| 2 | 85 | 部署后无敌 2 秒 | 29500000 | 14,0,0,0 | 17 | 19 |
| 3 | 85 | 部署后无敌 3 秒 | 32000000 | 16,0,0,0 | 17 | 19 |
</UnitTable>


<small>资料参考：[Supercell 更新公告](https://supercell.com/en/games/clashofclans/blog/release-notes/the-clash-of-titans-update-is-rolling-out/)、[COC Wiki 19 本指南](https://cocwiki.com/guides/town-hall-19)、[Clash of Clans Wiki](https://clashofclans.fandom.com/wiki/Dragon_Squad)；费用和时间另参考 [ClashKing Assets](https://github.com/ClashKingInc/ClashKingAssets/blob/fa40345986d5c862480e6fa34aa5100ab8eee345/assets/static_data.json)。部分中文名称为便于查询的暂译。COC Wiki 引用的 Wiki 资料依 CC BY-SA 3.0 整理，改编资料按 [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) 分享。</small>
