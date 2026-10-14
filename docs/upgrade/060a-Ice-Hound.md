---
title: "部落冲突 coc 寒冰猎犬（冰狗）升级数据"
navTitle: "寒冰猎犬"
shownTitle: "寒冰猎犬（冰狗）"
module: upgrade-home
imgFolder: home_tech/060a
wiki: https://clashofclans.fandom.com/wiki/Ice_Hound
canonical: /upgrade/060a-Ice-Hound
dataSyncedOn: 2026-10-13
description: "摆脱了熔岩引起的消化不良后，寒冰猎犬准备冻结敌军村庄。冷静点，否则......"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/060a-Ice-Hound.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2026-02-23'">

<template #introduction>

- *如想查看该兵种的普通版本，请访问：[熔岩猎犬](/upgrade/0085-Lava-Hound)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Ice_Hound.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

1. 寒冰猎犬的技能（奇冰制胜）：寒冰猎犬和迷你寒冰猎犬的攻击会让敌军和防御减速，寒冰猎犬被消灭后会冻结附近的一切。
2. 寒冰猎犬和迷你寒冰猎犬的普通攻击与 [冰冻法术](/upgrade/0104-Freeze-Spell) 不同，不能把敌方部队和建筑完全冻住，只是有一个减速效果。
3. 寒冰猎犬死亡后的冰冻效果与冰冻法术类似，可以把敌方部队和建筑完全冻住。
4. 寒冰猎犬的普通攻击和死亡冰冻效果和 [戈仑冰人](/upgrade/0087-Ice-Golem) 相同，只是冰冻时间不一样。

\* 寒冰猎犬有三段攻击偏好。场上有防空火箭时攻击 [防空火箭](/upgrade/0304-Air-Defense)，没有防空火箭时攻击其他防御建筑，没有防御建筑时攻击非防御建筑。

\* 1 - 4 级寒冰猎犬只在 奖章活动 中出现，不能通过常规方式得到。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2026/02/23">
        <TimelineRow>在 18 本新增 8 级熔岩猎犬，超级部队的等级也相应更新。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/06/16">
        <TimelineRow>1 级寒冰猎犬的死亡冰冻时间由 3.5 秒提升到 3.75 秒。</TimelineRow>
        <TimelineRow>在 16 本新增 7 级熔岩猎犬，超级部队的等级也相应更新。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/27">
        <TimelineRow>部队的训练时间取消，但增加了捐赠费用。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>迷你熔岩猎犬、迷你寒冰猎犬和迷你熔岩气球犬占用的人口数由 2 调整为 1.</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/02/10">
        <TimelineRow>寒冰猎犬的训练时间由 6:40 改为 5:47</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>6 级寒冰猎犬防守时分裂出的迷你寒冰猎犬的数量减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/05/02">
        <TimelineRow>家乡所有空军的攻击距离减少 0.5 格（超级飞龙除外，这玩意削了 1 格）。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>如果熔岩猎犬和寒冰猎犬在选择目标时，场上剩余的防空火箭都被隐形了，它们不会忘记锁定之前没有看到的防空火箭。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/12/07">
        <TimelineRow>新超级兵：寒冰猎犬。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
