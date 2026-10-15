#!/usr/bin/env python3
"""Manually update values in authored tables. Never replace a page or its schema.

The checked-in mapping names exact source tables and headers. Missing source fields
retain authored cells; new unavailable cells say 未知. Preview is the default.
"""
import argparse
import html
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'docs/.vitepress/theme/assets/unit-data'
MAPPINGS = ROOT / 'scripts/authored-table-mappings.json'


def plain(value):
    value = re.sub(r'\[([^]]+)\]\([^)]*\)', r'\1', str(value))
    return re.sub(r'\s+', '', html.unescape(re.sub(r'<[^>]+>', '', value)))


def parse_tables(text):
    constants = {}
    for key, expression in re.findall(r'const (\w+) = (.*?);', text, re.S):
        try:
            constants[key] = json.loads(expression)
        except json.JSONDecodeError:
            constants[key] = constants.get(expression, [])
    tables = []
    for block in re.finditer(r'<UnitTable\b[^>]*>.*?</UnitTable>', text, re.S):
        lines = list(re.finditer(r'^[ \t]*\|[^\n]*', block[0], re.M))
        if not lines:
            continue
        split = lambda line: [cell.strip() for cell in line.strip()[1:-1].split('|')]
        headers = split(lines[0][0])
        rows = [split(line[0]) for line in lines[2:]]
        if any(len(row) != len(headers) for row in rows):
            raise ValueError('Authored table has a different number of cells than its header')
        name = re.search(r':tableExtraInfo="(\w+)"', block[0])
        tables.append({'headers': headers, 'rows': rows,
                       'metadata': constants.get(name[1], []) if name else [],
                       'start': block.start() + lines[1].end() + 1,
                       'end': block.start() + lines[-1].end()})
    return tables


def translations():
    # Reuse the exact UI translator instead of maintaining a second Chinese dictionary.
    code = r'''
import fs from 'node:fs';
import {dataLabel} from './docs/.vitepress/theme/assets/data-labels.js';
const out={};
for(const file of fs.readdirSync('docs/.vitepress/theme/assets/unit-data')) {
 if(!file.endsWith('.json')) continue;
 const d=JSON.parse(fs.readFileSync('docs/.vitepress/theme/assets/unit-data/'+file));
 out[d.unitId]=Object.fromEntries(d.tables.map(t=>[t.sourceTableIndex,t.rows.map(r=>r.map(c=>dataLabel(c.raw)))]));
}
process.stdout.write(JSON.stringify(out));
'''
    result = subprocess.run(['node', '--disable-warning=MODULE_TYPELESS_PACKAGE_JSON', '--input-type=module', '-e', code],
                            cwd=ROOT, check=True, text=True, capture_output=True)
    return json.loads(result.stdout)


def duration(raw):
    if raw in ('Instant', '0'):
        return '0'
    parts = re.findall(r'(\d+(?:\.\d+)?)\s*([dhms])', raw)
    if not parts or re.sub(r'\d+(?:\.\d+)?\s*[dhms]|\s+', '', raw):
        raise ValueError(f'Unrecognized duration: {raw}')
    seconds = sum(float(n) * {'d': 86400, 'h': 3600, 'm': 60, 's': 1}[u] for n, u in parts)
    days, rest = divmod(round(seconds), 86400)
    hours, rest = divmod(rest, 3600)
    minutes, seconds = divmod(rest, 60)
    return ','.join(map(str, [days, hours, minutes, seconds]))


def number(value):
    return str(int(value)) if float(value).is_integer() else str(round(float(value), 8)).rstrip('0').rstrip('.')


def cell_text(cell, translated, meta=None):
    if cell['status'] == 'not_applicable':
        return '\\'
    if cell['status'] == 'unknown':
        return '未知'
    if meta and meta.get('type') == 'time':
        return cell.get('displayInput') or duration(cell['raw'])
    if cell.get('unit') == 'seconds':
        return cell['displayInput']
    if isinstance(cell['value'], (int, float)):
        return number(cell['value'])
    # The column heading already gives the rate's unit, as on the original site.
    if re.fullmatch(r'[\d,.]+/(hr|d)', cell['raw']):
        return cell['raw'].split('/')[0].replace(',', '')
    return translated.replace('|', '&#124;')


