#!/usr/bin/env python3
"""S001 independent exhaustive recurrence oracle and compact archive; no novelty claim."""
from __future__ import annotations

import argparse
from collections import Counter
import gzip
import hashlib
import json
import math
from pathlib import Path

PRIMES = (31, 37, 41, 43)
BASE_MIN, BASE_MAX = 2, 2000

def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def phi(n: int) -> int:
    return sum(math.gcd(i, n) == 1 for i in range(1, n + 1))

def recurrence(base: int, p: int) -> tuple[int, int]:
    """Do not use the engine's order reduction or repunit formula."""
    x, y = 1, 0
    first_x = first_y = None
    for k in range(1, p + 1):
        x = (x * base) % p
        y = (y * base + 1) % p
        if x == 1 and first_x is None:
            first_x = k
        if y == 0 and first_y is None:
            first_y = k
        if first_x is not None and first_y is not None:
            return first_x, first_y
    raise ValueError(f"recurrence not closed at p={p}, base={base}")

def verify(data: dict, primes=PRIMES, base_min=BASE_MIN, base_max=BASE_MAX) -> dict:
    if data["config"] != {"primes": list(primes), "base_min": base_min, "base_max": base_max}:
        raise ValueError("configuration mismatch")
    rows = data["rows"]
    if sha(json.dumps(rows, sort_keys=True, separators=(",", ":")).encode()) != data["rows_sha256"]:
        raise ValueError("canonical rows SHA mismatch")
    expected = [(p, b) for p in primes for b in range(base_min, base_max + 1) if b % p]
    if len(rows) != len(expected) or data["row_count"] != len(expected):
        raise ValueError("row count mismatch")
    if data["excluded_non_coprime"] != len(primes) * (base_max-base_min+1)-len(expected):
        raise ValueError("excluded count mismatch")
    by_p = {p: {"residues": {}, "order_histogram": Counter(), "repunit_histogram": Counter(),
                "order_three_residues": set(), "repunit_three_residues": set(), "base_one": 0}
            for p in primes}
    for (p, b), row in zip(expected, rows):
        o, a = recurrence(b, p)
        if row != {
            "prime": p, "base": b, "residue": b % p, "order": o,
            "repunit_length": a, "base_minus_one_divisible": b % p == 1,
            "order_three": o == 3, "repunit_three": a == 3,
        }:
            raise ValueError(f"row disagrees with independent recurrence at {(p,b)}")
        record = by_p[p]
        residue = b % p
        if residue in record["residues"] and record["residues"][residue] != (o,a):
            raise ValueError("same residue class different orders")
        record["residues"][residue] = (o,a)
        if o == 3: record["order_three_residues"].add(residue)
        if a == 3: record["repunit_three_residues"].add(residue)
        record["order_histogram"][o] += 1
        record["repunit_histogram"][a] += 1
        if residue == 1: record["base_one"] += 1
    summaries = {}
    for p in primes:
        record = by_p[p]
        if len(record["residues"]) != p-1:
            raise ValueError(f"not all residues covered at prime {p}")
        residue_orders = Counter(o for o,a in record["residues"].values())
        divisors = [d for d in range(1,p) if (p-1) % d == 0]
        if residue_orders != Counter({d: phi(d) for d in divisors}):
            raise ValueError(f"cyclic group totient distribution fails at {p}")
        if record["order_three_residues"] != {r for r in range(1,p) if (r*r+r+1)%p==0 and r != 1}:
            raise ValueError(f"Phi3 root comparison fails at {p}")
        if record["repunit_three_residues"] != record["order_three_residues"]:
            raise ValueError("repunit-3 roots differ from order-3 roots")
        summary = data["summary"][str(p)]
        if summary != {"included": sum(record["order_histogram"].values()),
                       "order_three": record["order_histogram"][3],
                       "repunit_three": record["repunit_histogram"][3],
                       "residue_one": record["base_one"]}:
            raise ValueError("engine's summary inconsistent")
        summaries[str(p)] = {
            "included": summary["included"],
            "excluded": base_max-base_min+1-summary["included"],
            "distinct_nonzero_residues": len(record["residues"]),
            "repeated_bases_beyond_unique_residues": summary["included"]-(p-1),
            "order_histogram": {str(k):v for k,v in sorted(record["order_histogram"].items())},
            "residue_order_histogram": {str(k):v for k,v in sorted(residue_orders.items())},
            "order_three_residues": sorted(record["order_three_residues"]),
            "repunit_three_residues": sorted(record["repunit_three_residues"]),
            "residue_one_bases": record["base_one"],
            "primitive_root_residues": residue_orders[p-1],
            "primitive_root_expected_phi": phi(p-1),
        }
    return {
        "session": "S001", "status": "EXPERIMENTAL_NOT_NOVELTY_EVIDENCE",
        "config": data["config"], "engine_row_count": data["row_count"],
        "excluded_non_coprime": data["excluded_non_coprime"],
        "rows_sha256": data["rows_sha256"],
        "independent_method": "direct multiplication and repunit recurrence for each row; cyclic group totient and Phi3 root checks",
        "primes": summaries,
        "tests": "all included rows independently checked, order histograms/summary/canonical hash verified",
    }

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--output", required=True)
    ap.add_argument("--archive", required=True)
    args = ap.parse_args()
    source = Path(args.input).read_bytes()
    obj = json.loads(source)
    manifest = verify(obj)
    archive = gzip.compress(source, compresslevel=9, mtime=0)
    Path(args.archive).parent.mkdir(parents=True, exist_ok=True)
    Path(args.archive).write_bytes(archive)
    manifest["json_sha256"] = sha(source)
    manifest["gzip_sha256"] = sha(archive)
    manifest["gzip_bytes"] = len(archive)
    manifest["json_bytes"] = len(source)
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.output).write_text(json.dumps(manifest, indent=2, sort_keys=True)+"\n",encoding="utf-8")
    print(f"PASS S001 full independent oracle: {obj['row_count']} rows, "
          f"rows_sha256={obj['rows_sha256']}, json_sha256={sha(source)}, gzip_sha256={sha(archive)}")
    for p, item in manifest["primes"].items():
        print(f"p={p}: included={item['included']} unique={item['distinct_nonzero_residues']}"
              f" ord3={item['order_three_residues']} primitive={item['primitive_root_residues']}")

if __name__ == "__main__":
    main()
