# Experiments and exposure ledger

| ID | Design | Evidence | Status |
| --- | --- | --- | --- |
| EXP-000 | Bootstrap instrument; primes 31,37,41,43; bases 2..200; Python exact modular arithmetic | Source ``scripts/enumerate.py``, 7 unit tests, [push CI](https://github.com/jfairfaxball-348/37/actions/runs/37920710063), [PR CI](https://github.com/jfairfaxball-348/37/actions/runs/37920729633); both succeeded. 777 rows; canonical rows SHA-256 `b539f662b79da38d949910875c20c3dcfb90f59b48a52772d7fff7607f7cf80f`; workflow artifact available | TOOL VERIFIED; mathematical novelty NOT CLAIMED |
| EXP-001 | Bounded S001 comparison, algebraic reduction and failure-oriented controls | [Next session](NEXT_SESSION.md) | NOT EXECUTED |

**Do not count implementation as a mathematical result.** In S001 replace EXP-001 with exact run/commit/CI/artifact/digest IDs and the full explored parameter envelope. Exclude cherry-picked runs from any later confirmatory claims. An output hash identifies bytes, not research validity.


## EXP-001 — S001 completed on GitHub Actions (2026-10-09)
**Frozen design:** p=31,37,41,43; b=2..2000 all integers, exact Python stdlib; exclude p|b and count exclusions; one nonzero residue per prime is one independent algebraic value. 15-min job ceiling, no random seeds, no adaptive batches, no holdout claimed. Instrument: scripts/enumerate.py (original) plus scripts/s001_validate.py (distinct direct recurrence), 9 arithmetic unit tests.

**Run input/code SHA:** `75c71352c0ff253673143c3ac8005a029777302d`. **GitHub Actions:** deep run [37921994616](https://github.com/jfairfaxball-348/37/actions/runs/37921994616), job 113791871984 SUCCESS; baseline run [37921994604](https://github.com/jfairfaxball-348/37/actions/runs/37921994604), job 113791872210 SUCCESS, baseline only b2..200. Python 3.12.15 Ubuntu Linux x64. Deep run artifact ID **11611558874**, ZIP SHA-256 `1b0e8279d72dc373267adc6eadbba8376d54d77074a46a9fc192eaec86a66f6c` (90-day retention, 2027-01-07). Archived data commit `c8df7f32a298a1d4674b400ae42511ff58493fc4`. Full raw JSON: 1,685,822 bytes SHA-256 `6c6f3d69507675f3038039208b1348dd79087e57d29a16210e84721f899ae397`; canonical rows SHA-256 `e8d41b25830b06518864e91ff5b2a2eb0d955f8b278bfacaea4f3c26187e3069`; durable deterministic gzip 36,122 bytes SHA-256 `bd1991d186b77df5e24b88e686320053a150dd2e5ea02701d65ce6fe5d7565ca`. Input/output/summary [manifest](data/S001_manifest.json) and full [archive](data/S001_full.json.gz).

**Outcome:** 7996 attempts; 7784 included, 212 excluded. Every row, summary, cyclic group phi histogram and Phi3 root set independently checked. Zero discrepancies. p37 1945 included but 36 unique residue classes; 108 bases of order 3 are repetitions of 10 and 26. Cross-prime details in [S001](sessions/S001.md); [NA-001–004](NOVELTY_LEDGER.md) all NOT_NOVEL. **NO SURVIVOR / PIVOT.** Data remain usable as negative baseline; no theorem or statistical generality certified. S002 uses new prime-power question, not post-hoc repeated p37 base successes.
