---
title: "部落冲突 coc 扫帚女巫升级数据"
navTitle: "扫帚女巫"
shownTitle: "扫帚女巫"
module: upgrade-temp
imgFolder: temp_troops/0e13
wiki: https://clashofclans.fandom.com/wiki/Broom_Witch
canonical: /upgrade/0e13-Broom-Witch
dataSyncedOn: 2026-10-13
description: "一名见习女巫，她会在战场上飞来飞去，召唤女巫精灵。她特别不喜欢那些站在塔上的傲慢法师。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0e13-Broom-Witch.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-08-11'">

<template #introduction>

<SwitchTabs contentClass="cp-unit-items" :stickyTabs="true" :pageTabs="true">
    <SwitchTab tabId="cp-unit-item-0" :activeTab="true">扫帚女巫</SwitchTab>
    <SwitchTab tabId="cp-unit-item-1">女巫精灵</SwitchTab>
</SwitchTabs>

<SwitchTabGroup id="cp-unit-item-0" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Broom_Witch_info.png" :imgAlt="$frontmatter.navTitle"
    description="一名见习女巫，她会在战场上飞来飞去，召唤女巫精灵。她特别不喜欢那些站在塔上的傲慢法师。" />

<SmallTitle>重要说明</SmallTitle>

1. 扫帚女巫是动漫与部落活动中的两个临时兵种之一，在活动中获取 3 000 魔法水晶（任务点数）即可解锁该兵种。它在 2025 年 8 月返场一次。
2. 与大雪怪类似，扫帚女巫在受到伤害时可分裂出女巫精灵。
3. 与熔岩猎犬类似，扫帚女巫有三段攻击偏好。当场上有法师塔时优先攻击法师塔，没有法师塔时优先攻击防御建筑，没有防御建筑时才攻击其他建筑、敌方英雄和援军。

</SwitchTabGroup>

<SwitchTabGroup id="cp-unit-item-1" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Witch_Spirit.png" imgAlt="扫帚女巫召唤的精灵"
    description="这些淘气的小火花看起来很可爱，但可以对附近的防御造成大量伤害。"
    :isSmallImg="true" />

<SmallTitle>重要说明</SmallTitle>

与小雪怪类似，女巫精灵攻击一次后就会死亡，[大守护者](/upgrade/0202-Grand-Warden) 的 [永恒书卷](/upgrade/0780-Eternal-Tome) 装备也无法阻止。

占据人口：在考虑女巫精灵与 [隐形弹簧](/upgrade/0381-Spring-Trap)、[镜像法术](/upgrade/0105-Clone-Spell) 或 [回溯法术](/upgrade/0107-Recall-Spell) 的相互作用时，女巫精灵应被视为 1 人口。<br>
攻击时机：根据解析安装包的结果，女巫精灵的攻击速度是一秒一次，但实际上女巫精灵的首次攻击时机为到达目标后 0.5 秒，且攻击一次后就会死亡，因此其攻速值无意义。

</SwitchTabGroup>

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/08/11">
        <TimelineRow>该兵种第 2 次推出，有效期至 2025/08/19.</TimelineRow>
        <TimelineRow>与上次推出时相比，6 - 7 本的扫帚女巫略微加强。</TimelineRow>
        <TimelineRow>与上次推出时相比，6 本的女巫精灵略微加强。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/08/08">
        <TimelineRow>该兵种第 1 次推出，有效期至 2024/08/31.</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
