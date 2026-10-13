import { createContentLoader } from "vitepress";

const villageNames = {
    "upgrade-home": "家乡",
    "upgrade-bh": "夜世界",
    "upgrade-capital": "部落都城",
    "upgrade-temp": "临时单位（历史）"
};

export default createContentLoader("upgrade/*.md", {
    transform(pages) {
        return pages.map(({ url, frontmatter }) => ({
            url,
            title: frontmatter.shownTitle || frontmatter.navTitle || frontmatter.title,
            village: villageNames[frontmatter.module] || "升级数据",
            keywords: [frontmatter.title, frontmatter.navTitle, frontmatter.shownTitle,
                url.replace(/.*\/[0-9a-f]{4}-/, "").replace(/-/g, " ")].join(" ")
        })).sort((a, b) => a.url.localeCompare(b.url));
    }
});
