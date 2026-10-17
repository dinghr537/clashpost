---
title: "部落冲突 coc 愤怒法术升级数据"
navTitle: "愤怒法术"
shownTitle: "愤怒法术"
englishName: "Angry Spell"
module: upgrade-home
imgFolder: home_tech/0187
wiki: https://clashofclans.fandom.com/wiki/Angry_Spell
canonical: /upgrade/0187-Angry-Spell
dataSyncedOn: 2026-10-13
---

<script setup>
const tableExtraInfo0 = [
    {
        "column": 3,
        "type": "cost",
        "icon": "Dark_Elixir",
        "gpClass": "research",
        "noGoldPass": false
    },
    {
        "column": 4,
        "type": "time",
        "gpClass": "research",
        "noGoldPass": false
    }
];
</script>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Angry_Spell_info.png" :imgAlt="$frontmatter.navTitle" :isSmallImg="true" />

<SmallTitle>重要说明</SmallTitle>

1. 解锁条件：8级暗黑法术工厂、15级大本营。

<SmallTitle>属性</SmallTitle>

<UnitProperties>
    <UnitProperty pKey="半径" pValue="6格" />
    <UnitProperty pKey="效果类型" pValue="范围伤害" />
    <UnitProperty pKey="目标" pValue="地面和空中" />
    <UnitProperty pKey="占据人口" pValue="1" />
    <UnitProperty pKey="所需暗黑法术工厂等级" pValue="8" />
</UnitProperties>

<SmallTitle>升级数据</SmallTitle>

<UnitTable :tableExtraInfo="tableExtraInfo0">

| 等级 | 愤怒持续时间 | 陷阱<br>持续时间 | 升级花费 | 升级时间 | 所需<br>实验室等级 | 所需<br>大本等级 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 7秒 | 5秒 | \ | \ | \ | \ |
| 2 | 8秒 | 5秒 | 150000 | 9,8,0,0 | 14 | 16 |
| 3 | 10秒 | 5秒 | 250000 | 12,0,0,0 | 15 | 17 |
| 4 | 12秒 | 5秒 | 400000 | 15,0,0,0 | 16 | 18 |
</UnitTable>


<SmallTitle>更新历史</SmallTitle>

<Timeline>
    <TimelineItem date="2026/08/31">
        <TimelineRow>修复较低大本等级玩家的部落城堡援军请求中不显示愤怒法术的问题；陨石戈仑在分裂、被投掷或合体时，不再丢失愤怒效果和目标。 <a href="https://supercell.com/en/games/clashofclans/blog/release-notes/august-update-3/" target="_blank" rel="noopener noreferrer">官方公告</a>（08/30 发布；<a href="https://clashofclans.fandom.com/wiki/Diggy?oldid=625147#History" target="_blank" rel="noopener noreferrer">更新日期</a>）</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2026/06/18">
        <TimelineRow>修复带有伤害倍率技能的部队在愤怒法术影响下，将该倍率错误用于防御建筑的问题。 <a href="https://clashofclans.fandom.com/wiki/Angry_Spell#History" target="_blank" rel="noopener noreferrer">来源</a></TimelineRow>
    </TimelineItem>
    <TimelineItem date="2026/06/16">
        <TimelineRow>推出愤怒法术，开放 1—4 级。 <a href="https://clashofclans.fandom.com/wiki/Angry_Spell#History" target="_blank" rel="noopener noreferrer">来源</a></TimelineRow>
    </TimelineItem>
</Timeline>
<p><small>数值核对：2026-10-13 · <a href="https://clashofclans.fandom.com/wiki/Angry_Spell?oldid=625021" target="_blank" rel="noopener noreferrer">部落冲突维基</a>。</small></p>
