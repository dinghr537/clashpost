---
title: "部落冲突 coc 独角（马）升级数据"
navTitle: "独角"
shownTitle: "独角（马）"
description: "独角不轻易相信他人，但它绝对值得您付出爱心和耐心与它建立信任，因为它会像天使一样治愈所有伤痛！"
module: upgrade-home
imgFolder: home_heroes/0283
wiki: https://clashofclans.fandom.com/wiki/Unicorn
canonical: /upgrade/0283-Unicorn
dataSyncedOn: 2026-10-13
---

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Unicorn_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>各等级图片</SmallTitle>

<Panel>
    <UnitImgGroup :folder="$frontmatter.imgFolder">
        <UnitImg imgTitle="所有等级" imgSrc="Unicorn_field.png" />
    </UnitImgGroup>
</Panel>

<SmallTitle>重要说明</SmallTitle>

1. 独角的技能（专属天使）：独角会跟随搭档英雄并提供治疗。
2. 独角是主人的专属天使，只要主人在场，独角的治疗目标永远都是主人。如果主人被召回或者阵亡，独角会像天使那样去辅助其他部队。主人被重新部署后，独角会立即调头回来找主人。
3. 天使不会主动帮独角补血，但当天使的奶溅射到独角时它是可以回血的。
4. 独角可以给空中部队补血，如空中模式的 [大守护者](/upgrade/0202-Grand-Warden)，但天使不行。
5. 同一目标受到多个治疗单位治疗时，新增单位的治疗效益会递减。按原站记录，第 1～8 个单位依次为 100%、100%、90%、90%、70%、40%、10%、0%；第 8 个起不再增加治疗量。此规则包含天使、独角和人形德鲁伊，不能直接用单个治疗量乘以单位数量。<small>（来源：<a href="https://clashpost.com/p/6925" target="_blank" rel="noopener noreferrer">原站治疗叠加记录（2025-02-14）</a>）</small>

<SmallTitle>属性</SmallTitle>

<UnitProperties>
    <UnitProperty pKey="治疗偏好" pValue="英雄" />
    <UnitProperty pKey="恢复类型" pValue="单个目标" />
    <UnitProperty pKey="作用目标" pValue="地面和空中目标" />
    <UnitProperty pKey="占据人口" pValue="20" />
    <UnitProperty pKey="移动速度" pValue="2 格/秒" />
    <UnitProperty pKey="治疗速度" pValue="1 秒/次" />
    <UnitProperty pKey="独角手长" pValue="2.5 格" />
    <UnitProperty pKey="所需战宠小屋等级" pValue="4" />
    <UnitProperty pKey="所需大本等级" pValue="14" />
</UnitProperties>

<SmallTitle>升级数据</SmallTitle>

<script setup>
const tableExtraInfo = [
    {
        "column": 4,
        "type": "cost",
        "gpClass": "research",
        "icon": "Dark_Elixir"
    },
    {
        "column": 5,
        "type": "time",
        "gpClass": "research"
    },
    {
        "column": 6,
        "type": "dailyCost",
        "icon": "Dark_Elixir"
    }
];
</script>

<UnitTable :tableExtraInfo="tableExtraInfo">

| 等级 |每秒恢复值|每次治疗的<br>恢复值| 生命值 | 升级花费 | 升级时间 | 日均耗油 |所需战宠<br>小屋等级|所需<br>大本等级|
| ---- |   ---   |       ----       |  ---   |   ----  |   ---   |   ---   |        ---        |      ----     |
| 1 | 50 | 50 | 1400 | \ | \ |  | 4 | 14 |
| 2 | 53 | 53 | 1450 | 50000 | 1,12,0,0 |  | 4 | 14 |
| 3 | 56 | 56 | 1500 | 65000 | 2,0,0,0 |  | 4 | 14 |
| 4 | 58 | 58 | 1550 | 80000 | 3,0,0,0 |  | 4 | 14 |
| 5 | 60 | 60 | 1600 | 95000 | 4,0,0,0 |  | 4 | 14 |
| 6 | 62 | 62 | 1675 | 110000 | 4,12,0,0 |  | 4 | 14 |
| 7 | 64 | 64 | 1725 | 125000 | 5,0,0,0 |  | 4 | 14 |
| 8 | 66 | 66 | 1800 | 140000 | 5,12,0,0 |  | 4 | 14 |
| 9 | 68 | 68 | 1875 | 155000 | 6,0,0,0 |  | 4 | 14 |
| 10 | 70 | 70 | 1950 | 170000 | 6,12,0,0 |  | 4 | 14 |
| 11 | 71 | 71 | 2025 | 200000 | 7,0,0,0 |  | 11 | 17 |
| 12 | 72 | 72 | 2100 | 230000 | 8,0,0,0 |  | 11 | 17 |
| 13 | 73 | 73 | 2175 | 260000 | 8,0,0,0 |  | 11 | 17 |
| 14 | 74 | 74 | 2250 | 290000 | 8,0,0,0 |  | 11 | 17 |
| 15 | 75 | 75 | 2325 | 320000 | 8,0,0,0 |  | 11 | 17 |
</UnitTable>

<SmallTitle>更新历史</SmallTitle>

<Timeline>
    <TimelineItem date="2025/10/06">
        <TimelineRow>8 级独角的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/24">
        <TimelineRow>在 17 本新增 11 ~ 15 级独角。</TimelineRow>
        <TimelineRow>2 ~ 10 级独角的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>2 ~ 10 级独角的升级费用和升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>4 ~ 10 级独角的升级时间减少。</TimelineRow>
        <TimelineRow>2 ~ 10 级独角的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/05/02">
        <TimelineRow>4 ~ 10 级独角的每秒恢复值从 59/62/65/68/71/74/77 降低至 58/60/62/64/66/68/70。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>部落冲突推出战宠，其中莱希、闪枭、大牦、独角是第一批推出的。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>
<p><small>数值核对：2026-10-13 · <a href="https://clashofclans.fandom.com/wiki/Unicorn?oldid=619842" target="_blank" rel="noopener noreferrer">部落冲突维基</a>。部分附加字段沿用原记录。</small></p>
