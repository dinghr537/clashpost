#!/usr/bin/env python3
"""Convert reviewed Wiki snapshots to per-unit data; --apply updates local pages."""
import argparse
from datetime import datetime
from decimal import Decimal, InvalidOperation
import html
import json
from pathlib import Path
import re
from urllib.parse import unquote, quote
from html.parser import HTMLParser

from check_upgrade_data import Tables, clean, seconds

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'docs/.vitepress/theme/assets/unit-data'
REVIEWED_IMAGES = json.loads((ROOT / 'docs/.vitepress/theme/assets/reviewed-wiki-images.json').read_text())['images']
RESOURCE_NAMES = {
    'Gold': 'Gold', 'Elixir': 'Elixir', 'Dark Elixir': 'Dark_Elixir',
    'Builder Gold': 'Gold2', 'Builder Elixir': 'Elixir2', 'Capital Gold': 'Gold3',
    'Shiny Ore': 'Shiny_Ore', 'Glowy Ore': 'Glowy_Ore', 'Starry Ore': 'Starry_Ore',
    'Gems': 'Gem', 'Gem': 'Gem', 'Experience': 'Exp',
    'Gold2': 'Gold2', 'Elixir2': 'Elixir2', 'Gold (Builder Base)': 'Gold2', 'Elixir (Builder Base)': 'Elixir2',
    'Wall Ring': 'Wall_Ring', 'Wall Rings': 'Wall_Ring',
}


def history_rows(table, through, since='2026-02-01'):
    """Read both Wiki history schemas; preserve imprecise dates for review."""
    if not table or not table[0] or table[0][0] not in ('Date', 'Patch') or 'Description' not in table[0]:
        return None
    result = []
    for row in table[1:]:
        raw = re.sub(r'(\d+)(st|nd|rd|th)\b', r'\1', row[0]).strip()
        date_info = {}
        if '?' in raw:
            date_info = {'dateRaw': row[0], 'dateUncertain': True}
            raw = raw.replace('?', '')
        span = re.fullmatch(r'([A-Za-z]+) (\d+)[–-](\d+),? (\d{4})', raw)
        if span:
            month, first, last, year = span.groups()
            raw = f'{month} {first}, {year}'
            date_info = {'dateRaw': row[0], 'dateEnd': datetime.strptime(f'{month} {last}, {year}', '%B %d, %Y').date().isoformat()}
        when = None
        for fmt in ('%B %d, %Y', '%d %B %Y', '%b %d, %Y', '%d %b %Y', '%B %d %Y', '%b %d %Y'):
            try:
                when = datetime.strptime(raw, fmt).date().isoformat()
                break
            except ValueError:
                pass
        if when is None:
            # Do not silently drop a new history format in the reviewed period.
            years = re.findall(r'\b\d{4}\b', raw)
            if any(since[:4] <= year <= through[:4] for year in years):
                raise ValueError(f'Unrecognised history date: {row[0]}')
            continue
        if since <= when <= through:
            result.append({'date': when, 'description': row[table[0].index('Description')], **date_info})
    return result


def is_unit_image(image, unit_id):
    # Names and numeric suffixes cannot distinguish sprites from diagrams,
    # screenshots or another game's artwork. Require a reviewed exact source.
    review = REVIEWED_IMAGES.get(unit_id + '/' + image['name'])
    return bool(review and review['sourceUrl'] == image.get('url'))


def reviewed_image(image, unit_id):
    review = REVIEWED_IMAGES[unit_id + '/' + image['name']]
    return {**image, 'sourceAlt': image.get('sourceAlt', image.get('alt', '')), 'alt': review['caption']}


