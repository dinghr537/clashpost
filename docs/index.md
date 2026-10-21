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
import { onMounted, onBeforeUnmount } from "vue";
import FeaturedCardGrid from "@/components/card/FeaturedCardGrid.vue";
import FeaturedCard from "@/components/card/FeaturedCard.vue";
import { calcAllCountdowns } from "@/assets/homepage-countdown.js";

let intervalId;
onMounted(() => {
    calcAllCountdowns();
    intervalId = setInterval(calcAllCountdowns, 1000);
});
onBeforeUnmount(() => clearInterval(intervalId));
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

<SmallTitle>倒计时</SmallTitle>

<div class="homepage-countdown-cards">
    <div id="countdown-cwl" class="homepage-countdown-group">
        <div class="homepage-countdown-title stage-1">联赛报名开始</div>
        <div class="homepage-countdown-title stage-2" style="display: none;">联赛报名结束</div>
        <div class="homepage-countdown-title stage-3" style="display: none;">所有部落联赛结束</div>
        <div class="homepage-countdown-time">加载中……</div>
    </div>
    <div id="countdown-raid-weekend" class="homepage-countdown-group">
        <div class="homepage-countdown-title stage-1">突袭周末开始</div>
        <div class="homepage-countdown-title stage-2" style="display: none;">突袭周末结束</div>
        <div class="homepage-countdown-time">加载中……</div>
    </div>
    <div id="countdown-trader" class="homepage-countdown-group">
        <div class="homepage-countdown-title">商人刷新</div>
        <div class="homepage-countdown-time">加载中……</div>
    </div>
    <div id="countdown-clan-games" class="homepage-countdown-group">
        <div class="homepage-countdown-title stage-1">竞赛开始</div>
        <div class="homepage-countdown-title stage-2" style="display: none;">竞赛结束</div>
        <div class="homepage-countdown-time">加载中……</div>
    </div>
    <div id="countdown-ranked-reset" class="homepage-countdown-group">
        <div class="homepage-countdown-title">排位周赛结算</div>
        <div class="homepage-countdown-time">加载中……</div>
    </div>
    <div id="countdown-gold-pass" class="homepage-countdown-group">
        <div class="homepage-countdown-title">月卡结算</div>
        <div class="homepage-countdown-time">加载中……</div>
    </div>
</div>

<div class="homepage-recommend">
<div class="homepage-recommend-item">
<SmallTitle>你知道吗</SmallTitle>

- 4 瓶任意等级的[地震法术](/upgrade/0181-Earthquake-Spell)都能摧毁任意等级的城墙；从 6 级开始，地震法术还能伤害地面部队。
- [飞龙公爵](/upgrade/0205-Dragon-Duke)远离友方飞行单位时会进入狂暴状态，机制类似于[飞龙宝宝](/upgrade/000a-Baby-Dragon)。
- [愤怒水母](/upgrade/0289-Angry-Jelly)和[阿啾](/upgrade/028a-Sneezy)跟随的英雄未被击倒时，不占用[回溯法术](/upgrade/0107-Recall-Spell)的召回人口。

</div>
<div class="homepage-recommend-item">
<SmallTitle>最新动态</SmallTitle>

- 2026/10/20：[烈焰之心](/upgrade/07e0-Fire-Heart)和[废墟骑士](/upgrade/0013-Ruin-Witch)削弱；[冰封箭矢](/upgrade/0744-Frozen-Arrow)增强，[传送吊坠](/upgrade/0726-Portal-Pendant)新增生命值加成。
- 同次维护：[野猪骑士](/upgrade/0081-Hog-Rider)、[超级野猪骑士](/upgrade/060f-Super-Hog-Rider)、[掘地矿工](/upgrade/000b-Miner)、[超级矿工](/upgrade/060e-Super-Miner)和[陨石戈仑](/upgrade/0012-Meteor-Golem)生命值提高，[皮卡超人](/upgrade/0009-P.E.K.K.A)伤害提高。
- 2026/10/08：新装备[传送吊坠](/upgrade/0726-Portal-Pendant)、临时兵种[图腾投手](/upgrade/0e1d-Totem-Thrower)开放。
- 2026/08/31：[地兽](/upgrade/0285-Diggy)新增 11–15 级；[废墟女巫](/upgrade/0013-Ruin-Witch)的骑士召唤上限提高到 10。
- 2026/08/12：飞龙公爵的新装备[反击卡组](/upgrade/07e5-Revenge-Deck)开放。
- 2026/07/14：[龙骑士](/upgrade/000e-Dragon-Rider)再次削弱，[雷电飞龙](/upgrade/000c-Electro-Dragon)和[德鲁伊](/upgrade/008a-Druid)部分等级增强。

</div>
</div>

<div class="homepage-attention">
<SmallTitle>注意</SmallTitle>

- 倒计时依赖设备时间，按国际服常规日程计算；特殊活动调整以游戏内时间为准。
- 排位周赛每周一北京时间 13:00 结算，不含传奇 I 的四周赛季。[规则来源](https://support.supercell.com/clash-of-clans/en/articles/ranked-leagues-4.html)。
- 最新动态手动维护，目前整理至 2026/10/20；点击单位名称可查看详细变化与来源。

</div>

<SmallTitle>数据说明</SmallTitle>

2026-10-13 已同步 357 个单位的数据页，包含 17 个新增单位：常驻单位、今年两批精工防御以及新增和回归的临时单位。费用、时间、属性和前置条件采用 Clash of Clans Wiki 当前表格，每页保留来源修订链接及可取得的 2026 年更新历史。

2026-10-20 另已更新本次平衡调整涉及的 10 项兵种或装备，包含召唤物的关联数据、说明和更新历史。调整范围依据 [Supercell 公告](https://supercell.com/en/games/clashofclans/blog/news/balance-changes-incoming-october-2026/)，具体等级数值另在各页标注参考来源；其他数据仍沿用上述同步记录。

其余 31 个往期活动单位保留历史数据，并在页首标注。来源缺项显示为“未知”或“不适用”；同步日期不表示游戏更新生效日期。

本项目作为「部落驿站」的继承项目继续整理升级数据。本地网站仅提供数据查询。

<style lang="scss">
@use '@/assets/mixins.scss' as *;

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

.homepage-countdown-cards {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    background: radial-gradient(ellipse at 50% 80%, rgba(135, 206, 235, 0.15), transparent);
}
.homepage-countdown-group {
    padding: 0.75rem;
    text-align: center;
}
.homepage-countdown-title {
    margin-bottom: 0.25rem;
    font-weight: 600;
}
.homepage-countdown-time {
    font-variant-numeric: tabular-nums;
}
.homepage-recommend {
    display: grid;
    grid-template-columns: minmax(0, 1fr);
    column-gap: 2rem;
}
.homepage-recommend-item, .homepage-attention {
    ul {
        margin-left: 1.5rem;
        padding-left: 0;

        &:last-child {
            margin-bottom: 0.5rem;
        }
    }
}
@media (min-width: $cp-col-tablat-big) {
    .homepage-countdown-cards {
        grid-template-columns: repeat(3, minmax(0, 1fr));
    }
    .homepage-recommend {
        grid-template-columns: repeat(2, minmax(0, 1fr));
    }
}
</style>
