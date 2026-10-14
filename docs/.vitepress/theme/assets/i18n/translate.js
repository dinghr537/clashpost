import chinese from "./zh-CN.json" with { type: "json" };

const terms = new Map(Object.entries(chinese.terms).map(([key, value]) => [key.toLowerCase(), value]));
const escape = value => value.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
const keys = Object.keys(chinese.terms).sort((a, b) => b.length - a.length);
const termPattern = new RegExp(`(?<![A-Za-z])(?:${keys.map(escape).join("|")})(?![A-Za-z])`, "gi");
const cache = new Map();

export function dataLabel(input) {
    const value = String(input ?? "");
    if (!/[A-Za-z]/.test(value)) return value;
    if (cache.has(value)) return cache.get(value);
    let result = terms.get(value.toLowerCase());
    if (!result) {
        result = value.replace(/(\d+)x(\d+)/g, "$1×$2")
            .replace(/\b(\d+(?:\.\d+)?)([KM])\b/g, (_, amount, unit) => String(Number(amount) * (unit === "K" ? 1000 : 1000000)))
            .replace(/(\d+) (?:level|levels) higher/gi, "高$1级")
            .replace(/(\d+) (?:level|levels) lower/gi, "低$1级")
            .replace(/(\d+) or more levels higher/gi, "高$1级或更多")
            .replace(/(\d+) or more levels lower/gi, "低$1级或更多")
            .replace(/\bWithin ([\d.]+) tiles of Hero\b/gi, "英雄周围$1格内")
            .replace(/\b(\d+) or higher\b/gi, "$1及以上")
            .replace(/\b([\d.]+) times\b/gi, "$1倍")
            .replace(/\b(\d+) shots\b/gi, "$1发")
            .replace(/\b(\d+) attacks\b/gi, "$1次攻击")
            .replace(/\/d\b/g, "/天");
        result = result.split(" / ").map(part => terms.get(part.toLowerCase()) || part).join(" / ");
        result = result.replace(/\b(.+?) Level Required\b/g, (_, name) => `所需${dataLabel(name)}等级`)
            .replace(/\bLevel (\d+)(\+)?\b/g, (_, level, plus) => `${level}级${plus ? "及以上" : ""}`)
            .replace(/\bAfter ([\d.]+)s\b/g, "$1秒后")
            .replace(/\bDPS after ([\d.]+)s\b/gi, "$1秒后每秒伤害")
            .replace(/\bWall(\d+)\b/g, "$1级城墙")
            .replace(/\bModule ([123]): /g, "模组$1：")
            .replace(termPattern, match => terms.get(match.toLowerCase()));
        result = result.replace(/([\d.]+)\s*tiles?\b/gi, "$1格")
            .replace(/([\d.]+)\s*seconds?\b/gi, "$1秒")
            .replace(/([\d.]+)\s*minutes?\b/gi, "$1分钟")
            .replace(/([\d.]+)\s*hours?\b/gi, "$1小时")
            .replace(/([\d.]+)\s*days?\b/gi, "$1天")
            .replace(/([\d.]+)\s*d\b/gi, "$1天")
            .replace(/([\d.]+)\s*h\b/gi, "$1小时")
            .replace(/([\d.]+)\s*m\b/g, "$1分")
            .replace(/([\d.]+)\s*s\b/gi, "$1秒")
            .replace(/\/hr\b/gi, "/小时")
            .replace(/\b(\d+)x\b/gi, "$1倍")
            .replace(/\bx([\d.]+)\b/gi, "×$1")
            .replace(/\band\b/gi, "和")
            .replace(/\bor\b/gi, "或");
    }
    cache.set(value, result);
    return result;
}

export function factLabel(value) {
    return chinese.facts[value] || dataLabel(value);
}

// Preserve the site's short, line-broken headings instead of flattening Wiki groups.
export function tableHeaderLines(header, columnInfo) {
    const parts = String(header).split(" / ");
    if (parts[0] === "Upgrade Cost" && columnInfo?.icon) return ["升级费用"];
    if (header === "Ability Attributes / Damage per Shot Increase") return ["技能状态下", "每次伤害增加"];
    if (parts[0] === "Ability Attributes") return ["技能", ...parts.slice(1).map(dataLabel)];
    if (/^Hero Boosts?$/.test(parts[0])) {
        return ["英雄", ...parts.slice(1).map(part => /^(Damage per Second Increase|DPS Increase)$/.test(part) ? "秒伤增加" : dataLabel(part))];
    }
    return parts.flatMap(part => {
        const label = dataLabel(part);
        return /^所需.+等级$/.test(label) ? ["所需", label.slice(2)] : [label];
    });
}

export function historyLabel(value) {
    return chinese.history[value] || dataLabel(value);
}

export function imageLabel(image, unitTitle) {
    if (!/[A-Za-z]/.test(image.alt)) return image.alt;
    const name = dataLabel(unitTitle);
    const filename = image.name.replace(/\.(?:png|jpe?g|webp)$/i, "");
    const suffix = filename.match(/(\d+(?:[-_]\d+)*)$/);
    return suffix ? `${name} · 外观 ${suffix[1].replaceAll("_", "-")}` : name;
}
