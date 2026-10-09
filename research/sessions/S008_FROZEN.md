# S008 source-first frozen comparator and test plan (NOT EXECUTED)

Date: 2026-10-09 UTC. Starting main `1fb7346c39122bdec83d6a336433bed4ac003092`. This is the **single fixed reference expression and verification plan**, recorded after source review and before ANY S008 arithmetic job. The strict novelty gate **failed before compute**. No S008 certificate run, exploration, PARI install, new generator or N1 candidate is authorized by this freeze.

## Field and one expression (known, not proposed as original)
Let `p=37`, `K=Q(zeta)`, `zeta=zeta_37`, `O_K=Z[zeta]`, `pi=1-zeta`, `nu=37-32=5`, and `g=2` (a primitive root modulo 37: its 18th power is -1 and its 12th power is not 1). Define `epsilon=zeta^18*(1+zeta)` and `sigma_a(zeta)=zeta^a`, for `1<=a<=36`.
For every a, `e_a` is the unique integer in `[-18,18]` congruent to `a^5 mod 37`. Freeze just
```
U = product_{a=1}^{36} (sigma_a^{-1}(epsilon))^{e_a}.
```
Here `sigma_a^{-1}` means substitution `zeta -> zeta^(a^{-1} mod 37)`, not a numerical reciprocal. The unbalanced original exponents `a^5` and balanced exponents differ by multiples of 37; hence these expressions differ by a 37th power in K. **This is only a trivial re-encoding of Lemmermeyer's recorded Kummer/Herbrand product**, not a second independently invented candidate. The factor `1+zeta` is a cyclotomic unit since `Norm_{K/Q}(1+zeta)=Phi_37(-1)=1`; all conjugates and integral powers are units. Do not infer local unramifiedness from this global unit fact.

## Benchmark predefinition; incompleteness is decisive
Metric M1: sum of the exact bit lengths of 36 signed integer coordinates in the canonical basis `1,zeta,...,zeta^35` for a *specified element*, plus 36 signs; evaluate only after canonical expansion/reduction using `Phi_37(zeta)=0`. Metric M2: UTF-8 byte count of a fully specified factored expression and its grammar, plus counted independent verifier operations/memory, **requiring the expression to generate the same Kummer class field**. A defining polynomial in x over K and an element U are **different objects**: no honest M1 comparison is available until conversion/isomorphism is validated. The 2010 source already supplies a 36-conjugate-factor expression; balancing exponent residues is a routine Kummer-class reduction, not a new shorter certificate. The 2025 example has `x^37 + A(y)` with 36 coefficient slots `y^0..y^35`, 35 visibly nonzero (all `y^2..y^35` and constant; no `y^1`) and coefficients up to 27 decimal digits, but is **not** a local ramification proof and was not independently reduced/measured here. No comparable validated bit-length and verifier-cost baselines for *both* exist; cannot truthfully claim a strict saving.

## EXACT one-plan verification, hypothetical only (no run)
1. Algebraic ring `Z[t]/Phi_37(t)` over integers, canonical coefficient-vector operations and independent multiplication oracle; verify U and U^{-1} with explicit products (unit property also follows algebraically from Norm).
2. At exactly the predeclared auxiliary rational prime `q=149=4*37+1`, choose the least `r in {2,...,148}` of order 37 modulo 149, and the prime of K given by `zeta -> r`. If `U(r)^4 != 1 mod149`, conclude U is not a 37th power in K, hence `[K(U^(1/37)):K]=37`. Equality is **inconclusive**; no adaptive second q in S008.
3. For all prime ideals not dividing 37, `U` is a unit, so `disc(X^37-U)=+/-37^37 U^36` is a local unit; no tame ramification.
4. For the wild prime `pi`, require a separately provided **exact** coordinate vector `V in O_K` with `v_pi(V)=0` and `U-V^37 in (pi^73)`; since `v_pi(37)=36`, Hensel's condition `v_pi(f(V))>2v_pi(f'(V))=72` proves a local 37th root and therefore **splitting**, stronger than unramifiedness. Use an independent exact integral ideal/modular-power check, not mere `mod37` or unstated PARI output. Failure to find V does NOT show ramification.
5. A second verifier reconstructs the same mod-pi^73 congruence without shared reduction code; report counts/versions/time. Full class group uniqueness/Hilbert identification requires independently checked `h(K)=37`; Gras 2018 section 4.4 states h=37, but this project did not compute a class-number certificate.
6. Compare byte count, canonical-bit M1 where compatible, all verification operations and data against MO 2010 factor and MO 2025 polynomial. Include machine-readable witness with basis convention, endianness, moduli, full independent replay and human algebraic-number-theorist proof/novelty review **before** an N1 candidate.

**Stop gate:** Original 2010 explicit factor already competes directly and the 2025 polynomial is known. No verified improvement or independent `pi^73` witness has been found. S008 execution of this hypothetical one-plan is **NOT justified**. Preserve as design/negative result only.
