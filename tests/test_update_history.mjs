import assert from "node:assert/strict";
import test from "node:test";
import { historyGaps, checkUpdateHistory } from "../scripts/check_update_history.mjs";

test("a date alone cannot hide a missing change on the same day", () => {
    const record = { unitId: "example", history: [{ date: "2026-07-14", description: "生命值降低。" }, { date: "2026-07-14", description: "每秒伤害降低。" }] };
    const page = '<TimelineItem date="2026/07/14"><TimelineRow>生命值降低。</TimelineRow></TimelineItem>';
    assert.deepEqual(historyGaps(record, page), ["example 2026-07-14: 每秒伤害降低。"]);
});

test("all imported and supplementary history reaches the authored pages", () => {
    assert.deepEqual(checkUpdateHistory().errors, []);
});