class VillageFilter(HTMLParser):
    """Some Wiki pages transclude all villages; retain the requested village tab."""
    def __init__(self, village):
        super().__init__(convert_charrefs=False)
        self.village = village
        self.stack = []
        self.skip_depth = None
        self.output = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        frame = next((frame for frame in reversed(self.stack) if frame.get('tabber')), None)
        if tag == 'li' and frame and attrs.get('data-hash'):
            frame['tabs'].append(attrs['data-hash'])
        if tag == 'div':
            entry = {}
            if 'wds-tabber' in attrs.get('class', ''):
                entry = {'tabber': True, 'tabs': [], 'index': 0}
            elif 'wds-tab__content' in attrs.get('class', '') and frame:
                tabs = frame['tabs']
                index = frame['index']
                frame['index'] += 1
                if self.skip_depth is None and self.village in tabs and index < len(tabs) and tabs[index] != self.village:
                    self.skip_depth = len(self.stack) + 1
            self.stack.append(entry)
        if self.skip_depth is None:
            self.output.append(self.get_starttag_text())

    def handle_endtag(self, tag):
        was_skipping = self.skip_depth is not None
        if tag == 'div' and self.stack:
            if self.skip_depth == len(self.stack):
                self.skip_depth = None
            self.stack.pop()
        if not was_skipping:
            self.output.append('</' + tag + '>')

    def handle_data(self, data):
        if self.skip_depth is None:
            self.output.append(data)

    def handle_entityref(self, name):
        self.handle_data('&' + name + ';')

    def handle_charref(self, name):
        self.handle_data('&#' + name + ';')


def resource(images):
    resources = []
    for image in images:
        match = re.search(r'/([^/]+\.png)(?:/revision|$)', image.get('data-src') or image.get('src', ''))
        # Filenames (e.g. ElixirB.png) need not be resource names; alt is also source evidence.
        for key in (image.get('data-image-key', ''), image.get('alt', ''), unquote(match[1]) if match else ''):
            key = key.replace('_', ' ').removesuffix('.png')
            if key in RESOURCE_NAMES:
                value = RESOURCE_NAMES[key]
                if value not in resources:
                    resources.append(value)
                break
    return ','.join(resources) or None


class SourceTables(Tables):
    """Retain group headings, resource icons and lightning level markers."""
    def __init__(self):
        super().__init__()
        self.section = ''
        self.heading = ''
        self.capture_heading = None
        self.heading_text = []
        self.contexts = []
        self.image_rows = []
        self.cell_images = []
        self.gallery = []
        self.facts = []
        self.summary_items = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in ('h2', 'h3', 'h4') and self.depth == 0:
            self.capture_heading = tag
            self.heading_text = []
        if tag == 'table' and self.depth == 0:
            self.current_context = {'section': self.section, 'heading': self.heading}
            self.current_image_rows = []
        if tag == 'tr' and self.depth == 1:
            self.current_cell_images = []
        if tag in ('td', 'th') and self.depth == 1:
            self.cell_images = []
        if tag == 'img':
            if self.depth == 1 and self.cell is not None:
                self.cell_images.append(attrs)
                if self.section.lower() == 'history' and attrs.get('alt'):
                    self.cell.append(' ' + attrs['alt'] + ' ')
                if 'Supercharge' in attrs.get('data-image-key', ''):
                    self.cell.append('⚡')
            if self.section.lower() not in ('history', 'trivia', 'upgrade differences', 'upgrade differences and summary'):
                url = attrs.get('data-src') or attrs.get('src', '')
                key = attrs.get('data-image-key')
                if key and url.startswith('https://static.wikia.nocookie.net/'):
                    self.gallery.append({'name': key, 'url': html.unescape(url), 'alt': attrs.get('alt', key)})
        if tag == 'li' and self.depth == 0 and ('Summary' in (self.section, self.heading) or self.summary_items):
            self.summary_items.append([])
        super().handle_starttag(tag, list(attrs.items()))

    def handle_data(self, data):
        if self.capture_heading:
            self.heading_text.append(data)
        if self.summary_items:
            self.summary_items[-1].append(data)
        super().handle_data(data)

    def handle_endtag(self, tag):
        if tag == 'li' and self.summary_items:
            value = clean(''.join(self.summary_items.pop()))
            if len(value) <= 300 and re.search(r'\d', value) and re.search(r'level|unlock|damage|health|hitpoints|seconds|tiles|space|heal|speed|trap|range|capacity', value, re.I):
                self.facts.append({'section': self.section, 'heading': self.heading, 'text': value})
        if tag == self.capture_heading:
            label = re.sub(r'\[[^\]]*\]', '', clean(''.join(self.heading_text))).strip()
            if tag == 'h2':
                self.section = label
                self.heading = ''
            else:
                self.heading = label
            self.capture_heading = None
        if tag in ('td', 'th') and self.depth == 1 and self.cell is not None:
            if not clean(''.join(self.cell)) and self.cell_images:
                self.cell.append(self.cell_images[0].get('alt', ''))
            self.current_cell_images.append((resource(self.cell_images), *self.span))
        if tag == 'tr' and self.depth == 1 and self.cells:
            self.current_image_rows.append(self.current_cell_images)
        if tag == 'table' and self.depth == 1:
            self.contexts.append(self.current_context)
            self.image_rows.append(self.expand(self.current_image_rows))
        super().handle_endtag(tag)


