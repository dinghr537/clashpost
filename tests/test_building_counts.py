"""Regression checks for authored count tables and reviewed source corrections."""
from copy import deepcopy
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from check_building_counts import compare_page, expand_groups
from sync_wiki_data import preserve_table_corrections, source_cell


def row(*values):
    return [source_cell(str(value)) for value in values]


def home_record():
    return {'tables': [{'sourceTableIndex': 2,
                        'headers': ['Town Hall Level', '1', '2', '3'],
                        'rows': [row('Number Available', 0, 0, 0),
                                 row('', 16, 17, 18), row('', 2, 3, 3)]}]}


def page(groups, counts, extra=''):
    return (f'<BuildingNum><BuildingNumRow title="大本等级" num="{groups}" />'
            f'<BuildingNumRow title="建筑数量" num="{counts}" /></BuildingNum>{extra}')


class BuildingCountTests(unittest.TestCase):
    def test_missing_hall_and_stale_count_are_reported(self):
        report = compare_page('unit', page('1 - 15, 16 - 17, 18', '0, 2, 3'), home_record(), [])
        self.assertEqual([(d['level'], d['display'], d['source']) for d in report['differences']], [(17, 2, 3)])
        report = compare_page('unit', page('1 - 15, 17 - 18', '0, 3'), home_record(), [])
        self.assertEqual([(d['level'], d['display'], d['source']) for d in report['differences']], [(16, None, 2)])

    def test_merging_uses_the_remaining_buildings(self):
        record = {'tables': [{'sourceTableIndex': 1, 'headers': ['Town Hall Level', '16', '17'],
                              'rows': [row('Number Available', '7/3', '7/0')]}]}
        report = compare_page('unit', page('16, 17', '3, 0'), record, [])
        self.assertEqual(report['differences'], [])
        self.assertEqual(report['cells'], 2)

    def test_first_level_requirement_catches_a_stale_source_count(self):
        record = {'tables': [{'sourceTableIndex': 1, 'headers': ['Town Hall Level', '4'],
                              'rows': [row('Number Available', 0)]}]}
        upgrades = ('<UnitTable>\n| 等级 | 所需大本等级 |\n| --- | --- |\n'
                    '| 1 | 4 |\n</UnitTable>')
        report = compare_page('unit', page('4', '0', upgrades), record, [])
        self.assertEqual(report['differences'][0]['row'], 'Initial level requirement')
        self.assertEqual(report['differences'][0]['level'], 4)

    def test_reviewed_disagreement_must_match_all_recorded_values(self):
        record = {'tables': [{'sourceTableIndex': 1,
                              'headers': ['Number Available', 'Builder Hall Level / 5'],
                              'rows': [row('Total', 2)]}]}
        review = [{'unitId': 'unit', 'sourceTableIndex': 1, 'row': 'Total',
                   'levels': [5], 'display': 1, 'source': 2}]
        difference, = compare_page('unit', page('5', '1'), record, review)['differences']
        self.assertTrue(difference['reviewed'])
        record['tables'][0]['rows'][0][1] = source_cell('3')
        difference, = compare_page('unit', page('5', '1'), record, review)['differences']
        self.assertFalse(difference['reviewed'])

    def test_ranges_reject_overlaps_and_mismatched_columns(self):
        with self.assertRaisesRegex(ValueError, 'duplicate'):
            expand_groups('1 - 3, 3 - 4', '0, 1')
        with self.assertRaisesRegex(ValueError, 'wrong number'):
            expand_groups('1 - 3, 4', '0')

    def test_old_snapshot_cannot_restore_reviewed_count(self):
        table = {'sourceTableIndex': 1, 'headers': ['Town Hall Level', '4'],
                 'rows': [row('Number Available', 1)]}
        record = {'tables': [table], 'sync': {'reviewedTableCorrections': [
            {'table': 1, 'cells': [{'rowKey': 'Number Available', 'header': '4'}]}]}}
        old = deepcopy(table)
        old['rows'][0][1] = source_cell('0')
        with self.assertRaisesRegex(ValueError, '数值发生变化'):
            preserve_table_corrections(record, [old])
        preserve_table_corrections(record, [deepcopy(table)])


if __name__ == '__main__':
    unittest.main()
