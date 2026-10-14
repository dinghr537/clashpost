import assert from "node:assert/strict";
import test from "node:test";
import { dataLabel } from "../docs/.vitepress/theme/assets/data-labels.js";
import { checkChineseUI, hasUntranslatedEnglish, inspectRecord } from "../scripts/check_chinese_ui.mjs";

test("localization preserves amounts, durations, dimensions and troop counts", () => {
    assert.equal(dataLabel("800K / 1M"), "800000 / 1000000");
    assert.equal(dataLabel("1m 30s"), "1分 30秒");
    assert.equal(dataLabel("3x3"), "3×3");
    assert.equal(dataLabel("x1"), "×1");
    assert.equal(dataLabel("1.7s / 20%"), "1.7秒 / 20%");
    assert.equal(dataLabel("Troops Spawned / P.E.K.K.As"), "召唤数量 / 皮卡超人");
});

test("new English source fields fail the release language check", () => {
    const data = { title: "废墟女巫", tables: [{ title: "Statistics", headers: ["New Untranslated Field"], rows: [] }], facts: [], history: [], images: [], notices: [] };
    assert.deepEqual(inspectRecord(data).errors, [["表头", "New Untranslated Field"]]);
    assert.equal(hasUntranslatedEnglish("X连弩"), false);
    assert.equal(hasUntranslatedEnglish("New Ability"), true);
});

test("all current source records and navigation labels render in Chinese", () => {
    const result = checkChineseUI();
    assert.ok(result.units >= 357);
    assert.deepEqual(result.errors, []);
});