def source_cell(raw, header=None):
    if raw == 'None' and header == 'Preferred Target':
        return {'status': 'known', 'value': raw, 'raw': raw}
    if raw in ('N/A', 'N/A (Owned)', 'None', 'Not Applicable', 'Not available', '-'):
        return {'status': 'not_applicable', 'value': None, 'raw': raw}
    if raw in ('', '?', 'Unknown', 'TBA', 'Varies') or '?' in raw:
        return {'status': 'unknown', 'value': None, 'raw': raw}
    if raw == 'Free':
        return {'status': 'known', 'value': 0, 'raw': raw}
    value = raw
    try:
        number = Decimal(raw.replace(',', ''))
        value = int(number) if number == int(number) else float(number)
    except (InvalidOperation, ValueError, OverflowError):
        pass
    return {'status': 'known', 'value': value, 'raw': raw}


def headers_and_rows(table):
    if not table or len(table) < 2:
        return [], [], 0
    width = len(table[0])
    count = 1
    # Grouped equipment headers repeat Level across their header rows.
    while count < len(table) and table[count] and (table[count][0] in ('Level', 'Supercharge Level') or (count == 1 and table[count][0] == table[0][0] and not re.search(r'\d', table[0][0]))):
        count += 1
    headers = []
    for column in range(width):
        parts = []
        for row in table[:count]:
            value = row[column] if column < len(row) else ''
            if value and value not in parts:
                parts.append(value)
        headers.append(' / '.join(parts))
    rows = [row + [''] * (width-len(row)) for row in table[count:]]
    if any(len(row) > width for row in rows):
        # A later row wider than the header belongs to a different layout.
        return [], [], 0
    return headers, rows, count


def is_data_table(headers, rows, context):
    if not rows or any(len(header) > 100 for header in headers):
        return False
    if context['section'].lower() in ('history', 'trivia', 'icon descriptions'):
        return False
    if context['section'].lower() in ('strategy', 'strategies', 'achievements') or context['heading'] in ('Achievements', 'Equipment Migration'):
        return False
    if context['heading'].startswith(('Number of Bomber hits', 'Number of Wall Breakers required')):
        return False
    if context['section'].lower().startswith('upgrade differences') and not ('Level' in headers and any('Cost' in header for header in headers)):
        return False
    if any('Completing upgrades with Gems' in header for header in headers):
        return False  # Strategy/return-on-investment comparisons are outside upgrade data.
    if any('Level' in header or 'Cost' in header or 'Time' in header for header in headers):
        return any(re.search(r'\d', cell) for row in rows for cell in row)
    stat_words = ('Damage', 'Hitpoints', 'Range', 'Attack Speed', 'Housing Space', 'Preferred Target', 'Movement Speed', 'Capacity', 'Conversion', 'Production', 'Number Available', 'Size')
    return any(word in header for header in headers for word in stat_words)


