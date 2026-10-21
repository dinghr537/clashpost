"""Catch source-key mistakes before they hide levels or merge separate entities."""
from copy import deepcopy
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from sync_wiki_data import source_cell, validate_table_levels, preserve_table_corrections


def table(index, headers, rows):
    return {'sourceTableIndex': index, 'headers': headers,
            'rows': [[source_cell(str(cell)) for cell in row] for row in rows]}


class TableVisibilityTests(unittest.TestCase):
    def test_duplicate_levels_require_distinct_prerequisites(self):
        ambiguous = table(3, ['Level', 'Hitpoints'], [[11, 2500], [11, 2700]])
        with self.assertRaisesRegex(ValueError, '重复等级'):
            validate_table_levels([ambiguous])
        variants = table(3, ['Level', 'Hitpoints', 'Town Hall Level Required'],
                         [[1, 700, 4], [1, 1000, 5]])
        validate_table_levels([variants])
        variants['rows'].append(deepcopy(variants['rows'][0]))
        with self.assertRaisesRegex(ValueError, '重复等级'):
            validate_table_levels([variants])

    def test_referenced_child_level_must_be_available(self):
        parent = table(2, ['Level', 'Child Level'], [[17, 4], [18, 4]])
        child = table(4, ['Level', 'Hitpoints'], [[1, 100], [2, 200], [3, 300]])
        references = [{'table': 2, 'column': 'Child Level', 'targetTable': 4}]
        with self.assertRaisesRegex(ValueError, '关联单位缺少等级'):
            validate_table_levels([parent, child], references)
        child['rows'].append([source_cell('4'), source_cell('400')])
        validate_table_levels([parent, child], references)

    def test_sync_cannot_merge_reviewed_entities_again(self):
        current = table(2, ['Helper', 'Town Hall Level Required'], [['A', 10], ['B', 10]])
        reviewed = {'tables': [current], 'sync': {'reviewedTableCorrections': [{'table': 2}]}}
        merged = table(2, current['headers'], [['A B', 10]])
        with self.assertRaisesRegex(ValueError, '条目缺失'):
            preserve_table_corrections(reviewed, [merged])
        expanded = deepcopy(current)
        expanded['rows'].append([source_cell('C'), source_cell('11')])
        preserve_table_corrections(reviewed, [expanded])


if __name__ == '__main__':
    unittest.main()
