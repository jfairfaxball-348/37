# Exact enumeration and falsification design

## Scope and representation

Initial rows are indexed by a prime `p` and positive integer base `b ≥ 2`, with `gcd(b,p)=1`. The canonical residue `b mod p` is retained. Each row contains:

- `ord_p(b)`, the least positive `k` with `b^k ≡ 1 (mod p)`.
- `A_p(b)`, the least positive `k` for which `p` divides `R_k(b)=1+b+...+b^(k-1)`.
- flags for length three, divisibility of `b-1`, and the residue class.

The two lengths must not be confused. If `b ≡ 1 (mod p)`, then `ord_p(b)=1` while `A_p(b)=p` (prime `p`); otherwise they coincide. Bases divisible by `p` are marked as excluded rather than forced into a misleading periodic-order computation. `R_k(b)` is computed by modular recurrence in independent oracle tests.

## Experimental protocol

- Begin with `p=37` and preregistered controls `p=31,41,43`. The controls are design choices, **not a mathematical null distribution** or automatically representative prime sample.
- Compare the **same residue class** across `b` and `b+p` and across other bases, not just pretty decimal digit strings.
- Search for exact identities, invariants and exceptional sets. Reduce each observation to known group/cyclotomic facts *before* calling it surprising.
- For stronger claims add a fresh family of primes/prime classes selected **before seeing its results**, retain a holdout region and quantify all searched parameter ranges and rejected hypotheses.
- Disclose limits: a base sweep repeats the same `p-1` nonzero residues; duplicate observations do not provide independent evidence. Control choice, selection of striking digits and multiple comparisons are exploration hazards.
- For each run record code commit, inputs, Python version, run ID, JSON hash, controls, test result, runner, and compute budget. Keep full outputs as Actions artifacts; commit durable extracts only when necessary.

## Engine and limits

Run `python3 scripts/enumerate.py --help`. The exact engine validates primes by trial division, factors `p-1` to reduce multiplicative order with modular exponentiation, and derives repunit length by the prime cases above. It caps base bounds, prime magnitude and total pair count. It makes **no claim** of optimizing huge-scale number theory computations. Independent unit tests enumerate modular oracles for small cases. For large campaigns, add another independently implemented method and keep algorithm/version pins before promoting observations.

GitHub Actions `research.yml` always executes checks and a bounded enumeration, with `workflow_dispatch` arguments for deeper sweeps; its compute never substitutes for proof or prior-art work.

