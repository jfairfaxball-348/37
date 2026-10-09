#!/usr/bin/env python3
"""S004 second, independent exhaustive oracle; direct quadruples and combinations."""
import argparse
from collections import Counter
from itertools import combinations, product
from pathlib import Path
import gzip
import hashlib
import json
import math
from scripts.s004_additive import PRIMES, FIELDS, canonical, normalized_forms

def validate(folder, tracked=None):
    folder=Path(folder)
    raw=(folder/"s004_full.json").read_bytes()
    compressed=(folder/"s004_full.json.gz").read_bytes()
    mraw=(folder/"s004_manifest.json").read_bytes()
    obj=json.loads(raw)
    m=json.loads(mraw)
    assert raw==canonical(obj) and mraw==canonical(m)
    assert gzip.decompress(compressed)==raw
    assert hashlib.sha256(raw).hexdigest()==m["json_sha256"]
    assert hashlib.sha256(compressed).hexdigest()==m["gzip_sha256"]
    assert hashlib.sha256(canonical(obj["rows"])).hexdigest()==m["rows_sha256"]
    assert len(raw)==m["json_bytes"] and len(compressed)==m["gzip_bytes"]
    assert m["row_count"]==len(obj["rows"])==32560
    assert obj["config"]["row_fields"]==list(FIELDS)
    assert obj["config"]["primes"]==list(PRIMES)
    position=0
    counts=Counter()
    hist={p:Counter() for p in PRIMES}
    for p in PRIMES:
        for x,y,z in combinations(range(1,p),3):
            row=obj["rows"][position]
            position+=1
            assert row[:4]==[p,x,y,z], ("population mismatch",position)
            a=(0,x,y,z)
            # Independent second construction: unordered index-pairs, never x!=y.
            restricted={sum(pair)%p for pair in combinations(a,2)}
            ordinary={sum(pair)%p for pair in product(a,repeat=2)}
            diffs={(q-t)%p for q,t in product(a,repeat=2)}
            # Direct four-index count rather than squared representation histogram.
            energy=sum(1 for i,j,k,l in product(a,repeat=4)
                       if (i+j-k-l)%p==0)
            assert row[4:8]==[len(ordinary),len(restricted),len(diffs),energy], (position,row)
            # Orbit is independently checked through all 12 normalizations.
            forms=normalized_forms(p,a)
            assert tuple(row[8])==min(forms)
            assert (row[9]==1)==(tuple(row[8])==min(normalized_forms(p,(0,1,2,3))))
            counts[(p,tuple(row[8]))]+=1
            hist[p][",".join(map(str,row[4:8]))]+=1
        s=obj["summary"][str(p)]
        assert s["anchored_rows"]==math.comb(p-1,3)
        assert s["translation_orbits"]==s["anchored_rows"]//4
        assert hist[p]==Counter(s["hist_sumset_restricted_difference_energy"])
        assert s["restricted_min_5"]+s["restricted_max_6"]==s["anchored_rows"]
    assert position==len(obj["rows"])
    for (p,rep),weight in counts.items():
        stab=12//len(normalized_forms(p,rep))
        assert weight==4*(p-1)//stab
    if tracked:
        tracked=Path(tracked)
        assert raw==(tracked/"S004_full.json").read_bytes()
        assert compressed==(tracked/"S004_full.json.gz").read_bytes()
        assert mraw==(tracked/"S004_manifest.json").read_bytes()
    print("PASS S004 exhaustive independent unordered-pair, four-index energy, affine orbit, hash and archive checks, rows=",position)

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--folder",default="out")
    ap.add_argument("--tracked")
    args=ap.parse_args()
    validate(args.folder,args.tracked)
