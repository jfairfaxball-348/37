# Claims and evidence register

| ID | Statement | Evidence/status | Novelty |
| --- | --- | --- | --- |
| BG-001 | `111 = 3 × 37 = Φ₃(10)`, and `ord₃₇(10)=3` | BACKGROUND: elementary calculation | NOT_NOVEL; [screen](NOVELTY_LEDGER.md) |
| BG-002 | For prime `p` and `p∤b`, the base-`b` repetend period of `1/p` equals `ord_p(b)` | BACKGROUND: standard multiplicative order theory | NOT_NOVEL; [screen](NOVELTY_LEDGER.md) |

**Original claims: none.** Enumerated examples are EXPERIMENTAL observations. No proof or formal verification of a novel mathematical assertion has occurred. Promote by unique ID only with source-backed conjecture, a falsification design and the applicable novelty audit.


## S001 checks — NOT ORIGINAL CLAIMS
- **EXP-S001-01 / EXPERIMENTAL:** In the predeclared window p∈{31,37,41,43}, 2≤b≤2000, the exact engine emitted 7784 valid coprime rows, 212 excluded; every row independently verified via modular recurrence. Full hashes and run references in [S001 report](sessions/S001.md).
- **BG-003 / BACKGROUND, NOT_NOVEL:** For any prime p, the cyclic group (Z/pZ)* has phi(d) elements of order d for each d|(p−1); number of primitive roots is phi(p−1). [NA-002](NOVELTY_LEDGER.md).
- **BG-004 / BACKGROUND, NOT_NOVEL:** For p≠3, x²+x+1 has precisely two roots mod p if 3|(p−1), otherwise none; [NA-001](NOVELTY_LEDGER.md).
- **BG-005 / BACKGROUND, NOT_NOVEL:** For p∤b the least repunit length equals ord_p(b) unless b≡1 mod p, when it equals p; [NA-003](NOVELTY_LEDGER.md).

**Original claims at S001 close: NONE.** No P0/S001 output is a new theorem.

## S002 — background and experimental assertions only
- **BG-006 / BACKGROUND, NOT_NOVEL:** odd-prime LTE order lifting: for p∤b, d=ord_p(b), s=v_p(b^d-1), ord_(p^k)(b)=d p^max(0,k-s); [NA-005](NOVELTY_LEDGER.md).
- **BG-007 / BACKGROUND, NOT_NOVEL:** p-adic repunit valuations, the p|(b-1) exception and p|b exclusion; [NA-006](NOVELTY_LEDGER.md).
- **BG-008 / BACKGROUND, NOT_NOVEL:** one exceptional p² lift per nonzero residue from Hensel/Teichmüller theory and affine Fermat quotient shifts; [NA-005](NOVELTY_LEDGER.md).
- **EXP-S002-01 / EXPERIMENTAL:** 7,784 full-window rows and 212 exclusions, full independent recurrence and modular valuations, p² class coverage 930/1332/1640/1806, exceptional unique classes 30/36/40/42. [Full evidence](sessions/S002.md). No claim of statistical independence, general theorem or novelty.
- **EXP-S002-02 / EXPERIMENTAL:** high-valuation rows s>=3 at primes 31/37/41/43: 1/1/1/0, [NA-007](NOVELTY_LEDGER.md); not significant by itself.

**S002 original claims: NONE. No candidate advanced to N1.**

## S003 — exact cubic-character controls, no original mathematical assertion
- **BG-009 / BACKGROUND, NOT_NOVEL:** Jacobi identities for nontrivial cubic characters, norm `N(J(chi,chi))=p` and `J(chi,bar chi)=-chi(-1)=-1`; switching chi to chi² conjugates the Eisenstein integer. [NA-008](NOVELTY_LEDGER.md).
- **BG-010 / BACKGROUND, NOT_NOVEL:** classical normalized `4p=L²+27M²`, cubic Gaussian period polynomial, order-three cyclotomic-number tables, primary normalization [NA-009](NOVELTY_LEDGER.md).
- **EXP-S003-01 / EXPERIMENTAL:** p=31/37/41/43, all residues and fixed probes 2/3/10; 3 split + 1 inert control, 21 tests and full independent integer/cube/class/period oracle PASS. Exact [session](sessions/S003.md), [manifest](data/S003_manifest.json). No theorem, no N1 candidate. Prior two NO SURVIVOR gates unchanged.
