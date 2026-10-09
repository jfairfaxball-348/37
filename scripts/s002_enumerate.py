#!/usr/bin/env python3
"""Frozen S002 prime-power exact sweep; no original theorem asserted."""
from __future__ import annotations
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
from scripts.enumerate import multiplicative_order

PRIMES=(31,37,41,43)
def vp(n,p):
    if not n: raise ValueError("valuation zero")
    k=0
    while n%p==0: n//=p; k+=1
    return k

def cyclo(n,b,cache):
    if (n,b) not in cache:
        v=b**n-1
        for j in range(1,n):
            if n%j==0: v//=cyclo(j,b,cache)
        cache[(n,b)]=v
    return cache[(n,b)]

def compute(primes=PRIMES, low=2, high=2000):
    if tuple(primes)!=PRIMES or (low,high)!=(2,2000):
        raise ValueError("frozen primes=31,37,41,43 bases=2..2000")
    rows=[]; excluded=[]; summary={}; cache={}
    for p in primes:
        counts=Counter(); seen=set(); exceptional=set(); index={}
        for b in range(low,high+1):
            if b%p==0:
                excluded.append({"prime":p,"base":b,"reason":"p_divides_b; R_n(b)=1 mod p for every n>=1"})
                counts["excluded"]+=1
                continue
            d=multiplicative_order(b,p)
            s=vp(b**d-1,p)
            d2=d if pow(b,d,p*p)==1 else d*p
            row={"prime":p,"base":b,"residue_p":b%p,"residue_p2":b%(p*p),
                 "order_p":d,"order_p2":d2,"valuation_bd_minus_1":s,
                 "cyclotomic_vp":vp(cyclo(d,b,cache),p),
                 "repunit_p":p if b%p==1 else d,
                 "repunit_p2":p*p if b%p==1 else d2,
                 "fermat_quotient_mod_p":((b**(p-1)-1)//p)%p,
                 "exceptional_lift":s>=2}
            rows.append(row);index[b]=row;seen.add(b%(p*p));counts["included"]+=1
            if s>=2: exceptional.add(b%(p*p));counts["exceptional_rows"]+=1
            if s>=3: counts["s_ge_3_rows"]+=1
            if b%p==1: counts["residue_one_rows"]+=1
        for b,row in index.items():
            other=index.get(b+p)
            if other:
                assert other["order_p"]==row["order_p"]
                counts["shift_pairs"]+=1
                if other["order_p2"]!=row["order_p2"]:counts["shift_order2_changed"]+=1
                if other["repunit_p2"]!=row["repunit_p2"]:counts["shift_repunit2_changed"]+=1
        assert len(seen)==p*(p-1) and len(exceptional)==p-1
        summary[str(p)]={**dict(counts),"unique_unit_classes_mod_p2":len(seen),
                         "unique_exceptional_classes_mod_p2":len(exceptional),
                         "exceptional_classes_mod_p2":sorted(exceptional)}
    digest=hashlib.sha256(json.dumps(rows,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    return {"schema_version":1,"session":"S002","status":"EXPERIMENTAL_NOT_NOVEL",
            "config":{"primes":list(primes),"base_min":low,"base_max":high,"levels":[1,2],"p3":"NOT_RUN"},
            "row_count":len(rows),"excluded_count":len(excluded),"rows_sha256":digest,
            "summary":summary,"excluded":excluded,"rows":rows}

def main():
    p=argparse.ArgumentParser();p.add_argument("--output",required=True);a=p.parse_args()
    data=compute(); dest=Path(a.output);dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(data,sort_keys=True,indent=2)+"\n",encoding="utf-8")
    print("S002 complete rows",data["row_count"],"excluded",data["excluded_count"],"sha256(rows)",data["rows_sha256"])
    for p,v in data["summary"].items():
        print("p",p,"exceptional classes",v["unique_exceptional_classes_mod_p2"],
              "exceptional rows",v["exceptional_rows"],"s>=3",v.get("s_ge_3_rows",0),
              "shift pairs",v["shift_pairs"],"shift order changes",v.get("shift_order2_changed",0))
if __name__=="__main__":main()
