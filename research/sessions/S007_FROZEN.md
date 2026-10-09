# S007 frozen specification — 37 is intrinsic

Date 2026-10-09 UTC. Starting remote main SHA `9a041c0178bbcace839dcc5d581bab55a1182c86`. Source of authorization: [newest direct user override](../prompts/S007_USER_OVERRIDE.md).

## Mechanism fixed before confirmatory run

The integer **37 is required intrinsically** as the first irregular prime: the classical irregular pair is (37,32), and 32=37−5. The pilot asks whether this special index is manifested in the 37-adic fourth-power reciprocal harmonic sum. This is a known Glaisher/Kummer-type phenomenon, **not a predeclared new theorem**. Source preflight: Glaisher 1900/1901, Kellner 2007 (DOI 10.1090/S0025-5718-06-01887-4), Hart–Harvey–Ong 2017 (DOI 10.1090/mcom/3211), OEIS A397134 and A251782. No missing hit is counted as novelty.

### Fixed input and output population
- Exactly primes `31,37,41,43,59,67`; 37 target, 31/41/43 nearby regular, 59/67 known irregular with different irregular index. These are **purposeful controls, not independent random samples**.
- Exponents r=2,4,6 only. For each (p,r), compute H_r=Σ_{k=1}^{p−1} 1/k^r as rational and as modular inverses modulo p³. Report H_r mod p² and H_r mod p³. Declare p³ an explanatory lift, not novel evidence.
- Independent full exact `Fraction` reduction of H_r numerator/denominator mod p³ and direct modular-inverse accumulation; assert equality for all 18 cells.
- Bernoulli B32 independently from exact rational recurrence; compare with recorded classical value −7709321041217/510, and assert 37 exactly once divides the numerator. Prime 37 was **not selected after observing these results**.
- Guardrails: deterministic Python standard-library only; no stochastic/adaptive search, no p beyond frozen six, no primes >67, no time-heavy field/class-number computation, no paid job.
- Expect pilot positive H4(37) ≡0 mod37², with finer p³ residue to be checked *rather than assumed*. Reject claims of originality from any finite congruence.

### Mechanism-level next target, subject to prescreen
The research-interest hypothesis (not yet an N1 candidate): a **compressed, independently verifiable Kummer generator/certificate** for the unramified degree-37 extension of K=Q(ζ37), exploiting the (37,32) eigenspace. Pre-existing Kummer/Herbrand construction and a complete 2025 PARI/GP polynomial already produce the extension. Thus *mere existence, a formula for a unit, or another unverified polynomial is NOT_NOVEL*. A later S008 would need a quantitatively defined compressed certificate, exact local 37-adic unramifiedness test and a source-backed advantage over both the 2010 discussion and 2025 polynomial. No S008 is executed within S007.

### Single job and stop
One frozen S007 GitHub Actions job may execute the exact pilot; tests and scaffold operate separately as ordinary quality checks. Do not self-authorize extra experiments. Archive exact S007 handoff; update all required ledgers, STATE, S007 report, NEXT_SESSION standalone S008 prompt. Run check_scaffold, unit tests, links and diff; commit/publish PR/merge after green, verify final remote main and Actions. **STOP S007** with results/uncertainty, no claim of a new theorem until substantiated.
