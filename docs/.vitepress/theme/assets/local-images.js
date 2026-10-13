import originalManifest from "./original-image-manifest.json";

export const imagePlaceholder = "/images/unavailable.svg";

export function resolveImage(src) {
    if (!src) return imagePlaceholder;
    if (src.startsWith("/images/") || src.startsWith("data:")) return src;
    if (/^https?:/.test(src) && !src.startsWith("https://static.clashpost.com/")) return src;
    const originalPath = src.replace("https://static.clashpost.com", "").split("?")[0];
    return originalManifest[originalPath]
        || originalManifest[originalPath.replace(/\.(png|jpe?g)$/i, ".webp")]
        || imagePlaceholder;
}
