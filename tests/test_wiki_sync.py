"""Cases that previously mixed villages, lost currencies or changed source meaning."""
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from sync_wiki_data import VillageFilter, SourceTables, headers_and_rows, source_cell, extra_info, duration_value, is_unit_image


class WikiSyncTests(unittest.TestCase):
    def test_default_portraits_and_level_sprites_survive_gallery_filter(self):
        for filename in ('Ruin_Witch_info.png', 'Totem_Thrower_info.png', 'Barbarian13.png'):
            self.assertTrue(is_unit_image({'name': filename}), filename)
        self.assertFalse(is_unit_image({'name': 'Dragon_Duke_Concept_Art5.jpg'}))

    def test_transcluded_villages_are_not_mixed(self):
        source = ('<div class="wds-tabber"><ul>'
                  '<li data-hash="Home_Village">Home</li><li data-hash="Builder_Base">Builder</li>'
                  '<li data-hash="Clan_Capital">Capital</li></ul>'
                  '<div class="wds-tab__content"><div>home</div></div>'
                  '<div class="wds-tab__content"><div>builder</div></div>'
                  '<div class="wds-tab__content"><div>capital</div></div></div>')
        for village, wanted, excluded in [('Home_Village', 'home', 'builder'), ('Builder_Base', 'builder', 'capital'), ('Clan_Capital', 'capital', 'home')]:
            parser = VillageFilter(village); parser.feed(source)
            result = ''.join(parser.output)
            self.assertIn('>' + wanted + '<', result)
            self.assertNotIn('>' + excluded + '<', result)

    def test_builder_resource_alt_survives_nonsemantic_filename(self):
        parser = SourceTables()
        parser.feed('<table><tr><th>Level</th><th>Research Cost<img data-image-key="ElixirB.png" alt="Builder Elixir"></th><th>Research Time</th></tr><tr><td>1</td><td>10,000</td><td>30m</td></tr></table>')
        headers, rows, _ = headers_and_rows(parser.tables[0])
        info = extra_info(headers, rows, parser.image_rows[0][0], 'upgrade-bh', 'research')
        self.assertEqual(info[0]['icon'], 'Elixir2')
        self.assertFalse(info[0]['noGoldPass'])
        self.assertEqual(info[1]['type'], 'time')

    def test_grouped_equipment_keeps_all_three_ore_costs(self):
        parser = SourceTables()
        parser.feed('<table><tr><th rowspan="2">Level</th><th colspan="3">Upgrade Cost</th></tr>'
                    '<tr><th>Shiny Ore</th><th>Glowy Ore</th><th>Starry Ore</th></tr>'
                    '<tr><td>3</td><td>240</td><td>20</td><td>0</td></tr></table>')
        headers, rows, _ = headers_and_rows(parser.tables[0])
        info = extra_info(headers, rows, [], 'upgrade-home', 'research')
        self.assertEqual([item['icon'] for item in info], ['Shiny_Ore', 'Glowy_Ore', 'Starry_Ore'])
        self.assertTrue(all(item['noGoldPass'] for item in info))
        self.assertEqual(rows, [['3', '240', '20', '0']])

    def test_zero_unknown_and_inapplicable_are_different(self):
        self.assertEqual(source_cell('Free')['value'], 0)
        self.assertEqual(source_cell('0')['status'], 'known')
        self.assertEqual(source_cell('Varies')['status'], 'unknown')
        self.assertEqual(source_cell('N/A')['status'], 'not_applicable')
        self.assertEqual(source_cell('None', 'Build Time')['status'], 'not_applicable')
        self.assertEqual(source_cell('None', 'Preferred Target')['status'], 'known')

    def test_same_level_condition_variants_are_not_deduplicated(self):
        headers, rows, _ = headers_and_rows([['Level', 'Hitpoints', 'Town Hall Level'], ['1', '600', '4'], ['1', '1000', '5'], ['1', '1400', '6']])
        self.assertEqual(len(rows), 3)
        self.assertEqual([row[-1] for row in rows], ['4', '5', '6'])

    def test_multiple_cost_columns_keep_their_own_resources(self):
        info = extra_info(['Level', 'Cost', 'Cumulative Cost', 'Cost'], [['5', '20000', '36000', '20000']], [None, 'Gold', 'Gold', 'Elixir'], 'upgrade-home', 'building')
        self.assertEqual([item['icon'] for item in info], ['Gold', 'Gold', 'Elixir'])
        self.assertEqual([item['noGoldPass'] for item in info], [False, True, False])

    def test_ore_capacity_is_not_an_upgrade_cost(self):
        info = extra_info(['Level', 'Ore Capacity / Shiny Ore', 'Build Cost'], [['1', '10000', '600000']], [None, 'Shiny_Ore', 'Elixir'], 'upgrade-home', 'building')
        self.assertEqual([item['column'] for item in info], [2])

    def test_boost_prices_do_not_get_upgrade_discounts(self):
        info = extra_info(['Level', 'Boost Cost'], [['1', '25000']], [None, 'Dark_Elixir'], 'upgrade-home', 'research')
        self.assertTrue(info[0]['noGoldPass'])

    def test_duration_is_days_hours_minutes_seconds(self):
        self.assertEqual(duration_value('5d 12h'), '5,12,0,0')
        self.assertEqual(duration_value('30s'), '0,0,0,30')
        self.assertEqual(duration_value('Instant'), '0')


if __name__ == '__main__':
    unittest.main()
