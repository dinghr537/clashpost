import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { historyLabel } from "../docs/.vitepress/theme/assets/data-labels.js";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const read = name => JSON.parse(fs.readFileSync(path.join(root, name), "utf8"));
const normalize = text => text.replace(/<[^>]*>/g, "").replace(/&amp;/g, "&").replace(/[\s，。；：、,.!?！？·「」]/g, "");

export function historyGaps(record, page, paraphrases = []) {
    const errors = [];
    for (const event of record.history) {
        const date = event.date.replaceAll("-", "/");
        const blocks = [...page.matchAll(/<TimelineItem date="([^"]+)">([\s\S]*?)<\/TimelineItem>/g)];
        const block = blocks.find(match => match[1] === date)?.[2];
        const reviewed = paraphrases.find(item => item.unitId === record.unitId && item.date === event.date && item.description === event.description);
        const expected = reviewed?.requiredText || historyLabel(event.description);
        if (!block || !normalize(block).includes(normalize(expected))) {
            errors.push(`${record.unitId} ${event.date}: ${event.description}`);
        }
    }
    return errors;
}

export function checkUpdateHistory() {
    const directory = "docs/.vitepress/theme/assets/unit-data";
    const paraphrases = read("scripts/history-paraphrases.json");
    const supplements = read("scripts/supplemental-history.json");
    const records = fs.readdirSync(path.join(root, directory)).map(file => read(`${directory}/${file}`));
    const errors = [];
    for (const record of records) {
        const page = fs.readFileSync(path.join(root, `docs/upgrade/${record.unitId}.md`), "utf8");
        errors.push(...historyGaps(record, page, paraphrases));
    }
    for (const event of supplements) {
        const record = records.find(record => record.unitId === event.unitId);
        if (!record?.history.some(saved => saved.date === event.date && saved.description === event.description && saved.sourceUrl === event.sourceUrl)) {
            errors.push(`${event.unitId}: official supplement missing: ${event.date}`);
        }
    }
    return { units: records.length, events: records.reduce((sum, record) => sum + record.history.length, 0), errors };
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
    const result = checkUpdateHistory();
    console.log(JSON.stringify(result, null, 2));
    if (result.errors.length) process.exitCode = 1;
}