def prerequisite(records, unit, level):
    matches = [t for t in records[unit]['tables'] if t['headers'][0] == 'Level' and 'Town Hall Level Required' in t['headers']]
    if len(matches) != 1:
        raise ValueError(f'{unit}: prerequisite table ambiguous')
    t = matches[0]
    for row in t['rows']:
        if row[0]['value'] == level:
            return row[t['headers'].index('Town Hall Level Required')]['value']
    return None


def evaluate(spec, source, row, translated, old, header, meta, records, min_town_hall=0):
    if isinstance(spec, int):
        cell = row[spec]
        # N/A means no research is performed for the initial unlocked level; it does
        # not invalidate the original page's separately supplied unlock condition.
        if cell['status'] != 'known' and plain(header).startswith('所需') and old:
            return old
        if cell['status'] == 'unknown':
            return old or '未知'
        text = cell_text(cell, translated[spec], meta)
        if old and ('href=' in old or re.search(r'\]\(/', old)):
            # Preserve authored route links and established names. New rows are linked separately.
            return old
        return text
    if 'computed' in spec:
        return ''  # UnitTable derives experience/daily cost from the updated cost/time cells.
    if 'requirement' in spec:
        cell = row[source['headers'].index(spec['requirement'])]
        if cell['status'] != 'known' or not isinstance(cell['value'], (int, float)):
            return old or '未知'
        result = prerequisite(records, spec['unit'], cell['value'])
        return number(max(result, min_town_hall)) if result is not None else old or '未知'
    if 'baseTroopRequirement' in spec:
        base = records[spec['baseTroopRequirement']]
        table = next(t for t in base['tables'] if t['headers'][0] == 'Level' and 'Laboratory Level Required' in t['headers'])
        match = next((r for r in table['rows'] if r[0]['value'] == row[0]['value']), None)
        if match:
            lab = match[table['headers'].index('Laboratory Level Required')]['value']
            result = prerequisite(records, '0483-Laboratory', lab) if isinstance(lab, (int, float)) else None
            if result is not None:
                return number(max(result, min_town_hall, 11))
        return old or '未知'
    if 'duration' in spec:
        cell = row[spec['duration']]
        return duration(cell['raw']) if cell['status'] == 'known' else '\\'
    if 'sum' in spec or 'multiply' in spec:
        columns = spec.get('sum', [spec.get('multiply')])
        if any(row[i]['status'] != 'known' or not isinstance(row[i]['value'], (int, float)) for i in columns):
            return old or '未知'
        value = sum(row[i]['value'] for i in columns)
        if 'multiply' in spec:
            value *= spec['factor']
        return number(value)
    if 'join' in spec:
        return ' / '.join(cell_text(row[i], translated[i]) for i in spec['join'])
    if 'percentOffset' in spec:
        raw = row[spec['percentOffset']]['raw']
        if not re.fullmatch(r'[\d.]+%', raw):
            raise ValueError('Conversion bonus is no longer a percentage')
        return number(float(raw[:-1]) + spec['offset']) + '%'
    raise ValueError(f'Unsupported authored mapping: {spec}')


