#!/usr/bin/env python3
"""Validate imported tables, conversions, image files and announced maximum levels."""
import argparse
from decimal import Decimal, InvalidOperation
import json
from pathlib import Path
import re

from sync_wiki_data import SourceTables, VillageFilter, headers_and_rows, is_unit_image, REVIEWED_IMAGES, history_rows
from check_upgrade_data import seconds
from update_authored_data import MAPPINGS, translations, update_page

ROOT = Path(__file__).resolve().parents[1]


def main():
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument('--cache', type=Path, help='Also compare every raw source cell against the pinned snapshots')
    args = cli.parse_args()
    inventory = json.loads((args.cache / 'inventory.json').read_text()) if args.cache else None
    sources = {item['unitId']: item for item in inventory['units']} if inventory else {}
    records = {p.stem: json.loads(p.read_text()) for p in (ROOT / 'docs/.vitepress/theme/assets/unit-data').glob('*.json')}
    mappings = json.loads(MAPPINGS.read_text())['units']
    translated = translations()
    errors = []
    count = 0
    for path in sorted((ROOT / 'docs/.vitepress/theme/assets/unit-data').glob('*.json')):
        record = json.loads(path.read_text()); records[record['unitId']] = record
        page = ROOT / 'docs/upgrade' / (record['unitId'] + '.md')
        if page.exists() and record['unitId'] in mappings:
            try:
                current = page.read_text()
                expected, _ = update_page(current, mappings[record['unitId']], record, translated[record['unitId']], records)
                if expected != current:
                    errors.append(record['unitId'] + ': authored table values need updating')
            except (ValueError, KeyError, StopIteration) as error:
                errors.append(record['unitId'] + ': ' + str(error))
        elif not page.exists() or record['unitId'] + '.json' not in page.read_text():
            errors.append(record['unitId'] + ': page does not load its data')
        parser = None
        if inventory:
            item = sources[record['unitId']]
            snapshot = json.loads(Path(item['snapshot']).read_text())['parse']
            if snapshot['revid'] != record['sync']['revision']:
                errors.append(record['unitId'] + ': revision mismatch')
            village = {'upgrade-bh': 'Builder_Base', 'upgrade-capital': 'Clan_Capital'}.get(record['module'], 'Home_Village')
            filtered = VillageFilter(village); filtered.feed(snapshot['text']['*'])
            parser = SourceTables(); parser.feed(''.join(filtered.output))
            for table in parser.tables:
                for event in history_rows(table, record['sync']['syncedOn']) or []:
                    if not any(all(saved.get(key) == value for key, value in event.items()) for saved in record['history']):
                        errors.append(record['unitId'] + ': source history omitted: ' + event['date'] + ' ' + event['description'])
        for table in record['tables']:
            label = record['unitId'] + ':' + str(table['sourceTableIndex'])
            width = len(table['headers']); metadata = {item['column']: item for item in table['extraInfo']}
            if parser:
                headers, raw_rows, _ = headers_and_rows(parser.tables[table['sourceTableIndex']])
                if table['headers'] != headers or [[cell['raw'] for cell in row] for row in table['rows']] != raw_rows:
                    errors.append(label + ': headers or raw source rows changed')
            for row in table['rows']:
                count += len(row)
                if len(row) != width:
                    errors.append(label + ': wrong column count')
                for column, cell in enumerate(row):
                    if cell['status'] not in ('known', 'unknown', 'not_applicable'):
                        errors.append(label + ': invalid cell status')
                    if cell['status'] != 'known' and cell['value'] is not None:
                        errors.append(label + ': unknown/NA has a value')
                    if cell.get('unit') == 'seconds':
                        expected = 0 if cell['raw'] == 'Instant' else seconds(cell['raw'], wiki=True)
                        if cell['value'] != expected or seconds(cell['displayInput']) != expected:
                            errors.append(label + ': duration conversion mismatch')
                    elif cell['status'] == 'known':
                        try:
                            expected = Decimal(cell['raw'].replace(',', ''))
                            if Decimal(str(cell['value'])) != expected:
                                errors.append(label + ': numeric conversion mismatch')
                        except InvalidOperation:
                            if cell['raw'] == 'Free' and cell['value'] != 0:
                                errors.append(label + ': Free is not zero')
                    info = metadata.get(column)
                    if info and (record['module'] == 'upgrade-capital' or any(icon in info.get('icon', '').split(',') for icon in ('Gem', 'Shiny_Ore', 'Glowy_Ore', 'Starry_Ore', 'Wall_Ring'))) and not info['noGoldPass']:
                        errors.append(label + ': ineligible resource gets Gold Pass')
            for column, header in enumerate(table['headers']):
                if 'Cost' in header and any(cell[column]['status'] == 'known' and isinstance(cell[column]['value'], (int, float)) for cell in table['rows']) and column not in metadata:
                    errors.append(label + ': numeric cost lacks resource metadata: ' + header)
        for image in record['images']:
            local = image.get('localPath')
            if not local or not (ROOT / 'docs/public' / local.lstrip('/')).is_file():
                errors.append(record['unitId'] + ': image not local: ' + image['name'])
            if local and local.startswith('/images/wiki/'):
                if not is_unit_image(image, record['unitId']):
                    errors.append(record['unitId'] + ': supplemental image has not been visually reviewed: ' + image['name'])
                elif image['alt'] != REVIEWED_IMAGES[record['unitId'] + '/' + image['name']]['caption']:
                    errors.append(record['unitId'] + ': image caption differs from reviewed description: ' + image['name'])
    image_sources = json.loads((ROOT / 'docs/public/images/wiki-sources.json').read_text())
    reviewed_sources = {(key.split('/')[0], review['sourceUrl']) for key, review in REVIEWED_IMAGES.items()}
    for page in (ROOT / 'docs/upgrade/category').glob('*.md'):
        for local in re.findall(r'imgSrc="(/images/wiki/[^"]+)"', page.read_text()):
            source = image_sources.get(local, {})
            if (source.get('unitId'), source.get('sourceUrl')) not in reviewed_sources:
                errors.append(page.name + ': category image has not been visually reviewed: ' + local)
    announced = re.findall(r'\(docs/upgrade/([^()]+)\.md\)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|', (ROOT / 'UPDATE_AUDIT_2026-10-13.md').read_text())
    for unit, old, required in announced:
        levels = [row[0]['value'] for table in records[unit]['tables'] if table['headers'][0] == 'Level' for row in table['rows'] if isinstance(row[0]['value'], int)]
        if max(levels, default=0) < int(required):
            errors.append(unit + ': missing announced maximum level ' + required)
    print(json.dumps({'units': len(records), 'cells': count, 'announcedLevelGroups': len(announced),
                      'pinnedSourcesCompared': bool(inventory), 'errors': sorted(set(errors))}, ensure_ascii=False, indent=2))
    if errors:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
