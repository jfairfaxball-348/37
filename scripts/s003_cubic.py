#!/usr/bin/env python3
"""S003 preregistered exact cubic-character sweep. All integers; no floating roots."""
from __future__ import annotations
import argparse
import gzip
import hashlib
import json
from pathlib import Path

PRIMES = (31, 37, 41, 43)
PROBES = (2, 3, 10)
NORMALIZATION = "least positive primitive root g; chi(g**k)=omega**(k mod 3); chi(0)=0; omega**2=-1-omega"


def prime_factors(n):
    return [q for q in range(2, n + 1) if n % q == 0 and all(q % i for i in range(2, int(q**0.5) + 1))]


def primitive_root(p):
    for g in range(2, p):
        if all(pow(g, (p - 1)//q, p) != 1 for q in prime_factors(p - 1)):
            return g
    raise ValueError("no primitive root")


def omega_pair(k):
    return ((1, 0), (0, 1), (-1, -1))[k % 3]


def pair_sum(pairs):
    return [sum(v[i] for v in pairs) for i in range(2)]


def norm(pair):
    a, b = pair
    return a*a - a*b + b*b


def multiply_periods(a, b, p):
    # independent additive convolution in Z[X]/(X**p-1)
    z = [0]*p
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                if bj:
                    z[(i+j) % p] += ai*bj
    return z


def rational_period_value(v):
    # In Z[zeta_p], sum(zeta_p**j,j=1..p-1)=-1.
    assert len(set(v[1:])) == 1, "nonrational symmetric period expression"
    return v[0] - v[1]


def representation(p):
    matches = [(L,M) for L in range(-2*p,2*p+1)
               for M in range(1,p+1)
               if L % 3 == 1 and L*L+27*M*M == 4*p]
    if len(matches) != 1:
        raise AssertionError(("ambiguous classical representation",p,matches))
    return list(matches[0])


def examine(p):
    if p % 3 == 2:
        cubes = {pow(x, 3, p) for x in range(1,p)}
        assert len(cubes) == p-1
        return {"p":p, "split":False, "nontrivial_cubic_character":False,
                "cube_map_image_size":len(cubes), "note":"inert negative control; no nontrivial cubic character"}
    assert p % 3 == 1
    g = primitive_root(p)
    log = {}
    cur = 1
    classes = [[],[],[]]
    for k in range(p-1):
        assert cur not in log
        log[cur] = k
        classes[k%3].append(cur)
        cur = cur*g % p
    assert cur == 1 and len(log) == p-1
    classes = [sorted(c) for c in classes]
    # Independent class oracle: subgroup of actual cubes and its two cosets.
    cube_set = {pow(x,3,p) for x in range(1,p)}
    oracle_classes = [sorted({pow(g,i,p)*a % p for a in cube_set}) for i in range(3)]
    assert classes == oracle_classes
    chi = [None] + [log[x]%3 for x in range(1,p)]
    terms_11, terms_1bar = [], []
    counts = [[0]*3 for _ in range(3)]
    for x in range(1,p):
        y=(1-x)%p
        if y:
            a,b=chi[x],chi[y]
            counts[a][b]+=1
            terms_11.append(omega_pair(a+b))
            terms_1bar.append(omega_pair(a-b))
    j11=pair_sum(terms_11)
    j1bar=pair_sum(terms_1bar)
    # Independent count oracle: count ordered x+y=1 by actual cubic coset membership,
    # then use the coefficient basis; no discrete-log labels or complex arithmetic.
    idx = {x:i for i,cl in enumerate(oracle_classes) for x in cl}
    oracle_counts = [[0]*3 for _ in range(3)]
    for x in range(p):
        y=(1-x)%p
        if x and y:
            oracle_counts[idx[x]][idx[y]]+=1
    assert counts == oracle_counts
    j_counts = pair_sum([tuple(count*coefficient for coefficient in omega_pair(i+j))
                         for i,row in enumerate(oracle_counts) for j,count in enumerate(row)])
    assert j11 == j_counts
    assert j1bar == [-1,0] and norm(j11)==p
    assert sum(map(sum,counts)) == p-2
    # Jacobi under chi -> chi**2 is complex conjugate, not the same oriented pair.
    conjugate = [j11[0]-j11[1],-j11[1]]
    direct_conjugate=pair_sum([omega_pair(2*(chi[x]+chi[(1-x)%p]))
                              for x in range(1,p) if (1-x)%p])
    assert conjugate==direct_conjugate
    assert chi[p-1] == 0
    # Cyclotomic numbers (i,j) = # x in C_i with x+1 in C_j.
    table = [[0]*3 for _ in range(3)]
    for i, cl in enumerate(classes):
        for x in cl:
            if (x+1)%p:
                table[i][idx[(x+1)%p]] += 1
    assert sum(map(sum,table)) == p-2
    # Gaussian periods eta_i = sum_{x in C_i} zeta_p**x.
    vectors = [[int(x in set(cl)) for x in range(p)] for cl in classes]
    e2parts = [multiply_periods(vectors[i],vectors[j],p)
               for i,j in ((0,1),(0,2),(1,2))]
    e2 = rational_period_value([sum(v[k] for v in e2parts) for k in range(p)])
    e3 = rational_period_value(multiply_periods(multiply_periods(vectors[0],vectors[1],p),vectors[2],p))
    L,M = representation(p)
    poly = [1,1,e2,-e3]
    expected = [1,1,-(p-1)//3,-(((L+3)*p-1)//27)]
    assert ((L+3)*p-1)%27==0
    assert poly==expected, (p,poly,expected)
    probes = {str(x): (None if x%p==0 else chi[x%p]) for x in PROBES}
    return {"p":p,"split":True,"primitive_root":g,"class_size":(p-1)//3,
        "classes":classes,"character_exponents":chi,"character_probes":probes,
        "jacobi_chi_chi":j11,"jacobi_chi_bar_chi":[-1,0],
        "jacobi_chi_squared_chi_squared":conjugate,"jacobi_norm":norm(j11),
        "jacobi_exponent_count_table":counts,"cyclotomic_plus_one_table":table,
        "representation_L_M":[L,M],"gaussian_period_polynomial":poly,
        "orientation_note":"switch chi to chi**2 conjugates J; M>0 does not set that orientation"}


def canonical(obj):
    return (json.dumps(obj,sort_keys=True,indent=2,ensure_ascii=True)+"\n").encode()


def generate():
    return {"session":"S003","stage":"E1","status":"EXPERIMENTAL_NOT_NOVELTY",
      "config":{"primes":list(PRIMES),"probes":list(PROBES),
        "normalization":NORMALIZATION,
        "fixed_inputs":"all x in F_p for each preregistered p; no adaptive additions",
        "arithmetic":"integer Eisenstein coefficient pairs; exact cyclotomic convolution"},
      "rows":[examine(p) for p in PRIMES]}


def persist(output):
    data=generate()
    raw=canonical(data)
    dest=Path(output);dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_bytes(raw)
    archive=gzip.compress(raw,compresslevel=9,mtime=0)
    (dest.parent/"s003_full.json.gz").write_bytes(archive)
    manifest={"session":"S003","config":data["config"],"row_count":len(data["rows"]),
       "json_bytes":len(raw),"json_sha256":hashlib.sha256(raw).hexdigest(),
       "gzip_bytes":len(archive),"gzip_sha256":hashlib.sha256(archive).hexdigest(),
       "rows_sha256":hashlib.sha256(canonical(data["rows"])).hexdigest(),
       "oracle":"independent cube-subgroup cosets, x+y=1 pair counts, additive period convolution; exact classical polynomial checks",
       "gate":"EXPERIMENTAL_ONLY_NO_N1"}
    (dest.parent/"s003_manifest.json").write_bytes(canonical(manifest))
    print(json.dumps({"sha256":manifest["json_sha256"],"gzip_sha256":manifest["gzip_sha256"],
                      "rows":[{k:v for k,v in row.items() if k in
                         ("p","split","primitive_root","jacobi_chi_chi","jacobi_chi_bar_chi",
                          "representation_L_M","gaussian_period_polynomial","cube_map_image_size")}
                         for row in data["rows"]]},sort_keys=True))


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",default="out/s003_full.json")
    persist(parser.parse_args().output)