def extra_info(headers, rows, icons, module, gp_class):
    metadata = []
    for column, header in enumerate(headers):
        icon = icons[column] if column < len(icons) else None
        leaf = header.split(' / ')[-1]
        icon = icon or RESOURCE_NAMES.get(leaf)
        values = [row[column] for row in rows if row[column] not in ('', 'N/A', '?', 'None', '-', 'Varies')]
        values = ['0' if value == 'Free' else value for value in values]
        is_ore = leaf in ('Shiny Ore', 'Glowy Ore', 'Starry Ore') and (header == leaf or 'Upgrade Cost' in header)
        is_cost = 'Cost' in header or is_ore
        is_time = any(word in header for word in ('Build Time', 'Upgrade Time', 'Research Time', 'Construction Time'))
        if is_cost and values and all(re.fullmatch(r'[\d,.]+', value) for value in values):
            if not icon:
                # Never guess a resource when the source does not identify it.
                continue
            resource_icons = icon.split(',')
            if module == 'upgrade-bh':
                resource_icons = [value + '2' if value in ('Gold', 'Elixir') else value for value in resource_icons]
            if module == 'upgrade-capital':
                resource_icons = ['Gold3' if value == 'Gold' else value for value in resource_icons]
            icon = ','.join(resource_icons)
            upgrade_table = any('Level' in value for value in headers) or 'Gear Up Cost' in header
            metadata.append({'column': column, 'type': 'cost', 'icon': icon, 'gpClass': gp_class,
                             'noGoldPass': module == 'upgrade-capital' or not upgrade_table or 'Cumulative' in header or 'Boost Cost' in header or icon in ('Gem', 'Wall_Ring', 'Shiny_Ore', 'Glowy_Ore', 'Starry_Ore')})
        elif is_time and values:
            try:
                for value in values:
                    if value != 'Instant':
                        seconds(value, wiki=True)
            except ValueError:
                continue
            metadata.append({'column': column, 'type': 'time', 'gpClass': gp_class,
                             'noGoldPass': module == 'upgrade-capital'})
    return metadata


