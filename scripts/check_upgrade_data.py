#!/usr/bin/env python3
"""Compare three Home Village upgrade tables with a pinned public Wiki revision.

Read-only: produces a reviewable report; never overwrites game data or pages.
"""
import argparse
import json
import re
from collections import Counter
from datetime import datetime
from decimal import Decimal
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
PILOTS = {
    "0301-Cannon": ("Cannon", ["Build Cost", "Build Time", "Town Hall Level Required", "Damage per Shot"]),
    "0200-Barbarian-King": ("Barbarian King", ["Upgrade Cost", "Upgrade Time", "Hero Hall Level Required"]),
    "0006-Wizard": ("Wizard", ["Research Cost", "Research Time", "Laboratory Level Required"]),
}
FIELDS = {
    "level": ("等级", "Level"),
    "cost": ("升级费用|升级花费", "Build Cost|Upgrade Cost|Research Cost"),
    "timeSeconds": ("升级时间", "Build Time|Upgrade Time|Research Time"),
    "townHallLevel": ("所需大本等级", "Town Hall Level Required"),
    "heroHallLevel": ("所需英雄殿堂等级", "Hero Hall Level Required"),
    "laboratoryLevel": ("所需实验室等级", "Laboratory Level Required"),
}
EXPECTED_LOCAL_FIELDS = {
    "0301-Cannon": {"townHallLevel"},
    "0200-Barbarian-King": {"townHallLevel", "heroHallLevel"},
    "0006-Wizard": {"townHallLevel", "laboratoryLevel"},
}


def cell(value, field, wiki=False):
    """Keep source semantics: a legacy placeholder is not a proven N/A."""
    raw = value.strip()
    if raw in ("N/A", "None"):
        return {"status": "not_applicable", "value": None, "raw": raw}
    if raw == "Free" or (field == "timeSeconds" and raw == "Instant"):
        return {"status": "known", "value": 0, "raw": raw}
    if raw in ("", "\\", "-", "—"):
        return {"status": "unknown", "value": None, "raw": raw}
    parsed = seconds(raw, wiki) if field == "timeSeconds" else number(raw)
    return {"status": "known", "value": parsed, "raw": raw}


def number(value):
    value = value.strip()
    if value in ("\\", "N/A", ""):
        return None
    match = re.fullmatch(r"([0-9]+(?:\.[0-9]+)?)([kKmMbBwWyY]?)", value.replace(",", ""))
    if not match:
        raise ValueError(f"Invalid numeric value: {value!r}")
    scale = {"": 1, "k": 1000, "m": 10**6, "b": 10**9, "w": 10**4, "y": 10**8}
    result = Decimal(match[1]) * scale[match[2].lower()]
    if result != result.to_integral_value():
        raise ValueError(f"Expected integer upgrade data: {value!r}")
    return int(result)


def seconds(value, wiki=False):
    if value.strip() in ("\\", "N/A", ""):
        return None
    if wiki:
        parts = re.findall(r"(\d+)\s*([dhms])", value)
        if not parts or re.sub(r"\d+\s*[dhms]|\s+", "", value):
            raise ValueError(f"Invalid Wiki duration: {value!r}")
        units = [unit for _, unit in parts]
        if len(units) != len(set(units)):
            raise ValueError(f"Repeated duration unit: {value!r}")
        return sum(int(amount) * {"d": 86400, "h": 3600, "m": 60, "s": 1}[unit] for amount, unit in parts)
    parts = [part.strip() for part in value.replace("，", ",").split(",")]
    if not 1 <= len(parts) <= 4 or any(not part.isdigit() for part in parts):
        raise ValueError(f"Invalid local duration: {value!r}")
    return sum(int(part) * unit for part, unit in zip(parts, [86400, 3600, 60, 1]))


def clean(value):
    return " ".join(re.sub(r"<[^>]+>|\*", " ", value).split())


class Tables(HTMLParser):
    """Read top-level HTML tables and expand rowspan/colspan before matching rows."""
    def __init__(self):
        super().__init__()
        self.tables = []
        self.depth = 0
        self.cell = None

    def handle_starttag(self, tag, attrs):
        if tag == "table":
            if self.depth == 0:
                self.rows = []
            self.depth += 1
        if self.depth != 1:
            return
        if tag == "tr":
            self.cells = []
        if tag in ("td", "th"):
            attrs = dict(attrs)
            self.cell = []
            self.span = (int(attrs.get("rowspan", 1)), int(attrs.get("colspan", 1)))
        if tag == "br" and self.cell is not None:
            self.cell.append(" ")

    def handle_data(self, data):
        if self.depth == 1 and self.cell is not None:
            self.cell.append(data)

    def handle_endtag(self, tag):
        if self.depth == 1:
            if tag in ("td", "th") and self.cell is not None:
                self.cells.append((clean("".join(self.cell)), *self.span))
                self.cell = None
            if tag == "tr" and self.cells:
                self.rows.append(self.cells)
        if tag == "table":
            self.depth -= 1
            if self.depth == 0:
                self.tables.append(self.expand(self.rows))

    @staticmethod
    def expand(rows):
        grid = {}
        result = []
        for row_index, cells in enumerate(rows):
            column = 0
            for value, rowspan, colspan in cells:
                while (row_index, column) in grid:
                    column += 1
                for r in range(rowspan):
                    for c in range(colspan):
                        key = (row_index + r, column + c)
                        if key in grid:
                            raise ValueError("Overlapping HTML table spans")
                        grid[key] = value
                column += colspan
            width = max((c for r, c in grid if r == row_index), default=-1) + 1
            result.append([grid.get((row_index, c), "") for c in range(width)])
        return result


