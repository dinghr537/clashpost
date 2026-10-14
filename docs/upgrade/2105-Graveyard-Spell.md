---
title: "部落冲突 coc 都城骷髅召唤法术升级数据"
navTitle: "骷髅召唤法术"
shownTitle: "骷髅召唤法术"
module: upgrade-capital
imgFolder: capital_tech/2105
wiki: https://clashofclans.fandom.com/wiki/Graveyard_Spell
canonical: /upgrade/2105-Graveyard-Spell
dataSyncedOn: 2026-10-13
description: "可怕的魔法让这个法术有了起死回生的魔力！战场上的部队阵亡后，骷髅召唤法术将召唤一定数量的骷髅兵，具体数量取决于阵亡部队的所需空间。如果飞行部队阵亡，则会召唤出飞行骷髅兵。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/2105-Graveyard-Spell.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2023-09-14'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Graveyard_Spell_info.png" :imgAlt="$frontmatter.navTitle"
    description="可怕的魔法让这个法术有了起死回生的魔力！<br>战场上的部队阵亡后，骷髅召唤法术将召唤一定数量的骷髅兵，具体数量取决于阵亡部队的所需空间。如果飞行部队阵亡，则会召唤出飞行骷髅兵。"
    :isSmallImg="true" />

<SmallTitle>重要说明</SmallTitle>

1. 当骷髅公园这个子城的大本营升到 2 级，系统会自动建造 [骷髅召唤法术工厂](/upgrade/2385-Graveyard-Spell-Factory)，建造完成后即解锁骷髅召唤法术。
2. 骷髅召唤法术可以在部队被打死之后生成骷髅，三个人口折合一个骷髅。攻击部队和防御部队都计入总数，产生的骷髅类型取决于死了的部队是哪种类型，地面部队产生地面骷髅，空中部队产生空中骷髅。
3. 死亡的地面部队和空中部队是分开计算的，比如说你打死了 5 人口的地面单位和 10 人口的空中单位，则只会生成 1 个地面骷髅和 3 个空中骷髅，一共生成 4 个骷髅，而不是 5 个。
4. 计算人口时需使用“防守人口”，而非“配兵人口”，相关数据在对应的兵种页面能看到。
5. 地面的骷髅携带盾牌，可以至少承受两次攻击，类似于家乡的骷髅法术召唤出来的骷髅。此外，空中的骷髅类似于家乡的骷髅陷阱中的对空骷髅，空中的骷髅移动速度更快，并且可以瞄准空中单位。
6. 如果生成的骷髅被障碍物阻挡或者离陆地太远，则骷髅不会生成。未能生成的骷髅也会计入总数，并受上限影响。

\* 骷髅召唤法术每次进攻都可以召唤这么多骷髅，因此两次进攻最多可召唤的数量就是上述数据乘以 2.

</template>

<template #history>

<Timeline>
    <TimelineItem date="2023/09/14">
        <TimelineRow>2 ~ 4级骷髅召唤法术召唤的骷髅兵数量从 25/29/32 减少至 24/27/29.</TimelineRow>
        <TimelineRow>将触发陷阱所需的骷髅数量从 1 个增加到 2.</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/01/23">
        <TimelineRow>骷髅召唤法术召唤的骷髅兵数量从 23/27/31/35 减少至 21/25/29/32.</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/12/21">
        <TimelineRow>骷髅召唤法术生成的骷髅数量从 30/33/36/39 降低至 23/27/31/35.</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/12/12">
        <TimelineRow>新法术：骷髅召唤法术。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