def duration_value(raw):
    if raw == 'Instant':
        return '0'
    amount = seconds(raw, wiki=True)
    days, remainder = divmod(amount, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, secs = divmod(remainder, 60)
    return ','.join(map(str, [days, hours, minutes, secs]))


def validate_table_levels(tables, references=()):
    """Reject ambiguous levels, while allowing explicitly different prerequisites."""
    for table in tables:
        if table['headers'][0] != 'Level':
            continue
        prerequisites = [i for i, h in enumerate(table['headers'])
                         if h in ('Town Hall Level Required', 'Town Hall Level', 'Hero Hall Level Required')]
        seen = set()
        for row in table['rows']:
            key = tuple(row[i]['value'] for i in [0, *prerequisites])
            if key in seen:
                raise ValueError(f"表 {table['sourceTableIndex']} 存在重复等级及前置条件：{key}")
            seen.add(key)
    for reference in references:
        parent = next(t for t in tables if t['sourceTableIndex'] == reference['table'])
        child = next(t for t in tables if t['sourceTableIndex'] == reference['targetTable'])
        column = parent['headers'].index(reference['column'])
        required = {r[column]['value'] for r in parent['rows'] if r[column]['status'] == 'known'}
        available = {r[0]['value'] for r in child['rows']}
        if required - available:
            raise ValueError(f"关联单位缺少等级：{reference['column']} {sorted(required - available)}")


def preserve_table_corrections(reviewed, tables):
    """Stop source keys or cells from undoing explicitly reviewed table repairs."""
    for correction in (reviewed or {}).get('sync', {}).get('reviewedTableCorrections', []):
        index = correction['table']
        old = next(t for t in reviewed['tables'] if t['sourceTableIndex'] == index)
        new = next((t for t in tables if t['sourceTableIndex'] == index), None)
        if new is None or new['headers'] != old['headers']:
            raise ValueError(f'已修正表 {index} 的结构变化，请人工核对')
        old_keys = {r[0]['raw'] for r in old['rows']}
        new_keys = {r[0]['raw'] for r in new['rows']}
        if old_keys - new_keys:
            raise ValueError(f'已修正表 {index} 的等级或条目缺失，请人工核对')
        for cell in correction.get('cells', []):
            header = cell['header']
            key_name = 'level' if 'level' in cell else 'rowKey'
            if key_name not in cell:
                raise ValueError(f'已修正表 {index} 的行标识缺失，请人工核对：{header}')
            row_key = cell[key_name]
            if header not in old['headers'] or header not in new['headers']:
                raise ValueError(f'已修正表 {index} 的字段缺失，请人工核对：{header}')
            old_rows = [r for r in old['rows'] if r[0]['value'] == row_key]
            new_rows = [r for r in new['rows'] if r[0]['value'] == row_key]
            if len(old_rows) != 1 or len(new_rows) != 1:
                raise ValueError(f'已修正表 {index} 的行不唯一，请人工核对：{row_key}')
            old_cell = old_rows[0][old['headers'].index(header)]
            new_cell = new_rows[0][new['headers'].index(header)]
            if (old_cell['status'], old_cell['value']) != (new_cell['status'], new_cell['value']):
                raise ValueError(f'已修正表 {index} 的数值发生变化，请人工核对：{row_key} / {header}')


def preserve_balance_update(reviewed, tables, date):
    """Require manual review before a source snapshot can undo a newer correction."""
    update = reviewed.get('sync', {}).get('balanceUpdate') if reviewed else None
    if not update:
        return
    if date < update['appliedOn']:
        raise ValueError('来源日期早于已核对的平衡更新，不能回退当前数值')
    for field in update['fields']:
        index, header = field['table'], field['header']
        if index < 0:
            continue  # Separately sourced child tables are retained below.
        old = next(t for t in reviewed['tables'] if t['sourceTableIndex'] == index)
        new = next((t for t in tables if t['sourceTableIndex'] == index), None)
        if new is None or header not in new['headers']:
            raise ValueError(f'平衡更新字段缺失，请先人工核对：{header}')
        old_col, new_col = old['headers'].index(header), new['headers'].index(header)
        levels = field.get('levels')
        bounds = [int(n) for n in levels.split('–')] if levels else None
        for row in old['rows']:
            if bounds and not bounds[0] <= row[0]['value'] <= bounds[-1]:
                continue
            candidates = [r for r in new['rows'] if r[0]['value'] == row[0]['value']] if bounds else new['rows']
            if len(candidates) != 1 or any(candidates[0][new_col][key] != row[old_col][key]
                                          for key in ('status', 'value')):
                raise ValueError(f'来源与已核对的平衡更新不一致，请先人工核对：{header}')
    tables.extend(t for t in reviewed['tables'] if t['sourceTableIndex'] < 0)


def make_record(item, date):
    page = ROOT / 'docs/upgrade' / (item['unitId'] + '.md')
    old = page.read_text(encoding='utf-8-sig') if page.exists() else ''
    snapshot = json.loads(Path(item['snapshot']).read_text())['parse']
    module_match = re.search(r'^module:\s*(\S+)', old, re.M)
    module = module_match[1] if module_match else ('upgrade-temp' if item['unitId'].startswith(('0e', '09')) else 'upgrade-home')
    if item['unitId'].startswith('09'):
        module = 'upgrade-temp'
    village = {'upgrade-home': 'Home_Village', 'upgrade-bh': 'Builder_Base', 'upgrade-capital': 'Clan_Capital'}.get(module, 'Home_Village')
    filtered = VillageFilter(village)
    filtered.feed(snapshot['text']['*'])
    parser = SourceTables()
    parser.feed(''.join(filtered.output))
    folder_match = re.search(r'^imgFolder:\s*(.+)', old, re.M)
    folder = folder_match[1].strip() if folder_match else item['folder'] + '/' + item['unitId'][:4]
    gp_match = re.search(r'"gpClass"\s*:\s*"([^"]+)"', old)
    gp_class = gp_match[1] if gp_match else ('building' if 'building' in folder or 'heroes/02' in folder else 'research')
    if item['unitId'].startswith('084') or item['unitId'].startswith('09'):
        gp_class = 'building'
    previous_path = DATA / (item['unitId'] + '.json')
    reviewed = json.loads(previous_path.read_text()) if previous_path.exists() else None
    previous = reviewed if '<SyncedUnitData' in old else None
    if previous:
        gp_class = next((info['gpClass'] for table in previous['tables'] for info in table['extraInfo'] if 'gpClass' in info), gp_class)
    title_match = re.search(r'^navTitle:\s*"([^"]+)"', old, re.M)
    title = title_match[1] if title_match else item['label']
    source_url = 'https://clashofclans.fandom.com/wiki/' + quote(snapshot['title'].replace(' ', '_'), safe='/()_-.')
    tables, history = [], []
    for index, (table, context) in enumerate(zip(parser.tables, parser.contexts)):
        events = history_rows(table, date)
        if events is not None:
            history.extend(events)
            continue
        headers, rows, header_count = headers_and_rows(table)
        if not is_data_table(headers, rows, context):
            continue
        if item['unitId'].startswith('25'):
            wanted = item['unitId'][5:].replace('-', ' ')
            if context['heading'] != wanted:
                continue
        if snapshot['title'] in ('Clan Capital Barracks', 'Clan Capital Spell Factories'):
            wanted = item['unitId'][5:].replace('-', ' ')
            normalise = lambda value: re.sub(r'[^a-z0-9]', '', value.lower())
            if normalise(context['section']) != normalise(wanted):
                continue
        icon_rows = parser.image_rows[index][:header_count]
        icons = [next((row[column] for row in reversed(icon_rows) if column < len(row) and row[column]), None)
                 for column in range(len(headers))]
        if item['unitId'] == '0500-Builders-Hut' and headers == ["Builder's Hut", 'Build Cost']:
            # Wiki Summary explicitly identifies the separate builder purchase prices as Gems.
            icons[1] = 'Gem'
        metadata = extra_info(headers, rows, icons, module, gp_class)
        typed_columns = {info['column']: info['type'] for info in metadata}
        cells = []
        for row in rows:
            converted = []
            for column, raw in enumerate(row):
                cell = source_cell(raw, headers[column])
                if cell['status'] == 'known' and typed_columns.get(column) == 'time':
                    cell['value'] = 0 if raw == 'Instant' else seconds(raw, wiki=True)
                    cell['unit'] = 'seconds'
                    cell['displayInput'] = duration_value(raw)
                converted.append(cell)
            cells.append(converted)
        tables.append({'sourceTableIndex': index, 'section': context['section'], 'title': context['heading'],
                       'headers': headers, 'rows': cells, 'extraInfo': metadata})
    if not tables:
        raise ValueError('No usable data tables; existing page preserved')
    validate_table_levels(tables, (reviewed or {}).get('levelReferences', []))
    preserve_table_corrections(reviewed, tables)
    preserve_balance_update(reviewed, tables, date)
    # Only images belonging to this exact unit page; do not match across villages.
    shared = snapshot['title'] in ('Clan Capital Barracks', 'Clan Capital Spell Factories') or item['unitId'].startswith('25')
    family_name = item['unitId'][5:].replace('-', ' ') if shared else snapshot['title'].split('/')[0]
    if snapshot['title'] == 'Ruin Witch/Ruin Knight':
        family_name = 'Ruin Knight'
    family = re.sub(r'[^a-z0-9]', '', family_name.lower())
    images, seen = [], set()
    original = json.loads((ROOT / 'docs/.vitepress/theme/assets/original-image-manifest.json').read_text())
    supplemental_path = ROOT / 'docs/.vitepress/theme/assets/supplemental-image-manifest.json'
    supplemental = json.loads(supplemental_path.read_text()) if supplemental_path.exists() else {}
    original = {**supplemental, **original}
    original = {unquote(key): value for key, value in original.items()}
    old_names = set()
    old_levels = []
    disabled_charge = 'Supercharging Disabled' in ''.join(filtered.output)
    if previous:
        images = [{**image, 'localPath': image.get('localPath') or original.get(image['logicalPath'])
                   or original.get(re.sub(r'\.(png|jpe?g)$', '.webp', image['logicalPath'], flags=re.I))}
                  for image in previous['images'] if 'static.clashpost.com' in image['url'] or is_unit_image(image, item['unitId'])]
        images = [reviewed_image(image, item['unitId']) if is_unit_image(image, item['unitId']) else image for image in images]
        for image in images:
            old_names.add(image['name'])
            seen.add(image['name'])
            if image.get('localPath'):
                seen.add(image['localPath'])
            old_levels.extend(int(value) for value in re.findall(r'\d+', image['alt']))
    for tag in re.findall(r'<(?:UnitInfo|UnitImg)\b[^>]*>', old):
        name_match = re.search(r'imgSrc="([^"]+)"', tag)
        if not name_match:
            continue
        name = unquote(name_match[1])
        old_names.add(name)
        label_match = re.search(r'imgTitle="([^"]+)"', tag)
        label = label_match[1] if label_match else title
        if disabled_charge and ('⚡' in label or '蓄能' in label):
            continue
        old_levels.extend(int(value) for value in re.findall(r'\d+', label))
        logical = '/upgrade/' + folder + '/' + name
        local = original.get(logical) or original.get(re.sub(r'\.(png|jpe?g)$', '.webp', logical, flags=re.I))
        if local and local not in seen:
            seen.add(local)
            images.append({'name': name, 'url': 'https://static.clashpost.com' + logical,
                           'alt': label, 'localPath': local, 'logicalPath': logical})
    old_max = max(old_levels, default=0)
    for image in parser.gallery:
        if not is_unit_image(image, item['unitId']):
            continue
        key_family = re.sub(r'[^a-z0-9]', '', image['name'].lower())
        if not key_family.startswith(family) and image['name'] not in old_names:
            continue
        logical = '/upgrade/' + folder + '/' + image['name']
        local = original.get(logical) or original.get(re.sub(r'\.(png|jpe?g)$', '.webp', logical, flags=re.I))
        if local and local in seen:
            continue
        level_match = re.search(r'(\d+)', image['name'])
        if images and image['name'] not in old_names and (not level_match or int(level_match[1]) <= old_max):
            continue
        if image['name'] in seen:
            continue
        seen.add(image['name'])
        images.append({**reviewed_image(image, item['unitId']), 'localPath': local, 'logicalPath': logical})
    facts = [fact['text'] for fact in parser.facts if not shared or re.sub(r'[^a-z0-9]', '', fact['section'].lower()) == family]
    selected_facts = []
    for fact in facts:
        if fact not in selected_facts and sum(map(len, selected_facts)) + len(fact) <= 900:
            selected_facts.append(fact)
    if item['unitId'] == '0205-Dragon-Duke':
        selected_facts.append('被动技能：附近 6 格没有其他空中部队时触发；陷阱伤害减免为 20%（按本页 Wiki 修订）。')
    if item['unitId'] == '0013-Ruin-Witch':
        selected_facts = [fact for fact in selected_facts if 'poor defender' not in fact]
    if item['unitId'] == '0726-Portal-Pendant':
        selected_facts = [fact for fact in selected_facts if 'exceptions:' not in fact]
        selected_facts.extend([
            '召回容量：英雄按 25 人口、战宠通常按 20 人口计。亡灵王自身不占容量，但携带的战宠通常仍计入容量。',
            '凤凰仍为蛋形态时，只有主人被召回才会一起召回，且不额外占用人口。',
            '愤怒水母正在对主人施加洗脑效果时，会随主人一起召回，且不额外占用人口。',
            '容量不足时优先召回英雄，再按人口从高到低召回；同人口优先召回先部署的单位。战宠不继承主人的优先权，可能与主人分开召回。',
        ])
    if item['unitId'] == '0305-Wizard-Tower' and not any(item['date'] == '2026-04-27' for item in history):
        # This pinned Wiki revision verifies both values, but does not date the change.
        history.append({'date': '2026-04-27', 'description': '十七级升级时间从 8 天 12 小时缩短为 5 天 12 小时。',
                        'sourceUrl': 'https://clashofclans.fandom.com/wiki/Wizard_Tower?oldid=625327',
                        'dateSourceUrl': 'https://www.clash.ninja/blog/april-2026-update-is-live', 'type': 'announcement'})
    if item['unitId'] == '0e1d-Totem-Thrower' and not any(event['date'] == '2026-10-08' for event in history):
        history.append({'date': '2026-10-08', 'description': '在 Portal Panic 活动中开放使用，活动截至 10 月 25 日。',
                        'sourceUrl': 'https://supercell.com/en/games/clashofclans/blog/news/the-portal-panic-medal-event-rifts-its-way-into-clash/', 'type': 'availability'})
    # Keep reviewed official supplements even when the Wiki history is incomplete.
    for event in json.loads((ROOT / 'scripts/supplemental-history.json').read_text()):
        if event['unitId'] == item['unitId'] and event['date'] <= date:
            entry = {key: value for key, value in event.items() if key != 'unitId'}
            if not any(h['date'] == entry['date'] and h['description'] == entry['description'] for h in history):
                history.append(entry)
    history.sort(key=lambda event: event['date'])
    notices = ['来源已停用该单位的蓄能；升级表以当前普通等级为准。'] if disabled_charge else []
    if module == 'upgrade-temp' and not item['unitId'].startswith('09'):
        notices.append('临时单位的来源表格同步日期不表示活动开放日期；本期可用状态在页首另行说明。')
    if item['unitId'][:4] in ('0906', '0907', '0908'):
        notices.append('家乡精工防御，属于 2026 年 4 月 1 日至 7 月 30 日的批次，现已结束；与夜世界同名防御分开记录。')
    if item['unitId'] == '0014-Ruin-Knight':
        notices.append('废墟骑士是废墟女巫的召唤物，等级随召唤它的部队变化，不能单独升级。')
    return {'unitId': item['unitId'], 'title': title, 'originalName': snapshot['title'], 'module': module,
            'imgFolder': folder, 'sync': {'status': 'synced', 'source': 'Clash of Clans Wiki', 'sourceUrl': source_url,
             'revision': snapshot['revid'], 'revisionUrl': source_url + '?oldid=' + str(snapshot['revid']),
             'syncedOn': date, 'scope': 'Source statistics tables and available 2026 history; base values',
             **({'balanceUpdate': reviewed['sync']['balanceUpdate']} if reviewed and reviewed['sync'].get('balanceUpdate') else {}),
             **({'reviewedTableCorrections': reviewed['sync']['reviewedTableCorrections']} if reviewed and reviewed['sync'].get('reviewedTableCorrections') else {})},
            **({'levelReferences': reviewed['levelReferences']} if reviewed and reviewed.get('levelReferences') else {}),
            'tables': tables, 'images': images, 'history': history,
            'facts': selected_facts,
            'notices': notices}


def page_content(item, record, existing_text=None):
    page = ROOT / 'docs/upgrade' / (item['unitId'] + '.md')
    text = existing_text if existing_text is not None else (page.read_text(encoding='utf-8-sig') if page.exists() else None)
    if text is not None:
        match = re.match(r'---\n(.*?)\n---', text, re.S)
        frontmatter = match[1]
        frontmatter = re.sub(r'^module:.*$', 'module: ' + record['module'], frontmatter, flags=re.M)
    else:
        raise ValueError(f"{item['unitId']}: 请先按同类原页面建立中文页面和字段映射，再导入；来源数据已保留在预览中")
    frontmatter = re.sub(r'^dataSyncedOn:.*\n?', '', frontmatter, flags=re.M).rstrip()
    frontmatter = re.sub(r'^dataReviewedOn:.*\n?', '', frontmatter, flags=re.M).rstrip()
    frontmatter += '\ndataSyncedOn: ' + record['sync']['syncedOn']
    # Markdown is authored content. Sync may update metadata and JSON data, but
    # must not replace explanations, table layouts, links or historical records.
    return '---\n' + frontmatter + '\n---' + text[match.end():]


def main():
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument('--cache', type=Path, required=True)
    cli.add_argument('--date', required=True)
    cli.add_argument('--apply', action='store_true')
    args = cli.parse_args()
    inventory = json.loads((args.cache / 'inventory.json').read_text())
    updated, failures, records = [], list(inventory['failures']), []
    preserved = []
    for item in inventory['units']:
        old_path = ROOT / 'docs/upgrade' / (item['unitId'] + '.md')
        if old_path.exists() and re.search(r'^module: upgrade-temp$', old_path.read_text(encoding='utf-8-sig'), re.M) and item['unitId'][:4] not in ('0e03', '0e06', '0e07', '0e0b', '0e0c', '0e12', '0e13', '0e16', '0e17', '0e18', '0e81', '0e1c', '0e1d', '0e1e', '0906', '0907', '0908', '0909', '090a', '090b'):
            preserved.append({'unitId': item['unitId'], 'reason': 'Historical temporary unit; source modes require separate review'})
            continue
        try:
            record = make_record(item, args.date)
            records.append(record)
            if args.apply:
                content = page_content(item, record)
                DATA.mkdir(parents=True, exist_ok=True)
                (DATA / (item['unitId'] + '.json')).write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
                (ROOT / 'docs/upgrade' / (item['unitId'] + '.md')).write_text(content)
            updated.append({'unitId': item['unitId'], 'revision': record['sync']['revision'], 'tables': len(record['tables']), 'new': item['new']})
        except (ValueError, KeyError, IndexError) as error:
            failures.append({'unitId': item['unitId'], 'error': str(error)})
    (args.cache / 'sync-preview.json').write_text(json.dumps({'date': args.date, 'updated': updated, 'failures': failures, 'preservedHistoricalUnits': preserved}, ensure_ascii=False, indent=2) + '\n')
    (args.cache / 'records-preview.json').write_text(json.dumps(records, ensure_ascii=False))
    print(json.dumps({'applied': args.apply, 'units': len(updated), 'newUnits': sum(item['new'] for item in updated), 'failures': failures}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
