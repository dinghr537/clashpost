---
title: "部落冲突 coc 大守护者（咏王）升级数据"
navTitle: "大守护者"
shownTitle: "大守护者（咏王）"
description: "大守护者是一位强大的魔法大师，他会用手中的法杖支援进攻部队。他可以跳过城墙或和空中部队一样飞翔，因此可以为任何进攻部队提供帮助。防守时，他将变成一座强大的防御塔。"
module: upgrade-home
imgFolder: home_heroes/0202
wiki: https://clashofclans.fandom.com/wiki/Grand_Warden
canonical: /upgrade/0202-Grand-Warden
dataSyncedOn: 2026-10-13
---

- *如想查看守护者学徒，请访问：[守护者学徒](/upgrade/0089-Apprentice-Warden)。*

<UnitInfo :folder="$frontmatter.imgFolder" imgSrc="Grand_Warden_info.png" :imgAlt="$frontmatter.navTitle" :description="$frontmatter.description" />

<SmallTitle>重要说明</SmallTitle>

1. 无论你使用了地面还是飞行模式，大守护者都可以无视城墙。
    - 防守时，大守护者始终处于地面模式。
2. 2024 年 11 月更新后，大守护者防守时不再变成雕像，而是会和其他英雄一样走动。
3. 英雄皮肤只改变外观，不改变战斗属性。可在英雄殿堂的英雄界面点击衣架图标查看和更换皮肤。<small>（来源：<a href="https://support.supercell.com/clash-of-clans/en/articles/heroes-hero-skins-4.html" target="_blank" rel="noopener noreferrer">Supercell：英雄皮肤</a>）</small>
4. 英雄在[英雄殿堂](/upgrade/0489-Hero-Hall)中解锁、升级和编队，等级上限由英雄殿堂等级决定。进攻阵容最多选择四名英雄；防守英雄通过英雄旗帜分配，可以与进攻阵容不同。<small>（来源：<a href="https://support.supercell.com/clash-of-clans/en/articles/about-heroes-pets-9.html" target="_blank" rel="noopener noreferrer">Supercell：英雄与战宠</a>）</small>
3. 下方的数据均为不含装备的数据。
4. 英雄在防守时没有装备。

<SmallTitle>大守护者的属性</SmallTitle>

<UnitProperties>
    <UnitProperty pKey="英雄类型" pValue="地面/空中辅助单位" />
    <UnitProperty pKey="攻击偏好" pValue="无" />
    <UnitProperty pKey="伤害类型" pValue="单体伤害" />
    <UnitProperty pKey="攻击的目标" pValue="地面和空中目标" />
    <UnitProperty pKey="占据人口" pValue="25" />
    <UnitProperty pKey="移动速度" pValue="2 格/秒" />
    <UnitProperty pKey="攻击速度" pValue="1.8 秒/次" />
    <UnitProperty pKey="攻击距离" pValue="7 格<sup>①</sup>" />
    <UnitProperty pKey="所需大本等级" pValue="11" />
    <UnitProperty pKey="搜索半径" pValue="10 格<sup>②</sup>" />
    <UnitProperty pKey="巡逻半径" pValue="2 格<sup>③</sup>" />
    <UnitProperty pKey="技能持续时间" pValue="与具体装备有关" />
    <UnitProperty pKey="光环半径" pValue="9 格<sup>④</sup>" />
</UnitProperties>

① 地面模式为 7 格，空中模式进攻时约 6.6 格。注意：6.6 这个数据是玩家自行测试得到的，并非官方数据。<br>
② 如果敌军进入这个范围，英雄会奔向敌军，并进行反击。<br>
③ 在没有敌人的情况下，英雄也会走动，而这个走动的范围叫巡逻半径。<br>
④ 这个光环半径是诸多装备的有效范围。

<SmallTitle>升级数据</SmallTitle>

<script setup>
const tableExtraInfo = [
    {
        "column": 4,
        "type": "cost",
        "gpClass": "building",
        "icon": "Elixir"
    },
    {
        "column": 5,
        "type": "time",
        "gpClass": "building"
    },
    {
        "column": 6,
        "type": "dailyCost",
        "icon": "Elixir"
    }
];
</script>

<UnitTable :tableExtraInfo="tableExtraInfo">

