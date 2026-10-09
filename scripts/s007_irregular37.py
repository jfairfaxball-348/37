#!/usr/bin/env python3
"""S007 exact 37-anchored Kummer/reciprocal harmonic pilot; NOT a discovery."""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from math import comb
from pathlib import Path

PRIMES = (31, 37, 41, 43, 59, 67)
POWERS = (2, 4, 6)
EXPECTED_B32 = Fraction(-7709321041217, 510)


def bernoulli(n: int) -> Fraction:
    """Exact independent rational Bernoulli recurrence; B1=-1/2."""
    values = [Fraction(1)]
    for m in range(1, n + 1):
        values.append(-sum(comb(m + 1, k) * values[k] for k in range(m))
                      / Fraction(m + 1))
    return values[n]


def direct_mod(p: int, r: int) -> int:
    """Direct inverse-power sum in Z / p^3, disjoint from Fraction method."""
    m = p ** 3
    return sum(pow(k, -r, m) for k in range(1, p)) % m


def fraction_mod(p: int, r: int) -> int:
    """Separate exact-rational sum, reduce its coprime denominator modulo p^3."""
    h = sum((Fraction(1, k ** r) for k in range(1, p)), Fraction(0))
    m = p ** 3
    assert h.denominator % p, "Denominator must be invertible modulo prime p"
    return h.numerator * pow(h.denominator, -1, m) % m


def run() -> dict:
    b32 = bernoulli(32)
    assert b32 == EXPECTED_B32
    assert b32.numerator % 37 == 0 and b32.numerator % (37**2) != 0
    rows = []
    for p in PRIMES:
        for r in POWERS:
            residue = direct_mod(p, r)
            assert residue == fraction_mod(p, r), (p, r, residue)
            rows.append({"p": p, "power": r,
                         "mod_p2": residue % (p ** 2),
                         "mod_p3": residue})
    h4 = next(z for z in rows if z["p"] == 37 and z["power"] == 4)
    assert h4["mod_p2"] == 0
    assert h4["mod_p3"] == 6 * 37 ** 2
    assert all(z["mod_p2"] != 0 for z in rows
               if z["power"] == 4 and z["p"] != 37)
    canonical = json.dumps(rows, sort_keys=True, separators=(",", ":")).encode()
    return {
        "session": "S007",
        "gate": "EXPERIMENTAL_CLASSICAL_NO_N1",
        "meaning_of_37": "first irregular prime: (37,32), 32=37-5",
        "frozen_primes": list(PRIMES),
        "frozen_powers": list(POWERS),
        "bernoulli_32": {"numerator": b32.numerator,
                         "denominator": b32.denominator,
                         "v37_numerator": 1},
        "independent_methods": ["direct modular inverse sum",
                                "exact Fraction numerator/denominator reduction"],
        "target_h4_37": {"mod_37_squared": 0,
                         "mod_37_cubed": h4["mod_p3"],
                         "normalized_mod_37": 6},
        "rows_sha256": hashlib.sha256(canonical).hexdigest(),
        "rows": rows,
        "novelty_warning": "Glaisher 1900/1901; Kellner 2007; Hart-Harvey-Ong 2017; OEIS A397134. Known phenomenon; no original theorem."
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    data = json.dumps(run(), indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(data, encoding="utf-8")
    print("S007 37-exact PASS: 18 independent cells; B32=-7709321041217/510; H4 mod 37^3=8214")
    print("rows_sha256=" + json.loads(data)["rows_sha256"])


if __name__ == "__main__":
    main()
