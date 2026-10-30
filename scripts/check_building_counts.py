#!/usr/bin/env python3
"""Compare authored building-count tables with the saved source records.

Source rows with "before/after merging" use the after-merging count, as the
site explicitly does for merged Home Village defenses. Known disagreements
are reported separately and only match the exact values that were reviewed.
"""
import json
from pathlib import Path
import re

from update_authored_data import parse_tables, plain

ROOT = Path(__file__).resolve().parents[1]
REVIEWS = ROOT / 'scripts/reviewed-building-count-differences.json'
ROW_NAMES = {
    '建筑数量': 'Total',
    '合计': 'Total',
    '第一区域的建筑数量上限': 'Stage 1 Limit',
    '第二区域的建筑数量上限': 'Stage 2 Limit',
}


def source_counts(record):
    candidates = []
    for table in record['tables']:
        headers = table['headers']
        rows = [[cell['raw'] for cell in row] for row in table['rows']]
        if not headers or not rows:
            continue
        counts = {}
        if headers[0] in ('Town Hall Level', 'Capital Hall Level') and rows[0][0] == 'Number Available':
            chunks = [(headers[1:], rows[0][1:])]
            chunks.extend((rows[i][1:], rows[i + 1][1:]) for i in range(1, len(rows) - 1, 2))
            counts['Total'] = {int(level): value for levels, values in chunks
                               for level, value in zip(levels, values) if level.isdigit()}
        elif headers[0] == 'Number Available' and any(h.startswith('Builder Hall Level / ') for h in headers):
            levels = [re.fullmatch(r'Builder Hall Level / (\d+)', h) for h in headers[1:]]
            if not all(levels):
                continue
            for row in rows:
                if row[0] in ('Total', 'Stage 1 Limit', 'Stage 2 Limit'):
                    counts[row[0]] = {int(level[1]): value for level, value in zip(levels, row[1:])}
        if counts:
            candidates.append((table['sourceTableIndex'], counts))
    if len(candidates) > 1:
        raise ValueError('multiple matching building-count source tables')
    return candidates[0] if candidates else None


def expand_groups(groups, values):
    levels = [part.strip() for part in groups.split(',')]
    counts = [part.strip() for part in values.split(',')]
    if len(levels) != len(counts):
        raise ValueError('building-count row has the wrong number of cells')
    expanded = {}
    for group, count in zip(levels, counts):
        match = re.fullmatch(r'(\d+)\s*(?:[-~–—]\s*(\d+))?', group)
        if not match or not (count.isdigit() or count in ('', '\\')):
            raise ValueError(f'unrecognized building-count cell: {group} / {count}')
        start = int(match[1])
        end = int(match[2] or start)
        if end < start:
            raise ValueError(f'reversed building-count range: {group}')
        for level in range(start, end + 1):
            if level in expanded:
                raise ValueError(f'duplicate building-count level: {level}')
            expanded[level] = int(count) if count.isdigit() else None
    return expanded


def compare_page(unit, text, record, reviews):
    blocks = re.findall(r'<BuildingNum>(.*?)</BuildingNum>', text, re.S)
    if not blocks:
        return {'blocks': 0, 'cells': 0, 'differences': [], 'uncompared': []}
    source = source_counts(record)
    if not source:
        return {'blocks': 0, 'cells': 0, 'differences': [], 'uncompared': [f'{unit}: no count source table']}
    index, source_rows = source
    compared_blocks = 0
    cells = 0
    differences = []
    uncompared = []
    initial_requirements = []
    for table in parse_tables(text):
        if not table['headers'] or plain(table['headers'][0]) != '等级':
            continue
        columns = [i for i, header in enumerate(table['headers'])
                   if '所需' in plain(header) and '大本' in plain(header)]
        if len(columns) != 1:
            continue
        first = next((row for row in table['rows'] if plain(row[0]) == '1'), None)
        requirement = plain(first[columns[0]]) if first else ''
        if requirement.isdigit():
            initial_requirements.append(int(requirement))
    for block_number, block in enumerate(blocks, 1):
        rows = re.findall(r'<BuildingNumRow\b[^>]*?title="([^"]+)"[^>]*?num="([^"]+)"', block)
        if not rows or rows[0][0] != '大本等级':
            uncompared.append(f'{unit}: block {block_number} is not a standard hall-count table')
            continue
        compared_blocks += 1
        for title, values in rows[1:]:
            row_name = ROW_NAMES.get(title)
            if row_name is None:
                uncompared.append(f'{unit}: block {block_number}, unsupported row {title}')
                continue
            if row_name not in source_rows:
                uncompared.append(f'{unit}: block {block_number}, no source row {row_name}')
                continue
            displayed = expand_groups(rows[0][1], values)
            if row_name == 'Total':
                for level in sorted(set(initial_requirements)):
                    if displayed.get(level) == 0:
                        differences.append({'unit': unit, 'block': block_number, 'sourceTable': index,
                                            'row': 'Initial level requirement', 'level': level,
                                            'display': 0, 'source': 1, 'reviewed': False})
            for level, raw in source_rows[row_name].items():
                if not raw:
                    continue
                if not re.fullmatch(r'\d+(?:\s*/\s*\d+)?', raw):
                    uncompared.append(f'{unit}: {row_name}, level {level}, source value {raw!r}')
                    continue
                expected = int(raw.split('/')[-1].strip())
                actual = displayed.get(level)
                cells += 1
                if actual == expected:
                    continue
                review = next((item for item in reviews if item['unitId'] == unit
                               and item['sourceTableIndex'] == index and item['row'] == row_name
                               and level in item['levels'] and item['display'] == actual
                               and item['source'] == expected), None)
                differences.append({'unit': unit, 'block': block_number, 'sourceTable': index,
                                    'row': row_name, 'level': level, 'display': actual,
                                    'source': expected, 'reviewed': bool(review)})
    return {'blocks': compared_blocks, 'cells': cells, 'differences': differences, 'uncompared': uncompared}


def check_building_counts(records, pages=None, reviews=None):
    pages = pages or ROOT / 'docs/upgrade'
    reviews = reviews if reviews is not None else json.loads(REVIEWS.read_text())
    result = {'pages': 0, 'blocks': 0, 'cells': 0, 'errors': [],
              'reviewedDifferences': [], 'uncompared': []}
    for path in sorted(pages.glob('*.md')):
        text = path.read_text()
        if '<BuildingNum>' not in text:
            continue
        record = records.get(path.stem)
        if not record:
            result['uncompared'].append(f'{path.stem}: no saved source record')
            continue
        try:
            page = compare_page(path.stem, text, record, reviews)
        except ValueError as error:
            result['errors'].append(f'{path.stem}: {error}')
            continue
        result['pages'] += bool(page['blocks'])
        result['blocks'] += page['blocks']
        result['cells'] += page['cells']
        result['uncompared'].extend(page['uncompared'])
        for difference in page['differences']:
            (result['reviewedDifferences'] if difference['reviewed'] else result['errors']).append(difference)
    return result


if __name__ == '__main__':
    data = ROOT / 'docs/.vitepress/theme/assets/unit-data'
    records = {path.stem: json.loads(path.read_text()) for path in data.glob('*.json')}
    report = check_building_counts(records)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if report['errors']:
        raise SystemExit(1)