| 等级 |每秒伤害|每次伤害|生命值 |升级费用|升级时间|日均消耗|所需英雄<br>殿堂等级|所需<br>大本等级|
| ---  |  ---  |  ---  |  ---  | ---   |  ---  |   ---  |       ---        |      ---      |
| 1 | 43 | 77.4 | 850 | 1000000 | \ |  | 5 | 11 |
| 2 | 44 | 79.2 | 868 | 1000000 | 0,2,0,0 |  | 5 | 11 |
| 3 | 46 | 82.8 | 886 | 1100000 | 0,4,0,0 |  | 5 | 11 |
| 4 | 48 | 86.4 | 904 | 1200000 | 0,8,0,0 |  | 5 | 11 |
| 5 | 49 | 88.2 | 923 | 1400000 | 0,10,0,0 |  | 5 | 11 |
| 6 | 51 | 91.8 | 942 | 1500000 | 0,12,0,0 |  | 5 | 11 |
| 7 | 54 | 97.2 | 961 | 1700000 | 0,14,0,0 |  | 5 | 11 |
| 8 | 56 | 100.8 | 982 | 1800000 | 0,16,0,0 |  | 5 | 11 |
| 9 | 59 | 106.2 | 1003 | 2000000 | 0,18,0,0 |  | 5 | 11 |
| 10 | 61 | 109.8 | 1025 | 2300000 | 0,20,0,0 |  | 5 | 11 |
| 11 | 64 | 115.2 | 1048 | 2700000 | 1,0,0,0 |  | 5 | 11 |
| 12 | 66 | 118.8 | 1072 | 3000000 | 1,0,0,0 |  | 5 | 11 |
| 13 | 70 | 126 | 1097 | 3400000 | 1,0,0,0 |  | 5 | 11 |
| 14 | 73 | 131.4 | 1122 | 3700000 | 1,0,0,0 |  | 5 | 11 |
| 15 | 77 | 138.6 | 1148 | 4100000 | 1,0,0,0 |  | 5 | 11 |
| 16 | 80 | 144 | 1173 | 4400000 | 1,0,0,0 |  | 5 | 11 |
| 17 | 83 | 149.4 | 1199 | 4800000 | 1,0,0,0 |  | 5 | 11 |
| 18 | 87 | 156.6 | 1224 | 5100000 | 1,0,0,0 |  | 5 | 11 |
| 19 | 90 | 162 | 1250 | 5500000 | 1,0,0,0 |  | 5 | 11 |
| 20 | 94 | 169.2 | 1275 | 6000000 | 1,0,0,0 |  | 5 | 11 |
| 21 | 98 | 176.4 | 1301 | 6100000 | 1,0,0,0 |  | 6 | 12 |
| 22 | 102 | 183.6 | 1327 | 6200000 | 1,0,0,0 |  | 6 | 12 |
| 23 | 106 | 190.8 | 1354 | 6300000 | 1,0,0,0 |  | 6 | 12 |
| 24 | 111 | 199.8 | 1381 | 6400000 | 1,0,0,0 |  | 6 | 12 |
| 25 | 116 | 208.8 | 1409 | 6500000 | 1,0,0,0 |  | 6 | 12 |
| 26 | 121 | 217.8 | 1438 | 6600000 | 1,12,0,0 |  | 6 | 12 |
| 27 | 126 | 226.8 | 1467 | 6700000 | 1,12,0,0 |  | 6 | 12 |
| 28 | 131 | 235.8 | 1497 | 6800000 | 1,12,0,0 |  | 6 | 12 |
| 29 | 137 | 246.6 | 1527 | 6900000 | 1,12,0,0 |  | 6 | 12 |
| 30 | 143 | 257.4 | 1558 | 7000000 | 1,12,0,0 |  | 6 | 12 |
| 31 | 149 | 268.2 | 1590 | 7100000 | 2,0,0,0 |  | 6 | 12 |
| 32 | 155 | 279 | 1622 | 7200000 | 2,0,0,0 |  | 6 | 12 |
| 33 | 162 | 291.6 | 1655 | 7300000 | 2,0,0,0 |  | 6 | 12 |
| 34 | 168 | 302.4 | 1688 | 7400000 | 2,0,0,0 |  | 6 | 12 |
| 35 | 175 | 315 | 1722 | 7500000 | 2,0,0,0 |  | 6 | 12 |
| 36 | 183 | 329.4 | 1757 | 7600000 | 2,0,0,0 |  | 6 | 12 |
| 37 | 190 | 342 | 1793 | 7700000 | 2,0,0,0 |  | 6 | 12 |
| 38 | 198 | 356.4 | 1829 | 7800000 | 2,0,0,0 |  | 6 | 12 |
| 39 | 207 | 372.6 | 1867 | 7900000 | 2,0,0,0 |  | 6 | 12 |
| 40 | 215 | 387 | 1904 | 8000000 | 2,0,0,0 |  | 6 | 12 |
| 41 | 221 | 397.8 | 1921 | 8300000 | 3,0,0,0 |  | 7 | 13 |
| 42 | 226 | 406.8 | 1938 | 8600000 | 3,0,0,0 |  | 7 | 13 |
| 43 | 230 | 414 | 1955 | 8900000 | 3,0,0,0 |  | 7 | 13 |
| 44 | 234 | 421.2 | 1972 | 9200000 | 3,0,0,0 |  | 7 | 13 |
| 45 | 237 | 426.6 | 1989 | 9500000 | 3,0,0,0 |  | 7 | 13 |
| 46 | 241 | 433.8 | 2006 | 9800000 | 3,0,0,0 |  | 7 | 13 |
| 47 | 244 | 439.2 | 2023 | 10100000 | 3,0,0,0 |  | 7 | 13 |
| 48 | 247 | 444.6 | 2040 | 10400000 | 3,0,0,0 |  | 7 | 13 |
| 49 | 251 | 451.8 | 2057 | 10700000 | 3,0,0,0 |  | 7 | 13 |
| 50 | 254 | 457.2 | 2074 | 11000000 | 3,0,0,0 |  | 7 | 13 |
| 51 | 258 | 464.4 | 2091 | 11400000 | 4,0,0,0 |  | 8 | 14 |
| 52 | 261 | 469.8 | 2108 | 11800000 | 4,0,0,0 |  | 8 | 14 |
| 53 | 264 | 475.2 | 2125 | 12200000 | 4,0,0,0 |  | 8 | 14 |
| 54 | 268 | 482.4 | 2142 | 12600000 | 4,0,0,0 |  | 8 | 14 |
| 55 | 271 | 487.8 | 2159 | 13000000 | 4,0,0,0 |  | 8 | 14 |
| 56 | 274 | 493.2 | 2176 | 13400000 | 4,0,0,0 |  | 8 | 14 |
| 57 | 276 | 496.8 | 2193 | 13800000 | 4,0,0,0 |  | 8 | 14 |
| 58 | 279 | 502.2 | 2210 | 14200000 | 4,0,0,0 |  | 8 | 14 |
| 59 | 281 | 505.8 | 2227 | 14600000 | 4,0,0,0 |  | 8 | 14 |
| 60 | 284 | 511.2 | 2244 | 15000000 | 4,0,0,0 |  | 8 | 14 |
| 61 | 286 | 514.8 | 2261 | 15500000 | 6,0,0,0 |  | 9 | 15 |
| 62 | 289 | 520.2 | 2278 | 16000000 | 6,0,0,0 |  | 9 | 15 |
| 63 | 292 | 525.6 | 2295 | 16500000 | 6,0,0,0 |  | 9 | 15 |
| 64 | 294 | 529.2 | 2312 | 17000000 | 6,0,0,0 |  | 9 | 15 |
| 65 | 297 | 534.6 | 2329 | 17500000 | 6,0,0,0 |  | 9 | 15 |
| 66 | 299 | 538.2 | 2346 | 18000000 | 7,0,0,0 |  | 10 | 16 |
| 67 | 302 | 543.6 | 2363 | 18500000 | 7,0,0,0 |  | 10 | 16 |
| 68 | 304 | 547.2 | 2380 | 19000000 | 7,0,0,0 |  | 10 | 16 |
| 69 | 307 | 552.6 | 2397 | 19500000 | 7,0,0,0 |  | 10 | 16 |
| 70 | 309 | 556.2 | 2414 | 20000000 | 7,12,0,0 |  | 10 | 16 |
| 71 | 312 | 561.6 | 2431 | 20500000 | 8,0,0,0 |  | 11 | 17 |
| 72 | 315 | 567 | 2448 | 21000000 | 8,0,0,0 |  | 11 | 17 |
| 73 | 318 | 572.4 | 2465 | 21500000 | 8,0,0,0 |  | 11 | 17 |
| 74 | 321 | 577.8 | 2482 | 22000000 | 8,0,0,0 |  | 11 | 17 |
| 75 | 324 | 583.2 | 2499 | 22500000 | 8,0,0,0 |  | 11 | 17 |
| 76 | 327 | 588.6 | 2516 | 23500000 | 8,0,0,0 |  | 12 | 18 |
| 77 | 330 | 594 | 2533 | 24500000 | 8,0,0,0 |  | 12 | 18 |
| 78 | 333 | 599.4 | 2550 | 25500000 | 8,0,0,0 |  | 12 | 18 |
| 79 | 336 | 604.8 | 2567 | 26500000 | 8,0,0,0 |  | 12 | 18 |
| 80 | 339 | 610.2 | 2584 | 27500000 | 8,0,0,0 |  | 12 | 18 |
| 81 | 342 | 615.6 | 2601 | 28500000 | 8,0,0,0 |  | 12 | 18 |
| 82 | 345 | 621 | 2618 | 29000000 | 8,0,0,0 |  | 12 | 18 |
| 83 | 348 | 626.4 | 2635 | 29500000 | 8,0,0,0 |  | 12 | 18 |
| 84 | 351 | 631.8 | 2652 | 30000000 | 8,0,0,0 |  | 12 | 18 |
| 85 | 354 | 637.2 | 2669 | 30500000 | 8,0,0,0 |  | 12 | 18 |
</UnitTable>

