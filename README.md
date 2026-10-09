# 37 — computational and algebraic mathematics research

**S005 first mandatory fifth-session audit COMPLETE, 9 October 2026: PIVOT / NO VIABLE TARGET.** Four earlier extensive and independently software-checked investigations S001–S004 all found NO SURVIVOR / PIVOT; **zero original theorems, zero N1 finalists, zero Lean/Palomar/submissions**. The 37-centred input-first method is PARKED and 37 is now an optional illustration only. S005 screened rank-two zero-sum stability and prime-modulus squarefree distribution, five primary comparators per question, with no justified tractable novelty survivor. [Read the 5/5 audit](research/sessions/S005.md), [full progress correction](research/PROGRESS_AUDITS.md), and [the S006 source-first contract](research/NEXT_SESSION.md). S006 has NOT been executed.

**S002 complete, 9 October 2026: prime-square lifting and cyclotomic/repunit valuation sweep (7,784 valid rows), independent full GitHub Actions verification. Every observed pattern is explained by classical LTE/Hensel/Fermat quotient theory: NO SURVIVOR / PIVOT. S001 also had NO SURVIVOR / PIVOT. No original theorem, novelty certification, formal proof, registry, preprint or journal publication is claimed.**

This project uses **37 as an exploratory seed** for rigorous research in modular arithmetic, multiplicative orders, repunits, cyclotomic factors, finite-field structure and related integer sequences. It is deliberately not committed to any claim that 37 is exceptional. The research question is *which, if any, apparently distinctive observations survive base changes, control primes, algebraic explanation and a substantive novelty audit?* Widen the mathematical direction when evidence justifies it.

## Research method

1. Deep **bounded, reproducible enumeration** with fixed inputs and independent checks.
2. **Pattern discovery** with counterexample attempts, base/residue controls, and holdout ranges; record negative findings.
3. Translate observations into **exact hypotheses and algebraic explanations** with explicit quantifiers.
4. Immediately screen the literature for each interesting or potentially useful observation. Require a deep, source-logged **novelty/prior-art audit** before promoting a result.
5. Proof or counterexample; independent mathematical verification; optional Lean 4 formalisation for precise target statements; post-proof novelty audit; optional Palomar verification; paper, arXiv and journal only if justified and separately authorized.

**No finite computation proves an unrestricted statement; no LLM agreement is independent review; no successful formalisation certifies novelty.**

The [current state](research/STATE.json), [research process](docs/RESEARCH_PIPELINE.md), [session protocol](docs/SESSION_PROTOCOL.md), [novelty policy](docs/NOVELTY_STANDARD.md), [enumeration design](docs/ENUMERATION_DESIGN.md), [claims register](research/CLAIMS.md), and [next session](research/NEXT_SESSION.md) are authoritative. [AGENTS.md](AGENTS.md) governs automated work.

## Known starting point (not an original discovery)

