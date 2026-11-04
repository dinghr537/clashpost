import { defineConfig, HeadConfig } from "vitepress";
import { appendFile, readFile } from 'node:fs/promises'
import { createRequire } from 'node:module'
import { dirname, resolve } from 'node:path'
import { publicWikiLinks } from './theme/assets/wiki-links.mjs'

const siteUrl = "https://cocpost.com";
const require = createRequire(import.meta.url);
const mathRendererPackage = require.resolve("markdown-it-mathjax3/package.json");
const mathRendererRequire = createRequire(mathRendererPackage);

// https://vitepress.dev/reference/site-config
export default defineConfig({
    title: "部落驿站",
    description: "部落冲突升级数据查询：升级费用、时间与前置条件。",
    lang: "zh-Hans-CN",
    cleanUrls: true,
    ignoreDeadLinks: true,
    buildEnd: async ({ outDir }) => {
        // MathJax produces SVG in the HTML, so Vite's JS-bundle license list misses it.
        const packages = [mathRendererPackage, mathRendererRequire.resolve("mathjax-full/package.json")];
        for (const packagePath of packages) {
            const { name, version, license } = JSON.parse(await readFile(packagePath, "utf8"));
            const licenseText = await readFile(resolve(dirname(packagePath), "LICENSE"), "utf8");
            await appendFile(resolve(outDir, "third-party-licenses.txt"),
                `\n## ${name} - ${version} (${license})\n\n${licenseText.trim()}\n`);
        }
    },
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
            target: ["es2020", "chrome71", "edge79", "firefox75", "safari13"],
            license: { fileName: "third-party-licenses.txt" }
        },
        resolve: {
            alias: {
                "@": resolve(import.meta.dirname, "./theme"),
                "#": resolve(import.meta.dirname, "../..")
            }
        }
    }
});
