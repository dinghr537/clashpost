---
title: "部落冲突 coc 夜世界狂暴野蛮人升级数据"
navTitle: "狂暴野蛮人"
shownTitle: "狂暴野蛮人"
description: "为什么野蛮人会狂暴不安、横冲直撞还满身戾气？没人敢去问他。也许是因为他找不到自己的剑了？"
module: upgrade-bh
imgFolder: bh_tech/1000
wiki: https://clashofclans.fandom.com/wiki/Raged_Barbarian
canonical: /upgrade/1000-Raged-Barbarian
dataSyncedOn: 2026-10-13
---

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Raged_Barbarian_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>各等级图片</SmallTitle>

<Panel>
    <UnitImgGroup :folder="$frontmatter.imgFolder">
        <UnitImg imgTitle="1 - 4 级" imgSrc="Raged_Barbarian1.png" />
        <UnitImg imgTitle="5 - 8 级" imgSrc="Raged_Barbarian5.png" />
        <UnitImg imgTitle="9 - 12 级" imgSrc="Raged_Barbarian9.png" />
        <UnitImg imgTitle="13 - 16 级" imgSrc="Raged_Barbarian13.png" />
        <UnitImg imgTitle="17 - 20 级" imgSrc="Raged_Barbarian17.png" />
    </UnitImgGroup>
</Panel>

<SmallTitle>狂暴野蛮人的属性</SmallTitle>

<UnitProperties>
    <UnitProperty pKey="部队类型" pValue="地面近战单位" />
    <UnitProperty pKey="攻击偏好" pValue="无" />
    <UnitProperty pKey="伤害类型" pValue="单体伤害" />
    <UnitProperty pKey="攻击的目标" pValue="仅地面目标" />
    <UnitProperty pKey="部队重量" pValue="4" />
    <UnitProperty pKey="移动速度" pValue="2.4 格/秒" />
    <UnitProperty pKey="攻击速度" pValue="0.8 秒/次" />
    <UnitProperty pKey="攻击距离" pValue="0.4 格" />
    <UnitProperty pKey="所需训练营等级" pValue="1" />
    <UnitProperty pKey="所需夜世界大本等级" pValue="2" />
</UnitProperties>

<SmallTitle>特殊技能的属性</SmallTitle>

<UnitProperties>
    <UnitProperty pKey="技能名称" pValue="野蛮狂暴" />
    <UnitProperty pKey="技能类型" pValue="被动技能" />
    <UnitProperty pKey="技能描述" pValue="部署后有狂暴效果" />
    <UnitProperty pKey="技能下速度提升" pValue="2 格/秒" />
    <UnitProperty pKey="技能下伤害提升" pValue="70%" />
</UnitProperties>

<SmallTitle>升级数据</SmallTitle>

<script setup>
const tableExtraInfo = [
    {
        "column": 6,
        "type": "cost",
        "gpClass": "research",
        "icon": "Elixir2"
    },
    {
        "column": 7,
        "type": "time",
        "gpClass": "research"
    }
];
</script>

<UnitTable :tableExtraInfo="tableExtraInfo">

| 等级 | 每秒伤害 | 每次伤害 |每个兵营的<br>部队数量|技能<br>狂暴时间|  生命值  | 升级花费 | 升级时间 |所需实验室和<br>大本营等级|
| ---- |   ---   |   ---   |         ---        |      ---       |   ---   |   ---   |    ---   |           ---          |
| 1 | 45 | 36 | 3 | \ | 500 | \ | \ | 1 |
| 2 | 45 | 36 | 3 | 6秒 | 500 | 3500 | 0,0,0,30 | 1 |
| 3 | 58 | 46.4 | 3 | 6秒 | 550 | 7000 | 0,0,5,0 | 2 |
| 4 | 58 | 46.4 | 3 | 8秒 | 550 | 10000 | 0,0,15,0 | 2 |
| 5 | 70 | 56 | 3 | 8秒 | 605 | 90000 | 0,5,0,0 | 3 |
| 6 | 70 | 56 | 4 | 8秒 | 605 | 180000 | 0,10,0,0 | 3 |
| 7 | 83 | 66.4 | 4 | 8秒 | 666 | 300000 | 0,15,0,0 | 4 |
| 8 | 83 | 66.4 | 4 | 10秒 | 666 | 330000 | 0,20,0,0 | 4 |
| 9 | 93 | 74.4 | 4 | 10秒 | 732 | 700000 | 1,0,0,0 | 5 |
| 10 | 93 | 74.4 | 4 | 12秒 | 732 | 900000 | 1,12,0,0 | 5 |
| 11 | 103 | 82.4 | 4 | 12秒 | 805 | 1000000 | 2,0,0,0 | 6 |
| 12 | 103 | 82.4 | 4 | 14秒 | 805 | 1200000 | 2,12,0,0 | 6 |
| 13 | 112 | 89.6 | 4 | 14秒 | 886 | 2000000 | 3,12,0,0 | 7 |
| 14 | 112 | 89.6 | 4 | 16秒 | 886 | 2200000 | 4,12,0,0 | 7 |
| 15 | 120 | 96 | 4 | 16秒 | 974 | 3000000 | 5,12,0,0 | 8 |
| 16 | 120 | 96 | 4 | 18秒 | 974 | 3200000 | 5,12,0,0 | 8 |
| 17 | 128 | 102.4 | 4 | 18秒 | 1072 | 3800000 | 6,0,0,0 | 9 |
| 18 | 128 | 102.4 | 4 | 20秒 | 1072 | 4000000 | 6,0,0,0 | 9 |
| 19 | 136 | 108.8 | 4 | 20秒 | 1179 | 4600000 | 6,12,0,0 | 10 |
| 20 | 136 | 108.8 | 4 | 22秒 | 1179 | 5200000 | 6,12,0,0 | 10 |
</UnitTable>

<SmallTitle>更新历史</SmallTitle>

<Timeline>
    <TimelineItem date="2023/10/09">
        <TimelineRow>15 ~ 20 级狂暴野蛮人的每秒伤害增加。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/05/15">
        <TimelineRow>新增 19 - 20 级狂暴野蛮人。</TimelineRow>
        <TimelineRow>由于夜世界重做，部队的伤害、生命值等数据都有变化。</TimelineRow>
        <TimelineRow>狂暴野蛮人的兵种重量从 2 提升至 4.</TimelineRow>
        <TimelineRow>狂暴野蛮人的移动速度由 16 提升至 19.2.</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>修复了狂暴野蛮人、超级野蛮人和隐秘弓箭手的技能持续时间计时不太准确的问题。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/06/22">
        <TimelineRow>狂暴野蛮人的兵种重量从 1 提升至 2.</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/06/18">
        <TimelineRow>夜世界 9 本开放，所有兵种可升至 18 级。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>
<p><small>数值核对：2026-10-13 · <a href="https://clashofclans.fandom.com/wiki/Raged_Barbarian?oldid=624622" target="_blank" rel="noopener noreferrer">部落冲突维基</a>。部分附加字段沿用原记录。</small></p>
