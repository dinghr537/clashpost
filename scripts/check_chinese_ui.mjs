#!/usr/bin/env node
// Run manually after a data import or while preparing a release.
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { dataLabel, factLabel, historyLabel, imageLabel } from "../docs/.vitepress/theme/assets/data-labels.js";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");

export function hasUntranslatedEnglish(value) {
    // X连弩 is the site's established Chinese name, including the letter X.
    return /[A-Za-z]/.test(String(value).replace(/X(?=连弩)/g, ""));
}

export function inspectRecord(data) {
    const labels = [["单位名称", dataLabel(data.title)]];
    for (const table of data.tables) {
        labels.push(["表名", dataLabel(table.title)]);
        table.headers.forEach(value => labels.push(["表头", dataLabel(value)]));
        table.rows.flat().filter(cell => cell.status === "known").forEach(cell => {
            const value = typeof cell.value === "number" && cell.unit !== "seconds"
                ? String(cell.value) : cell.displayInput ?? dataLabel(cell.raw);
            labels.push(["单元格", value], ["单元格提示", dataLabel(cell.raw)]);
        });
    }
    data.facts.forEach(value => labels.push(["能力说明", factLabel(value)]));
    data.notices.forEach(value => labels.push(["备注", dataLabel(value)]));
    data.history.forEach(value => labels.push(["更新历史", historyLabel(value.description)]));
    data.images.filter(image => image.localPath).forEach(image => labels.push(["图片说明", imageLabel(image, data.title)]));
    return { count: labels.length, errors: labels.filter(([, value]) => hasUntranslatedEnglish(value) || /NaN|undefined/.test(value)) };
}

export function checkChineseUI() {
    const dataFolder = path.join(root, "docs/.vitepress/theme/assets/unit-data");
    const errors = [];
    let count = 0;
    const files = fs.readdirSync(dataFolder).filter(file => file.endsWith(".json"));
    for (const file of files) {
        const record = JSON.parse(fs.readFileSync(path.join(dataFolder, file), "utf8"));
        const result = inspectRecord(record);
        count += result.count;
        result.errors.forEach(([type, value]) => errors.push(`${record.unitId} ${type}: ${value}`));
    }
    const pages = path.join(root, "docs/upgrade");
    for (const file of fs.readdirSync(pages).filter(file => file.endsWith(".md"))) {
        const text = fs.readFileSync(path.join(pages, file), "utf8");
        for (const match of text.matchAll(/^(navTitle|shownTitle):\s*"([^"]+)"/gm)) {
            if (hasUntranslatedEnglish(match[2])) errors.push(`${file} ${match[1]}: ${match[2]}`);
        }
    }
    const categories = path.join(pages, "category");
    for (const file of fs.readdirSync(categories).filter(file => file.endsWith(".md"))) {
        const text = fs.readFileSync(path.join(categories, file), "utf8");
        for (const match of text.matchAll(/<ListItem\s+name="([^"]+)"/g)) {
            if (hasUntranslatedEnglish(match[1])) errors.push(`category/${file}: ${match[1]}`);
        }
    }
    return { units: files.length, labels: count, errors: [...new Set(errors)] };
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
    const result = checkChineseUI();
    if (result.errors.length) {
        console.error(`中文展示检查失败：${result.errors.length} 项需要补译。`);
        result.errors.forEach(error => console.error(error));
        process.exitCode = 1;
    } else {
        console.log(`中文展示检查通过：${result.units} 个同步单位，${result.labels} 个展示文本；目录及页面名称无漏译。`);
    }
}
