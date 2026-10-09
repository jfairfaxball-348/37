#!/usr/bin/env python3
"""Independent S002 oracle: direct p² power/repunit recurrence plus modular valuation."""
from __future__ import annotations
import argparse
from collections import Counter
import gzip
import hashlib
import json
from pathlib import Path

PRIMES=(31,37,41,43)
def sha(bs):return hashlib.sha256(bs).hexdigest()
def oracle(b,p):
    m=p*p;power=1;repunit=0;results=[None,None,None,None]
    for n in range(1,m+1):
        power=power*b%m;repunit=(repunit*b+1)%m
        if results[0] is None and power%p==1:results[0]=n
        if results[1] is None and power==1:results[1]=n
        if results[2] is None and repunit%p==0:results[2]=n
        if results[3] is None and repunit==0:results[3]=n
        if all(v is not None for v in results):return tuple(results)
    raise ValueError(f"recurrence fails to close: {(p,b)}")
def modular_valuation(b,d,p):
    for n in range(1,12):
        if pow(b,d,p**(n+1))!=1:return n
    raise ValueError("valuation exceeds independent verifier cap")
def verify(data):
    config={"primes":[31,37,41,43],"base_min":2,"base_max":2000,"levels":[1,2],"p3":"NOT_RUN"}
    if data["config"]!=config or data["session"]!="S002" or data["schema_version"]!=1:
        raise ValueError("S002 frozen configuration mismatch")
    rows=data["rows"]
    expected=[(p,b) for p in PRIMES for b in range(2,2001) if b%p]
    excluded=[{"prime":p,"base":b,"reason":"p_divides_b; R_n(b)=1 mod p for every n>=1"}
              for p in PRIMES for b in range(2,2001) if b%p==0]
    if data["row_count"]!=len(expected) or len(rows)!=len(expected) or data["excluded"]!=excluded or data["excluded_count"]!=len(excluded):
        raise ValueError("coverage, exclusions or row count mismatch")
    if data["rows_sha256"]!=sha(json.dumps(rows,sort_keys=True,separators=(",",":")).encode()):
        raise ValueError("canonical digest mismatch")
    groups={p:{"classes":set(),"exceptional":set(),"counts":Counter(),"index":{}} for p in PRIMES}
    for (p,b),row in zip(expected,rows):
        d,d2,r1,r2=oracle(b,p)
        s=modular_valuation(b,d,p)
        q=((pow(b,p-1,p*p)-1)//p)%p
        predicted={"prime":p,"base":b,"residue_p":b%p,"residue_p2":b%(p*p),
                   "order_p":d,"order_p2":d2,"valuation_bd_minus_1":s,
                   "cyclotomic_vp":s,"repunit_p":r1,"repunit_p2":r2,
                   "fermat_quotient_mod_p":q,"exceptional_lift":s>=2}
        if row!=predicted:raise ValueError(f"row mismatch {(p,b)} predicted {predicted} got {row}")
        if (p-1)%d or d2!=(d if s>=2 else p*d) or r2!=(p*p if b%p==1 else d2):
            raise ValueError(f"background theory mismatch {(p,b)}")
        if (q==0)!=(s>=2):raise ValueError("Fermat quotient consistency")
        g=groups[p];g["classes"].add(b%(p*p));g["index"][b]=(d,d2,r2)
        g["counts"]["included"]+=1
        if s>=2:g["exceptional"].add(b%(p*p));g["counts"]["exceptional_rows"]+=1
        if s>=3:g["counts"]["s_ge_3_rows"]+=1
        if b%p==1:g["counts"]["residue_one_rows"]+=1
    summaries={}
    for p,g in groups.items():
        g["counts"]["excluded"]=sum(b%p==0 for b in range(2,2001))
        for b,(d,d2,r2) in g["index"].items():
            if b+p in g["index"]:
                other=g["index"][b+p]
                if d!=other[0]:raise ValueError("base change modified order mod p")
                g["counts"]["shift_pairs"]+=1
                if d2!=other[1]:g["counts"]["shift_order2_changed"]+=1
                if r2!=other[2]:g["counts"]["shift_repunit2_changed"]+=1
        if len(g["classes"])!=p*(p-1) or len(g["exceptional"])!=p-1:
            raise ValueError("complete residue or unique-lift invariant")
        if Counter(c%p for c in g["exceptional"])!=Counter({r:1 for r in range(1,p)}):
            raise ValueError("exactly one exceptional lift per nonzero residue failed")
        record={**dict(g["counts"]),"unique_unit_classes_mod_p2":len(g["classes"]),
                "unique_exceptional_classes_mod_p2":len(g["exceptional"]),
                "exceptional_classes_mod_p2":sorted(g["exceptional"])}
        if record!=data["summary"][str(p)]:raise ValueError(f"summary mismatch p={p}")
        summaries[str(p)]=record
    return {"session":"S002","status":"EXPERIMENTAL_NOT_NOVEL","config":config,
            "row_count":len(rows),"excluded_count":len(excluded),
            "rows_sha256":data["rows_sha256"],"summary":summaries,
            "independent_method":"direct modular multiplication and repunit recurrence for all rows, successive modulus valuations and full Hensel residue-class checks",
            "p3_holdout":"NOT_RUN_NO_NOVELTY_JUSTIFICATION"}
def main():
    p=argparse.ArgumentParser()
    for opt in ("input","manifest","archive"):p.add_argument("--"+opt,required=True)
    a=p.parse_args();source=Path(a.input).read_bytes();data=json.loads(source);manifest=verify(data)
    archive=gzip.compress(source,compresslevel=9,mtime=0)
    manifest.update({"json_sha256":sha(source),"json_bytes":len(source),
                     "gzip_sha256":sha(archive),"gzip_bytes":len(archive)})
    Path(a.archive).parent.mkdir(parents=True,exist_ok=True)
    Path(a.archive).write_bytes(archive)
    Path(a.manifest).write_text(json.dumps(manifest,sort_keys=True,indent=2)+"\n",encoding="utf-8")
    print("PASS S002 all-row independent oracle rows",len(data["rows"]),
          "raw_sha256",manifest["json_sha256"],"gzip_sha256",manifest["gzip_sha256"])
if __name__=="__main__":main()
