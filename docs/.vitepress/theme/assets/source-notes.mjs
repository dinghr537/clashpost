// Move short source notes out of upgrade-page content while keeping each
// reference beside the relevant section or sentence. The Markdown itself stays
// intact, so source history and attribution remain reviewable in the repository.
export function sourceNotes(md) {
    md.core.ruler.before("normalize", "upgrade_source_notes", state => {
        if (state.inlineMode || !/^upgrade\/[^/]+\.md$/.test(state.env.relativePath || "")) return;

        const source = state.src;
        const pattern = /(?:<p>\s*)?<small>([\s\S]*?)<\/small>(?:\s*<\/p>)?/g;
        const notes = [];
        let text = "";
        let end = 0;
        for (const match of source.matchAll(pattern)) {
            // The existing Wiki attribution already sits at the foot of the page.
            if (match[1].trimStart().startsWith("数值核对：")) continue;

            text += source.slice(end, match.index);
            end = match.index + match[0].length;
            const number = notes.length + 1;
            const reference = `<sup class="cp-source-ref"><a id="cp-source-ref-${number}" href="#cp-source-note-${number}" aria-label="查看资料说明 ${number}">${number}</a></sup>`;
            const lineStart = source.lastIndexOf("\n", match.index - 1) + 1;
            const linePrefix = source.slice(lineStart, match.index).trim();
            const headingEnd = text.lastIndexOf("</SmallTitle>");
            const headingStart = text.lastIndexOf("<SmallTitle>");
            if (!linePrefix && headingStart >= 0 && headingEnd > headingStart) {
                text = text.slice(0, headingEnd) + reference + text.slice(headingEnd);
            } else {
                text += reference;
            }
            notes.push(match[1].trim());
        }
        if (!notes.length) return;

        text += source.slice(end);
        const entries = notes.map((note, index) => {
            const number = index + 1;
            const content = md.renderInline(note, state.env);
            return `<li id="cp-source-note-${number}">${content} <a class="cp-source-back" href="#cp-source-ref-${number}" aria-label="返回说明 ${number} 的位置">↩</a></li>`;
        }).join("\n");
        state.src = `${text}\n\n<section class="cp-source-notes" aria-label="资料与说明">\n<p class="cp-source-notes-title">资料与说明</p>\n<ol>\n${entries}\n</ol>\n</section>\n`;
    });
}
