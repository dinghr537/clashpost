---
title: "部落驿站"
customTitle: true
titleTemplate: "部落冲突升级数据查询"
description: "查询部落冲突家乡、夜世界和部落都城的升级等级、资源消耗、升级时间与前置条件。"
module: home
canonical: /
hasUpdateTime: false
---

<script setup>
import FeaturedCardGrid from "@/components/card/FeaturedCardGrid.vue";
import FeaturedCard from "@/components/card/FeaturedCard.vue";
</script>

<div id="homepage-site-name"><h1>部落驿站</h1></div>
<p id="homepage-site-description">部落冲突升级数据查询</p>

查询建筑、部队、英雄和装备的升级费用、时间与前置条件。右上角搜索可以按中文名称、简称或英文名称查找单位。

<SmallTitle>按村庄查询</SmallTitle>

<FeaturedCardGrid>
    <FeaturedCard link="/upgrade/category/home" title="家乡" subtitle="建筑、部队、英雄与装备"
        imgSrc="https://static.clashpost.com/upgrade/upgrade_home.jpg" />
    <FeaturedCard link="/upgrade/category/bh" title="夜世界" subtitle="建筑、部队与英雄"
        imgSrc="https://static.clashpost.com/upgrade/upgrade_bh.jpg" />
    <FeaturedCard link="/upgrade/category/capital" title="部落都城" subtitle="建筑、部队与法术"
        imgSrc="https://static.clashpost.com/upgrade/upgrade_capital.jpg" />
</FeaturedCardGrid>

<SmallTitle>快速查询</SmallTitle>

- [大本营](/upgrade/0400-Town-Hall)
- [加农炮](/upgrade/0301-Cannon)
- [野蛮人之王（蛮王）](/upgrade/0200-Barbarian-King)
- [法师](/upgrade/0006-Wizard)
- [地震金靴](/upgrade/0702-Earthquake-Boots)
- [全部升级数据](/upgrade)

<SmallTitle>数据说明</SmallTitle>

当前页面沿用原项目历史资料，各单位的收录进度不同，部分已收录 2026 年 4 月内容，尚未完成最新版本的全量同步。后续按官网、Clash of Clans Wiki、Clash Ninja 或其他选定来源逐批更新，并记录来源与同步日期。

本项目作为「部落驿站」的继承项目继续整理升级数据。本地网站仅提供数据查询。

<style lang="scss">
#homepage-site-name h1 {
    margin-bottom: 0.5rem;
}
#homepage-site-description {
    margin: 0 0 1rem;
    font-size: 1.2rem;
    color: var(--cp-grey-text-light);
}
.cp-theme-dark #homepage-site-description {
    color: var(--cp-grey-text-dark);
}
</style>
