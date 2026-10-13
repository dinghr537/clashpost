#!/usr/bin/env python3
"""Audit local originals and report unresolved primary image references, offline."""
import argparse
import json
import re
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HOST = 'https://static.clashpost.com'


class ImageReferences(HTMLParser):
    def __init__(self, folder):
        super().__init__()
        self.folder = folder
        self.containers = []
        self.references = set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        folder = attrs.get('folder') or attrs.get('imgfolder') or self.folder
        if tag in ('unitimggroup', 'listitems'):
            self.containers.append(folder)
        src = attrs.get('imgsrc') or (attrs.get('src') if tag == 'pic' else None)
        if not src:
            return
        if src.startswith(HOST):
            self.references.add(src[len(HOST):])
        elif src.startswith('/upgrade/'):
            self.references.add(src)
        elif tag in ('unitimg', 'listitem', 'unitinfo'):
            if tag != 'unitinfo' and self.containers:
                folder = self.containers[-1]
            self.references.add(f'/upgrade/{folder}/{src}')

    def handle_endtag(self, tag):
        if tag in ('unitimggroup', 'listitems') and self.containers:
            self.containers.pop()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    mapping = json.loads((ROOT / 'docs/.vitepress/theme/assets/original-image-manifest.json').read_text())
    references = {}
    pages = list((ROOT / 'docs/upgrade').rglob('*.md')) + [ROOT / 'docs/index.md', ROOT / 'docs/upgrade.md']
    for page in pages:
        text = page.read_text(encoding='utf-8-sig')
        folder = re.search(r'^imgFolder:\s*(.+)$', text, re.M)
        images = ImageReferences(folder.group(1).strip() if folder else '')
        images.feed(text)
        for image in images.references:
            references.setdefault(image, set()).add(str(page.relative_to(ROOT)))
        resources = re.findall(r'"icon"\s*:\s*"([^"]+)"|resourceType="([^"]+)"', text)
        for icon, property_resource in resources:
            for resource in (icon or property_resource).split(','):
                references.setdefault(f'/resources/{resource.strip()}.png', set()).add(str(page.relative_to(ROOT)))
    missing = []
    for image, pages in sorted(references.items()):
        local = mapping.get(image) or mapping.get(re.sub(r'\.(png|jpe?g)$', '.webp', image, flags=re.I))
        if not local:
            missing.append({'sourceUrl': HOST + image, 'pages': sorted(pages)})
    broken_files = [local for local in mapping.values() if not (ROOT / 'docs/public' / local.lstrip('/')).is_file()]
    report = {'originalFiles': len(mapping), 'primaryReferences': len(references),
              'resolvedReferences': len(references) - len(missing), 'missing': missing,
              'brokenLocalFiles': sorted(set(broken_files))}
    if args.output:
        args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if broken_files:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
