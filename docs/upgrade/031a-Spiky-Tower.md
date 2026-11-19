---
title: "部落冲突 尖刺塔升级数据"
navTitle: "尖刺塔"
shownTitle: "尖刺塔"
englishName: "Spiky Tower"
description: "尖刺塔的属性、解锁条件和升级数据。"
module: upgrade-home
wiki: https://clashofclans.fandom.com/wiki/Spiky_Tower
canonical: /upgrade/031a-Spiky-Tower
dataVersionUpdatedOn: 2026-11-17
---

<UnitInfo folder="" imgSrc="/images/th19/031a-Spiky-Tower/level_2.webp" :imgAlt="$frontmatter.navTitle" />

<SmallTitle>各等级图片</SmallTitle>

<Panel>
    <UnitImgGroup folder="">
        <UnitImg imgTitle="1 级" imgSrc="/images/th19/031a-Spiky-Tower/level_1.webp" />
        <UnitImg imgTitle="2 级" imgSrc="/images/th19/031a-Spiky-Tower/level_2.webp" />
    </UnitImgGroup>
</Panel>

<SmallTitle>建筑数量对照表</SmallTitle>

<BuildingNum>
    <BuildingNumRow title="大本等级" num="1 - 18, 19" />
    <BuildingNumRow title="建筑数量" num="0, 2" />
</BuildingNum>

<SmallTitle>重要说明</SmallTitle>

19 本最多可放置两座尖刺塔。有敌军进入 11 格范围时，尖刺塔开始启动。启动后，每次受到部队攻击，它都会按攻击者自身的最大生命值造成反伤。法术伤害、英雄装备技能和摧毁塔的最后一击不会触发反伤。冰冻法术对塔无效。

<SmallTitle>升级数据</SmallTitle>

<script setup>
const tableExtraInfo = [{"column": 3, "type": "cost", "gpClass": "building", "icon": "Dark_Elixir"}, {"column": 4, "type": "time", "gpClass": "building"}];
</script>

<UnitTable :tableExtraInfo="tableExtraInfo">

| 等级 | 反击伤害（目标生命上限） | 生命值 | 升级费用 | 升级时间 | 所需大本等级 |
| --- | --- | --- | --- | --- | --- |
| 1 | 6% | 5959 | 500000 | 15,0,0,0 | 19 |
| 2 | 9% | 6363 | 510000 | 15,12,0,0 | 19 |
</UnitTable>

<small>反伤的触发条件见[Supercell 更新公告](https://supercell.com/en/games/clashofclans/blog/release-notes/the-clash-of-titans-update-is-rolling-out/)。各级反伤比例、生命值、升级费用和时间见[Clash of Clans Wiki](https://clashofclans.fandom.com/wiki/Spiky_Tower?oldid=626489)。</small>
