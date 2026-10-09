#!/usr/bin/env python3
"""S004 frozen exhaustive four-point additive statistics; no novelty claims."""
from __future__ import annotations
import argparse
from collections import Counter
from itertools import combinations
from pathlib import Path
import gzip
import hashlib
import json
import math

PRIMES = (31, 37, 41, 43)
METHOD = "all A=(0,a,b,c), 1<=a<b<c<p; no exclusions; prime seed 37; other primes controls"
FIELDS = ("p","a","b","c","sumset","restricted","difference","energy","orbit","ap")

def canonical(obj):
    return (json.dumps(obj, sort_keys=True, separators=(",",":"), ensure_ascii=True)+"\n").encode("ascii")

def normalized_forms(p, a):
    out = set()
    for x in a:
        for y in a:
            if x == y:
                continue
            inv = pow((y-x) % p, -1, p)
            out.add(tuple(sorted(((z-x)*inv) % p for z in a)))
    return out

def orbit(p, a):
    return min(normalized_forms(p, a))

def metrics(p, a, ap_orbit):
    # First method: ordered pair-comprehension and convolution representation counts.
    representation = Counter((x+y) % p for x in a for y in a)
    restricted = {(x+y) % p for x in a for y in a if x != y}
    difference = {(x-y) % p for x in a for y in a}
    energy = sum(v*v for v in representation.values())
    rep = orbit(p, a)
    assert 7 <= len(representation) <= 10
    assert 5 <= len(restricted) <= 6
    assert len(difference) >= 7 and energy >= 28
    return [p,a[1],a[2],a[3],len(representation),len(restricted),
            len(difference),energy,list(rep),int(rep == ap_orbit)]

def generate():
    rows = []
    summary = {}
    for p in PRIMES:
        ap_orbit = orbit(p,(0,1,2,3))
        hist = Counter()
        classes = Counter()
        ap = 0
        for triple in combinations(range(1,p), 3):
            r = metrics(p, (0,*triple), ap_orbit)
            rows.append(r)
            hist[",".join(map(str,r[4:8]))] += 1
            classes[tuple(r[8])] += 1
            ap += r[9]
        expected = math.comb(p-1,3)
        assert sum(hist.values()) == expected == sum(classes.values())
        # Each affine orbit contributes 4*(p-1)/|stabilizer| anchored rows.
        stabilizers = Counter()
        for rep, size in classes.items():
            forms = normalized_forms(p, rep)
            assert 12 % len(forms) == 0
            stab = 12//len(forms)
            assert size == 4*(p-1)//stab, (p, rep, size, stab)
            stabilizers[str(stab)] += 1
        summary[str(p)] = {
          "anchored_rows":expected, "translation_orbits":expected//4,
          "affine_orbits":len(classes), "affine_orbit_stabilizer_hist":dict(sorted(stabilizers.items())),
          "four_term_AP_rows":ap,
          "hist_sumset_restricted_difference_energy":dict(sorted(hist.items())),
          "restricted_min_5":sum(v for k,v in hist.items() if k.split(",")[1]=="5"),
          "restricted_max_6":sum(v for k,v in hist.items() if k.split(",")[1]=="6")
        }
    assert len(rows)==sum(math.comb(p-1,3) for p in PRIMES)==32560
    return {"session":"S004","stage":"E1","status":"EXPERIMENTAL_ONLY",
            "config":{"primes":list(PRIMES),"set_size":4,"anchored_zero":True,
                      "population":METHOD,"sample":"NONE_EXHAUSTIVE",
                      "row_fields":list(FIELDS),
                      "energy":"ordered quadruples a+b=c+d mod p",
                      "affine":"x -> u*x+v, u != 0 mod p; orbit=min 12 ordered-pair normalized forms"},
            "rows":rows,"summary":summary}

def persist(folder):
    folder = Path(folder)
    folder.mkdir(parents=True,exist_ok=True)
    obj = generate()
    raw = canonical(obj)
    zipped = gzip.compress(raw, compresslevel=9, mtime=0)
    (folder/"s004_full.json").write_bytes(raw)
    (folder/"s004_full.json.gz").write_bytes(zipped)
    manifest = {"session":"S004", "config":obj["config"], "row_count":len(obj["rows"]),
        "json_bytes":len(raw),"json_sha256":hashlib.sha256(raw).hexdigest(),
        "gzip_bytes":len(zipped),"gzip_sha256":hashlib.sha256(zipped).hexdigest(),
        "rows_sha256":hashlib.sha256(canonical(obj["rows"])).hexdigest(),
        "independent_oracle":"direct ordered four-index energy and unordered-pair restricted sums on every archived row",
        "summary":obj["summary"],"gate":"EXPERIMENTAL_NO_N1"}
    (folder/"s004_manifest.json").write_bytes(canonical(manifest))
    print("S004_PREREGISTERED_SUMMARY "+json.dumps({k:{x:v for x,v in m.items() if x!="hist_sumset_restricted_difference_energy"}
                   for k,m in obj["summary"].items()},sort_keys=True))
    print("S004_ARCHIVE_HASHES "+json.dumps({x:manifest[x] for x in ("json_sha256","gzip_sha256","rows_sha256","json_bytes","gzip_bytes")},sort_keys=True))

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--folder",default="out")
    persist(ap.parse_args().folder)
