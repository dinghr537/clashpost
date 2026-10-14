---
title: "部落冲突升级数据（临时单位）"
shownTitle: "升级数据"
description: "这里归档了部分《部落冲突》游戏数据，包括升级时间、资源消耗等内容，可供玩家查询和参考。本页面是部落冲突临时兵种的数据。"
module: upgrade-temp
canonical: /upgrade/category/temp
---

<script setup>
import ListItems from "@/customized/upgrade/ListItems.vue";
import ListItem from "@/customized/upgrade/ListItem.vue";
import { getCookie } from "@/assets/global/utils.js";

let activeTabIndex = 0;
const activeTabCookieValue = getCookie("cp-upgrade-active-tab");
if (activeTabCookieValue === "temp-troops") {
    activeTabIndex = 1;
} else if (activeTabCookieValue === "temp-others") {
    activeTabIndex = 2;
}
</script>

如需查看其他版块（家乡、夜世界、都城）的内容，请使用左侧菜单栏。

<SwitchTabs contentClass="cp-upgrade-item" :stickyTabs="true" :averageTabs="true" :pageTabs="true">
    <SwitchTab tabId="cp-upgrade-crafted"
        :activeTab="activeTabIndex === 0"
        upgradeCookieValue="temp-crafted">精工防御</SwitchTab>
    <SwitchTab tabId="cp-upgrade-temp-troops"
        :activeTab="activeTabIndex === 1"
        upgradeCookieValue="temp-troops">兵种</SwitchTab>
    <SwitchTab tabId="cp-upgrade-temp-others"
        :activeTab="activeTabIndex === 2"
        upgradeCookieValue="temp-others">其他</SwitchTab>
</SwitchTabs>

<SwitchTabGroup id="cp-upgrade-crafted" class="cp-upgrade-item">
    <ListItems title="2026 年 8 月批次（当前）" imgFolder="crafted_buildings">
        <ListItem name="蛋糕投掷器" imgSrc="/images/wiki/0909-Cake-A-Pult/75cd0aeeb2-Cake-A-Pult4.png" link="0909-Cake-A-Pult" />
        <ListItem name="英雄猎台" imgSrc="/images/wiki/090a-Hero-Hunter/0d883fe1c5-Hero_Hunter4.png" link="090a-Hero-Hunter" />
        <ListItem name="火热蜡烛" imgSrc="/images/wiki/090b-Hot-Candle/4449bd1e5e-Hot_Candle4-1.png" link="090b-Hot-Candle" />
    </ListItems>
    <ListItems title="2026 年 4—7 月批次（已结束）" imgFolder="crafted_buildings">
        <ListItem name="精工空中炸弹发射器" imgSrc="/images/wiki/0906-Crafted-Air-Bombs/b3ae94b629-Air_Bombs10_Crafted.png" link="0906-Crafted-Air-Bombs" />
        <ListItem name="精工熔岩发射器" imgSrc="/images/wiki/0907-Crafted-Lava-Launcher/434191ebcf-Lava_Launcher7_Crafted.png" link="0907-Crafted-Lava-Launcher" />
        <ListItem name="精工炙热熔炉" imgSrc="/images/wiki/0908-Crafted-Roaster/f6c5d978aa-Roaster10_Crafted.png" link="0908-Crafted-Roaster" />
    </ListItems>
    <ListItems title="2025 - 2026" imgFolder="temp_crafted">
        <ListItem name="钩索塔" imgSrc="0900/Hook_Tower4.png" link="0900-Hook-Tower" :lazyLoading="false" />
        <ListItem name="旋转喷火器" imgSrc="0901/Flame_Spinner4.png" link="0901-Flame-Spinner" :lazyLoading="false" />
        <ListItem name="碎岩迫击炮" imgSrc="0902/Crusher_Mortar4.png" link="0902-Crusher-Mortar" :lazyLoading="false" />
        <ListItem name="英雄警钟" imgSrc="0903/Hero_Bell4.png" link="0903-Hero-Bell" :lazyLoading="false" />
        <ListItem name="炸弹蜂巢" imgSrc="0904/Bomb_Hive4.png" link="0904-Bomb-Hive" :lazyLoading="false" />
        <ListItem name="圣光灯塔" imgSrc="0905/Light_Beam4.png" link="0905-Light-Beam" :lazyLoading="false" />
    </ListItems>
    <div class="cp-upgrade-index-tip">
        <SmallTitle>注意</SmallTitle>
        <ol>
            <li>小标题显示的年份以精工防御第一次推出时为准。</li>
            <li>当前批次与已结束批次分开展示；往期数据页会说明是否已重新同步来源。</li>
            <li>如想查看精制台的数据，请移步：<a href="/upgrade/048a-Crafting-Station">精制台</a>。</li>
        </ol>
    </div>
