"""S001 oracle regression, including mutation rejection."""
import copy
import unittest
from scripts.enumerate import enumerate_pairs
from scripts.s001_validate import verify, recurrence

class S001Tests(unittest.TestCase):
    def test_independent_oracle(self):
        data = enumerate_pairs([31,37,41,43],2,100)
        result = verify(data,base_max=100)
        self.assertEqual(result["primes"]["37"]["order_three_residues"],[10,26])
        self.assertEqual(result["primes"]["41"]["order_three_residues"],[])
        self.assertEqual(recurrence(38,37),(1,37))
    def test_detects_mutation_even_with_rehashed_rows(self):
        data = enumerate_pairs([31,37,41,43],2,80)
        bad = copy.deepcopy(data)
        bad["rows"][0]["order"] = 999
        import hashlib,json
        bad["rows_sha256"] = hashlib.sha256(json.dumps(bad["rows"],sort_keys=True,separators=(",",":")).encode()).hexdigest()
        with self.assertRaises(ValueError):
            verify(bad,base_max=80)

if __name__ == "__main__":
    unittest.main()
