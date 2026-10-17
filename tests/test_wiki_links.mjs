import assert from "node:assert/strict";
import test from "node:test";
import { createMarkdownRenderer } from "vitepress";
import { publicWikiUrl, publicWikiLinks } from "../docs/.vitepress/theme/assets/wiki-links.mjs";

test("public article links retain the section and other parameters", () => {
    assert.equal(publicWikiUrl("https://clashofclans.fandom.com/wiki/Portal_Pendant?oldid=625662#Summary"), "https://clashofclans.fandom.com/wiki/Portal_Pendant#Summary");
    assert.equal(publicWikiUrl("https://clashofclans.fandom.com/wiki/Test?lang=zh&oldid=1&x=2#History"), "https://clashofclans.fandom.com/wiki/Test?lang=zh&x=2#History");
    for (const url of ["/upgrade/test?oldid=1", "https://example.com/?oldid=1", undefined]) assert.equal(publicWikiUrl(url), url);
});

test("Markdown and authored HTML links open articles without rewriting code or source text", async () => {
    const md = await createMarkdownRenderer(process.cwd(), { config: publicWikiLinks });
    const href = "https://clashofclans.fandom.com/wiki/Portal_Pendant?oldid=625662#Summary";
    const source = `[来源](${href})\n\n<p><small><a href="${href}">修订 625662</a></small></p>\n\n<TimelineRow><a href='https://clashofclans.fandom.com/wiki/Test?oldid=1&amp;x=2'>来源</a></TimelineRow>\n\n\`${href}\``;
    const html = md.render(source);
    assert.equal((html.match(/href="https:\/\/clashofclans.fandom.com\/wiki\/Portal_Pendant#Summary"/g) || []).length, 2);
    assert.ok(html.includes("href='https://clashofclans.fandom.com/wiki/Test?x=2'"));
    assert.ok(html.includes(`<code>${href}</code>`));
    assert.ok(source.includes("?oldid=625662"));
});
