---
title: "部落冲突 coc 精工空中炸弹发射器升级数据"
navTitle: "精工空中炸弹发射器"
shownTitle: "精工空中炸弹发射器"
module: upgrade-temp
imgFolder: crafted_buildings/0906
wiki: https://clashofclans.fandom.com/wiki/Air_Bombs/Home_Village
canonical: /upgrade/0906-Crafted-Air-Bombs
dataSyncedOn: 2026-10-13
---

<script setup>
const tableExtraInfo0 = [
    {
        "column": 2,
        "type": "cost",
        "icon": "Dark_Elixir",
        "gpClass": "building",
        "noGoldPass": false
    },
    {
        "column": 3,
        "type": "time",
        "gpClass": "building",
        "noGoldPass": false
    }
];
const tableExtraInfo1 = [
    {
        "column": 2,
        "type": "cost",
        "icon": "Elixir",
        "gpClass": "building",
        "noGoldPass": false
    },
    {
        "column": 3,
        "type": "time",
        "gpClass": "building",
        "noGoldPass": false
    }
];
const tableExtraInfo2 = [
    {
        "column": 2,
        "type": "cost",
        "icon": "Gold",
        "gpClass": "building",
        "noGoldPass": false
    },
    {
        "column": 3,
        "type": "time",
        "gpClass": "building",
        "noGoldPass": false
    }
];
</script>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Air_Bombs10_Crafted.png" :imgAlt="$frontmatter.navTitle" :isSmallImg="true" />

<SmallTitle>各等级图片</SmallTitle>

<Panel>
    <UnitImgGroup :folder="$frontmatter.imgFolder">
        <UnitImg imgTitle="10 级" imgSrc="Air_Bombs10_Crafted.png" />
        <UnitImg imgTitle="1 级" imgSrc="Air_Bombs1_Crafted.png" />
        <UnitImg imgTitle="2 级" imgSrc="Air_Bombs2_Crafted.png" />
        <UnitImg imgTitle="3 级" imgSrc="Air_Bombs3_Crafted.png" />
        <UnitImg imgTitle="4 级" imgSrc="Air_Bombs4_Crafted.png" />
        <UnitImg imgTitle="5 级" imgSrc="Air_Bombs5_Crafted.png" />
        <UnitImg imgTitle="6 级" imgSrc="Air_Bombs6_Crafted.png" />
        <UnitImg imgTitle="7 级" imgSrc="Air_Bombs7_Crafted.png" />
        <UnitImg imgTitle="8 级" imgSrc="Air_Bombs8_Crafted.png" />
        <UnitImg imgTitle="9 级" imgSrc="Air_Bombs9_Crafted.png" />
    </UnitImgGroup>
</Panel>

<SmallTitle>重要说明</SmallTitle>

1. 家乡精工防御，属于 2026 年 4 月 1 日至 7 月 30 日的批次，现已结束；与夜世界同名防御分开记录。

<SmallTitle>建筑数量对照表</SmallTitle>

<BuildingNum>
    <BuildingNumRow title="大本等级" num="1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18" />
    <BuildingNumRow title="建筑数量" num="0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1" />
</BuildingNum>

<SmallTitle>属性</SmallTitle>

<UnitProperties>
    <UnitProperty pKey="占地面积" pValue="3×3" />
</UnitProperties>

<SmallTitle>属性</SmallTitle>

<UnitProperties>
    <UnitProperty pKey="射程" pValue="11格" />
    <UnitProperty pKey="伤害类型" pValue="范围伤害 - 1.5格" />
    <UnitProperty pKey="攻击目标" pValue="空中" />
</UnitProperties>

<SmallTitle>模组一：生命值</SmallTitle>

<UnitTable :tableExtraInfo="tableExtraInfo0">

| 等级 | 生命值 | 升级费用 | 升级时间 | 升级后可<br>获得的经验 |
| --- | --- | --- | --- | --- |
| 1 | 600 | \ | \ | \ |
| 2 | 1000 | 40000 | 0,8,0,0 | 169 |
| 3 | 1500 | 50000 | 0,10,0,0 | 189 |
| 4 | 2000 | 60000 | 0,11,0,0 | 198 |
| 5 | 2600 | 70000 | 0,13,0,0 | 216 |
| 6 | 3200 | 80000 | 0,15,0,0 | 232 |
| 7 | 3800 | 90000 | 1,3,0,0 | 311 |
| 8 | 4400 | 100000 | 2,6,0,0 | 440 |
| 9 | 5200 | 110000 | 4,12,0,0 | 623 |
| 10 | 6000 | 120000 | 9,0,0,0 | 881 |
</UnitTable>

<SmallTitle>模组二：伤害</SmallTitle>

<UnitTable :tableExtraInfo="tableExtraInfo1">

| 等级 | 每次伤害 | 升级费用 | 升级时间 | 升级后可<br>获得的经验 |
| --- | --- | --- | --- | --- |
| 1 | 590 | \ | \ | \ |
| 2 | 620 | 3000000 | 0,4,0,0 | 120 |
| 3 | 650 | 4000000 | 0,6,0,0 | 146 |
| 4 | 680 | 5000000 | 0,8,0,0 | 169 |
| 5 | 710 | 6000000 | 0,10,0,0 | 189 |
| 6 | 740 | 7000000 | 0,12,0,0 | 207 |
| 7 | 775 | 8000000 | 1,0,0,0 | 293 |
| 8 | 820 | 9000000 | 2,0,0,0 | 415 |
| 9 | 880 | 10000000 | 4,0,0,0 | 587 |
| 10 | 950 | 11000000 | 8,0,0,0 | 831 |
</UnitTable>

