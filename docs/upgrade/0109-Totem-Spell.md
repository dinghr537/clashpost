---
title: "部落冲突 coc 图腾法术升级数据"
navTitle: "图腾法术"
shownTitle: "图腾法术"
module: upgrade-home
imgFolder: home_tech/0109
wiki: https://clashofclans.fandom.com/wiki/Totem_Spell
canonical: /upgrade/0109-Totem-Spell
dataSyncedOn: 2026-10-13
description: "嘿，看那边！施放图腾法术吸引地面和空中防御的火力。附近的敌人会优先攻击图腾，从而减轻其他友方部队的压力。图腾由高密度的宇宙巨石锻造而成，落地时还会对区域内的目标造成伤害与击晕效果。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0109-Totem-Spell.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2026-02-23'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Totem_Spell_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

1. 图腾法术部署后会生成一个图腾（看起来像一根棍子），能击晕敌方建筑和部队，并使它们重置攻击目标。
    - 重置效果并不会使敌方建筑强制攻击图腾，如果我方其他单位与敌方建筑的距离比图腾与该建筑的更近，该建筑会攻击其他单位，而非图腾。
    - 图腾法术无法对城墙造成伤害。
2. 图腾是地面部队的同时，也是空中部队。因此，只攻击地面目标、只攻击空中目标和攻击地面和空中目标的防守方建筑、部队也会攻击图腾。
3. 图腾法术无法触发陷阱、法术塔及引出部落城堡内的部队。
    - 如果其他部队触发了陷阱，图腾仍会受到除了位移效果外的影响。
4. [镜像法术](/upgrade/0105-Clone-Spell)、[回溯法术](/upgrade/0107-Recall-Spell)、[冰障法术](/upgrade/0186-Ice-Block-Spell) 无法对图腾造成影响。
5. 虽然 [治疗法术](/upgrade/0101-Healing-Spell) 能治疗图腾，但是图腾不会被 [天使](/upgrade/0007-Healer) 和 [德鲁伊](/upgrade/008a-Druid) 锁定。
6. 图腾被计作 20 人口，可以用作 [暗黑王冠](/upgrade/0724-Dark-Crown) 的人口计算，也可以免疫 [隐形弹簧](/upgrade/0381-Spring-Trap) 的**弹飞**效果。但是，对于 [天鹰火炮](/upgrade/030b-Eagle-Artillery)，图腾法术与其他 1 单位的法术一样只会计作 5 人口。
7. [大守护者](/upgrade/0202-Grand-Warden) 的 [永恒书卷](/upgrade/0780-Eternal-Tome) 装备不能令图腾免疫伤害。
8. 2026/02 更新后，图腾落地时不能对地方建筑和部队造成伤害了，但游戏内的简介仍然保留了相关表述。本页暂时采用官方表述。

\* 这是图腾不受到伤害时的掉血速度。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2026/02/23">
        <TimelineRow>图腾的有效半径由 6 格改为 5 格。</TimelineRow>
        <TimelineRow>图腾落地时不能对地方建筑和部队造成伤害了。</TimelineRow>
        <TimelineRow>守护者学徒和生命宝石装备无法再给图腾施加加血效果了。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2026/01/12">
        <TimelineRow>图腾增加生命值衰减机制，每秒自动减少 334 生命值（类似于攻城训练营和攻城滚木车）。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/11/27">
        <TimelineRow>18 本推出，并在 16 本新增图腾法术。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