</SwitchTabGroup>

<SwitchTabGroup id="cp-upgrade-temp-troops" class="cp-upgrade-item">
    <ListItems title="2012 - 2021" imgFolder="temp_troops">
        <ListItem name="寒冰法师" imgSrc="0e00/Ice_Wizard_thumb.png" link="0e00-Ice-Wizard" />
        <ListItem name="野蛮人攻城槌" imgSrc="0e01/Battle_Ram_thumb.png" link="0e01-Battle-Ram" />
        <ListItem name="南瓜野蛮人" imgSrc="0e02/Pumpkin_Barbarian_thumb.png" link="0e02-Pumpkin-Barbarian" />
        <ListItem name="骷髅巨人" imgSrc="0e03/Giant_Skeleton_thumb.png" link="0e03-Giant-Skeleton" />
        <ListItem name="骷髅飞桶" imgSrc="0e04/Skeleton_Barrel_thumb.png" link="0e04-Skeleton-Barrel" />
        <ListItem name="艾尔普里莫" imgSrc="0e05/El_Primo_thumb.png" link="0e05-El-Primo" />
        <ListItem name="派对法师" imgSrc="0e06/Party_Wizard_thumb.png" link="0e06-Party-Wizard" />
        <ListItem name="皇家幽灵" imgSrc="0e07/Royal_Ghost_thumb.png" link="0e07-Royal-Ghost" />
    </ListItems>
    <ListItems title="2022 - 2024" imgFolder="temp_troops">
        <ListItem name="蛮羊骑士" imgSrc="0e08/Ram_Rider_thumb.png" link="0e08-Ram-Rider" />
        <ListItem name="野蛮箭手" imgSrc="0e09/Barcher_thumb.png" link="0e09-Barcher" />
        <ListItem name="野猪法师" imgSrc="0e0a/Hog_Wizard_thumb.png" link="0e0a-Hog-Wizard" />
        <ListItem name="熔岩气球" imgSrc="0e0b/Lavaloon_thumb.png" link="0e0b-Lavaloon" />
        <ListItem name="女巫戈仑" imgSrc="0e0c/Witch_Golem_thumb.png" link="0e0c-Witch-Golem" />
        <ListItem name="饼干皮卡" imgSrc="0e0d/C.O.O.K.I.E_thumb.png" link="0e0d-C.O.O.K.I.E" />
        <ListItem name="烟花炮手" imgSrc="0e0e/Firecracker_thumb.png" link="0e0e-Firecracker" />
        <ListItem name="驭水青龙" imgSrc="0e0f/Azure_Dragon_thumb.png" link="0e0f-Azure-Dragon" />
        <ListItem name="任意球野蛮人" imgSrc="0e10/Barbarian_Kicker_thumb.png" link="0e10-Barbarian-Kicker" />
        <ListItem name="边线球巨人" imgSrc="0e11/Giant_Thrower_thumb.png" link="0e11-Giant-Thrower" />
        <ListItem name="机甲超人" imgSrc="0e12/M.E.C.H.A_thumb.png" link="0e12-M.E.C.H.A" />
        <ListItem name="扫帚女巫" imgSrc="0e13/Broom_Witch_thumb.png" link="0e13-Broom-Witch" />
        <ListItem name="寒冰亡灵" imgSrc="0e14/Ice_Minion_thumb.png" link="0e14-Ice-Minion" />
    </ListItems>
    <ListItems title="2025 - 2026" imgFolder="temp_troops">
        <ListItem name="灵蛇飞桶" imgSrc="0e15/Snake_Barrel_thumb.png" link="0e15-Snake-Barrel" />
        <ListItem name="战吼狂人" imgSrc="0e16/YEETer_thumb.png" link="0e16-YEETer" />
        <ListItem name="霸天巨人" imgSrc="0e17/Giant_Giant_thumb.png" link="0e17-Giant-Giant" />
        <ListItem name="皮卡凯恩" imgSrc="0e18/K.A.N.E_thumb.png" link="0e18-K.A.N.E" />
        <ListItem name="铁臂终结者" imgSrc="0e19/Disarmer_thumb.png" link="0e19-The-Disarmer" />
        <ListItem name="收债哥布林" imgSrc="0e1a/Debt_Collector_thumb.png" link="0e1a-Debt-Collector" />
        <ListItem name="陨石戈仑" imgSrc="0e1b/Meteor_Golem_thumb.png" link="0e1b-Meteor-Golem" />
        <ListItem name="大象骑士" imgSrc="/images/wiki/0e1e-Elephant-Rider/948c93088a-Elephant_Rider_info.png" link="0e1e-Elephant-Rider" />
        <ListItem name="送葬者大雪怪" imgSrc="/images/wiki/0e1c-Yeti-Undertaker/904013a536-Yeti_Undertaker_info.png" link="0e1c-Yeti-Undertaker" />
        <ListItem name="图腾投手" imgSrc="/images/wiki/0e1d-Totem-Thrower/80c7cabc25-Totem_Thrower_info.png" link="0e1d-Totem-Thrower" />
    </ListItems>
    <div class="cp-upgrade-index-tip">
        <SmallTitle>注意</SmallTitle>
        <ol>
            <li>小标题显示的年份以临时单位第一次推出时为准。</li>
            <li>已同步页面采用来源当前表格；未重新核对的往期单位保留历史数据。来源同步日期不表示活动开放日期。</li>
            <li>临时兵种、法术无法升级，它的等级根据你的大本营等级自动确定。</li>
            <li>临时陷阱无法升级，不管玩家是几本，陷阱的属性都是一样的。</li>
            <li>临时兵种和法术无法捐赠给其他部落成员。</li>
        </ol>
    </div>
