"""Regression cases for source interpretation and silently omitted prerequisites."""
import importlib.util
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

SPEC = importlib.util.spec_from_file_location(
    "upgrade_data", Path(__file__).resolve().parents[1] / "scripts/check_upgrade_data.py"
)
checker = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(checker)


class UpgradeDataTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.page = self.root / "docs/upgrade/0006-Wizard.md"
        self.page.parent.mkdir(parents=True)
        self.local_headers = ["等级", "升级花费", "升级时间", "所需实验室等级", "所需大本等级"]
        self.local_rows = [["1", "120k", "0, 4", "1", "5"]]
        self.source_headers = ["Level", "Research Cost", "Research Time", "Laboratory Level Required"]
        self.source_rows = [["1", "120,000", "4h", "1"]]

    def compare(self):
        lines = ["| " + " | ".join(row) + " |" for row in [
            self.local_headers, ["---"] * len(self.local_headers), *self.local_rows
        ]]
        self.page.write_text("<UnitTable>\n" + "\n".join(lines) + "\n</UnitTable>", encoding="utf-8")
        html_rows = "<tr>" + "".join(f"<th>{header}</th>" for header in self.source_headers) + "</tr>"
        html_rows += "".join("<tr>" + "".join(f"<td>{value}</td>" for value in row) + "</tr>" for row in self.source_rows)
        snapshot = {"parse": {"title": "Wizard", "revid": 123, "text": {"*": f"<table>{html_rows}</table>"}}}
        with patch.object(checker, "ROOT", self.root):
            return checker.compare("0006-Wizard", snapshot)

    def test_equivalent_number_and_time_formats_are_not_changes(self):
        report = self.compare()
        self.assertEqual(report["changes"], [])
        self.assertEqual(report["semanticDifferences"], [])

    def test_na_is_a_semantic_difference_not_a_numeric_change(self):
        self.source_rows[0][3] = "N/A"
        report = self.compare()
        self.assertEqual(report["changes"], [])
        difference, = report["semanticDifferences"]
        self.assertEqual(difference["field"], "laboratoryLevel")
        self.assertEqual(difference["wiki"], {"status": "not_applicable", "value": None, "raw": "N/A"})

    def test_legacy_placeholder_does_not_equal_confirmed_na(self):
        self.local_rows[0][1] = "\\"
        self.source_rows[0][1] = "N/A"
        report = self.compare()
        unknown, = report["unknownCells"]
        self.assertEqual(unknown["local"]["status"], "unknown")
        self.assertEqual(unknown["local"]["raw"], "\\")
        self.assertEqual(unknown["wiki"]["status"], "not_applicable")

    def test_known_zero_is_preserved(self):
        self.assertEqual(checker.cell("0", "cost"), {"status": "known", "value": 0, "raw": "0"})
        self.assertEqual(checker.cell("", "cost")["status"], "unknown")

    def test_missing_local_prerequisite_fails_instead_of_reporting_zero_changes(self):
        self.local_headers.pop(3)
        self.local_rows[0].pop(3)
        with self.assertRaisesRegex(ValueError, "missing expected prerequisite columns: laboratoryLevel"):
            self.compare()

    def test_unrecognised_prerequisite_header_fails(self):
        self.local_headers[3] = "所需科技等级"
        with self.assertRaisesRegex(ValueError, "laboratoryLevel"):
            self.compare()

    def test_missing_fields_are_reported_in_both_directions(self):
        self.source_headers.append("Hero Hall Level Required")
        self.source_rows[0].append("1")
        report = self.compare()
        self.assertEqual(report["missingInSourceFields"], ["townHallLevel"])
        self.assertEqual(report["missingInLocalFields"], ["heroHallLevel"])

    def test_new_and_missing_levels_are_visible(self):
        self.local_rows.append(["2", "200k", "0, 5", "2", "6"])
        self.source_rows.append(["3", "300,000", "6h", "3"])
        report = self.compare()
        self.assertEqual(report["missingLevels"], [2])
        self.assertEqual([row["level"] for row in report["newLevels"]], [3])

    def test_duplicate_source_levels_are_preserved_as_variants(self):
        self.source_rows.append(["1", "130,000", "4h", "1"])
        report = self.compare()
        ambiguous, = report["ambiguousLevels"]
        self.assertEqual(ambiguous["level"], 1)
        self.assertEqual(len(ambiguous["variants"]), 2)
        self.assertEqual(report["changes"], [])
        self.assertEqual(report["missingLevels"], [])

    def test_rowspan_and_colspan_preserve_column_alignment(self):
        parser = checker.Tables()
        parser.feed('<table><tr><th colspan="2">Header</th></tr>'
                    '<tr><td rowspan="2">1</td><td>10</td></tr>'
                    '<tr><td>20</td></tr></table>')
        self.assertEqual(parser.tables, [[["Header", "Header"], ["1", "10"], ["1", "20"]]])

    def test_bad_or_repeated_duration_units_are_rejected(self):
        for value in ["1h junk", "1h 2h", "tomorrow"]:
            with self.subTest(value=value), self.assertRaises(ValueError):
                checker.seconds(value, wiki=True)

    def test_empty_table_is_rejected(self):
        self.local_rows.clear()
        with self.assertRaisesRegex(ValueError, "no level rows"):
            self.compare()


if __name__ == "__main__":
    unittest.main()
