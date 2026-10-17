// Keep revision IDs in source records; readers should open the public article.
export function publicWikiUrl(value) {
    if (!value) return value;
    try {
        const url = new URL(value);
        if (url.hostname !== "clashofclans.fandom.com" || !url.searchParams.has("oldid")) return value;
        url.searchParams.delete("oldid");
        return url.href;
    } catch {
        return value;
    }
}

export function publicWikiLinks(md) {
    const renderLink = md.renderer.rules.link_open || ((tokens, index, options, env, self) => self.renderToken(tokens, index, options));
    md.renderer.rules.link_open = (tokens, index, ...args) => {
        const token = tokens[index];
        const href = token.attrGet("href");
        if (href) token.attrSet("href", publicWikiUrl(href));
        return renderLink(tokens, index, ...args);
    };
    // Authored unit pages also contain raw HTML anchors inside Vue components.
    for (const type of ["html_inline", "html_block"]) {
        const renderHtml = md.renderer.rules[type];
        md.renderer.rules[type] = (...args) => renderHtml(...args).replace(
            /<a\b(?:[^>"']|"[^"]*"|'[^']*')*>/gi,
            tag => tag.replace(/(\shref\s*=\s*)(["'])(.*?)\2/i, (attribute, prefix, quote, href) => {
                const decoded = md.utils.unescapeAll(href);
                const publicUrl = publicWikiUrl(decoded);
                return publicUrl === decoded ? attribute : prefix + quote + md.utils.escapeHtml(publicUrl) + quote;
            })
        );
    }
}
