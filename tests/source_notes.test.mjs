import assert from "node:assert/strict";
import test from "node:test";
import { createMarkdownRenderer } from "vitepress";
import { sourceNotes } from "../docs/.vitepress/theme/assets/source-notes.mjs";

const renderer = createMarkdownRenderer(`${process.cwd()}/docs`, { config: sourceNotes });

test("upgrade pages link section and inline notes to the page footer", async () => {
    const md = await renderer;
    const html = await md.render(
        '<SmallTitle>升级数据</SmallTitle>\n\n<small>来源：[Wiki](https://example.com)</small>\n\n正文<small>补充说明</small>\n\n<small>数值核对：原始来源</small>',
        { relativePath: "upgrade/example.md" },
    );

    assert.match(html, /升级数据<sup class="cp-source-ref"><a id="cp-source-ref-1" href="#cp-source-note-1"/);
    assert.match(html, /正文<sup class="cp-source-ref"><a id="cp-source-ref-2" href="#cp-source-note-2"/);
    assert.match(html, /<li id="cp-source-note-1">来源：<a href="https:\/\/example\.com"/);
    assert.match(html, /<li id="cp-source-note-2">补充说明 .*href="#cp-source-ref-2"/);
    assert.match(html, /<small>数值核对：原始来源<\/small>/);
});

test("other pages retain their ordinary small text", async () => {
    const md = await renderer;
    const html = await md.render("正文<small>普通小字</small>", { relativePath: "sources.md" });
    assert.match(html, /<small>普通小字<\/small>/);
    assert.doesNotMatch(html, /cp-source-note/);
});