def extract(headers, rows, wiki=False):
    mapping = {}
    for key, aliases in FIELDS.items():
        names = aliases[1 if wiki else 0].split("|")
        matches = [i for i, header in enumerate(headers) if clean(header).replace(" ", "") in [n.replace(" ", "") for n in names]]
        if len(matches) > 1:
            raise ValueError(f"Ambiguous column: {key}")
        if matches:
            mapping[key] = matches[0]
    if not {"level", "cost", "timeSeconds"}.issubset(mapping):
        raise ValueError("Table is missing level, cost or time")
    values = []
    for row in rows:
        if len(row) != len(headers):
            raise ValueError("Unexpected number of table columns")
        entry = {}
        for key, column in mapping.items():
            entry[key] = number(row[column]) if key == "level" else cell(row[column], key, wiki)
        if entry["level"] is None or entry["level"] < 1:
            raise ValueError("Missing or invalid level")
        values.append(entry)
    if not values:
        raise ValueError("Table has no level rows")
    return values


def compare(unit, snapshot):
    title, required_headers = PILOTS[unit]
    data_path = ROOT / 'docs/.vitepress/theme/assets/unit-data' / (unit + '.json')
    if data_path.exists():
        return compare_synced(unit, snapshot, json.loads(data_path.read_text()))
    page = ROOT / "docs" / "upgrade" / f"{unit}.md"
    content = page.read_text(encoding="utf-8-sig")
    block = re.search(r"<UnitTable\b[^>]*>(.*?)</UnitTable>", content, re.S)
    if not block:
        raise ValueError("Local UnitTable not found")
    lines = [line.strip() for line in block[1].splitlines() if line.strip().startswith("|")]
    split = lambda line: [cell.strip() for cell in line[1:-1].split("|")]
    local = extract(split(lines[0]), [split(line) for line in lines[2:]])
    missing_required = EXPECTED_LOCAL_FIELDS[unit] - local[0].keys()
    if missing_required:
        raise ValueError(f"Local table is missing expected prerequisite columns: {', '.join(sorted(missing_required))}")
    if len({row["level"] for row in local}) != len(local):
        raise ValueError("Duplicate local levels")
    parsed = snapshot.get("parse", {})
    if parsed.get("title") != title or not isinstance(parsed.get("revid"), int):
        raise ValueError("Snapshot title or revision does not match the requested unit")
    parser = Tables()
    parser.feed(parsed["text"]["*"])
    candidates = [table for table in parser.tables if table and set(required_headers).issubset(set(table[0]))]
    if len(candidates) != 1:
        raise ValueError(f"Expected one matching Wiki table, found {len(candidates)}")
    source_rows = extract(candidates[0][0], candidates[0][1:], wiki=True)
    counts = Counter(row["level"] for row in source_rows)
    ambiguous = sorted(level for level, count in counts.items() if count > 1)
    source = {row["level"]: row for row in source_rows if row["level"] not in ambiguous}
    old = {row["level"]: row for row in local}
    changes = []
    semantic_differences = []
    unknown_cells = []
    for level in sorted(old.keys() & source.keys()):
        for field in sorted((old[level].keys() & source[level].keys()) - {"level"}):
            local_cell, source_cell = old[level][field], source[level][field]
            difference = {"level": level, "field": field, "local": local_cell, "wiki": source_cell}
            if "unknown" in (local_cell["status"], source_cell["status"]):
                unknown_cells.append(difference)
            elif local_cell["status"] != source_cell["status"]:
                semantic_differences.append(difference)
            elif local_cell["status"] == "known" and local_cell["value"] != source_cell["value"]:
                changes.append(difference)
    return {
        "reportVersion": 2,
        "unit": unit,
        "localBaseline": "Legacy Markdown; unit update dates vary",
        "comparedAt": datetime.now(ZoneInfo("America/Vancouver")).isoformat(timespec="seconds"),
        "source": {"name": "Clash of Clans Wiki", "url": f"https://clashofclans.fandom.com/wiki/{title.replace(' ', '_')}", "revision": parsed["revid"], "revisionUrl": f"https://clashofclans.fandom.com/wiki/{title.replace(' ', '_')}?oldid={parsed['revid']}"},
        "scope": "Primary Home Village upgrade table; base cost, time and available requirements only",
        "changes": changes,
        "semanticDifferences": semantic_differences,
        "unknownCells": unknown_cells,
        "newLevels": [source[level] for level in sorted(source.keys() - old.keys())],
        "missingLevels": sorted(old.keys() - source.keys() - set(ambiguous)),
        "ambiguousLevels": [{"level": level, "variants": [row for row in source_rows if row["level"] == level]} for level in ambiguous],
        "missingInSourceFields": sorted(local[0].keys() - source_rows[0].keys()),
        "missingInLocalFields": sorted(source_rows[0].keys() - local[0].keys()),
        "independentCorroboration": False,
        "pageModified": False,
    }


