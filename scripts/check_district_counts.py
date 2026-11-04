#!/usr/bin/env python3
"""Compare Clan Capital district counts with saved source tables, offline."""
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
DISTRICTS = {
    '野蛮人兵营': 'Barbarian Camp', '法师山谷': 'Wizard Valley',
    '气球环礁': 'Balloon Lagoon', '建筑工人工坊': "Builder's Workshop",
    '飞龙悬崖': 'Dragon Cliffs', '戈仑石场': 'Golem Quarry',
    '骷髅公园': 'Skeleton Park', '哥布林矿井': 'Goblin Mines',
}


def compare_district_page(unit, text, record):
    blocks = re.findall(r'<DistrictTable\b[^>]*>(.*?)</DistrictTable>', text, re.S)
    result = {'countBlocks': 0, 'cells': 0, 'otherBlocks': 0, 'errors': [], 'uncompared': []}
    sources = [table for table in record.get('tables', [])
               if table['headers'] and table['headers'][0] == 'Number Available'
               and any(h.startswith('District Hall Level / ') for h in table['headers'])]
    if len(sources) > 1:
        raise ValueError('multiple district-count source tables')
    source = sources[0] if sources else None
    source_rows = {row[0]['raw']: row[1:] for row in source['rows']} if source else {}
    shown = set()
    for block in blocks:
        lines = re.findall(r'^\s*\|[^\n]*', block, re.M)
        grid = [[cell.strip() for cell in line.strip().strip('|').split('|')] for line in lines]
        if len(grid) < 3:
            result['uncompared'].append(f'{unit}: empty district table')
            continue
        # Wall upgrade costs also use DistrictTable but are not building counts.
        if grid[0][0] == '子城名称':
            result['otherBlocks'] += 1
            continue
        if grid[0][0] or not all(level.isdigit() for level in grid[0][1:]):
            result['uncompared'].append(f'{unit}: unrecognized district table header')
            continue
        result['countBlocks'] += 1
        if not source:
            result['uncompared'].append(f'{unit}: no saved district-count table')
            continue
        levels = [int(level) for level in grid[0][1:]]
        for row in grid[2:]:
            district = DISTRICTS.get(row[0])
            if not district:
                result['uncompared'].append(f'{unit}: unknown district {row[0]}')
                continue
            if len(row) != len(grid[0]):
                result['errors'].append(f'{unit}: wrong column count for {district}')
                continue
            if district in shown:
                result['errors'].append(f'{unit}: duplicate district {district}')
                continue
            shown.add(district)
            if district not in source_rows:
                result['uncompared'].append(f'{unit}: {district} absent from source')
                continue
            available = {int(header.rsplit('/', 1)[1]): cell['raw'].strip()
                         for header, cell in zip(source['headers'][1:], source_rows[district])
                         if header.startswith('District Hall Level / ')}
            for level, value in zip(levels, row[1:]):
                raw = available.get(level, '').replace(',', '').strip()
                displayed = value.replace(',', '').strip()
                if not raw or raw.lower() in ('n/a', 'na', '-', '–', '—'):
                    continue
                if not raw.isdigit():
                    result['uncompared'].append(f'{unit}: {district} level {level}, source {raw!r}')
                    continue
                result['cells'] += 1
                if not displayed.isdigit() or int(displayed) != int(raw):
                    result['errors'].append({'unit': unit, 'district': district, 'level': level,
                                             'display': displayed, 'source': raw,
                                             'sourceTable': source['sourceTableIndex']})
    if source and result['countBlocks']:
        for district, values in source_rows.items():
            if district not in shown and any(cell['raw'].strip() not in ('', '0', 'N/A', '-', '—', '–') for cell in values):
                result['uncompared'].append(f'{unit}: source district {district} absent from page')
    return result


def check_district_counts(records, pages=None):
    pages = pages or ROOT / 'docs/upgrade'
    result = {'pages': 0, 'countBlocks': 0, 'cells': 0, 'otherBlocks': 0, 'errors': [], 'uncompared': []}
    for path in sorted(pages.glob('*.md')):
        text = path.read_text()
        if '<DistrictTable' not in text:
            continue
        page = compare_district_page(path.stem, text, records.get(path.stem, {}))
        result['pages'] += bool(page['countBlocks'])
        for key in ('countBlocks', 'cells', 'otherBlocks'):
            result[key] += page[key]
        result['errors'].extend(page['errors'])
        result['uncompared'].extend(page['uncompared'])
    return result


if __name__ == '__main__':
    data = ROOT / 'docs/.vitepress/theme/assets/unit-data'
    records = {path.stem: json.loads(path.read_text()) for path in data.glob('*.json')}
    report = check_district_counts(records)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if report['errors']:
        raise SystemExit(1)
