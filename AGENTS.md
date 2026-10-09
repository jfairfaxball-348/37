# Instructions for every research session in 37

## Authority
Read `README.md`, `research/STATE.json`, `research/NEXT_SESSION.md`, `research/CLAIMS.md`, `research/CANDIDATES.md`, `research/NOVELTY_LEDGER.md`, `research/DECISION_LOG.md` and relevant protocols **before** working. Repository commits and current explicit user instructions take precedence over chat memory and archived prompts. Pin the starting remote HEAD; inspect prior sessions and live CI. Do not execute next session within the session that writes it.

## Mission and scope
Seek a **genuine, worthwhile, original mathematical contribution**, initially using number 37 as a *seed*, not a privileged hypothesis. Explore deep finite enumeration, residue patterns, algebraic structure and nontrivial generalization. Investigate whether patterns are explained by base representation, cyclotomic identities, multiplicative-order theory, or already-known theorems. Explicitly compare 37 against nearby/structurally comparable primes and changes of base, and distinguish numerical coincidences from invariant mathematics. Pivot when algebraic/prior-art evidence warrants. Negative results count. Prefer mathematically consequential theorems to recreational numeric curiosity.

Follow `docs/RESEARCH_PIPELINE.md` and `docs/NOVELTY_STANDARD.md`. Any interesting/useful lead gets a **contemporaneous prior-art screen**; candidate promotion requires an exact, source-backed novelty audit. No 'no hit means novel', guessed open problems, unsupported novelty or fabricated references.

## Compute and research integrity
Use repository code and GitHub Actions as the compute lab when needed; prefer Python standard library, exact integer arithmetic and reproducible test fixtures. For substantial searches record commit SHA, workflow run/job/artifact, script/config, parameter window, seed if any, versions, time/cost ceiling, checksums, positive and negative observations, independent checks, adaptive-search exposure and next holdout. Respect resource budgets and GitHub platform limits; split work into bounded jobs rather than indefinite runs. Never cherry-pick favourable base/primes after viewing outputs and present them as confirmatory. Discovery data are exploratory, not independent verification.

Labels: BACKGROUND, EXPERIMENTAL, CONJECTURE, PROVED_ON_PAPER, FORMAL_VERIFIED, NOVELTY_UNCERTAIN, NOT_NOVEL, REFUTED, PARKED. Formally verified means precisely encoded, kernel-checked statement under its trust assumptions, not historical novelty, human proof review or peer review. No proof or publication may be claimed without records and evidence.

## Standing closeout and publication authorization
For **every** requested bounded session, autonomously:
1. Complete the authorized work and record failures, scope, claims, sources, decisions and reproducibility.
2. Update state/ledgers, append one session report in `research/sessions/` and write `research/NEXT_SESSION.md` as the **complete copy/paste next-session prompt**. Archive the previous executable prompt in `research/prompts/` before replacing it.
3. Run `python3 scripts/check_scaffold.py`, `python3 -m unittest discover -s tests -v`, relevant exact reproductions and whitespace/links/safety checks. For code changes use PR-triggered GitHub Actions and inspect actual run/jobs; do not misreport queued or absent CI as passing.
4. Commit and publish to GitHub; normally use a branch → PR → merge into `main`, verify merged PR and remote `main` HEAD, and check workflow results. This routine GitHub publication and merging **is authorized**. If merge is blocked, retain the published PR, report the obstacle plainly, and never claim success.
5. In the final user reply report evidence and a **standalone copyable next-session prompt**, ready to run from `main`. If a real user decision blocks progress, state that instead of inventing approval. No separate permission needed for routine research files, scripts, CI, commits, PRs or merges.

Use a bounded session and STOP; do not silently start the next session. Every fifth substantive session is a progress/correction audit, additionally earlier if candidates repeatedly fail novelty. Publish correction/negative information as faithfully as positive results.

## External boundaries
No emails, researcher contact, issue-based solicitation, registration, Palomar submission, arXiv upload, journal submission, paid compute, purchases or public claims of review without **separate explicit user authority**. Public literature searches and routine GitHub publication are allowed. The human author retains responsibility for validity and AI contribution disclosure. No secrets, private messages, personal data or inaccessible source material committed. Never rewrite or delete authoritative research history to make a result seem stronger.

