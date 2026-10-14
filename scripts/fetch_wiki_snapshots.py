#!/usr/bin/env python3
"""Manually cache pinned public Wiki revisions for a requested data update."""
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlencode
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
NEW_UNITS = {
    '0842-Logger': ('Logger', '滚木守卫', 'home_heroes'),
    '0013-Ruin-Witch': ('Ruin Witch', '废墟女巫', 'home_tech'),
    '0014-Ruin-Knight': ('Ruin Witch/Ruin Knight', '废墟骑士', 'home_tech'),
    '0187-Angry-Spell': ('Angry Spell', '愤怒法术', 'home_tech'),
    '0747-Monolith-Arrow': ('Monolith Arrow', '擎天箭矢', 'home_heroes'),
    '07e5-Revenge-Deck': ('Revenge Deck', '反击卡组', 'home_heroes'),
    '0726-Portal-Pendant': ('Portal Pendant', '传送吊坠', 'home_heroes'),
    '0803-Prospector': ('Prospector', '探矿者', 'home_tech'),
    '0906-Crafted-Air-Bombs': ('Air Bombs/Home Village', '精工空中炸弹发射器', 'crafted_buildings'),
    '0907-Crafted-Lava-Launcher': ('Lava Launcher/Home Village', '精工熔岩发射器', 'crafted_buildings'),
    '0908-Crafted-Roaster': ('Roaster/Home Village', '精工炙热熔炉', 'crafted_buildings'),
    '0909-Cake-A-Pult': ('Cake-A-Pult', '蛋糕投掷器', 'crafted_buildings'),
    '090a-Hero-Hunter': ('Hero Hunter', '英雄猎台', 'crafted_buildings'),
    '090b-Hot-Candle': ('Hot Candle', '火热蜡烛', 'crafted_buildings'),
    '0e1c-Yeti-Undertaker': ('Yeti Undertaker', '送葬者大雪怪', 'temp_troops'),
    '0e1d-Totem-Thrower': ('Totem Thrower', '图腾投手', 'temp_troops'),
    '0e1e-Elephant-Rider': ('Elephant Rider', '大象骑士', 'temp_troops'),
}


def inventory():
    items = []
    for page in sorted((ROOT / 'docs/upgrade').glob('*.md')):
        text = page.read_text(encoding='utf-8-sig')
        wiki = re.search(r'^wiki:\s*(\S+)', text, re.M)
        if not wiki:
            continue
        title = unquote(wiki[1].split('/wiki/', 1)[1]).replace('_', ' ')
        items.append({'unitId': page.stem, 'title': title, 'new': False})
    for unit_id, (title, label, folder) in NEW_UNITS.items():
        if not any(item['unitId'] == unit_id for item in items):
            items.append({'unitId': unit_id, 'title': title, 'label': label, 'folder': folder, 'new': True})
    return items


def fetch(title, cache):
    path = cache / (hashlib.sha256(title.encode()).hexdigest()[:20] + '.json')
    if path.exists():
        data = json.loads(path.read_text())
        if 'parse' in data:
            return data, path
    query = urlencode({'action': 'parse', 'page': title, 'prop': 'text|revid', 'redirects': 1, 'format': 'json'})
    request = Request('https://clashofclans.fandom.com/api.php?' + query, headers={'User-Agent': 'ClashpostManualDataSync/0.1'})
    with urlopen(request, timeout=30) as response:
        data = json.load(response)
    if 'parse' not in data:
        raise ValueError(data.get('error', {}).get('info', 'Wiki parse result missing'))
    path.write_text(json.dumps(data, ensure_ascii=False))
    return data, path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--cache', type=Path, required=True)
    parser.add_argument('--workers', type=int, default=6)
    args = parser.parse_args()
    args.cache.mkdir(parents=True, exist_ok=True)
    items = inventory()
    by_title = {}
    for item in items:
        by_title.setdefault(item['title'], []).append(item)
    results, failures = [], []
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        jobs = {pool.submit(fetch, title, args.cache): title for title in by_title}
        for index, future in enumerate(as_completed(jobs), 1):
            title = jobs[future]
            try:
                data, path = future.result()
                for item in by_title[title]:
                    results.append({**item, 'snapshot': str(path), 'revision': data['parse']['revid'], 'resolvedTitle': data['parse']['title']})
            except Exception as error:
                failures.extend({**item, 'error': str(error)} for item in by_title[title])
            if index % 20 == 0 or index == len(jobs):
                print(f'Wiki revisions cached: {index}/{len(jobs)}; unit failures: {len(failures)}', flush=True)
    result = {'fetchedAt': datetime.now().isoformat(timespec='seconds'), 'units': sorted(results, key=lambda item: item['unitId']), 'failures': failures}
    (args.cache / 'inventory.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'units': len(results), 'failures': failures}, ensure_ascii=False), flush=True)


if __name__ == '__main__':
    main()
