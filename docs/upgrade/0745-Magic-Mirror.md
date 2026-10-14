---
title: "部落冲突 coc 克隆魔镜（复制魔镜）装备升级数据"
navTitle: "克隆魔镜"
shownTitle: "克隆魔镜（复制魔镜）"
module: upgrade-home
imgFolder: home_heroes/0745
wiki: https://clashofclans.fandom.com/wiki/Magic_Mirror
canonical: /upgrade/0745-Magic-Mirror
dataSyncedOn: 2026-10-13
description: "克隆魔镜弓箭女皇的第二件史诗装备，它在 2024 年 8 月 7 日的镜像克隆神技活动中首次亮相，并在 8 月 9 日的动漫与部落活动中开放购买。带上克隆魔镜装备后，使用技能时会召唤女王的临时分身并使女王本体隐形一秒。"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0745-Magic-Mirror.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2024-11-25'">

<template #introduction>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Magic_Mirror_info.png" :imgAlt="$frontmatter.navTitle" description="召唤弓箭女皇的克隆体。" />

<SmallTitle>说明</SmallTitle>

1. 克隆魔镜是 [弓箭女皇](/upgrade/0201-Archer-Queen) 的第二件史诗装备，它在 2024 年 8 月 7 日的镜像克隆神技活动中首次亮相，并在 8 月 9 日的动漫与部落活动中首次开放购买。
2. 带上克隆魔镜装备后，使用技能时会召唤女王的临时分身并使女王本体隐形一秒。
    - 克隆体的生命值只与装备等级有关，与女王等级无关。
    - 无论装备等级是多少，游戏内显示的克隆体等级都显示为本体等级。
3. 另外，克隆魔镜还能增加女王的生命值与使用技能时恢复的生命值。
4. 将克隆魔镜与其他装备搭配时，其他装备的效果只对女王本体有效 ，对克隆体无效。比如说：
    - 将克隆魔镜与 [隐形药水瓶](/upgrade/0741-Invisibility-Vial) 搭配时，女王本体的隐形时间会被延长至隐形药水瓶的隐形时间，而克隆体完全不会隐形。
    - 将克隆魔镜与 [冰冻箭矢](/upgrade/0744-Frozen-Arrow) 搭配时，只有女王本体射出的箭有冰冻效果，克隆体射出的箭没有。
5. 女王的克隆体会被游戏视为英雄，具体表现为：
    - [疗伤法术](/upgrade/0101-Healing-Spell) 和 [天使](/upgrade/0007-Healer) 对克隆体的治疗效果会遵循英雄的治疗衰减机制。
    - 在使用 [回溯法术](/upgrade/0107-Recall-Spell) 时，女王的克隆体为 25 单位。
    - 女王的克隆体属于 [英雄猎手](/upgrade/0088-Headhunter) 的优先攻击目标。

注：如果升级费用中有多种资源，则同时需要多种资源才能升级。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2024/11/25">
        <TimelineRow>现在 8 本就可以解锁弓箭女皇了，该页面的部分信息需要同步更改。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/08/08">
        <TimelineRow>新装备：克隆魔镜。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
