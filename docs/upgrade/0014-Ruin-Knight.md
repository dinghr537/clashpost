---
title: "部落冲突 coc 废墟骑士升级数据"
navTitle: "废墟骑士"
shownTitle: "废墟骑士"
englishName: "Ruin Knight"
module: upgrade-home
imgFolder: home_tech/0014
wiki: https://clashofclans.fandom.com/wiki/Ruin_Witch/Ruin_Knight
canonical: /upgrade/0014-Ruin-Knight
dataSyncedOn: 2026-10-13
---

<script setup>
const tableExtraInfo0 = [];
</script>

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Ruin_Knight1.png" :imgAlt="$frontmatter.navTitle" :isSmallImg="true" />

<SmallTitle>重要说明</SmallTitle>

1. 废墟骑士 是 废墟女巫 的召唤物，等级随召唤它的部队变化，不能单独升级。

相关单位：[废墟女巫](/upgrade/0013-Ruin-Witch)。

<SmallTitle>属性</SmallTitle>

<UnitProperties>
    <UnitProperty pKey="攻击偏好" pValue="无" />
    <UnitProperty pKey="伤害倍率" pValue="城墙 (伤害 ×3)" />
    <UnitProperty pKey="攻击方式" pValue="单体" />
    <UnitProperty pKey="占据人口" pValue="20" />
    <UnitProperty pKey="移动速度" pValue="2 格/秒" />
    <UnitProperty pKey="攻击间隔" pValue="1秒" />
    <UnitProperty pKey="射程" pValue="0.6格" />
</UnitProperties>

<SmallTitle>升级数据</SmallTitle>

<UnitTable :tableExtraInfo="tableExtraInfo0">

| 等级 | 每秒伤害 | 每次伤害 | 对墙伤害 | 生命值 |
| --- | --- | --- | --- | --- |
| 1 | 255 | 255 | 765 | 3100 |
| 2 | 285 | 285 | 855 | 3400 |
| 3 | 315 | 315 | 945 | 3700 |
| 4 | 345 | 345 | 1035 | 4000 |
</UnitTable>

<SmallTitle>更新历史</SmallTitle>

<Timeline>
    <TimelineItem date="2026/08/31">
        <TimelineRow>移除废墟骑士的生命值持续衰减。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2026/06/16">
        <TimelineRow>新增废墟骑士，共4级。</TimelineRow>
    </TimelineItem>
</Timeline>


<p><small>数值核对：2026-10-13 · <a href="https://clashofclans.fandom.com/wiki/Ruin_Witch/Ruin_Knight?oldid=625189" target="_blank" rel="noopener noreferrer">部落冲突维基</a>。</small></p>
