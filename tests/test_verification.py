import pathlib
import re
import subprocess
import sys
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
PAGES = ROOT / "docs/upgrade"
CHECKLIST = ROOT / "docs/verification.md"


def checklist_rows():
    """Checklist table rows keyed by every unit page they link to."""
    rows = {}
    for line in CHECKLIST.read_text().splitlines():
        for unit in re.findall(r"\(/upgrade/([^)]+)\)", line):
            rows.setdefault(unit, []).append(line)
    return rows


def plain(text):
    text = re.sub(r"<[^>]+>", "", text.replace("<br>", ""))
    return re.sub(r"[\s①-⑳#*]", "", text)


class VerificationChecklistTests(unittest.TestCase):
    def test_checklist_matches_pages(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts/generate_verification.py"), "--check"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_every_pending_cell_on_a_page_is_listed(self):
        """Independent of the generator: any table cell showing 待更新 or a * marker must be listed."""
        rows = checklist_rows()
        for page in sorted(PAGES.glob("*.md")):
            text = page.read_text()
            lines = text.splitlines()
            for index, line in enumerate(lines):
                if not line.lstrip().startswith("|") or ("待更新" not in line and "cp-outdated" not in line):
                    continue
                # The header is the first line of this table block.
                start = index
                while start > 0 and lines[start - 1].lstrip().startswith("|"):
                    start -= 1
                headers = [plain(h) for h in lines[start].strip()[1:-1].split("|")]
                cells = line.strip()[1:-1].split("|")
                with self.subTest(page=page.stem, row=plain(cells[0])):
                    self.assertIn(page.stem, rows, "page has pending cells but is missing from the checklist")
                    listed = "".join(plain(r) for r in rows[page.stem])
                    for heading, cell in zip(headers, cells):
                        if "待更新" in cell or "cp-outdated" in cell:
                            self.assertIn(heading, listed)

    def test_every_pending_property_is_listed(self):
        rows = checklist_rows()
        for page in sorted(PAGES.glob("*.md")):
            for name in re.findall(r'pKey="([^"]+)" pValue="待更新', page.read_text()):
                with self.subTest(page=page.stem, property=name):
                    self.assertIn(page.stem, rows)
                    self.assertIn(name, "".join(rows[page.stem]))


if __name__ == "__main__":
    unittest.main()
