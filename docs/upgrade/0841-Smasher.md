---
title: "部落冲突 coc 粉碎者升级数据"
navTitle: "粉碎者"
shownTitle: "粉碎者"
description: "这位重型守卫会对地面和空中部队造成溅射伤害。粉碎者是个输不起的暴躁角色——如果大本营被摧毁，他就会勃然大怒；如果他自己被击倒，他也会留下愤怒的余威。"
module: upgrade-home
imgFolder: home_th/0841
wiki: https://clashofclans.fandom.com/wiki/Smasher
canonical: /upgrade/0841-Smasher
dataSyncedOn: 2026-10-13
dataVersionUpdatedOn: 2026-11-16
---

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Smasher_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>各等级图片</SmallTitle>

<Panel>
    <UnitImgGroup :folder="$frontmatter.imgFolder">
        <UnitImg imgTitle="所有等级" imgSrc="Smasher1.png" />
    </UnitImgGroup>
</Panel>

<SmallTitle>重要说明</SmallTitle>

- 毒药法术对粉碎者造成正常值 30% 的伤害；被冻结时粉碎者不会激活。<small>（来源：<a href="https://supercell.com/en/games/clashofclans/blog/release-notes/the-sound-of-clash-update/" target="_blank" rel="noopener noreferrer">Supercell 四月更新公告</a>）</small>

- 粉碎者的特殊技能（败局狂怒）：大本营被摧毁会进入狂暴状态，这种状态会持续到他被击倒为止。另外，粉碎者在被击倒后会释放一个狂暴法术，其效果与 [狂暴法术塔](/upgrade/0311-Spell-Tower) 相同，可强化防御建筑和防守方单位。
    - 无论粉碎者被击倒前是否进入了狂暴状态，这个狂暴法术都会释放。

<SmallTitle>属性</SmallTitle>

<UnitProperties>
    <UnitProperty pKey="攻击偏好" pValue="无" />
    <UnitProperty pKey="伤害类型" pValue="范围伤害" />
    <UnitProperty pKey="伤害半径" pValue="2.5 格" />
    <UnitProperty pKey="攻击的目标" pValue="地面和空中目标" />
    <UnitProperty pKey="移动速度" pValue="2.5 格/秒" />
    <UnitProperty pKey="攻击速度" pValue="1.8 秒/次" />
    <UnitProperty pKey="攻击距离" pValue="1.25 格" />
    <UnitProperty pKey="警戒半径" pValue="14 格" />
    <UnitProperty pKey="巡逻半径" pValue="12 格" />
    <UnitProperty pKey="狂暴状态下移动速度提升" pValue="1.5 格/秒" />
    <UnitProperty pKey="狂暴状态下伤害提升" pValue="60%" />
    <UnitProperty pKey="所需大本等级" pValue="18" />
</UnitProperties>

<small>警戒半径：敌军进入后，守卫会看向部队的方向，准备反击。</small>

<small>巡逻半径：没有敌人时守卫的走动范围。</small>

<SmallTitle>升级数据</SmallTitle>

<small>19 本资料参考 [Supercell 官方公告](https://supercell.com/en/games/clashofclans/blog/release-notes/the-clash-of-titans-update-is-rolling-out/)与 [部落冲突 Wiki](https://clashofclans.fandom.com/wiki/Smasher)。</small>

<small>2–5 级费用采用 [Supercell 19 本更新公告](https://supercell.com/en/games/clashofclans/blog/release-notes/the-clash-of-titans-update-is-rolling-out/)中的数值；维基列出的费用不同。</small>

<script setup>
const tableExtraInfo = [
    {
        "column": 4,
        "type": "cost",
        "noGoldPass": true,
        "icon": "Elixir"
    },
    {
        "column": 5,
        "type": "time",
        "noGoldPass": true,
    }
];
</script>


<UnitTable :tableExtraInfo="tableExtraInfo">

| 等级 | 每秒伤害 | 每次伤害 | 生命值 | 升级费用 | 升级时间 | 所需大本等级 |
|  --- |   ---   |    ---  |   ---  |   ---   |   ---   |     ---     |
| 1 | 500 | 900 | 12000 | \ | \ | 18 |
| 2 | 550 | 990 | 13000 | 15000000 | 5,0,0,0 | 18 |
| 3 | 600 | 1080 | 14000 | 18000000 | 7,0,0,0 | 18 |
| 4 | 650 | 1170 | 15000 | 21000000 | 9,0,0,0 | 18 |
| 5 | 700 | 1260 | 16000 | 23000000 | 11,0,0,0 | 18 |
| 6 | 750 | 1350 | 17000 | 24000000 | 12,0,0,0 | 19 |
| 7 | 800 | 1440 | 18000 | 25000000 | 12,12,0,0 | 19 |
| 8 | 850 | 1530 | 19000 | 26000000 | 13,0,0,0 | 19 |
| 9 | 900 | 1620 | 20000 | 27000000 | 13,12,0,0 | 19 |
| 10 | 950 | 1710 | 21000 | 28000000 | 14,0,0,0 | 19 |
</UnitTable>

<SmallTitle>更新历史</SmallTitle>

<Timeline>
    <TimelineItem date="2026/11/16">
        <TimelineRow>19 本版本新增 6–10 级。<a href="https://supercell.com/en/games/clashofclans/blog/release-notes/the-clash-of-titans-update-is-rolling-out/" target="_blank" rel="noopener noreferrer">官方公告</a></TimelineRow>
    </TimelineItem>
    <TimelineItem date="2026/04/27">
        <TimelineRow>毒药法术重新对粉碎者造成伤害，伤害为正常值的 30%。<a href="https://supercell.com/en/games/clashofclans/blog/release-notes/the-sound-of-clash-update/" target="_blank" rel="noopener noreferrer">官方公告</a></TimelineRow>
        <TimelineRow>守卫被冻结时，不再触发激活。 <a href="https://supercell.com/en/games/clashofclans/blog/release-notes/the-sound-of-clash-update/" target="_blank" rel="noopener noreferrer">官方公告</a></TimelineRow>
    </TimelineItem>
    <TimelineItem date="2026/02/23">
        <TimelineRow>开始受到毒药法术影响：承受完整伤害，移速和攻速降低效果按通常值的 70% 生效。此规则后来在四月调整。 <a href="https://supercell.com/en/games/clashofclans/blog/release-notes/the-february-update-has-escaped/" target="_blank" rel="noopener noreferrer">官方公告</a></TimelineRow>
    </TimelineItem>
    <TimelineItem date="2026/01/12">
        <TimelineRow>巡逻半径从 10 格增加到 12 格。</TimelineRow>
        <TimelineRow>警戒半径从 12 格增加到 14 格。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/11/17">
        <TimelineRow>推出守卫系统，粉碎者是第一批推出的守卫。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>
<p><small>数值核对：2026-10-13 · <a href="https://clashofclans.fandom.com/wiki/Smasher?oldid=625037" target="_blank" rel="noopener noreferrer">部落冲突维基</a>。部分附加字段沿用原记录。</small></p>
