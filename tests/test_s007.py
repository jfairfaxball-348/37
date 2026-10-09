"""S007 bounded exact checks. These verify known arithmetic, not novelty."""
from fractions import Fraction
import unittest

from scripts.s007_irregular37 import (EXPECTED_B32, PRIMES, POWERS,
                                     bernoulli, direct_mod, fraction_mod, run)


class S007Kummer37Tests(unittest.TestCase):
    def test_frozen_window(self):
        self.assertEqual(PRIMES, (31, 37, 41, 43, 59, 67))
        self.assertEqual(POWERS, (2, 4, 6))

    def test_known_bernoulli_index(self):
        self.assertEqual(bernoulli(0), Fraction(1))
        self.assertEqual(bernoulli(1), Fraction(-1, 2))
        self.assertEqual(bernoulli(2), Fraction(1, 6))
        self.assertEqual(bernoulli(32), EXPECTED_B32)
        self.assertEqual(EXPECTED_B32.numerator % 37, 0)
        self.assertNotEqual(EXPECTED_B32.numerator % 1369, 0)

    def test_two_oracles_all_18_cells(self):
        for p in PRIMES:
            for r in POWERS:
                with self.subTest(p=p, r=r):
                    self.assertEqual(direct_mod(p, r), fraction_mod(p, r))

    def test_37_exceptional_fourth_power(self):
        self.assertEqual(direct_mod(37, 4) % 37**2, 0)
        self.assertEqual(direct_mod(37, 4), 8214)
        self.assertEqual(direct_mod(37, 4) // 37**2, 6)
        for p in PRIMES:
            if p != 37:
                self.assertNotEqual(direct_mod(p, 4) % p**2, 0)

    def test_manifest_structure(self):
        payload = run()
        self.assertEqual(len(payload["rows"]), 18)
        self.assertEqual(payload["gate"], "EXPERIMENTAL_CLASSICAL_NO_N1")
        self.assertEqual(len(payload["rows_sha256"]), 64)


if __name__ == "__main__":
    unittest.main()
