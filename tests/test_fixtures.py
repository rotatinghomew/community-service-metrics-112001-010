import json
from pathlib import Path
import unittest

FIXTURES = Path(__file__).resolve().parents[1] / "fixtures"

class SyntheticSourceTests(unittest.TestCase):
    def test_tables_have_records_and_consistent_fields(self):
        paths = sorted(FIXTURES.glob("*.json"))
        self.assertGreaterEqual(len(paths), 3)
        for path in paths:
            with self.subTest(table=path.name):
                records = json.loads(path.read_text(encoding="utf-8"))
                self.assertTrue(records)
                self.assertTrue(all(isinstance(record, dict) for record in records))
                fields = set(records[0])
                self.assertTrue(all(set(record) == fields for record in records))
                self.assertTrue(all(value is not None for record in records for value in record.values()))

if __name__ == "__main__":
    unittest.main()
