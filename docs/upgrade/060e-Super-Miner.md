---
title: "部落冲突 coc 超级矿工（超矿）升级数据"
navTitle: "超级矿工"
shownTitle: "超级矿工（超矿）"
description: "拿着大钻机，留着拉风的胡子，这位超级矿工随时准备暗中破坏敌方防御！"
module: upgrade-home
imgFolder: home_tech/060e
wiki: https://clashofclans.fandom.com/wiki/Super_Miner
canonical: /upgrade/060e-Super-Miner
dataSyncedOn: 2026-10-13
dataBalanceUpdatedOn: 2026-10-20
---

- *如想查看该兵种的普通版本，请访问：[掘地矿工](/upgrade/000b-Miner)。*
- *如想查看都城的超级矿工，请访问：[都城超级矿工](/upgrade/200f-Super-Miner)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Super_Miner_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>各等级图片</SmallTitle>

<Panel>
    <UnitImgGroup :folder="$frontmatter.imgFolder">
        <UnitImg imgTitle="所有等级" imgSrc="Super_Miner7.png" />
    </UnitImgGroup>
</Panel>

<SmallTitle>重要说明</SmallTitle>

1. 超级矿工的技能（终极大爆炸）：被消灭时丢下一个炸药桶。
2. 超级矿工使用钻机进行攻击，攻击时间越长伤害越高，类似于 [地狱飞龙](/upgrade/0604-Inferno-Dragon)。
3. 超级矿工能免疫 [飓风陷阱](/upgrade/0386-Tornado-Trap) 的转圈效果。

<SmallTitle>属性</SmallTitle>

<UnitProperties>
    <UnitProperty pKey="部队类型" pValue="地面近战单位" />
    <UnitProperty pKey="攻击偏好" pValue="无" />
    <UnitProperty pKey="伤害类型" pValue="单体伤害" />
    <UnitProperty pKey="攻击的目标" pValue="仅地面目标" />
    <UnitProperty pKey="占据人口" pValue="24" />
    <UnitProperty pKey="移动速度" pValue="4 格/秒 (进攻)<br>2.8 格/秒 (防守)" />
    <UnitProperty pKey="攻击速度" pValue="0.25 秒/次" />
    <UnitProperty pKey="攻击距离" pValue="0.6 格" />
    <UnitProperty pKey="死亡后的爆炸半径" pValue="2 格" />
    <UnitProperty pKey="最低矿工等级" pValue="7" />
    <UnitProperty pKey="最低大本等级" pValue="13" />
    <UnitProperty pKey="强化费用" pValue="2.5 万黑油" />
    <UnitProperty pKey="强化有效期" pValue="3 天" />
    <UnitProperty pKey="训练时间" pValue="无" trainingSystem="2025" />
    <UnitProperty pKey="捐赠费用" pValue="12,12,36000,Elixir" :isDonationCost="true" />
</UnitProperties>

<SmallTitle>升级数据</SmallTitle>

<UnitTable>

| 等级 |  初始秒伤  |  1.5 秒后秒伤  | 3 秒后秒伤 |  死亡伤害 | 生命值 |所需大本等级|
| ---- |    ----   |      ----     |    ----   |    ----   |  ---- |    ----   |
| 7 | 170 | 340 | 520 | 1400 | 3000 | 13 |
| 8 | 185 | 370 | 560 | 1600 | 3300 | 14 |
| 9 | 205 | 405 | 605 | 1800 | 3600 | 15 |
| 10 | 225 | 440 | 650 | 2000 | 4000 | 16 |
| 11 | 245 | 475 | 695 | 2200 | 4650 | 17 |
| 12 | 265 | 510 | 740 | 2400 | 5150 | 18 |
</UnitTable>

<SmallTitle>更新历史</SmallTitle>

<Timeline>
    <TimelineItem date="2026/10/20">
        <TimelineRow>提高 11、12 级生命值，分别由 4400、5000 提高至 4650、5150。</TimelineRow>
        <TimelineRow><a href="https://supercell.com/en/games/clashofclans/blog/news/balance-changes-incoming-october-2026/" target="_blank" rel="noopener noreferrer">官方公告</a>（10/17 发布） · <a href="https://clashfox.com/blog/balance-changes-before-town-hall-19-fire-heart-and-ruin-witch-nerfed-hogs-and-p-e-k-k-a-bu" target="_blank" rel="noopener noreferrer">数值参考</a> · <a href="https://x.com/ClashofClans/status/2112450159326179560" target="_blank" rel="noopener noreferrer">10/20 维护完成</a>；维护后已在游戏内确认调整生效。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/11/17">
        <TimelineRow>18 本推出，并在 18 本新增 12 级掘地矿工，超级部队的等级也相应更新。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/06/30">
        <TimelineRow>7 ~ 11 级超级矿工的生命值增加。</TimelineRow>
        <TimelineRow>9 ~ 11 级超级矿工的每秒伤害提升。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/27">
        <TimelineRow>部队的训练时间取消，但增加了捐赠费用。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/02/10">
        <TimelineRow>17 本新增 11 级掘地矿工，超级部队的等级也相应更新。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>16 本推出，并在 16 本新增 10 级掘地矿工，超级部队的等级也相应更新。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>9 级超级矿工的生命值由 3200 提升到 3500。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/12/12">
        <TimelineRow>新超级兵：超级矿工。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>
<p><small>数值核对：2026-10-13 · <a href="https://clashofclans.fandom.com/wiki/Super_Miner?oldid=620353" target="_blank" rel="noopener noreferrer">部落冲突维基</a>。部分附加字段沿用原记录。</small></p>
