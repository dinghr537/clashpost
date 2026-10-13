# 升级数据结构约定

这是后续迁移的结构约定，当前页面仍以原 Markdown 为数据来源。差异报告是核对产物，不直接作为页面的数据文件。

## 单位与等级

- `unitId` 沿用页面单位 ID，例如 `0200-Barbarian-King`。
- `village` 区分 `home`、`builder`、`capital`。
- `mode` 标识标准、改装等模式；不同模式分开记录。
- 等级保存在 `levels`。每个等级拥有 `variants`，没有分支条件也明确提供一个默认变体。
- 同等级可以有多个互斥条件变体，以 `variantId` 区分，不能仅按等级去重。

## 字段状态

数值字段使用 `{ "status": "known", "value": 120 }`，数值为非负整数。`value: 0` 是明确的零，不等于未知或不适用。

不适用使用 `{ "status": "not_applicable", "value": null }`；未取得或未解决使用 `{ "status": "unknown", "value": null }`。取自页面时可保留 `raw` 原文与简短 `note`，不能仅用 `null` 代表所有情况。

## 费用、时间与前置条件

- `upgradeCosts.status` 为 `known` 时，`value` 是资源到数量的映射，例如 `{ "Shiny_Ore": 240, "Glowy_Ore": 20 }`，表示两种资源同时需要。零消耗用数量 `0` 明确表达，缺失资源不能自动补零。
- 整体费用未知或不适用时，分别用对应状态和 `value: null`。只有部分资源已知时，整体仍标 `unknown`，可在 `knownParts` 记录已取得的资源数量，避免展示成完整费用。
- `upgradeTimeSeconds` 存整数秒数。瞬时升级使用已知的 `0`，没有时间字段的适用性需要确认后标记，不能直接从空白推断。
- `requirements` 保存升级前置条件，例如英雄殿堂、实验室、铁匠铺和大本等级，各条件也保留字段状态。
- `appliesWhen` 描述变体适用条件；它与升级前置条件分开。例如蛮王一级属性可能随当前大本等级变化。
- 来源直接给出的前置条件记录 `basis: "source"`。确需从其他表推导时，记录 `basis: "derived"` 和推导依据，不让推导条件看起来像来源原值。

示例：地震金靴 3 级的多资源费用与时间字段。这里只示范结构，数值取自现有仓库，尚未同步新来源：

```json
{
  "unitId": "0702-Earthquake-Boots",
  "village": "home",
  "mode": "default",
  "sync": {
    "sourceUrl": null,
    "syncedOn": null,
    "scope": "legacy upgrade table",
    "status": "legacy"
  },
  "levels": [
    {
      "level": 3,
      "variants": [
        {
          "variantId": "default",
          "appliesWhen": {},
          "upgradeCosts": {
            "status": "known",
            "value": { "Shiny_Ore": 240, "Glowy_Ore": 20 }
          },
          "upgradeTimeSeconds": {
            "status": "unknown",
            "value": null,
            "note": "旧表没有时间列；迁移时确认是否不适用。"
          },
          "requirements": {
            "blacksmithLevel": { "status": "known", "value": 1, "basis": "source" },
            "townHallLevel": { "status": "known", "value": 8, "basis": "source" }
          }
        }
      ]
    }
  ]
}
```

## 同步信息与发布检查

`sync` 至少记录 `sourceUrl`、`syncedOn`、`scope` 和 `status`（`legacy`、`partial`、`synced`）。`synced` 表示这一范围正确同步了指定来源，不表示独立验证了游戏数值。可取得修订号或版本时补充记录。

若同一单位部分等级或字段采用不同来源，其变体或字段应覆盖默认 `sync` 信息，避免整页被误标为全部同步。实际迁移时先检查单位和模式、等级与变体组合、费用资源、字段状态与数值是否合法，再生成页面。