def compare_synced(unit, snapshot, record):
    """Compare conditions as well as levels after the migration to JSON."""
    from sync_wiki_data import VillageFilter
    title, required = PILOTS[unit]
    parsed = snapshot.get('parse', {})
    if parsed.get('title') != title or not isinstance(parsed.get('revid'), int):
        raise ValueError('Snapshot title or revision does not match the requested unit')
    filtered = VillageFilter('Home_Village'); filtered.feed(parsed['text']['*'])
    parser = Tables(); parser.feed(''.join(filtered.output))
    sources = [table for table in parser.tables if table and set(required).issubset(table[0])]
    locals_ = [table for table in record['tables'] if set(required).issubset(table['headers'])]
    if len(sources) != 1 or len(locals_) != 1:
        raise ValueError('Expected one matching source and local primary table')
    source_rows = extract(sources[0][0], sources[0][1:], wiki=True)
    local_rows = extract(locals_[0]['headers'], [[cell['raw'] for cell in row] for row in locals_[0]['rows']], wiki=True)
    def condition_key(row):
        return (row['level'], *[(field, row[field]['status'], row[field]['value']) for field in sorted(row) if field.endswith('Level')])
    source = {condition_key(row): row for row in source_rows}
    local = {condition_key(row): row for row in local_rows}
    if len(source) != len(source_rows) or len(local) != len(local_rows):
        raise ValueError('Repeated level/condition combination in primary upgrade table')
    changes, semantic, unknown = [], [], []
    for key in source.keys() & local.keys():
        for field in sorted((source[key].keys() & local[key].keys()) - {'level'}):
            a, b = local[key][field], source[key][field]
            entry = {'level': key[0], 'conditions': key[1:], 'field': field, 'local': a, 'wiki': b}
            if 'unknown' in (a['status'], b['status']):
                unknown.append(entry)
            elif a['status'] != b['status']:
                semantic.append(entry)
            elif a['value'] != b['value']:
                changes.append(entry)
    counts = Counter(row['level'] for row in source_rows)
    return {'reportVersion': 3, 'unit': unit, 'localBaseline': record['sync']['syncedOn'],
            'comparedAt': datetime.now(ZoneInfo('America/Vancouver')).isoformat(timespec='seconds'),
            'source': {'name': 'Clash of Clans Wiki', 'revision': parsed['revid'], 'url': record['sync']['sourceUrl']},
            'scope': 'Primary Home Village upgrade table, including level/condition variants',
            'changes': changes, 'semanticDifferences': semantic, 'unknownCells': unknown,
            'newLevels': [source[key] for key in sorted(source.keys()-local.keys())],
            'missingLevels': [local[key] for key in sorted(local.keys()-source.keys())],
            'ambiguousLevels': [{'level': level, 'variants': [row for row in source_rows if row['level'] == level]} for level, count in counts.items() if count > 1],
            'missingInSourceFields': sorted(local_rows[0].keys()-source_rows[0].keys()),
            'missingInLocalFields': sorted(source_rows[0].keys()-local_rows[0].keys()),
            'independentCorroboration': False, 'pageModified': False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--unit", choices=PILOTS, required=True)
    parser.add_argument("--snapshot", type=Path, help="Saved MediaWiki parse JSON with text and revid")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        if args.output.resolve().is_relative_to(ROOT):
            raise ValueError("Save review reports outside the repository, e.g. /tmp/cannon-diff.json")
        if args.snapshot:
            snapshot = json.loads(args.snapshot.read_text(encoding="utf-8"))
        else:
            title = PILOTS[args.unit][0]
            query = urlencode({"action": "parse", "page": title, "prop": "text|revid", "format": "json"})
            request = Request(f"https://clashofclans.fandom.com/api.php?{query}", headers={"User-Agent": "ClashpostUpgradeReview/0.1"})
            with urlopen(request, timeout=30) as response:
                snapshot = json.load(response)
        report = compare(args.unit, snapshot)
        args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"{args.unit}: {len(report['changes'])} numeric changes, {len(report['semanticDifferences'])} semantic differences, {len(report['newLevels'])} new levels, {len(report['ambiguousLevels'])} ambiguous levels, {len(report['unknownCells'])} unknown cells. Report: {args.output}")
    except (ValueError, KeyError, OSError) as error:
        parser.exit(1, f"Cannot verify upgrade data: {error}\n")


if __name__ == "__main__":
    main()
