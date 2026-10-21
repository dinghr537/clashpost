---
title: "部落冲突 coc 陨石戈仑升级数据"
navTitle: "陨石戈仑"
shownTitle: "陨石戈仑"
description: "来自宇宙的它们，将加入您的军队！这对热衷投掷的组合，会将自己扔向任何目标，造成近战伤害。当它们分开时，小陨石戈仑会攻击附近目标，或者寻找同伴重新合体变成陨石戈仑！"
module: upgrade-home
imgFolder: home_tech/0012
wiki: https://clashofclans.fandom.com/wiki/Meteor_Golem
canonical: /upgrade/0012-Meteor-Golem
dataSyncedOn: 2026-10-13
dataBalanceUpdatedOn: 2026-10-20
---

- *如想查看陨石戈仑的设计原型，请访问：[戈仑石人](/upgrade/0083-Golem)。*
- *如想查看作为临时兵种的陨石戈仑数据，请访问：[陨石戈仑（临时兵种）](/upgrade/0e1b-Meteor-Golem)。*

<SwitchTabs contentClass="cp-unit-items" :stickyTabs="true" :pageTabs="true">
    <SwitchTab tabId="cp-unit-item-0" :activeTab="true">陨石戈仑</SwitchTab>
    <SwitchTab tabId="cp-unit-item-1">小陨石戈仑</SwitchTab>
</SwitchTabs>

<!-- ↓↓↓ 陨石戈仑 ↓↓↓ -->
<SwitchTabGroup id="cp-unit-item-0" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Meteor_Golem_info.png" imgAlt="陨石戈仑"
    description="来自宇宙的它们，将加入您的军队！这对热衷投掷的组合，会将自己扔向任何目标，造成近战伤害。当它们分开时，小陨石戈仑会攻击附近目标，或者寻找同伴重新合体变成陨石戈仑！" />

<SmallTitle>各等级图片</SmallTitle>

<Panel>
    <UnitImgGroup :folder="$frontmatter.imgFolder">
        <UnitImg imgTitle="1 级" imgSrc="Meteor_Golem1.png" />
        <UnitImg imgTitle="2 级" imgSrc="Meteor_Golem2.png" />
        <UnitImg imgTitle="3 级" imgSrc="Meteor_Golem3.png" />
    </UnitImgGroup>
</Panel>

<SmallTitle>重要说明</SmallTitle>

1. 陨石戈仑最初在 2025/10 的宇宙摇滚活动中作为临时兵种推出，在 2025/11 的 18 本版本更新后成为永久兵种。
2. 陨石戈仑由两只小陨石戈仑组成，其攻击方式是让其中一只小陨石戈仑将另一只投掷到目标身上，造成范围伤害。这种攻击方式会使两只小陨石戈仑分开，但只要两只小陨石戈仑相遇即可再次合体。
    - 任意两只小陨石戈仑都能合体，不需要来自同一母体。
    - 小陨石戈仑的生命值为陨石戈仑分离那一刻的一半生命值。
    - 小陨石戈仑合体后的生命值由两只小陨石戈仑的剩余生命值决定，如果其中一个或两个受到伤害，则总生命值减少。
    - [镜像法术](/upgrade/0105-Clone-Spell) 复制的陨石戈仑一旦分离就不能再合体。
3. 小陨石戈仑可以跳过 [城墙](/upgrade/0300-Walls)，但陨石戈仑不能。
4. 两只小陨石戈仑合体后有短暂的无敌状态。

<SmallTitle>属性</SmallTitle>

<UnitProperties>
    <UnitProperty pKey="部队类型" pValue="地面单位" />
    <UnitProperty pKey="攻击偏好" pValue="无" />
    <UnitProperty pKey="伤害加成" pValue="对墙 5 倍伤害" />
    <UnitProperty pKey="伤害类型" pValue="投掷后造成范围伤害" />
    <UnitProperty pKey="伤害半径" pValue="1 格" />
    <UnitProperty pKey="攻击的目标" pValue="地面和空中目标" />
    <UnitProperty pKey="占据人口" pValue="40" />
    <UnitProperty pKey="移动速度" pValue="1.5 格/秒" />
    <UnitProperty pKey="进攻时机" pValue="到达目标 1 秒后" />
    <UnitProperty pKey="最远投掷距离" pValue="5 格" />
    <UnitProperty pKey="所需训练营等级" pValue="19" />
    <UnitProperty pKey="所需大本等级" pValue="17" />
    <UnitProperty pKey="训练时间" pValue="无" trainingSystem="2025" />
    <UnitProperty pKey="捐赠费用" pValue="20,20,60000,Elixir" :isDonationCost="true" />
</UnitProperties>

<SmallTitle>升级数据</SmallTitle>

<script setup>
const tableExtraInfo = [
    {
        "column": 3,
        "type": "cost",
        "gpClass": "research",
        "icon": "Elixir"
    },
    {
        "column": 4,
        "type": "time",
        "gpClass": "research"
    }
];
</script>

<UnitTable :tableExtraInfo="tableExtraInfo">

