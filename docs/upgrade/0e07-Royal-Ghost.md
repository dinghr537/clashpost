---
title: "部落冲突 coc 皇家幽灵升级数据"
navTitle: "皇家幽灵"
shownTitle: "皇家幽灵"
description: "透明的皇家幽灵很难被人注意到，他为此很苦恼，因此决心大肆破坏来找回应有的存在感。皇家幽灵实在太透明了，有时候连城墙都不会阻拦他！"
module: upgrade-temp
imgFolder: temp_troops/0e07
wiki: https://clashofclans.fandom.com/wiki/Royal_Ghost
canonical: /upgrade/0e07-Royal-Ghost
dataSyncedOn: 2026-10-13
---

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Royal_Ghost_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>各等级图片</SmallTitle>

<Panel>
    <UnitImgGroup :folder="$frontmatter.imgFolder">
        <UnitImg imgTitle="所有等级" imgSrc="Royal_Ghost1.png" />
    </UnitImgGroup>
</Panel>

<SmallTitle>属性</SmallTitle>

<UnitProperties>
    <UnitProperty pKey="部队类型" pValue="地面近战单位" />
    <UnitProperty pKey="攻击偏好" pValue="无" />
    <UnitProperty pKey="伤害类型" pValue="单体伤害" />
    <UnitProperty pKey="攻击的目标" pValue="仅地面目标" />
    <UnitProperty pKey="占据人口" pValue="8" />
    <UnitProperty pKey="移动速度" pValue="2 格/秒" />
    <UnitProperty pKey="攻击速度" pValue="1 秒/次" />
    <UnitProperty pKey="首次进攻时机" pValue="到达目标后 2.4 秒" />
    <UnitProperty pKey="攻击距离" pValue="0.5 格" />
    <UnitProperty pKey="所需训练营等级" pValue="7" />
    <UnitProperty pKey="所需大本等级" pValue="5" />
    <UnitProperty pKey="特殊技能" pValue="匿迹隐形<sup>*</sup>" />
    <UnitProperty pKey="减速比例" pValue="50% 攻速<br>50% 移速" />
    <UnitProperty pKey="训练时间" pValue="37" trainingSystem="2022" />
</UnitProperties>

\* 皇家幽灵在部署后的 12 秒内不能被锁定为目标，也不能被城墙阻拦。此外，被皇家幽灵命中的目标还有减速效果。

<p>临时单位的来源表格同步日期不表示活动开放日期；本期可用状态在页首另行说明。</p>

<SmallTitle>升级数据</SmallTitle>

<UnitTable>

| 等级 | 每秒伤害 | 每次伤害 | 生命值 |对应的<br>大本等级|
| ---- |  ----   |  ----   |  ----  |       ---      |
| 1 | 235 | 235 | 130 | 6 |
| 2 | 315 | 315 | 160 | 7 |
| 3 | 395 | 395 | 190 | 8 |
| 4 | 475 | 475 | 215 | 9 |
| 5 | 555 | 555 | 240 | 10 |
| 6 | 635 | 635 | 265 | 11 |
| 7 | 720 | 720 | 300 | 12 |
| 8 | 800 | 800 | 325 | 13 |
| 9 | 880 | 880 | 350 | 14 |
| 10 | 965 | 965 | 380 | 15 |
| 11 | 1050 | 1050 | 410 | 16 |
| 12 | 1135 | 1135 | 445 | 17 |
| 13 | 1220 | 1220 | 480 | 18 |
</UnitTable>

<SmallTitle>更新历史</SmallTitle>

<Timeline>
    <TimelineItem date="2022/10">
        <TimelineRow>该兵种第 3 次推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/10">
        <TimelineRow>该兵种第 2 次推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/10">
        <TimelineRow>该兵种第 1 次推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>
<p><small>数值核对：2026-10-13 · <a href="https://clashofclans.fandom.com/wiki/Royal_Ghost?oldid=625494" target="_blank" rel="noopener noreferrer">部落冲突维基</a>。部分附加字段沿用原记录。</small></p>
