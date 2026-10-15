"""Regression cases for updating values without replacing the authored page."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from update_authored_data import parse_tables, update_page
from sync_wiki_data import source_cell


class AuthoredTableTests(unittest.TestCase):
    def setUp(self):
        self.text = ('说明和链接：[相关单位](/upgrade/example)\n<UnitProperties>属性</UnitProperties>\n'
                     '<UnitTable>\n\n| 等级 | 生命值 | 所需大本等级 | 附加字段 |\n'
                     '| --- | --- | --- | --- |\n| 1 | 100 | 4 | 原说明 |\n</UnitTable>\n'
                     '<Panel>公式</Panel>\n<Timeline>历史</Timeline>\n')
        self.source = {'sourceTableIndex': 3, 'headers': ['Level', 'Hitpoints', 'Town Hall Level'],
                       'rows': [[source_cell(v) for v in row] for row in [['1', '200', '4'], ['1', '300', '5'], ['2', '400', '6']]]}
        self.record = {'unitId': 'test', 'tables': [self.source]}
        self.mapping = {'table': 0, 'headers': parse_tables(self.text)[0]['headers'],
                        'sourceTableIndex': 3, 'sourceHeaders': self.source['headers'][:],
                        'columns': {'0': 0, '1': 1, '2': 2}}
        self.translated = {'3': [[c['raw'] for c in row] for row in self.source['rows']]}

    def update(self, text=None):
        return update_page(text or self.text, [self.mapping], self.record, self.translated, {})

    def test_update_preserves_non_table_content_columns_and_condition_variants(self):
        result, report = self.update()
        before, after = parse_tables(self.text)[0], parse_tables(result)[0]
        self.assertEqual(result[:after['start']], self.text[:before['start']])
        self.assertEqual(result[after['end']:], self.text[before['end']:])
        self.assertEqual(after['headers'], before['headers'])
        self.assertEqual(after['rows'], [['1', '200', '4', '原说明'], ['1', '300', '5', '原说明'], ['2', '400', '6', '未知']])
        self.assertEqual(len(report[0]['unknownNewCells']), 1)
        self.assertEqual(self.update(result)[0], result)

    def test_changed_source_schema_stops_update(self):
        self.source['headers'][1] = 'Different entity hitpoints'
        with self.assertRaisesRegex(ValueError, 'source schema changed'):
            self.update()

    def test_unknown_source_preserves_existing_value(self):
        self.source['rows'][0][1] = source_cell('Unknown')
        result, _ = self.update()
        self.assertEqual(parse_tables(result)[0]['rows'][0][1], '100')

    def test_derived_table_is_not_replaced_with_parent_data(self):
        self.mapping = {'table': 0, 'keepOriginal': True, 'reason': '召唤物单独维护'}
        self.assertEqual(self.update()[0], self.text)

    def test_special_historical_levels_stay_before_regular_levels(self):
        self.source['rows'] = self.source['rows'][-1:]
        self.translated['3'] = self.translated['3'][-1:]
        result, _ = self.update(self.text.replace('| 1 |', '| 1<sup>*</sup> |'))
        self.assertEqual([r[0] for r in parse_tables(result)[0]['rows']], ['1<sup>*</sup>', '2'])

    def test_markdown_table_has_no_blank_line_after_separator(self):
        result, _ = self.update(self.text.replace('| 1 |', '\n\n| 1 |'))
        self.assertNotIn('| --- | --- | --- | --- |\n\n', result)

    def test_experience_is_recomputed_from_updated_time(self):
        self.mapping['columns']['3'] = {'computed': 'exp'}
        result, _ = self.update()
        self.assertTrue(all(row[3] == '' for row in parse_tables(result)[0]['rows']))

    def test_changed_multiplier_evidence_stops_update(self):
        self.mapping['columns']['1'] = {'multiply': 1, 'factor': 0.6,
                                        'evidence': {'table': 2, 'header': 'Attack Speed', 'raw': '0.6s'}}
        self.record['tables'].append({'sourceTableIndex': 2, 'headers': ['Attack Speed'],
                                      'rows': [[source_cell('0.7s')]]})
        with self.assertRaisesRegex(ValueError, 'calculation factor changed'):
            self.update()


if __name__ == '__main__':
    unittest.main()