<SmallTitle>技能回血数据</SmallTitle>

下表中的生命值恢复量是基础属性，与装备无关。即使没有装备，开技能也会回血。

<Table maxWidth="25rem">

| 大守护者等级 | 开启技能后生命值恢复 |
|     ---     |         ---        |
|    1 - 4    |          90        |
|    5 - 9    |          97        |
|   10 - 14   |         109        |
|   15 - 19   |         122        |
|   20 - 24   |         135        |
|   25 - 29   |         149        |
|   30 - 34   |         165        |
|   35 - 39   |         182        |
|   40 - 44   |         202        |
|   45 - 49   |         211        |
|   50 - 54   |         220        |
|   55 - 59   |         229        |
|   60 - 64   |         238        |
|   65 - 69   |         247        |
|   70 - 74   |         256        |
|   75 - 79   |         265        |
|      80     |         275        |
</Table>

<SmallTitle>更新历史</SmallTitle>

<Timeline>
    <TimelineItem date="2026/06/15">
        <TimelineRow>新增81至85级大守护者，降低76至80级的圣水升级费用。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2026/02/23">
        <TimelineRow>21 ~ 25、36 ~ 40、46 ~ 55 级大守护者的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/11/17">
        <TimelineRow>18 本推出，并在 18 本新增 76 ~ 80 级大守护者。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/10/06">
        <TimelineRow>现在 14 级大本营即可解锁 56 ~ 60 级大守护者。</TimelineRow>
        <TimelineRow>10、26 ~ 70 级大守护者的升级时间减少。</TimelineRow>
        <TimelineRow>21 ~ 64 级大守护者的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2025/03/27">
        <TimelineRow>取消英雄的恢复时间，现在英雄可以像战宠一样瞬间恢复。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/11/25">
        <TimelineRow>英雄的升级操作被整合进英雄殿堂，取消王座，同时引入英雄栏位和战旗的概念。</TimelineRow>
        <TimelineRow>英雄不再拥有警戒半径，遇到敌人后头顶不会冒问号，而是直接反击。</TimelineRow>
        <TimelineRow>在 17 本新增 71 - 75 级大守护者。</TimelineRow>
        <TimelineRow>11 ~ 60 级大守护者的升级时间减少。</TimelineRow>
        <TimelineRow>1 级大守护者的升级费用降低。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2024/06/18">
        <TimelineRow>5 ~ 10、12 ~ 55 级大守护者的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/12/12">
        <TimelineRow>16 本推出，同时在 16 本新增 66 ~ 70 级大守护者。</TimelineRow>
        <TimelineRow>所有等级大守护者的每秒伤害和生命值降低。</TimelineRow>
        <TimelineRow>所有等级的升级时间和升级成本降低。</TimelineRow>
        <TimelineRow>废除原来的技能系统，用装备系统代替。</TimelineRow>
        <TimelineRow>现在所有英雄开启技能后都会回血了。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/06/12">
        <TimelineRow>15 本新增 61 ~ 65 级大守护者。</TimelineRow>
        <TimelineRow>大守护者现在不太会跟随野蛮人和弓箭手了。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2023/05/15">
        <TimelineRow>在重新部署召回的大守护者时，大守护者将重新计算跟随军队。</TimelineRow>
        <TimelineRow>增加雷霆泰坦的「大守护者权重」，让大守护者更有可能跟随他们。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/10/10">
        <TimelineRow>15 本推出，并在 15 本新增 56 ~ 60 级大守护者。</TimelineRow>
        <TimelineRow>2 ~ 55 级大守护者的升级费用减少。</TimelineRow>
        <TimelineRow>6 ~ 50 级大守护者的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2022/02/15">
        <TimelineRow>英雄引入额外生命值概念，战斗时先消耗额外生命值再消耗本身的生命值，也就是说你可以连续打两场。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/12/09">
        <TimelineRow>1 ~ 20，22 ~ 40 级大守护者的升级花费降低。</TimelineRow>
        <TimelineRow>2 ~ 15 级大守护者的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/29">
        <TimelineRow>降低了大守护者跟随战宠的几率。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/04/12">
        <TimelineRow>现在英雄可以搭配战宠了。</TimelineRow>
        <TimelineRow>14 本推出，并在 14 本新增 51 ~ 55 级大守护者。</TimelineRow>
        <TimelineRow>修复了其他友军都没攻打城墙的情况下，大守护者会去攻打城墙的问题。</TimelineRow>
        <TimelineRow>如果在大守护者受到伤害的同时激活永恒书卷技能，他可以免疫伤害，不会再出现一个黑雷把血炸空的同时开大的情况了。</TimelineRow>
        <TimelineRow>1 ~ 10 级大守护者的升级花费降低。</TimelineRow>
        <TimelineRow>2 ~ 8 级大守护者的升级时间减少。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2021/01/20">
        <TimelineRow>大守护者降低跟随攻城滚木车和攻城飞艇的优先级，以减少他跟随这两种攻城机器冲向敌方大本营并陷入危险的几率。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/12/07">
        <TimelineRow>战斗结束时，如果英雄的技能尚未使用，英雄会自动恢复一部分生命值（数值等于他们使用技能时可恢复的生命值）。这样就缩短了英雄的冷却时间，让他们可以更快投入下一场战斗！</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/10/12">
        <TimelineRow>更新后，英雄会一直处于防御状态，而且在进行防御后会自动恢复为满血状态。“正在防御”和“正在休息”两种模式间的切换功能已被移除。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/06/22">
        <TimelineRow>所有等级大守护者的恢复时间减少。</TimelineRow>
        <TimelineRow>优化了大守护者的机制，现在他在空中模式时能更有效地跟随部队，不会那么容易分心。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/05/20">
        <TimelineRow>调整大守护者的 AI，降低跟随飞龙和皮卡超人的优先级。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2020/03/30">
        <TimelineRow>调整了大守护者 AI，让他在友军被冻住时反应更合理；如果没有跟随任何友军，他会更频繁地重新选择目标。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/12/09">
        <TimelineRow>13 本推出，并在 13 本新增 41 ~ 50 级大守护者。</TimelineRow>
        <TimelineRow>进攻时，如果英雄技能一直没有被手动开启，英雄在即将被击败时会自动开启英雄技能进行自救。该功能可以在“设置>更多设置”中关闭。</TimelineRow>
        <TimelineRow>如果大守护者在攻击城墙，而他附近的友军全部阵亡，系统将强制他更换目标。</TimelineRow>
        <TimelineRow>略微降低大守护者跟随熔岩猎犬的倾向。</TimelineRow>
        <TimelineRow>大守护者攻击时发射的光束将更像是从法杖射出的，而不是腹部。</TimelineRow>
    </TimelineItem>
    <TimelineItem date="2019/06/18">
        <TimelineRow>12 本新增 31 ~ 40 级大守护者。</TimelineRow>
        <TimelineRow>为了让英雄可以穿上皮肤，继蛮王和女王之后，本次更新之后大守护者也改成了 3D 模型。</TimelineRow>
    </TimelineItem>
    <TimelineItem :historyBottom="true" />
</Timeline>
<p><small>数值核对：2026-10-13 · <a href="https://clashofclans.fandom.com/wiki/Grand_Warden?oldid=625324" target="_blank" rel="noopener noreferrer">部落冲突维基</a>。部分附加字段沿用原记录。</small></p>
