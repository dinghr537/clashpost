import { defineConfig, HeadConfig } from "vitepress";
import { resolve } from 'node:path'

// https://vitepress.dev/reference/site-config
export default defineConfig({
    title: "部落驿站",
    description: "部落冲突升级数据查询：升级费用、时间与前置条件。",
    lang: "zh-Hans-CN",
    cleanUrls: true,
    ignoreDeadLinks: true,
    head: [
        ["meta", { name: "format-detection", content: "telephone=no"}],
        ["link", { rel: "icon", href: "/favicon.svg", type: "image/svg+xml" }]
    ],
    transformHead: ({ pageData }) => {
        const head: HeadConfig[] = [];
        if (pageData.frontmatter.robots) {
            head.push(["meta", { name: "robots", content: pageData.frontmatter.robots }]);
        }
        const canonical = pageData.frontmatter.canonical;
        if (canonical === "/") {
            head.push(["link", { rel: "canonical", content: "https://clashpost.com" }]);
        } else {
            head.push(["link", { rel: "canonical", content: "https://clashpost.com" + canonical }]);
        }
        return head;
    },
    markdown: {
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
        hostname: "https://clashpost.com",
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