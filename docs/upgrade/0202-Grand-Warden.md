---
title: "部落冲突 coc 大守护者（咏王）升级数据"
navTitle: "大守护者"
shownTitle: "大守护者（咏王）"
module: upgrade-home
imgFolder: home_heroes/0202
wiki: https://clashofclans.fandom.com/wiki/Grand_Warden
canonical: /upgrade/0202-Grand-Warden
dataSyncedOn: 2026-10-13
description: "大守护者是一位强大的魔法大师，他会用手中的法杖支援进攻部队。他可以跳过城墙或和空中部队一样飞翔，因此可以为任何进攻部队提供帮助。防守时，他将变成一座强大的防御塔。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0202-Grand-Warden.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2026-02-23'">

<template #introduction>

- *如想查看守护者学徒，请访问：[守护者学徒](/upgrade/0089-Apprentice-Warden)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Grand_Warden_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

1. 无论你使用了地面还是飞行模式，大守护者都可以无视城墙。
    - 防守时，大守护者始终处于地面模式。
2. 2024 年 11 月更新后，大守护者防守时不再变成雕像，而是会和其他英雄一样走动。
3. 下方的数据均为不含装备的数据。
4. 英雄在防守时没有装备。

攻击距离：地面模式为 7 格，空中模式进攻时约 6.6 格。注意：6.6 这个数据是玩家自行测试得到的，并非官方数据。<br>
搜索半径：如果敌军进入这个范围，英雄会奔向敌军，并进行反击。<br>
巡逻半径：在没有敌人的情况下，英雄也会走动，而这个走动的范围叫巡逻半径。<br>
光环半径：这个光环半径是诸多装备的有效范围。

下表中的生命值恢复量是基础属性，与装备无关。即使没有装备，开技能也会回血。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2026/02/23">
        <TimelineRow>21 ~ 25、36 ~ 40、46 ~ 55 级大守护者的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/11/17">
        <TimelineRow>18 本推出，并在 18 本新增 76 ~ 80 级大守护者。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/10/06">
        <TimelineRow>现在 14 级大本营即可解锁 56 ~ 60 级大守护者。</TimelineRow>
        <TimelineRow>10、26 ~ 70 级大守护者的升级时间减少。</TimelineRow>
        <TimelineRow>21 ~ 64 级大守护者的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/27">
        <TimelineRow>取消英雄的恢复时间，现在英雄可以像战宠一样瞬间恢复。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>英雄的升级操作被整合进英雄殿堂，取消王座，同时引入英雄栏位和战旗的概念。</TimelineRow>
        <TimelineRow>英雄不再拥有警戒半径，遇到敌人后头顶不会冒问号，而是直接反击。</TimelineRow>
        <TimelineRow>在 17 本新增 71 - 75 级大守护者。</TimelineRow>
        <TimelineRow>11 ~ 60 级大守护者的升级时间减少。</TimelineRow>
        <TimelineRow>1 级大守护者的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/18">
        <TimelineRow>5 ~ 10、12 ~ 55 级大守护者的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>16 本推出，同时在 16 本新增 66 ~ 70 级大守护者。</TimelineRow>
        <TimelineRow>所有等级大守护者的每秒伤害和生命值降低。</TimelineRow>
        <TimelineRow>所有等级的升级时间和升级成本降低。</TimelineRow>
        <TimelineRow>废除原来的技能系统，用装备系统代替。</TimelineRow>
        <TimelineRow>现在所有英雄开启技能后都会回血了。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>15 本新增 61 ~ 65 级大守护者。</TimelineRow>
        <TimelineRow>大守护者现在不太会跟随野蛮人和弓箭手了。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/05/15">
        <TimelineRow>在重新部署召回的大守护者时，大守护者将重新计算跟随军队。</TimelineRow>
        <TimelineRow>增加雷霆泰坦的「大守护者权重」，让大守护者更有可能跟随他们。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>15 本推出，并在 15 本新增 56 ~ 60 级大守护者。</TimelineRow>
        <TimelineRow>2 ~ 55 级大守护者的升级费用减少。</TimelineRow>
        <TimelineRow>6 ~ 50 级大守护者的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/02/15">
        <TimelineRow>英雄引入额外生命值概念，战斗时先消耗额外生命值再消耗本身的生命值，也就是说你可以连续打两场。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/12/09">
        <TimelineRow>1 ~ 20，22 ~ 40 级大守护者的升级花费降低。</TimelineRow>
        <TimelineRow>2 ~ 15 级大守护者的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/29">
        <TimelineRow>降低了大守护者跟随战宠的几率。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>现在英雄可以搭配战宠了。</TimelineRow>
        <TimelineRow>14 本推出，并在 14 本新增 51 ~ 55 级大守护者。</TimelineRow>
        <TimelineRow>修复了其他友军都没攻打城墙的情况下，大守护者会去攻打城墙的问题。</TimelineRow>
        <TimelineRow>如果在大守护者受到伤害的同时激活永恒书卷技能，他可以免疫伤害，不会再出现一个黑雷把血炸空的同时开大的情况了。</TimelineRow>
        <TimelineRow>1 ~ 10 级大守护者的升级花费降低。</TimelineRow>
        <TimelineRow>2 ~ 8 级大守护者的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/01/20">
        <TimelineRow>大守护者降低跟随攻城滚木车和攻城飞艇的优先级，以减少他跟随这两种攻城机器冲向敌方大本营并陷入危险的几率。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/12/07">
        <TimelineRow>战斗结束时，如果英雄的技能尚未使用，英雄会自动恢复一部分生命值（数值等于他们使用技能时可恢复的生命值）。这样就缩短了英雄的冷却时间，让他们可以更快投入下一场战斗！</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/10/12">
        <TimelineRow>更新后，英雄会一直处于防御状态，而且在进行防御后会自动恢复为满血状态。“正在防御”和“正在休息”两种模式间的切换功能已被移除。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/06/22">
        <TimelineRow>所有等级大守护者的恢复时间减少。</TimelineRow>
        <TimelineRow>优化了大守护者的机制，现在他在空中模式时能更有效地跟随部队，不会那么容易分心。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/05/20">
        <TimelineRow>调整大守护者的 AI，降低跟随飞龙和皮卡超人的优先级。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/03/30">
        <TimelineRow>调整了大守护者 AI，让他在友军被冻住时反应更合理；如果没有跟随任何友军，他会更频繁地重新选择目标。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/12/09">
        <TimelineRow>13 本推出，并在 13 本新增 41 ~ 50 级大守护者。</TimelineRow>
        <TimelineRow>进攻时，如果英雄技能一直没有被手动开启，英雄在即将被击败时会自动开启英雄技能进行自救。该功能可以在“设置>更多设置”中关闭。</TimelineRow>
        <TimelineRow>如果大守护者在攻击城墙，而他附近的友军全部阵亡，系统将强制他更换目标。</TimelineRow>
        <TimelineRow>略微降低大守护者跟随熔岩猎犬的倾向。</TimelineRow>
        <TimelineRow>大守护者攻击时发射的光束将更像是从法杖射出的，而不是腹部。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/06/18">
        <TimelineRow>12 本新增 31 ~ 40 级大守护者。</TimelineRow>
        <TimelineRow>为了让英雄可以穿上皮肤，继蛮王和女王之后，本次更新之后大守护者也改成了 3D 模型。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
