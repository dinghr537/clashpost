import { defineConfig, HeadConfig } from "vitepress";
import { resolve } from 'node:path'
import { publicWikiLinks } from './theme/assets/wiki-links.mjs'

const siteUrl = "https://cocpost.com";

// https://vitepress.dev/reference/site-config
export default defineConfig({
    title: "部落驿站",
    description: "部落冲突升级数据查询：升级费用、时间与前置条件。",
    lang: "zh-Hans-CN",
    cleanUrls: true,
    ignoreDeadLinks: true,
    head: [
        ["meta", { name: "format-detection", content: "telephone=no"}],
        ["link", { rel: "icon", href: "/favicon.ico?v=20261017", sizes: "32x32" }],
        ["link", { rel: "icon", href: "/favicon.svg?v=20261017", type: "image/svg+xml", sizes: "any" }],
        ["link", { rel: "apple-touch-icon", href: "/apple-touch-icon.png", sizes: "180x180" }],
        ["link", { rel: "manifest", href: "/manifest.webmanifest" }]
    ],
    transformHead: ({ pageData }) => {
        const head: HeadConfig[] = [];
        if (pageData.frontmatter.robots) {
            head.push(["meta", { name: "robots", content: pageData.frontmatter.robots }]);
        }
        const canonical = pageData.frontmatter.canonical;
        if (canonical) {
            head.push(["link", { rel: "canonical", href: new URL(canonical, siteUrl).href }]);
        }
        return head;
    },
    markdown: {
        config: publicWikiLinks,
        math: true,
        image: {
            lazyLoad: true
        },
        externalLinks: {
            target: "_blank",
            rel: "noopener noreferrer"
        }
    },
    sitemap: {
        hostname: siteUrl,
        transformItems: (items) => {
            const excludedUrls = [
                "/faq",
                "/settings",
                "p/260",
                "p/1828",
            ]
            const filteredItems = items.filter(item => {
                const itemUrl = item.url;
                const notExcluded = !excludedUrls.includes(itemUrl);
                const notPostCollection = !itemUrl.match(/(p\/category|p\/author|p\/page)/g);
                return notExcluded && notPostCollection;
            });
            return filteredItems;
        }
    },
    vite: {
        server: { watch: { usePolling: true, interval: 500 } },
        build: {
            target: ["es2020", "chrome71", "edge79", "firefox75", "safari13"]
        },
        resolve: {
            alias: {
                "@": resolve(import.meta.dirname, "./theme"),
                "#": resolve(import.meta.dirname, "../..")
            }
        }
    }
});