</SwitchTabGroup>

<SwitchTabGroup id="cp-upgrade-temp-others" class="cp-upgrade-item">
    <ListItems title="法术" imgFolder="temp_others">
        <ListItem name="圣诞奇袭" imgSrc="0e80/Santas_Surprise.png" link="0e80-Santas-Surprise" />
        <ListItem name="生日大爆炸" imgSrc="0e81/Birthday_Boom.png" link="0e81-Birthday-Boom" />
        <ListItem name="黄牌法术" imgSrc="0e83/Yellow_Card.png" link="0e83-Yellow-Card" />
        <ListItem name="袋装小冰怪" imgSrc="0e82/Bag_of_Frostmites.png" link="0e82-Bag-of-Frostmites" />
    </ListItems>
    <ListItems title="陷阱" imgFolder="temp_others">
        <ListItem name="南瓜炸弹" imgSrc="0f00/Pumpkin_Bomb.png" link="0f00-Pumpkin-Bomb" />
        <ListItem name="圣诞陷阱" imgSrc="0f01/Santa_Strike.png" link="0f01-Santa-Strike" />
        <ListItem name="冰冻陷阱" imgSrc="0f02/Freeze_Trap.png" link="0f02-Freeze-Trap" />
        <ListItem name="玲珑陷阱" imgSrc="0f03/Shrink_Trap.png" link="0f03-Shrink-Trap" />
    </ListItems>
    <div class="cp-upgrade-index-tip">
        <SmallTitle>注意</SmallTitle>
        <ol>
            <li>已同步页面采用来源当前表格；未重新核对的往期单位保留历史数据。来源同步日期不表示活动开放日期。</li>
            <li>临时兵种、法术无法升级，它的等级根据你的大本营等级自动确定。</li>
            <li>临时陷阱无法升级，不管玩家是几本，陷阱的属性都是一样的。</li>
            <li>临时兵种和法术无法捐赠给其他部落成员。</li>
        </ol>
    </div>
</SwitchTabGroup>

<style lang="scss">
.cp-upgrade-index-tip .cp-small-subtitle {
    margin: 0 0 1rem 0.125rem;
}

.cp-upgrade-crafted-building-available {
    background-color: var(--cp-success-bg-light);
}

.cp-theme-dark .cp-upgrade-crafted-building-available {
    background-color: var(--cp-success-bg-dark);
}
</style>
