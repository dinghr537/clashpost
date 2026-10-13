#!/usr/bin/env python3
"""Copy original clashpost image files exported with the browser pageAssets tool."""
import argparse
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse, unquote

ROOT = Path(__file__).resolve().parents[1]

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--directory', type=Path, required=True)
    parser.add_argument('--since-manifest', type=Path, required=True)
    args = parser.parse_args()
    since = args.since_manifest.stat().st_mtime
    manifest_path = ROOT / 'docs/.vitepress/theme/assets/original-image-manifest.json'
    sources_path = ROOT / 'docs/public/images/original-sources.json'
    mapping = json.loads(manifest_path.read_text()) if manifest_path.exists() else {}
    sources = json.loads(sources_path.read_text()) if sources_path.exists() else {}
    for metadata in args.directory.glob('*/manifest.json'):
        if metadata.stat().st_mtime < since:
            continue
        for asset in json.loads(metadata.read_text()).get('assets', []):
            url = asset.get('url', '')
            parsed = urlparse(url)
            if parsed.scheme != 'https' or parsed.hostname != 'static.clashpost.com' or asset.get('kind') != 'image':
                continue
            relative = Path(unquote(parsed.path).lstrip('/'))
            if '..' in relative.parts:
                raise ValueError('Invalid image path')
            source = Path(asset['path'])
            if not source.is_file():
                continue
            target = ROOT / 'docs/public/images/original' / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, target)
            mapping[parsed.path] = '/images/original/' + relative.as_posix()
            sources[parsed.path] = {'sourceUrl': url, 'localPath': mapping[parsed.path],
                                    'importedAt': datetime.now(timezone.utc).isoformat(timespec='seconds')}
    manifest_path.write_text(json.dumps(mapping, ensure_ascii=False, indent=2)+'\n')
    sources_path.write_text(json.dumps(sources, ensure_ascii=False, indent=2)+'\n')
    print(f'Original website images stored locally: {len(mapping)}')

if __name__ == '__main__':
    main()
