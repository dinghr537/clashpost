"""Keep the pre-sync unit-page structure while allowing source-backed value edits."""
from collections import Counter
from io import BytesIO
import json
from pathlib import Path
import re
import subprocess
import sys
import tarfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from update_authored_data import parse_tables

BASELINE = '9e77a85'


class OriginalContentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        archive = subprocess.check_output(['git', 'archive', BASELINE, 'docs/upgrade'], cwd=ROOT)
        with tarfile.open(fileobj=BytesIO(archive)) as files:
            cls.pages = {f.name: files.extractfile(f).read().decode('utf-8-sig')
                         for f in files if f.isfile() and f.name.endswith('.md')}

    def test_all_original_pages_keep_components_headers_links_and_history(self):
        for name, original in self.pages.items():
            with self.subTest(page=name):
                path = ROOT / name
                self.assertTrue(path.is_file())
                current = path.read_text()
                self.assertNotIn('<SyncedUnitData', current)
                # A matching label in another mode must not hide a removed property.
                old_keys = Counter(re.findall(r'<UnitProperty\b[^\n]*?pKey="([^"]+)"', original))
                new_keys = Counter(re.findall(r'<UnitProperty\b[^\n]*?pKey="([^"]+)"', current))
                self.assertFalse(old_keys - new_keys)
                for component in ('Panel', 'SwitchTabGroup', 'BuildingNum', 'DistrictTable'):
                    self.assertGreaterEqual(len(re.findall('<' + component + r'\b', current)),
                                            len(re.findall('<' + component + r'\b', original)), component)
                for pattern in (r'imgHd="([^"]+)"', r'<TimelineItem\b[^>]*?date="([^"]+)"'):
                    self.assertFalse(Counter(re.findall(pattern, original)) - Counter(re.findall(pattern, current)))
                before = parse_tables(original)
                after = parse_tables(current)
                if path.stem == '0487-Pet-House':
                    columns = json.loads(re.search(r'const columns = (.*?);', current, re.S)[1])
                    self.assertEqual([c['heading'] for c in columns], before[0]['headers'])
                    continue
                self.assertGreaterEqual(len(after), len(before))
                for index, table in enumerate(before):
                    expected = table['headers'][:]
                    if path.stem == '030a-Inferno-Tower':
                        expected = [h.replace('1.25', '1.5') for h in expected]
                    self.assertEqual(after[index]['headers'], expected)
                    self.assertGreaterEqual(len(after[index]['rows']), len(table['rows']))
                    old_links = set(re.findall(r'(?:href="|\]\()(/[^"\s)]+)', str(table['rows'])))
                    new_links = set(re.findall(r'(?:href="|\]\()(/[^"\s)]+)', str(after[index]['rows'])))
                    self.assertFalse(old_links - new_links)


if __name__ == '__main__':
    unittest.main()