def update_table(old, mapping, record, translated, records, min_town_hall=0):
    if old['headers'] != mapping['headers']:
        raise ValueError(f"{record['unitId']}: authored header changed; review mapping before updating")
    metas = {m['column']: m for m in old['metadata']}
    by_key = {}
    for row in old['rows']:
        by_key.setdefault(plain(row[0]), []).append(row)
    rows, source_keys, preserved, unknown = [], set(), [], []
    for source_map in [mapping] + mapping.get('additionalSourceTables', []):
        source = next(t for t in record['tables'] if t['sourceTableIndex'] == source_map['sourceTableIndex'])
        if source['headers'] != source_map['sourceHeaders']:
            raise ValueError(f"{record['unitId']}: source schema changed; review mapping before updating")
        for spec in source_map['columns'].values():
            evidence = spec.get('evidence') if isinstance(spec, dict) else None
            if isinstance(evidence, dict):
                dependency = next(t for t in record['tables'] if t['sourceTableIndex'] == evidence['table'])
                column = dependency['headers'].index(evidence['header'])
                if len(dependency['rows']) != 1 or dependency['rows'][0][column]['raw'] != evidence['raw']:
                    raise ValueError(f"{record['unitId']}: calculation factor changed; review mapping before updating")
        prefix = source_map.get('levelPrefix', '')
        for ri, row in enumerate(source['rows']):
            if isinstance(row[0]['value'], (int, float)) and row[0]['value'] < mapping.get('minimumLevel', 0):
                continue
            label = translated[str(source['sourceTableIndex'])][ri]
            key = prefix + plain(number(row[0]['value']) if isinstance(row[0]['value'], (int, float)) else label[0])
            candidates = by_key.get(key, [])
            if not candidates and 'href=' in ''.join(r[0] for r in old['rows']):
                candidates = [r for r in old['rows'] if plain(r[0]) == plain(label[0])]
            # A source level may have multiple TH-dependent variants; match the old
            # variant by its requirement when possible, and keep every source row.
            previous = candidates[0] if candidates else None
            reqcols = [(i, int(source_map['columns'][str(i)])) for i, h in enumerate(old['headers'])
                       if '大本' in plain(h) and isinstance(source_map['columns'].get(str(i)), int)]
            if candidates and reqcols:
                matches = [r for r in candidates if all(plain(r[i]) == plain(label[j]) for i, j in reqcols)]
                previous = matches[0] if matches else previous
            out = []
            for col, heading in enumerate(old['headers']):
                fallback = previous[col] if previous else ''
                spec = source_map['columns'].get(str(col))
                if spec is None:
                    value = fallback or '未知'
                    preserved.append(heading)
                else:
                    value = evaluate(spec, source, row, label, fallback, heading, metas.get(col), records, min_town_hall)
                if col == 0:
                    value = prefix + value if prefix else value
                if value == '未知':
                    unknown.append({'level': key, 'column': heading})
                out.append(value)
            rows.append(out)
            source_keys.add(key)
    for row in old['rows']:
        if plain(row[0]) not in source_keys:
            # Existing supercharge history is kept, with a status note when retired.
            rows.append(row)
    # Keep historical event-only levels (e.g. 1* and 2*) in their original numeric
    # position, ahead of regular levels. Stable sorting retains conditional variants.
    labels = [re.fullmatch(r'(⚡?)(\d+)(?:\*)?', plain(r[0])) for r in rows]
    if all(labels):
        rows = [row for _, row in sorted(zip(labels, rows), key=lambda pair: (bool(pair[0][1]), int(pair[0][2])))]
    return rows, {'preservedColumns': sorted(set(preserved)), 'unknownNewCells': unknown}


def update_page(text, plans, record, translated, records):
    tables = parse_tables(text)
    if len(tables) != len(plans):
        raise ValueError(f"{record['unitId']}: authored table count changed")
    changes, report = [], []
    minimum = re.search(r'<UnitProperty pKey="所需大本等级" pValue="(\d+)"', text)
    minimum = int(minimum[1]) if minimum else 0
    for plan, old in zip(plans, tables):
        if plan.get('keepOriginal'):
            report.append({'table': plan['table'], 'retained': plan['reason']})
            continue
        rows, status = update_table(old, plan, record, translated, records, minimum)
        replacement = '\n'.join('| ' + ' | '.join(row) + ' |' for row in rows)
        changes.append((old['start'], old['end'], replacement))
        report.append({'table': plan['table'], 'rows': len(rows), **status})
    for start, end, replacement in reversed(changes):
        text = text[:start] + replacement + text[end:]
    return text, report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apply', action='store_true')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    mappings = json.loads(MAPPINGS.read_text())['units']
    records = {p.stem: json.loads(p.read_text()) for p in DATA.glob('*.json')}
    translated = translations()
    results, prepared = {}, []
    for unit, plans in mappings.items():
        path = ROOT / 'docs/upgrade' / (unit + '.md')
        updated, report = update_page(path.read_text(), plans, records[unit], translated[unit], records)
        results[unit] = report
        prepared.append((path, updated))
    # Validate the whole batch before writing any page.
    if args.apply:
        for path, text in prepared:
            path.write_text(text)
    args.output.write_text(json.dumps(results, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'pages': len(results), 'tablesUpdated': sum('rows' in r for rs in results.values() for r in rs),
                      'newUnknownCells': sum(len(r.get('unknownNewCells', [])) for rs in results.values() for r in rs),
                      'applied': args.apply}, ensure_ascii=False))


if __name__ == '__main__':
    main()
