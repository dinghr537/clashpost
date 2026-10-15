---
title: "部落冲突 coc 骷髅巨人升级数据"
navTitle: "骷髅巨人"
shownTitle: "骷髅巨人"
description: "骷髅巨人从小就骨骼粗大，他能炸毁的可不只是城墙。被消灭后，他的超大炸弹能对周围的一切造成伤害。"
module: upgrade-temp
imgFolder: temp_troops/0e03
wiki: https://clashofclans.fandom.com/wiki/Giant_Skeleton
canonical: /upgrade/0e03-Giant-Skeleton
dataSyncedOn: 2026-10-13
---

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Giant_Skeleton_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" :isSmallImg="true" />

<SmallTitle>各等级图片</SmallTitle>

<Panel>
    <UnitImgGroup :folder="$frontmatter.imgFolder">
        <UnitImg imgTitle="所有等级" imgSrc="Giant_Skeleton1.png" />
    </UnitImgGroup>
</Panel>

<SmallTitle>属性</SmallTitle>

<UnitProperties>
    <UnitProperty pKey="部队类型" pValue="地面近战单位" />
    <UnitProperty pKey="攻击偏好" pValue="防御建筑 (偏好类型 1)" :isDefensePreferredTroop="true" />
    <UnitProperty pKey="伤害类型" pValue="单体伤害" />
    <UnitProperty pKey="攻击的目标" pValue="地面和空中目标" />
    <UnitProperty pKey="占据人口" pValue="20" />
    <UnitProperty pKey="移动速度" pValue="1.5 格/秒" />
    <UnitProperty pKey="攻击速度" pValue="2 秒/次" />
    <UnitProperty pKey="攻击距离" pValue="1 格" />
    <UnitProperty pKey="死亡爆炸半径" pValue="2 格" />
    <UnitProperty pKey="死亡爆炸延时" pValue="2 秒" />
    <UnitProperty pKey="所需训练营等级" pValue="3" />
    <UnitProperty pKey="所需大本等级" pValue="1<sup>*</sup>" />
    <UnitProperty pKey="训练时间" pValue="30" trainingSystem="2022" />
</UnitProperties>

\* 理论上来说，1 级大本营可以解锁骷髅巨人，但因为新手教程会引导玩家升级至 2 本，所以实际上 2 本才能训练和使用骷髅巨人。

<p>临时单位的来源表格同步日期不表示活动开放日期；本期可用状态在页首另行说明。</p>

<SmallTitle>升级数据</SmallTitle>

<UnitTable>

| 等级 | 每秒伤害 | 每次伤害 | 死亡伤害 | 生命值 |对应的<br>大本等级|
| ---- |  ----   |  ----   |    ---  |  ----  |        ---      |
| 1 | 60 | 120 | 1400 | 2100 | 6 |
| 2 | 75 | 150 | 1600 | 2700 | 7 |
| 3 | 100 | 200 | 1800 | 3600 | 8 |
| 4 | 120 | 240 | 2000 | 4200 | 9 |
| 5 | 140 | 280 | 2200 | 4800 | 10 |
| 6 | 160 | 320 | 2400 | 5200 | 11 |
| 7 | 180 | 360 | 2600 | 5800 | 12 |
| 8 | 200 | 400 | 2800 | 6300 | 13 |
| 9 | 210 | 420 | 3000 | 6900 | 14 |
| 10 | 230 | 460 | 3200 | 7500 | 15 |
| 11 | 255 | 510 | 3400 | 8100 | 16 |
| 12 | 280 | 560 | 3600 | 8700 | 17 |
| 13 | 310 | 620 | 3800 | 9500 | 18 |
</UnitTable>

<SmallTitle>更新历史</SmallTitle>

<Timeline>
    <TimelineItem date="2022/10">
        <TimelineRow>该兵种第 4 次推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2018/10">
        <TimelineRow>该兵种第 3 次推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2017/12/28">
        <TimelineRow>该兵种第 2 次推出，有效期至 2018/01/03.</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2017/10">
        <TimelineRow>该兵种第 1 次推出。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>
<p><small>数值核对：2026-10-13 · <a href="https://clashofclans.fandom.com/wiki/Giant_Skeleton?oldid=623284" target="_blank" rel="noopener noreferrer">部落冲突维基</a>。部分附加字段沿用原记录。</small></p>
