---
title: "部落冲突 coc 传送吊坠升级数据"
navTitle: "传送吊坠"
shownTitle: "传送吊坠"
englishName: "Portal Pendant"
module: upgrade-home
imgFolder: home_heroes/0726
wiki: https://clashofclans.fandom.com/wiki/Portal_Pendant
canonical: /upgrade/0726-Portal-Pendant
dataSyncedOn: 2026-10-13
---

<script setup>
const tableExtraInfo0 = [
    {
        "column": 6,
        "type": "cost",
        "icon": "Shiny_Ore",
        "gpClass": "research",
        "noGoldPass": true
    },
    {
        "column": 7,
        "type": "cost",
        "icon": "Glowy_Ore",
        "gpClass": "research",
        "noGoldPass": true
    },
    {
        "column": 8,
        "type": "cost",
        "icon": "Starry_Ore",
        "gpClass": "research",
        "noGoldPass": true
    }
];
</script>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Portal_Pendant.png" :imgAlt="$frontmatter.navTitle" :isSmallImg="true" />

<SmallTitle>重要说明</SmallTitle>

1. 启用技能可将范围内的友方部队、英雄和战宠召回部署栏，在允许部署的区域重新放下；攻城机器不能被召回。重新部署后，单位会获得回血和加速效果。
2. 召回容量按人口计算：英雄算 25 人口，战宠通常算 20 人口。亡灵王自身不占召回容量，但他携带的战宠通常仍计入容量。战宠有以下例外：
    - [凤凰](/upgrade/0287-Phoenix) 仍处于蛋形态时，只有主人被召回才会一起召回，且不额外占用人口。
    - [愤怒水母](/upgrade/0289-Angry-Jelly) 正在对主人施加洗脑效果时，会随主人一起召回，且不额外占用人口。
3. 容量不足时优先召回英雄，再召回人口较高的单位；人口相同时，先部署的优先。战宠不继承主人的优先权，因此可能与主人分开召回。重新部署时也按人口从高到低排列，同人口按最初部署顺序排列。
4. 召回会保留单位已有的状态，但离开原法术范围后，相应法术效果通常会消失。等待重新部署时，多数效果仍继续计时；以下计时会暂停：镜像法术复制单位的存活时间、愤怒水母及愤怒法术的愤怒效果、主动英雄装备效果（如狂暴药水瓶、永恒书卷），以及凤凰临时复活英雄的计时。

<p><small>以上机制整理自 <a href="https://clashofclans.fandom.com/wiki/Portal_Pendant?oldid=625662#Summary" target="_blank" rel="noopener noreferrer">部落冲突维基：传送吊坠（修订 625662）</a>。</small></p>

<SmallTitle>升级数据</SmallTitle>

<UnitTable :tableExtraInfo="tableExtraInfo0">

| 等级 | 技能<br>传送门半径（格） | 技能<br>重新部署回血比例 | 技能<br>重新部署加速 | 技能<br>召回人口容量 | 英雄<br>回血增加 | 升级费用 | 升级费用 | 升级费用 | 所需<br>铁匠铺等级 | 所需<br>大本等级 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 7 | +22% | 3.5秒 | 160 | 558 | \ | \ | \ | 1 | 8 |
| 2 | 7 | +22% | 3.5秒 | 160 | 587 | 120 | \ | \ | 1 | 8 |
| 3 | 7.2 | +24% | 4秒 | 175 | 615 | 240 | 20 | \ | 1 | 8 |
| 4 | 7.2 | +24% | 4秒 | 175 | 644 | 400 | \ | \ | 1 | 8 |
| 5 | 7.2 | +24% | 4秒 | 175 | 673 | 600 | \ | \ | 1 | 8 |
| 6 | 7.4 | +26% | 4.5秒 | 190 | 704 | 840 | 100 | \ | 1 | 8 |
| 7 | 7.4 | +26% | 4.5秒 | 190 | 730 | 1120 | \ | \ | 1 | 8 |
| 8 | 7.4 | +26% | 4.5秒 | 190 | 759 | 1440 | \ | \ | 1 | 8 |
| 9 | 7.6 | +28% | 5秒 | 205 | 788 | 1800 | 200 | 10 | 1 | 8 |
| 10 | 7.6 | +28% | 5秒 | 205 | 817 | 1900 | \ | \ | 1 | 8 |
| 11 | 7.6 | +28% | 5秒 | 205 | 845 | 2000 | \ | \ | 1 | 8 |
| 12 | 7.8 | +30% | 5.5秒 | 220 | 874 | 2100 | 400 | 20 | 1 | 8 |
| 13 | 7.8 | +30% | 5.5秒 | 220 | 903 | 2200 | \ | \ | 3 | 10 |
| 14 | 7.8 | +30% | 5.5秒 | 220 | 932 | 2300 | \ | \ | 3 | 10 |
| 15 | 8 | +31% | 6秒 | 280 | 960 | 2400 | 600 | 30 | 3 | 10 |
| 16 | 8 | +31% | 6秒 | 280 | 989 | 2500 | \ | \ | 5 | 12 |
| 17 | 8 | +31% | 6秒 | 280 | 1018 | 2600 | \ | \ | 5 | 12 |
| 18 | 8.5 | +32% | 6.5秒 | 340 | 1047 | 2700 | 600 | 50 | 5 | 12 |
| 19 | 8.5 | +32% | 6.5秒 | 340 | 1107 | 2800 | \ | \ | 7 | 14 |
| 20 | 8.5 | +32% | 6.5秒 | 340 | 1139 | 2900 | \ | \ | 7 | 14 |
| 21 | 9 | +33% | 7秒 | 360 | 1171 | 3000 | 600 | 100 | 7 | 14 |
| 22 | 9 | +33% | 7秒 | 360 | 1205 | 3100 | \ | \ | 8 | 15 |
| 23 | 9 | +33% | 7秒 | 360 | 1239 | 3200 | \ | \ | 8 | 15 |
| 24 | 9.5 | +34% | 7.5秒 | 380 | 1273 | 3300 | 600 | 120 | 8 | 15 |
| 25 | 9.5 | +34% | 7.5秒 | 380 | 1309 | 3400 | \ | \ | 9 | 16 |
| 26 | 9.5 | +34% | 7.5秒 | 380 | 1345 | 3500 | \ | \ | 9 | 16 |
| 27 | 10 | +35% | 8秒 | 400 | 1381 | 3600 | 600 | 150 | 9 | 16 |
</UnitTable>

<SmallTitle>更新历史</SmallTitle>

<Timeline>
    <TimelineItem date="2026/10/08">
        <TimelineRow>传送吊坠在裂隙之乱奖章活动中开放。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2026/09/22">
        <TimelineRow>调整15至27级的重新部署回血比例： 15-17级： 32% → 31% 18-20级： 34% → 32% 21-23级： 36% → 33% 24-26级： 38% → 34% 27级： 40% → 35%</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2026/08/31">
        <TimelineRow>传送吊坠已加入游戏文件。</TimelineRow>
    </TimelineItem>
</Timeline>


<p><small>数值核对：2026-10-13 · <a href="https://clashofclans.fandom.com/wiki/Portal_Pendant?oldid=625662" target="_blank" rel="noopener noreferrer">部落冲突维基</a>。</small></p>