For decimal base 10, `111 = 3 × 37`, `Φ₃(10) = 10² + 10 + 1 = 111`, `ord₃₇(10)=3`, and `1/37 = 0.027027…`. These are standard repunit/multiplicative-order facts. In particular, a visually striking decimal string is *not* a new result. See the [baseline prior-art screen](research/NOVELTY_LEDGER.md) and the [OEIS entry on repunit divisibility](https://oeis.org/A172372).

## S001 exact archive and evidence

Read the [S001 report](research/sessions/S001.md), [checked manifest](research/data/S001_manifest.json) and [durable full JSON archive](research/data/S001_full.json.gz) (gzip, decompress to recover unfiltered source JSON). GitHub Actions [deep run 37921994616](https://github.com/jfairfaxball-348/37/actions/runs/37921994616) validated every output row independently. The S002 prompt is archived in [S002_INPUT](research/prompts/S002_INPUT.md); classical lifting was not a novelty claim.

## S002 complete prime-power archive and evidence

Read the [S002 report](research/sessions/S002.md), the [independently checked S002 manifest](research/data/S002_manifest.json), and full exact [S002 compressed JSON](research/data/S002_full.json.gz). GitHub Actions [full S002 run 37926530437](https://github.com/jfairfaxball-348/37/actions/runs/37926530437) checked every p-square row independently and uploaded artifact 11613668670. The S003 prompt is archived in [S003_INPUT](research/prompts/S003_INPUT.md); the completed cubic-character identities were NOT_NOVEL.

## Reproduce enumeration

Requires only Python 3.11+ (standard library).

```bash
python3 scripts/check_scaffold.py
python3 -m unittest discover -s tests -v
python3 scripts/enumerate.py --primes 31,37,41,43 --base-min 2 --base-max 200 --output out/baseline.json
```

S002 prime-power replay:

```bash
python3 -m scripts.s002_enumerate --output out/s002_full.json
python3 -m scripts.s002_validate --input out/s002_full.json --manifest out/s002_manifest.json --archive out/s002_full.json.gz
```

The machine-readable output records precise configuration, rows, sample counts, and a SHA-256 of canonical row data. It enumerates multiplicative orders and least repunit lengths for valid prime/base pairs. The routine is a **measurement instrument**, not proof, novelty detection or an original result. Read [design and limits](docs/ENUMERATION_DESIGN.md).

[GitHub Actions research checks](.github/workflows/research.yml) run for PRs/pushes and can be manually dispatched with a larger base bound; outputs are workflow artifacts, not automatically accepted mathematical claims. The repository is the authoritative research record, and every bounded session ends with checked GitHub publication and a standalone copy/paste prompt in `research/NEXT_SESSION.md`.


## S003 exact cubic-character archive and new pivot

The [S003 report](research/sessions/S003.md), [complete deterministic archive](research/data/S003_full.json.gz) and [manifest](research/data/S003_manifest.json) contain exact normalized Jacobi sums in integer Eisenstein coefficients and independently verified cubic Gaussian periods. Hosted Actions [run 37928972106](https://github.com/jfairfaxball-348/37/actions/runs/37928972106) passed all 21 tests and the independent oracle. The archived S004 prompt proposed a **different additive-sumset** E1 exploration, not executed in S003.

## S004 complete: additive four-point exhaustive experiment (NO SURVIVOR)
[S004 report](research/sessions/S004.md), [full unfiltered raw JSON](research/data/S004_full.json), [deterministic gzip](research/data/S004_full.json.gz), [S004 manifest](research/data/S004_manifest.json) and [verbatim input](research/prompts/S004_INPUT.md) document all **32560** anchored sets (primes 31,37,41,43), affine duplicate weights and **five** coarse sumset/restricted/difference/energy profiles. One [hosted run 37931379701](https://github.com/jfairfaxball-348/37/actions/runs/37931379701) passed 26 tests and the full independent four-index/unordered-pair oracle. Classical additive combinatorics accounts for the observations; no novel theorem or N1 candidate was found (**fourth consecutive NO SURVIVOR / PIVOT**). [S005](research/sessions/S005.md) completed the mandatory progress audit; [S006](research/NEXT_SESSION.md) is the unexecuted next source-only pivot.

S004 exact independent replay (Python 3.12 standard library):

```bash
python3 -m scripts.s004_additive --folder out
python3 -m scripts.s004_validate --folder out --tracked research/data
```

## S006 terminal research-method closeout (2026-10-09)
[S006 literature-only audit](research/sessions/S006.md) examined two exact local/genus/class questions for primitive positive definite binary quadratic forms against **12 primary sources** and found **NO VIABLE TARGET / STOP_CURRENT_PROGRAMME** for the present AI-led source-audit-to-original-theorem search. The -23 genus example is classical; modern form-class/prime-representation results (2012–2025) compete closely. No original theorem, N1 finalist, Lean/Palomar or preprint/journal result exists. S001–S004 remain NO SURVIVOR; S005 was PIVOT/NO VIABLE TARGET. The [terminal S007 handoff](research/NEXT_SESSION.md) requires new explicit **human-led rechartering**; it authorizes no new session. Documentation-only PRs now run quality checks **without automatically running the old bounded enumeration** (that step requires manual dispatch).

## S007 recharter: 37 MUST be essential (2026-10-09)
The user expressly overrode the former terminal closeout and required future work to be **mathematically about 37**, not merely to insert 37 as a convenient modulus. [S007 report](research/sessions/S007.md) documents a new bounded source-first research direction: first Kummer irregular pair **(37,32)**, its classical quartic harmonic manifestation (18 exact independently verified frozen cells in [S007 data](research/data/S007_37_exact.json); [hosted run 37943949693](https://github.com/jfairfaxball-348/37/actions/runs/37943949693)), and a strictly prospective 37-cyclotomic unramified degree-37 Kummer certificate project. The harmonic congruence is NOT novel; original Kummer/Herbrand constructions and the 2025 publicly printed PARI polynomial are already prior art. **No original theorem, no N1 finalist**. [S008](research/NEXT_SESSION.md) is an explicitly 37-specific standalone next-session instruction; the old S006 STOP remains preserved as historical method assessment. No S008 work has been executed.
