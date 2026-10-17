#!/usr/bin/env python3
"""Manually download only missing, exact-unit Wiki images from a sync preview."""
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import quote, unquote, urlparse
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / 'docs/.vitepress/theme/assets/supplemental-image-manifest.json'
SOURCES = ROOT / 'docs/public/images/wiki-sources.json'


def source_file_page(url):
    """Link to file metadata for rights review; this does not verify a license."""
    parsed = urlparse(url)
    match = re.match(r'/clashofclans/images/[^/]+/[^/]+/([^/]+)', parsed.path)
    if parsed.hostname == 'static.wikia.nocookie.net' and match:
        return 'https://clashofclans.fandom.com/wiki/File:' + quote(unquote(match[1]), safe='')
    return None


def download(record, image):
    filename = re.sub(r'[^A-Za-z0-9_.-]', '_', image['name'])
    filename = hashlib.sha256(image['url'].encode()).hexdigest()[:10] + '-' + filename
    local = '/images/wiki/' + record['unitId'] + '/' + filename
    path = ROOT / 'docs/public' / local.lstrip('/')
    if not path.exists():
        request = Request(image['url'], headers={'User-Agent': 'ClashpostManualImageSync/0.1'})
        with urlopen(request, timeout=30) as response:
            content_type = response.headers.get('Content-Type', '')
            data = response.read()
        if not content_type.startswith('image/') or not data:
            raise ValueError('Source did not return an image')
        # The response must be an actual supported bitmap/vector, not an HTML error page.
        if not (data.startswith(b'\x89PNG\r\n\x1a\n') or data.startswith(b'\xff\xd8') or
                data.startswith(b'GIF8') or (data[:4] == b'RIFF' and data[8:12] == b'WEBP') or b'<svg' in data[:300]):
            raise ValueError('Unrecognised image signature')
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
    return image['logicalPath'], local, {'unitId': record['unitId'], 'sourceUrl': image['url'],
            'sourcePage': record['sync']['revisionUrl'], 'sourceFilePage': source_file_page(image['url']),
            'importedOn': record['sync']['syncedOn']}


def main():
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument('--preview', type=Path, required=True)
    cli.add_argument('--workers', type=int, default=6)
    args = cli.parse_args()
    records = json.loads(args.preview.read_text())
    manifest = json.loads(MANIFEST.read_text()) if MANIFEST.exists() else {}
    sources = json.loads(SOURCES.read_text()) if SOURCES.exists() else {}
    wanted = {image['logicalPath']: (record, image) for record in records for image in record['images'] if not image['localPath']}
    failures = []
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(download, record, image): logical for logical, (record, image) in wanted.items()}
        for index, future in enumerate(as_completed(futures), 1):
            try:
                logical, local, source = future.result()
                manifest[logical] = local
                sources[local] = source
            except Exception as error:
                failures.append({'image': futures[future], 'error': str(error)})
            if index % 30 == 0 or index == len(futures):
                print(f'Images: {index}/{len(futures)}; failures: {len(failures)}', flush=True)
    MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
    SOURCES.write_text(json.dumps(sources, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'downloadedOrCached': len(wanted)-len(failures), 'failures': failures}, ensure_ascii=False, indent=2))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
