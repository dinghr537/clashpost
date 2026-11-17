import pathlib
import subprocess
import sys
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]


class VerificationChecklistTests(unittest.TestCase):
    def test_checklist_matches_pending_source_fields(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts/generate_verification.py"), "--check"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
