---
title: "部落冲突 coc 派对法师升级数据"
navTitle: "派对法师"
shownTitle: "派对法师"
description: "听见远处架子鼓的声音了吗？派对法师华丽登场！他脚踩节奏，手扔火球，绝对是庆功派对的灵魂人物。"
module: upgrade-temp
imgFolder: temp_troops/0e06
wiki: https://clashofclans.fandom.com/wiki/Party_Wizard
canonical: /upgrade/0e06-Party-Wizard
dataSyncedOn: 2026-10-13
---

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Party_Wizard_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>各等级图片</SmallTitle>

<Panel>
    <UnitImgGroup :folder="$frontmatter.imgFolder">
        <UnitImg imgTitle="所有等级" imgSrc="Party_Wizard1.png" />
    </UnitImgGroup>
</Panel>

<SmallTitle>重要说明</SmallTitle>

派对法师一般在部落冲突生日（8 月 2 日）前后推出，他比 [普通法师](/upgrade/0006-Wizard) 的移动速度更快，伤害也更高，但生命值更少。

<SmallTitle>属性</SmallTitle>

<UnitProperties>
    <UnitProperty pKey="部队类型" pValue="地面远程单位" />
    <UnitProperty pKey="攻击偏好" pValue="无" />
    <UnitProperty pKey="伤害类型" pValue="范围伤害" />
    <UnitProperty pKey="伤害半径" pValue="0.3 格" />
    <UnitProperty pKey="攻击的目标" pValue="地面和空中目标" />
    <UnitProperty pKey="占据人口" pValue="4" />
    <UnitProperty pKey="移动速度" pValue="3 格/秒" />
    <UnitProperty pKey="攻击速度" pValue="1 秒/次" />
    <UnitProperty pKey="攻击距离" pValue="3 格" />
    <UnitProperty pKey="所需训练营等级" pValue="7" />
    <UnitProperty pKey="所需大本等级" pValue="5" />
    <UnitProperty pKey="训练时间" pValue="30" trainingSystem="2022" />
</UnitProperties>

<p>临时单位的来源表格同步日期不表示活动开放日期；本期可用状态在页首另行说明。</p>

<SmallTitle>升级数据</SmallTitle>

<UnitTable>

| 等级 | 每秒伤害 | 每次伤害 | 生命值 | 对应的大本等级 |
| ---- |  ----   |  ----   |  ----  |      ----    |
| 1 | 95 | 95 | 90 | 6 |
| 2 | 125 | 125 | 110 | 7 |
| 3 | 155 | 155 | 130 | 8 |
| 4 | 205 | 205 | 155 | 9 |
| 5 | 270 | 270 | 180 | 10 |
| 6 | 295 | 295 | 205 | 11 |
| 7 | 320 | 320 | 230 | 12 |
| 8 | 345 | 345 | 255 | 13 |
| 9 | 370 | 370 | 280 | 14 |
| 10 | 395 | 395 | 305 | 15 |
| 11 | 420 | 420 | 330 | 16 |
| 12 | 445 | 445 | 355 | 17 |
| 13 | 470 | 470 | 380 | 18 |
</UnitTable>

\* 游戏内部确实规定了 1 级派对法师的属性，但是派对法师 5 本才会解锁，这时候系统会自动把派对法师升到 2 级，所以 1 级派对法师实际上不会出现。

<SmallTitle>更新历史</SmallTitle>

<Timeline>
    <TimelineItem date="2023/08">
        <TimelineRow>该兵种第 4 次推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/08">
        <TimelineRow>该兵种第 3 次推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/08">
        <TimelineRow>该兵种第 2 次推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/08">
        <TimelineRow>该兵种第 1 次推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>
<p><small>数值核对：2026-10-13 · <a href="https://clashofclans.fandom.com/wiki/Party_Wizard?oldid=623061" target="_blank" rel="noopener noreferrer">部落冲突维基</a>。部分附加字段沿用原记录。</small></p>
