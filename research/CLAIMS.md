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