<SmallTitle>模组三：攻击冷却</SmallTitle>

<UnitTable :tableExtraInfo="tableExtraInfo2">

| 等级 | 攻击冷却 | 升级费用 | 升级时间 | 升级后可<br>获得的经验 |
| --- | --- | --- | --- | --- |
| 1 | 3.4秒 | \ | \ | \ |
| 2 | 3.2秒 | 3500000 | 0,6,0,0 | 146 |
| 3 | 3秒 | 4500000 | 0,8,0,0 | 169 |
| 4 | 2.8秒 | 5500000 | 0,10,0,0 | 189 |
| 5 | 2.6秒 | 6500000 | 0,12,0,0 | 207 |
| 6 | 2.4秒 | 7500000 | 0,14,0,0 | 224 |
| 7 | 2.2秒 | 8500000 | 1,2,0,0 | 305 |
| 8 | 2秒 | 10000000 | 2,4,0,0 | 432 |
| 9 | 1.8秒 | 11500000 | 4,6,0,0 | 605 |
| 10 | 1.6秒 | 13000000 | 8,12,0,0 | 856 |
</UnitTable>

<SmallTitle>更新历史</SmallTitle>

<Timeline>
    <TimelineItem date="2026/07/31">
        <TimelineRow>本批空中炸弹发射器停止开放。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2026/05/26">
        <TimelineRow>精工空中炸弹发射器射程9格→11格；攻击间隔：1级3.8秒→3.4秒，2级3.6秒→3.2秒，3级3.4秒→3秒，4级3.2秒→2.8秒，5级3秒→2.6秒，6级2.8秒→2.4秒，7级2.6秒→2.2秒，8级2.4秒→2秒，9级2.2秒→1.8秒，10级2秒→1.6秒。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2026/04/01">
        <TimelineRow>新增空中炸弹发射器。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2026/03/30">
        <TimelineRow>公布空中炸弹发射器，共30级。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2026/03/27">
        <TimelineRow>调整2至9级的生命值： 2级： 1,200 → 1,000 3级： 1,800 → 1,500 4级： 2,400 → 2,000 5级： 3,000 → 2,600 6级： 3,600 → 3,200 7级： 4,200 → 3,800 8级： 4,800 → 4,400 9级： 5,400 → 5,200 调整2至9级的每次伤害： 2级： 630 → 620 3级： 670 → 650 4级： 710 → 680 5级： 750 → 710 6级： 790 → 740 7级： 830 → 775 8级： 870 → 820 9级： 910 → 880 调整全部模组的升级费用： 模组1（生命值）： 2级： 45,000 → 40,000 暗黑重油 3级： 60,000 → 50,000 暗黑重油 4级： 75,000 → 60,000 暗黑重油 5级： 90,000 → 70,000 暗黑重油 6级： 95,000 → 80,000 暗黑重油 7级： 100,000 → 90,000 暗黑重油 8级： 105,000 → 100,000 暗黑重油 10级： 115,000 → 120,000 暗黑重油 模组2（伤害）： 3级： 3,500,000 → 4,000,000 圣水 4级： 4,000,000 → 5,000,000 圣水 5级： 4,500,000 → 6,000,000 圣水 6级： 6,000,000 → 7,000,000 圣水 7级： 7,500,000 → 8,000,000 圣水 7级： 9,000,000 → 9,000,000 圣水 9级： 10,500,000 → 10,000,000 圣水 10级： 12,000,000 → 11,000,000 圣水 模组3（攻击冷却）： 2级： 4,000,000 → 3,500,000 金币 3级： 5,000,000 → 4,500,000 金币 4级： 6,000,000 → 5,500,000 金币 5级： 7,000,000 → 6,500,000 金币 6级： 8,000,000 → 7,500,000 金币 7级： 9,000,000 → 8,500,000 金币 9级： 11,000,000 → 11,500,000 金币 10级： 12,000,000 → 13,000,000 金币 调整全部模组的升级时间： 模组1（生命值）： 2级： 12小时 → 8小时 3级： 16小时 → 10小时 4级： 20小时 → 11小时 5级： 1天 → 13小时 6级： 1天 6小时 → 15小时 7级： 1天 12小时 → 1天 3小时 8级： 2天 → 2天 6小时 9级： 2天 12小时 → 4天 12小时 10级： 3天 → 9天 模组2（伤害）： 2级： 1天 12小时 → 4小时 3级： 2天 → 6小时 4级： 2天 12小时 → 8小时 5级： 2天 14小时 → 10小时 6级： 2天 16小时 → 12小时 7级： 2天 18小时 → 1天 8级： 2天 20小时 → 2天 9级： 2天 22小时 → 4天 10级： 3天 → 8天 模组3（攻击冷却）： 2级： 1天 → 6小时 3级： 1天 6小时 → 8小时 4级： 1天 12小时 → 10小时 5级： 1天 18小时 → 12小时 6级： 2天 → 14小时 7级： 2天 6小时 → 1天 2小时 8级： 2天 12小时 → 2天 4小时 9级： 2天 18小时 → 4天 6小时 10级： 3天 → 8天 12小时</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2026/02/23">
        <TimelineRow>已加入游戏文件。</TimelineRow>
    </TimelineItem>
</Timeline>


<p><small>数值核对：2026-10-13 · <a href="https://clashofclans.fandom.com/wiki/Air_Bombs/Home_Village?oldid=625572" target="_blank" rel="noopener noreferrer">部落冲突维基</a>。</small></p>
