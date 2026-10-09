# 37 — computational and algebraic mathematics research

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

The [S003 report](research/sessions/S003.md), [complete deterministic archive](research/data/S003_full.json.gz) and [manifest](research/data/S003_manifest.json) contain exact normalized Jacobi sums in integer Eisenstein coefficients and independently verified cubic Gaussian periods. Hosted Actions [run 37928972106](https://github.com/jfairfaxball-348/37/actions/runs/37928972106) passed all 21 tests and the independent oracle. The [S004 prompt](research/NEXT_SESSION.md) proposes a **different additive-sumset** E1 exploration, not executed in S003.
