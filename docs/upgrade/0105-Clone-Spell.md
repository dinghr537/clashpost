---
title: "部落冲突 coc 镜像法术（克隆法术）升级数据"
navTitle: "镜像法术"
shownTitle: "镜像法术（克隆法术）"
description: "使用镜像法术复制出一批奇袭部队！镜像法术将会在施放地点生成一个圆形光环，任何进入光环的部队都会被复制，被复制部队的存活时间有限。复制的部队单位达到其单位上限时，镜像法术将会失效。"
module: upgrade-home
imgFolder: home_tech/0105
wiki: https://clashofclans.fandom.com/wiki/Clone_Spell
canonical: /upgrade/0105-Clone-Spell
dataSyncedOn: 2026-10-13
---

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Clone_Spell.png" :imgAlt="$frontmatter.navTitle"
    description="使用镜像法术复制出一批奇袭部队！<br>镜像法术将会在施放地点生成一个圆形光环，任何进入光环的部队都会被复制，被复制部队的存活时间有限。复制的部队单位达到其单位上限时，镜像法术将会失效。"
    :isSmallImg="true" />

<SmallTitle>重要说明</SmallTitle>

1. 镜像法术按圈内单位在战场上出现的先后顺序逐个复制，剩余人口不足以复制的单位会被跳过。一轮结束后，若仍有容量便开始下一轮；新进入范围的单位从下一轮开始参与复制。复制人口用尽时光环提前结束，多瓶镜像的容量分别计算。<small>（来源：<a href="https://clashpost.com/p/2211" target="_blank" rel="noopener noreferrer">原站镜像机制研究（2025-07-03 修订）</a>）</small>
2. 镜像法术对我方英雄、战宠和攻城机器无效。

<SmallTitle>属性</SmallTitle>

<UnitProperties>
    <UnitProperty pKey="作用半径" pValue="3.5 格" />
    <UnitProperty pKey="作用类型" pValue="复制部队" />
    <UnitProperty pKey="作用目标" pValue="我方部队" />
    <UnitProperty pKey="法术持续时间" pValue="18 秒" />
    <UnitProperty pKey="复制间隔" pValue="0.3 秒" />
    <UnitProperty pKey="复制出的军队有效时间" pValue="30 秒" />
    <UnitProperty pKey="占用的法术空间" pValue="3" />
    <UnitProperty pKey="所需法术工厂等级" pValue="5" />
    <UnitProperty pKey="所需大本等级" pValue="10" />
    <UnitProperty pKey="法术配置时间" pValue="无" trainingSystem="2025" />
    <UnitProperty pKey="捐赠费用" pValue="9,9,27000,Elixir" :isDonationCost="true" />
</UnitProperties>

<SmallTitle>升级数据</SmallTitle>

<script setup>
const tableExtraInfo = [
    {
        "column": 2,
        "type": "cost",
        "gpClass": "research",
        "icon": "Elixir"
    },
    {
        "column": 3,
        "type": "time",
        "gpClass": "research"
    }
];
</script>

<UnitTable :tableExtraInfo="tableExtraInfo">

| 等级 |最大复制<br>人口数| 升级花费 | 升级时间 |所需<br>实验室等级| 所需大本等级 |
| ---- |       ----     |   ----   |  ----   |       ----     |     ----    |
| 1 | 22 | \ | \ | 1 | 10 |
| 2 | 24 | 1500000 | 1,0,0,0 | 8 | 10 |
| 3 | 26 | 2500000 | 2,0,0,0 | 8 | 10 |
| 4 | 28 | 3000000 | 2,6,0,0 | 9 | 11 |
| 5 | 30 | 4000000 | 2,12,0,0 | 9 | 11 |
| 6 | 34 | 5000000 | 4,0,0,0 | 11 | 13 |
| 7 | 38 | 8000000 | 5,0,0,0 | 12 | 14 |
| 8 | 42 | 9000000 | 7,0,0,0 | 13 | 15 |
| 9 | 48 | 26000000 | 13,12,0,0 | 16 | 18 |
</UnitTable>

<SmallTitle>更新历史</SmallTitle>

<Timeline>
    <TimelineItem date="2026/04/27">
        <TimelineRow>新增 9 级镜像法术。 <a href="https://clashofclans.fandom.com/wiki/Clone_Spell#History" target="_blank" rel="noopener noreferrer">来源</a></TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/27">
        <TimelineRow>法术的配置时间取消，但新增了捐赠费用。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>4 ~ 5、7 ~ 8 级镜像法术的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>2 ~ 8 级镜像法术的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/18">
        <TimelineRow>6 ~ 8 级镜像法术的升级时间减少。</TimelineRow>
        <TimelineRow>7 ~ 8 级镜像法术的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>3 ~ 8 级镜像法术的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>15 本新增 8 级镜像法术。</TimelineRow>
        <TimelineRow>6 级镜像法术的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>2 ~ 6 级镜像法术的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/06/27">
        <TimelineRow>1 ~ 4 级镜像法术可复制的部队人口数增加。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/12/09">
        <TimelineRow>2 ~ 6 级镜像法术的升级费用降低。</TimelineRow>
        <TimelineRow>2 ~ 5 级镜像法术的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>14 本推出，并在 14 本新增 7 级镜像法术。</TimelineRow>
        <TimelineRow>6 级镜像法术可复制的部队单位从 33 提高到 34。</TimelineRow>
        <TimelineRow>2 ~ 5 级镜像法术的升级费用降低。</TimelineRow>
        <TimelineRow>2 ~ 3 级镜像法术的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/06/22">
        <TimelineRow>13 本新增 6 级镜像法术。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>
<p><small>数值核对：2026-10-13 · <a href="https://clashofclans.fandom.com/wiki/Clone_Spell?oldid=622840" target="_blank" rel="noopener noreferrer">部落冲突维基</a>。部分附加字段沿用原记录。</small></p>
