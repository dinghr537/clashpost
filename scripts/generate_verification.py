"""Generate docs/verification.md from what the unit pages actually display.

Every table cell, unit property and building-count row that shows "待更新" is
listed, and every pre-update value flagged with the outdated marker (shown as *)
is listed separately. Run with --check to fail when the checklist is stale.
"""
import collections
import pathlib
import re
import sys

root = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / 'scripts'))
from update_authored_data import OUTDATED, plain

PENDING = '待更新'
# Sentences that only explain the label, or restate gaps already listed from tables.
COVERED = re.compile(r'标为待更新|标为“待更新”|暂列为待更新|属性尚待更新|伤害尚待更新')
pages = root / 'docs/upgrade'


def label(text):
    """Column heading without footnote markers or line breaks."""
    return re.sub(r'[①-⑳#*]', '', plain(text.replace('<br>', '')))


def format_levels(levels):
    nums, other = [], []
    for level in levels:
        (nums if re.fullmatch(r'\d+', level) else other).append(level)
    runs = []
    for n in sorted({int(x) for x in nums}):
        if runs and n == runs[-1][-1] + 1:
            runs[-1].append(n)
        else:
            runs.append([n])
    out = [str(r[0]) if len(r) == 1 else f'{r[0]}–{r[-1]}' for r in runs]
    return '、'.join(out + sorted(set(other), key=other.index))


def markdown_tables(text):
    """Every Markdown table on a page, whether or not it sits in <UnitTable>."""
    tables = []
    for block in re.finditer(r'(?:^[ \t]*\|[^\n]*\n?)+', text, re.M):
        lines = [l.strip() for l in block[0].splitlines() if l.strip()]
        if len(lines) < 3 or not re.fullmatch(r'\|[\s:|-]+\|', lines[1]):
            continue
        split = lambda line: [cell.strip() for cell in line[1:-1].split('|')]
        tables.append({'start': block.start(), 'headers': split(lines[0]), 'rows': [split(l) for l in lines[2:]]})
    return tables


def scan(marker):
    """{(unit, title, part, fields): [levels]} for table cells containing marker."""
    found = collections.defaultdict(list)
    properties = []
    for page in sorted(pages.glob('*.md')):
        unit, text = page.stem, page.read_text()
        if marker not in text:
            continue
        title = re.search(r'^navTitle:\s*"?([^"\n]+)', text, re.M)
        title = title[1] if title else unit
        for table in markdown_tables(text):
            part = re.findall(r'imgAlt="([^"]+)"', text[:table['start']])
            part = part[-1] if part else title
            part = '' if part in (title, '$frontmatter.navTitle') else part
            for row in table['rows']:
                fields = tuple(label(table['headers'][i]) for i, cell in enumerate(row) if i and marker in cell)
                if fields:
                    found[(unit, title, part, fields)].append(plain(row[0]))
        if marker == PENDING:
            for name in re.findall(r'pKey="([^"]+)" pValue="待更新', text):
                properties.append((unit, title, name))
            for name in re.findall(r'<BuildingNumRow title="[^"]*" num="[^"]*待更新', text):
                properties.append((unit, title, '建筑数量'))
            for line in text.splitlines():
                if PENDING not in line or line.lstrip().startswith('|') or 'pKey=' in line or COVERED.search(line):
                    continue
                note = plain(re.sub(r'<a [^>]*>[^<]*</a>|\[([^]]*)\]\([^)]*\)', lambda m: m[1] or '', line))
                properties.append((unit, title, note))
    return found, properties


def table_rows(found):
    rows = []
    for (unit, title, part, fields), levels in sorted(found.items()):
        where = f'{part}：' if part else ''
        rows.append(f'| [{title}](/upgrade/{unit}) | {where}{format_levels(levels)} | {"、".join(fields)} |')
    return rows


pending, properties = scan(PENDING)
outdated, _ = scan(OUTDATED)

lines = [
    '---',
    'title: "待更新数据核对清单"',
    'module: verification',
    'canonical: /verification',
    'robots: noindex, nofollow',
    'hasUpdateTime: false',
    '---',
    '',
    '本清单由各单位页实际显示的内容自动生成：页面上每一处“待更新”，以及每一个以 * 标出、暂列更新前数值的格子，都会列在这里。“待更新”表示官方公告、Wiki 和 ClashKing 游戏数据目前都还没有提供该数值。',
]
if pending:
    lines += ['', '## 待更新', '', '| 单位 | 等级 | 字段 |', '| --- | --- | --- |', *table_rows(pending)]
if properties:
    lines += ['', '## 属性与说明中的待更新事项', '', '| 单位 | 内容 |', '| --- | --- |']
    grouped = collections.defaultdict(list)
    for unit, title, name in properties:
        grouped[name].append(f'[{title}](/upgrade/{unit})')
    lines += [f'| {"、".join(units)} | {name} |' for name, units in grouped.items()]
if outdated:
    lines += ['', '## 可能需要更新（暂列更新前数值，页面以 * 标出）', '', '| 单位 | 等级 | 字段 |', '| --- | --- | --- |', *table_rows(outdated)]

result = '\n'.join(lines) + '\n'
destination = root / 'docs/verification.md'
if '--check' in sys.argv:
    if destination.read_text() != result:
        raise SystemExit('待更新清单与页面不一致；请运行 python3 scripts/generate_verification.py')
else:
    destination.write_text(result)
count = lambda found: sum(len(v) * len(k[3]) for k, v in found.items())
print('pending cells', count(pending), 'properties', len(properties), 'outdated cells', count(outdated))