| 等级 |  投掷伤害 | 生命值 | 升级花费|  升级时间  |所需实验室等级|所需大本等级|
| ---- |   ----   |  ---- |    ---  |     ---   |     ---     |   ----    |
| 1 | 480 | 15300 | \ | \ | 1 | 17 |
| 2 | 530 | 16900 | 28000000 | 14,0,0,0 | 15 | 17 |
| 3 | 580 | 18500 | 30000000 | 16,0,0,0 | 16 | 18 |
</UnitTable>
</SwitchTabGroup>

<!-- ↓↓↓ 小陨石戈仑 ↓↓↓ -->
<SwitchTabGroup id="cp-unit-item-1" class="cp-unit-items">
<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Meteormite_info.png" imgAlt="小陨石戈仑"
    description="分开的小陨石戈仑会对一个附近的目标进行攻击，或者寻找它的同伴重新合体。即便在分开后，这些顽皮的小石头也能翻越城墙。" />

<SmallTitle>各等级图片</SmallTitle>

<Panel>
    <UnitImgGroup :folder="$frontmatter.imgFolder">
        <UnitImg imgTitle="1 级" imgSrc="Meteormite1.png" />
        <UnitImg imgTitle="2 级" imgSrc="Meteormite2.png" />
        <UnitImg imgTitle="3 级" imgSrc="Meteormite3.png" />
    </UnitImgGroup>
</Panel>

<SmallTitle>属性</SmallTitle>

<UnitProperties>
    <UnitProperty pKey="部队类型" pValue="地面单位" />
    <UnitProperty pKey="攻击偏好" pValue="无" />
    <UnitProperty pKey="伤害类型" pValue="单体伤害" />
    <UnitProperty pKey="攻击的目标" pValue="仅地面目标" />
    <UnitProperty pKey="占据人口" pValue="20" />
    <UnitProperty pKey="移动速度" pValue="2 格/秒" />
    <UnitProperty pKey="攻击速度" pValue="1.5 秒/次" />
    <UnitProperty pKey="攻击距离" pValue="0.8 格" />
    <UnitProperty pKey="合体时的最大距离" pValue="0.5 格" />
</UnitProperties>

<SmallTitle>升级数据</SmallTitle>

<UnitTable>

| 等级 | 每秒伤害 | 每次伤害 | 生命值 |
| ---- |   ---   |   ---   |  ----  |
| 1 | 180 | 270 | 7650 |
| 2 | 200 | 300 | 8450 |
| 3 | 220 | 330 | 9250 |
</UnitTable>
</SwitchTabGroup>

<SmallTitle>更新历史</SmallTitle>

<Timeline>
    <TimelineItem date="2026/10/20">
        <TimelineRow>提高 1–3 级生命值，分别由 14500、16000、17500 提高至 15300、16900、18500；满血分裂后的小陨石戈仑生命值相应提高至 7650、8450、9250。</TimelineRow>
        <TimelineRow><a href="https://supercell.com/en/games/clashofclans/blog/news/balance-changes-incoming-october-2026/" target="_blank" rel="noopener noreferrer">官方公告</a>（10/17 发布） · <a href="https://clashfox.com/blog/balance-changes-before-town-hall-19-fire-heart-and-ruin-witch-nerfed-hogs-and-p-e-k-k-a-bu" target="_blank" rel="noopener noreferrer">数值参考</a> · <a href="https://x.com/ClashofClans/status/2112450159326179560" target="_blank" rel="noopener noreferrer">10/20 维护完成</a>；维护后已在游戏内确认调整生效。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2026/08/31">
        <TimelineRow>修复陨石戈仑在分裂、被投掷或合体时丢失愤怒法术效果及目标的问题。 <a href="https://supercell.com/en/games/clashofclans/blog/release-notes/august-update-3/" target="_blank" rel="noopener noreferrer">官方公告</a>（08/30 发布；<a href="https://clashofclans.fandom.com/wiki/Diggy?oldid=625147#History" target="_blank" rel="noopener noreferrer">更新日期</a>）</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2026/07/14">
        <TimelineRow>生命值调整：1级13,000→14,500，2级14,500→16,000，3级16,000→17,500；伤害调整：1级450→480，2级500→530，3级550→580。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2026/07/13">
        <TimelineRow>7 月 13—14 日的部队狂欢活动中，多人对战和复仇战加入 60 个临时版本的陨石戈仑及小陨石戈仑。 <a href="https://clashofclans.fandom.com/wiki/Meteor_Golem#History" target="_blank" rel="noopener noreferrer">来源</a></TimelineRow>
    </TimelineItem>
    <TimelineItem date="2026/01/28">
        <TimelineRow>所有等级陨石戈仑和小陨石戈仑的生命值和伤害降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2026/01/12">
        <TimelineRow>陨石戈仑对城墙的伤害降低 50%（现在对墙只有 5 倍伤害了）。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/11/17">
        <TimelineRow>18 本推出，陨石戈仑成为永久兵种，共推出 3 个等级。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/10/10">
        <TimelineRow>推出临时兵种：陨石戈仑，有效期至 2025/11/01.</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>
<p><small>数值核对：2026-10-13 · <a href="https://clashofclans.fandom.com/wiki/Meteor_Golem?oldid=624499" target="_blank" rel="noopener noreferrer">部落冲突维基</a>。部分附加字段沿用原记录。</small></p>
