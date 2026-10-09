# S003 — cubic characters and exact Jacobi-sum feasibility (standalone copy/paste prompt)

Work in @GitHub https://github.com/jfairfaxball-348/37 (repository ID 1411685319). The repository is authoritative. Execute **exactly ONE bounded S003 E1 exploratory investigation**, then checks, commit, push, PR and merge where permitted, verify actual Actions/remote main, and write the complete S004 prompt. **STOP after S003; do not execute S004.**

## Read first; preserve gates
Read README.md, AGENTS.md, research/STATE.json, research/NEXT_SESSION.md, research/CLAIMS.md, research/CANDIDATES.md, research/NOVELTY_LEDGER.md, research/EXPERIMENT_LEDGER.md, research/DECISION_LOG.md, research/PROGRESS_AUDITS.md, research/sessions/S001.md, research/sessions/S002.md, both manifests, and all docs/ pipeline, session, design and novelty standards. Pin remote main SHA, inspect latest merged/unmerged PR and GitHub Actions. Archive the exact currently authoritative S003 prompt verbatim in research/prompts/S003_INPUT.md before replacing research/NEXT_SESSION.md. S001 and S002 BOTH ended **NO SURVIVOR / PIVOT**; there is no established original theorem or N1 finalist. Do not revive standard order lifting under a new name.

## Materially different objective
Explore a *new algebraic framework*: cubic multiplicative characters, cyclotomic number tables of order 3 and Jacobi sums in Z[ω], ω²+ω+1=0. Use p=37 as seed; p=31 and 43 as declared split controls (p≡1 mod 3), p=41 as negative/inert control (p≡2 mod 3). Do **not** interpret the lack of a nontrivial cubic character at 41 as surprising. Work with exact integer coefficient pairs (A+Bω), not floating point roots. For split primes specify a primitive-root and cubic-character normalization in advance, track consequences of replacing χ by χ², and verify J(χ,χ̄) and J(χ,χ) identities where correctly applicable (avoid unexamined normalization/sign errors). Investigate the classical representations 4p=L²+27M², norm J(χ,χ)=p, cubic period polynomials and splitting/character-interaction invariants, then look for a genuinely consequential pattern beyond the textbook identities.

## Existing literature FIRST
Before proposing originality, inspect and record at least:
- Berndt, Evans and Williams, *Gauss and Jacobi Sums*, relevant chapters and known corrections (https://mathweb.ucsd.edu/~revans/contents.html and https://mathweb.ucsd.edu/~revans/errata/).
- Literature on cubic reciprocity, Gauss periods and primary Eisenstein-integer normalization (e.g. Ireland–Rosen).
- Helou, *Reciprocity for Jacobi Sums*, JNT 1993, DOI 10.1006/jnth.1993.1046.
- Related primary evaluations, OEIS for any exact numerical sequence and the nearest modern peer-reviewed/published results.
- The S002/S001 ledgers' lessons on false novelty and repeated classes.

Record literal search queries, URLs, publication/access dates, exact reading depth (full theorem/proof vs abstract/index only), 3–5 nearest competitors **for every worthwhile observation**, explicit hypotheses, negative cases and missing sources. Classical cubic reciprocity, Jacobi sums and 4p=L²+27M² are NOT novel. An inability to access a paper does not imply originality.

## Frozen bounded computation
Define a predeclared small finite set of prime controls and integer inputs, exact algebraic character tables, checksums, and an independent oracle (for example direct finite-field counting versus formal Z[ω] pair calculations). Use GitHub Actions with **one maximum-15-minute computational job** on hosted free runners, Python standard library unless already justified, no paid service, no stochastic extrapolation. Capture exact source/commit, script/config, run/job/artifact IDs, versions, data archives and SHA-256, full negative findings, and normalization dependencies. No adaptive expansion disguised as a confirmatory test; no automatic inference across all primes.

## Gate and session closure
Select **at most one** precisely quantified and potentially significant proposition for a later N1 audit ONLY if genuinely non-routine, defensibly distinct and falsifiable. Otherwise explicitly **NO SURVIVOR / PIVOT** to a materially new S004 direction. Update research/sessions/S003.md, STATE.json, all applicable claim/candidate/experiment/novelty/decision/progress/AI-use ledgers, archive the S003 prompt, and write an actual standalone S004 copy/paste prompt to research/NEXT_SESSION.md. Run `python3 scripts/check_scaffold.py`, `python3 -m unittest discover -s tests -v`, independent exact replay, `git diff --check`, local Markdown link checks and all relevant GitHub Actions (push and PR). Commit, publish PR and merge when possible, verify final remote main SHA and actual success status; if blocked publish the branch/PR and disclose the gate, never claim merge/CI that did not occur. No external researcher contact, spending, Lean, Palomar, arXiv, journal action or S004 execution without separate authority. STOP.
