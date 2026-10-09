#!/usr/bin/env python3
"""Exact, bounded order/repunit exploration. Standard library; no novelty claims."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any

SCHEMA_VERSION = 1
MAX_BASE = 100_000
MAX_PRIME = 100_000
MAX_PAIRS = 500_000


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def prime_factors(n: int) -> list[int]:
    """Sorted distinct prime factors."""
    if n < 1:
        raise ValueError("n must be positive")
    result: list[int] = []
    for d in (2,):
        if n % d == 0:
            result.append(d)
            while n % d == 0:
                n //= d
    d = 3
    while d * d <= n:
        if n % d == 0:
            result.append(d)
            while n % d == 0:
                n //= d
        d += 2
    if n > 1:
        result.append(n)
    return result


def multiplicative_order(base: int, prime: int) -> int:
    """ord_prime(base); precondition: prime is prime and base is coprime to it."""
    if prime < 2 or not is_prime(prime):
        raise ValueError("modulus must be prime")
    if math.gcd(base, prime) != 1:
        raise ValueError("base must be coprime to modulus")
    order = prime - 1
    for factor in prime_factors(order):
        while order % factor == 0 and pow(base, order // factor, prime) == 1:
            order //= factor
    return order


def least_repunit_length(base: int, prime: int, order: int | None = None) -> int:
    """Least k>=1 for R_k(base) divisible by prime; prime does not divide base."""
    if base < 2 or not is_prime(prime) or math.gcd(base, prime) != 1:
        raise ValueError("expected base>=2, prime modulus, and coprimality")
    if base % prime == 1:
        return prime
    if order is None:
        order = multiplicative_order(base, prime)
    return order


def enumerate_pairs(primes: list[int], base_min: int, base_max: int) -> dict[str, Any]:
    if not primes or len(set(primes)) != len(primes):
        raise ValueError("primes must be a nonempty distinct list")
    if any(p > MAX_PRIME or not is_prime(p) for p in primes):
        raise ValueError("all moduli must be primes <= MAX_PRIME")
    if not (2 <= base_min <= base_max <= MAX_BASE):
        raise ValueError("require 2 <= base_min <= base_max <= MAX_BASE")
    if len(primes) * (base_max - base_min + 1) > MAX_PAIRS:
        raise ValueError("requested search exceeds MAX_PAIRS; split into bounded runs")

    primes = sorted(primes)
    rows: list[dict[str, Any]] = []
    summary: dict[str, dict[str, int]] = {}
    excluded = 0
    for prime in primes:
        included = 0
        order_three = 0
        repunit_three = 0
        residue_one = 0
        for base in range(base_min, base_max + 1):
            if math.gcd(base, prime) != 1:
                excluded += 1
                continue
            order = multiplicative_order(base, prime)
            repunit = least_repunit_length(base, prime, order)
            is_residue_one = base % prime == 1
            rows.append({
                "prime": prime,
                "base": base,
                "residue": base % prime,
                "order": order,
                "repunit_length": repunit,
                "base_minus_one_divisible": is_residue_one,
                "order_three": order == 3,
                "repunit_three": repunit == 3,
            })
            included += 1
            order_three += order == 3
            repunit_three += repunit == 3
            residue_one += is_residue_one
        summary[str(prime)] = {
            "included": included, "order_three": order_three,
            "repunit_three": repunit_three, "residue_one": residue_one,
        }
    canonical = json.dumps(rows, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return {
        "schema_version": SCHEMA_VERSION,
        "description": "EXPERIMENTAL exact integer data; not an algebraic theorem or novelty audit",
        "config": {"primes": primes, "base_min": base_min, "base_max": base_max},
        "row_count": len(rows),
        "excluded_non_coprime": excluded,
        "rows_sha256": hashlib.sha256(canonical).hexdigest(),
        "summary": summary,
        "rows": rows,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--primes", default="31,37,41,43", help="comma-separated primes")
    parser.add_argument("--base-min", type=int, default=2)
    parser.add_argument("--base-max", type=int, default=200)
    parser.add_argument("--output", default="-", help="output JSON file; '-' for stdout")
    args = parser.parse_args()
    try:
        primes = [int(piece.strip()) for piece in args.primes.split(",")]
        data = enumerate_pairs(primes, args.base_min, args.base_max)
    except (ValueError, OverflowError) as error:
        parser.error(str(error))
    content = json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    if args.output == "-":
        print(content, end="")
    else:
        output = Path(args.output)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(content, encoding="utf-8")
        print("Wrote " + str(output) + " (" + str(data["row_count"]) + " rows); sha256(rows)=" + data["rows_sha256"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

