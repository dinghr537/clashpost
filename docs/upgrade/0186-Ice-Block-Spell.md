---
title: "部落冲突 coc 冰障法术升级数据"
navTitle: "冰障法术"
shownTitle: "冰障法术"
module: upgrade-home
imgFolder: home_tech/0186
wiki: https://clashofclans.fandom.com/wiki/Ice_Block_Spell
canonical: /upgrade/0186-Ice-Block-Spell
dataSyncedOn: 2026-10-13
description: "冻得结结实实，绝对安全！利用此冷冻合剂将您的地面与空中部队包裹在冰块中，几乎可以抵挡所有伤害，但同时会冻结他们的移动与攻击！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0186-Ice-Block-Spell.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-06-19'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Ice_Block_Spell_info.png" :imgAlt="$frontmatter.navTitle"
    description="冻得结结实实，绝对安全！<br>利用此冷冻合剂将您的地面与空中部队包裹在冰块中，几乎可以抵挡所有伤害，但同时会冻结他们的移动与攻击！" />

<SmallTitle>重要说明</SmallTitle>

1. 冰障法术会暂时冻结部队，让部队无法攻击和移动，被冻结的部队在此期间会获得减伤效果。
    - 冰障法术对敌方单位无效。
    - 冰障法术的定身及减伤效果只对法术释放时在法术范围内的部队有效，对法术释放后进入范围的部队无效。
    - 冰障法术对攻城机器无效。
    - 冰障法术对释放法术时位于地下的部队（例如 [掘地矿工](/upgrade/000b-Miner)）无效。但如果掘地矿工在法术释放时位于地面，则会受到影响。
2. 冰障法术的作用是冻结我方部队，让我方部队获得减伤效果，而 [冰冻法术](/upgrade/0104-Freeze-Spell) 的作用是冻结敌方单位，停止敌方的移动和攻击。两者的作用不同，不要混淆。
3. 冰障法术的减伤效果不能与 [巨型手套](/upgrade/0704-Giant-Gauntlet)、[永恒书卷](/upgrade/0780-Eternal-Tome) 等单位的减伤效果直接叠加，只能取最高的减伤效果。
4. 被冻结的部队会受到 [空气炮](/upgrade/0306-Air-Sweeper)、[飓风陷阱](/upgrade/0386-Tornado-Trap) 等单位的位移效果影响，会被带着移动。
5. 即使 [戈仑石人](/upgrade/0083-Golem)、[熔岩猎犬](/upgrade/0085-Lava-Hound)、[大雪怪](/upgrade/000d-Yeti) 这类会生成派生单位的兵种已经被冻结，它们也可以正常生成派生单位，且新生成的单位不会被冻结。
6. 冰障法术对 [蝙蝠法术](/upgrade/0184-Bat-Spell) 和 [骷髅法术](/upgrade/0183-Skeleton-Spell) 生成的部队有效，即使是新生成的单位也会被冻结。
7. 即使 [烈焰熔炉](/upgrade/008b-Furnace) 被冰障法术冻结，它也可以分裂出部队。
8. 在冻结期间，[德鲁伊](/upgrade/008a-Druid) 的变身计时器不会停止。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/06/19">
        <TimelineRow>新法术：冰障法术，14 本可解锁，共推出 5 个等级。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
