---
title: "部落冲突 coc 超级炸弹人（超炸）升级数据"
navTitle: "超级炸弹人"
shownTitle: "超级炸弹人（超炸）"
module: upgrade-home
imgFolder: home_tech/0603
wiki: https://clashofclans.fandom.com/wiki/Super_Wall_Breaker
canonical: /upgrade/0603-Super-Wall-Breaker
dataSyncedOn: 2026-10-13
description: "谁能想到，脚踩炸弹滚出去比抱着它跑出去效果好这么多！超级炸弹人使用的是延时引信炸弹，无论什么情况它都会爆炸。拒绝哑弹！"
---

<script setup>
import SyncedUnitData from "@/customized/upgrade/SyncedUnitData.vue";
import unitData from "@/assets/unit-data/0603-Super-Wall-Breaker.json";
</script>

<SyncedUnitData :data="unitData" :historyAfter="'2025-11-17'">

<template #introduction>

- *如想查看该兵种的普通版本，请访问：[炸弹人](/upgrade/0004-Wall-Breaker)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Super_Wall_Breaker_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

1. 超级炸弹人的技能（超级炸弹）：一定会引爆的大号炸弹。也就是说如果超级炸弹人中途死亡，炸弹会就地爆炸。
2. 和 [普通炸弹人](/upgrade/0004-Wall-Breaker) 一样，超级炸弹人也是范围伤害，同样可以同时炸开两层连起来的墙。下图中画出来的所有 [城墙](/upgrade/0300-Walls) 都可以受到伤害。

<Pic src="/upgrade/description/Breaking_Walls_2.jpg" caption="超级炸弹人的伤害范围" :lazyLoading="false" maxWidth="10rem" width="284" height="228" />

3. 根据解析安装包的结果，超级炸弹人的攻速是一秒一次，也即每秒伤害等于每次伤害。但实际上它引爆炸弹后自身也会死亡，所以这个兵种不讨论攻速。下方所说的攻击伤害均为每次伤害。
4. 超级炸弹人的伤害分为主动伤害和死亡伤害。如果炸弹人成功爆破，则建筑受到炸弹人的主动伤害加死亡伤害；如果在爆破之前被打死，并且死亡伤害波及到了建筑，则建筑受到炸弹人的死亡伤害。
5. 即使超级炸弹人被 [弹簧](/upgrade/0381-Spring-Trap) 弹飞，炸弹仍然可以爆炸，满级超级炸弹人的死亡伤害可以直接炸掉最高级城墙。
6. [狂暴法术](/upgrade/0102-Rage-Spell) 只对主动伤害有效，对死亡伤害无效。
7. [大守护者](/upgrade/0202-Grand-Warden) 的 [永恒书卷](/upgrade/0780-Eternal-Tome) 装备无法让超级炸弹人攻击后存活。
8. 2020 年 10 月更新后，对超级炸弹人而言，[弹跳法术](/upgrade/0103-Jump-Spell) 覆盖的城墙，等价于城墙消失。
9. 超级炸弹人的寻路机制和普通炸弹人一样。
10. 部分高本玩家会用“炸弹人”指代超级炸弹人，而非普通炸弹人，在看解说视频的时候需要注意一下。

\* 5 - 6 级超级炸弹人只在 奖章活动 中出现，不能通过常规方式得到。

注意：

- 上方的“面板伤害”解释："78/175"表示主动伤害为 78，死亡伤害为 175。
- 上方的“中途死亡”指的是超级炸弹人中途死亡的爆炸伤害，“成功爆破”指的是超级炸弹人成功自爆的伤害。 成功爆破的伤害是两个面板伤害加起来，再算上对城墙的 40 倍伤害。

</template>

<template #history>

<Timeline>
    <TimelineItem date="2025/11/17">
        <TimelineRow>18 本推出，并在 18 本新增 14 级炸弹人，超级部队的等级也相应更新。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/27">
        <TimelineRow>部队的训练时间取消，但增加了捐赠费用。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>17 本推出，并在 17 本新增 13 级炸弹人，超级部队的等级也相应更新。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>16 本推出，并在 16 本新增 12 级炸弹人，超级部队的等级也相应更新。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>15 本推出，并在 15 本新增 11 级炸弹人，超级部队的等级也相应更新。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/06/27">
        <TimelineRow>为配合城墙的生命值调整，7 ~ 9 级超级炸弹人被摧毁时造成的伤害也一起降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>14 本推出，并在 14 本新增 10 级炸弹人，超级部队的等级也相应更新。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/12/07">
        <TimelineRow>超级部队的有效时间从 7 天缩短为 3 天。</TimelineRow>
        <TimelineRow>所有部队的强化费用统一调整为 25,000 暗黑重油。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/05/20">
        <TimelineRow>超级炸弹人的炸弹爆炸范围从 2 格缩小至 1.6 格。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/03/30">
        <TimelineRow>部落冲突新增“超级兵种”玩法，超级炸弹人是首批推出的超级兵种之一。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>

</template>

</SyncedUnitData>
