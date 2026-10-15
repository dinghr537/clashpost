---
title: "部落冲突 coc 战吼狂人升级数据"
navTitle: "战吼狂人"
shownTitle: "战吼狂人"
description: "战吼狂人的攻击范围超远，战斗一开始他会投出 4 名忠诚的部族成员，攻击一切目标！之后，他会投掷自己最擅长的巨矛。现在，大声喊出来——咦哈！"
module: upgrade-temp
imgFolder: temp_troops/0e16
wiki: https://clashofclans.fandom.com/wiki/YEETer
canonical: /upgrade/0e16-YEETer
dataSyncedOn: 2026-10-13
---

<SwitchTabs contentClass="cp-unit-items" :stickyTabs="true" :pageTabs="true">
    <SwitchTab tabId="cp-unit-item-0" :activeTab="true">战吼狂人</SwitchTab>
    <SwitchTab tabId="cp-unit-item-1">部族小队</SwitchTab>
</SwitchTabs>

<!-- ↓↓↓ 战吼狂人 ↓↓↓ -->
<SwitchTabGroup id="cp-unit-item-0" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="YEETer_info.png" imgAlt="战吼狂人"
    description="战吼狂人的攻击范围超远，战斗一开始他会投出 4 名忠诚的部族成员，攻击一切目标！之后，他会投掷自己最擅长的巨矛。现在，大声喊出来——咦哈！" />

<SmallTitle>各等级图片</SmallTitle>

<Panel>
    <UnitImgGroup :folder="$frontmatter.imgFolder">
        <UnitImg imgTitle="所有等级" imgSrc="YEETer1.png" />
    </UnitImgGroup>
</Panel>

<SmallTitle>重要说明</SmallTitle>

1. 战吼狂人在 2025 年 4 月的部落狂热活动中作为临时兵种推出。
2. 战吼狂人扔部族成员时，攻击距离为 7 格；扔长矛时，攻击距离为 6 格。
3. 战吼狂人扔部族成员和扔长矛都可造成伤害，且伤害值是一样的。

<SmallTitle>战吼狂人的属性</SmallTitle>

<UnitProperties>
    <UnitProperty pKey="部队类型" pValue="地面远程单位" />
    <UnitProperty pKey="攻击偏好" pValue="无" />
    <UnitProperty pKey="伤害类型" pValue="单体伤害" />
    <UnitProperty pKey="攻击的目标" pValue="地面和空中目标" />
    <UnitProperty pKey="占据人口" pValue="45" />
    <UnitProperty pKey="移动速度" pValue="4 格/秒" />
    <UnitProperty pKey="攻击速度" pValue="2 秒/次" />
    <UnitProperty pKey="攻击距离" pValue="6 格或 7 格" />
    <UnitProperty pKey="所需训练营等级" pValue="1" />
    <UnitProperty pKey="所需大本等级" pValue="4" />
    <UnitProperty pKey="训练时间" pValue="无" trainingSystem="2025" />
</UnitProperties>

<p>临时单位的来源表格同步日期不表示活动开放日期；本期可用状态在页首另行说明。</p>

<SmallTitle>升级数据</SmallTitle>

<UnitTable>

| 等级 | 每秒伤害 | 每次伤害 | 生命值 |对应的<br>大本等级|
| ---- |   ---   |   ---   |   ---  |       ---      |
| 1 | 75 | 150 | 1250 | 3 |
| 2 | 80 | 160 | 1400 | 4 |
| 3 | 90 | 180 | 1550 | 5 |
| 4 | 100 | 200 | 1700 | 6 |
| 5 | 110 | 220 | 1950 | 7 |
| 6 | 120 | 240 | 2250 | 8 |
| 7 | 135 | 270 | 2600 | 9 |
| 8 | 150 | 300 | 2950 | 10 |
| 9 | 165 | 330 | 3300 | 11 |
| 10 | 180 | 360 | 3650 | 12 |
| 11 | 195 | 390 | 4050 | 13 |
| 12 | 210 | 420 | 4500 | 14 |
| 13 | 230 | 460 | 5000 | 15 |
| 14 | 250 | 500 | 5600 | 16 |
| 15 | 275 | 550 | 6200 | 17 |
| 16 | 300 | 600 | 6800 | 18 |
</UnitTable>
</SwitchTabGroup>

<!-- ↓↓↓ 部族小队 ↓↓↓ -->
<SwitchTabGroup id="cp-unit-item-1" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="YEETer_info.png" imgAlt="战吼狂人"
    description="数量占优时，体型便不再重要！战吼狂人登场时，会将这个四人小队投掷到战场上——他们擅长近战，会用迷你但强大的双手猛击一切目标！" />

<SmallTitle>各等级图片</SmallTitle>

<Panel>
    <UnitImgGroup :folder="$frontmatter.imgFolder">
        <UnitImg imgTitle="所有等级" imgSrc="Tribal_Tag_Team1.png" />
    </UnitImgGroup>
</Panel>

<SmallTitle>部族小队的属性</SmallTitle>

<UnitProperties>
    <UnitProperty pKey="部队类型" pValue="地面近战单位" />
    <UnitProperty pKey="攻击偏好" pValue="无" />
    <UnitProperty pKey="伤害类型" pValue="单体伤害" />
    <UnitProperty pKey="攻击的目标" pValue="仅地面目标" />
    <UnitProperty pKey="占据人口" pValue="5" />
    <UnitProperty pKey="移动速度" pValue="3.5 格/秒" />
    <UnitProperty pKey="攻击速度" pValue="1 秒/次" />
    <UnitProperty pKey="攻击距离" pValue="0.6 格" />
</UnitProperties>

<SmallTitle>升级数据</SmallTitle>

<UnitTable>

| 等级 | 每秒伤害 | 每次伤害 | 生命值 |对应的<br>大本等级|
| ---- |   ---   |   ---   |   ---  |       ----     |
| 1 | 30 | 60 | 800 | 3 |
| 2 | 40 | 80 | 1000 | 4 |
| 3 | 50 | 100 | 1200 | 5 |
| 4 | 60 | 120 | 1400 | 6 |
| 5 | 70 | 140 | 1600 | 7 |
| 6 | 85 | 170 | 2000 | 8 |
| 7 | 100 | 200 | 2400 | 9 |
| 8 | 115 | 230 | 2700 | 10 |
| 9 | 130 | 260 | 3000 | 11 |
| 10 | 145 | 290 | 3300 | 12 |
| 11 | 160 | 320 | 3700 | 13 |
| 12 | 175 | 350 | 4100 | 14 |
| 13 | 190 | 380 | 4500 | 15 |
| 14 | 210 | 420 | 5000 | 16 |
| 15 | 230 | 460 | 5500 | 17 |
| 16 | 250 | 500 | 6000 | 18 |
</UnitTable>
</SwitchTabGroup>

<!-- ↓↓↓ 公共部分 ↓↓↓ -->
<SmallTitle>更新历史</SmallTitle>

<Timeline>
    <TimelineItem date="2025/04/01">
        <TimelineRow>该兵种第 1 次推出，有效期至 2025/05/01.</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>
<p><small>数值核对：2026-10-13 · <a href="https://clashofclans.fandom.com/wiki/YEETer?oldid=625260" target="_blank" rel="noopener noreferrer">部落冲突维基</a>。部分附加字段沿用原记录。</small></p>
