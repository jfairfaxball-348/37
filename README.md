# 37 — computational and algebraic mathematics research

**Stage P0 complete: research infrastructure bootstrapped, 9 October 2026. No original theorem, novelty certification, formal proof, registration, preprint or publication is claimed.**

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

## Reproduce enumeration

Requires only Python 3.11+ (standard library).

```bash
python3 scripts/check_scaffold.py
python3 -m unittest discover -s tests -v
python3 scripts/enumerate.py --primes 31,37,41,43 --base-min 2 --base-max 200 --output out/baseline.json
```

The machine-readable output records precise configuration, rows, sample counts, and a SHA-256 of canonical row data. It enumerates multiplicative orders and least repunit lengths for valid prime/base pairs. The routine is a **measurement instrument**, not proof, novelty detection or an original result. Read [design and limits](docs/ENUMERATION_DESIGN.md).

[GitHub Actions research checks](.github/workflows/research.yml) run for PRs/pushes and can be manually dispatched with a larger base bound; outputs are workflow artifacts, not automatically accepted mathematical claims. The repository is the authoritative research record, and every bounded session ends with checked GitHub publication and a standalone copy/paste prompt in `research/NEXT_SESSION.md`.

