"""Independent oracle tests for bounded exact number-theory enumeration."""
import hashlib
import json
import math
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.enumerate import (  # noqa: E402
    enumerate_pairs, is_prime, least_repunit_length, multiplicative_order,
    prime_factors,
)


def oracle_order(base: int, prime: int) -> int:
    residue = 1
    for k in range(1, prime + 1):
        residue = (residue * base) % prime
        if residue == 1:
            return k
    raise AssertionError("order not found")


def oracle_repunit_length(base: int, prime: int) -> int:
    residue = 0
    for k in range(1, prime + 1):
        residue = (residue * base + 1) % prime
        if residue == 0:
            return k
    raise AssertionError("repunit length not found")


class ExactEnumerateTests(unittest.TestCase):
    def test_prime_validation_and_factors(self):
        self.assertEqual([n for n in range(2, 45) if is_prime(n)],
                         [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43])
        self.assertEqual(prime_factors(36), [2, 3])
        self.assertEqual(prime_factors(1), [])
        with self.assertRaises(ValueError):
            prime_factors(0)

    def test_37_decimal_example_is_background(self):
        self.assertEqual(multiplicative_order(10, 37), 3)
        self.assertEqual(least_repunit_length(10, 37), 3)
        self.assertEqual(multiplicative_order(38, 37), 1)
        self.assertEqual(least_repunit_length(38, 37), 37)
        with self.assertRaises(ValueError):
            multiplicative_order(37, 37)

    def test_independent_recursion_oracles(self):
        for prime in [3, 7, 31, 37, 41, 43]:
            for base in range(2, 83):
                if math.gcd(base, prime) != 1:
                    continue
                order = multiplicative_order(base, prime)
                self.assertEqual(order, oracle_order(base, prime), (prime, base))
                self.assertEqual(least_repunit_length(base, prime, order),
                                 oracle_repunit_length(base, prime), (prime, base))
                self.assertEqual((prime - 1) % order, 0)

    def test_modular_residue_invariance(self):
        for prime in [7, 31, 37, 41, 43]:
            for base in range(2, 59):
                if base % prime:
                    self.assertEqual(multiplicative_order(base, prime),
                                     multiplicative_order(base + prime, prime))
                    self.assertEqual(least_repunit_length(base, prime),
                                     least_repunit_length(base + prime, prime))

    def test_config_and_deterministic_digest(self):
        result = enumerate_pairs([43, 31, 37, 41], 2, 60)
        self.assertEqual(result["config"]["primes"], [31, 37, 41, 43])
        self.assertEqual(result, enumerate_pairs([31, 37, 41, 43], 2, 60))
        rows = result["rows"]
        digest = hashlib.sha256(
            json.dumps(rows, sort_keys=True, separators=(",", ":")).encode()
        ).hexdigest()
        self.assertEqual(result["rows_sha256"], digest)
        self.assertEqual(result["row_count"] + result["excluded_non_coprime"], 4 * 59)

    def test_invalid_searches_rejected(self):
        for primes, a, b in [([37, 37], 2, 10), ([4], 2, 10),
                              ([37], 1, 10), ([37], 2, 100001)]:
            with self.assertRaises(ValueError):
                enumerate_pairs(primes, a, b)
        with self.assertRaises(ValueError):
            enumerate_pairs([31, 37, 41, 43, 47, 53], 2, 100_000)

    def test_cli_writes_valid_json(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "output.json"
            subprocess.run(
                [sys.executable, str(ROOT / "scripts/enumerate.py"),
                 "--primes", "37,31", "--base-min", "2",
                 "--base-max", "50", "--output", str(path)],
                check=True, capture_output=True, text=True,
            )
            record = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(record["config"]["primes"], [31, 37])
            self.assertTrue(record["row_count"] > 0)


if __name__ == "__main__":
    unittest.main()

