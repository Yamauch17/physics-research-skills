# REVIEW REPORT — <repo / result>

**Repo:** ... **Reviewed commit:** <hash> **Date:** ...
**Method:** independent-first re-derivation + executable spot-checks at fresh inputs.
**Data caveats:** <what was re-run vs read from cache>.

**Overall verdict:** <Accept / Minor / Major / Reject> — <one-line reason>.

## 1. Workspace asset mapping (files ↔ claims)
| File | Claim(s) | Ledger IDs |
|------|----------|-----------|

## 2. Critical physics/logic & math flaws (RED)
> Errors that corrupt presented results, or latent errors that will corrupt the intended future
> application (state the scope). Write "none found" if empty.

## 3. Numerical, data & code divergences (YELLOW)

## 4. Step-by-step divergence analysis
Per finding:
- **[File & context]**
- **[My first-principles version]**
- **[Project's version]**
- **[Diagnosis]** — and the one-line required fix.

## 5. Presentation & minor concerns

## 6. Scorecard & recommendation
| Axis | /10 |
|------|-----|
| Theory / design correctness | |
| Mathematical rigor | |
| Numerical / code reliability | |
| Reproducibility | |

**Recommendation:** <Accept / Minor / Major / Reject>. Mechanical mapping: a red flag on a presented
result ⇒ at least Major.

## Appendices
- **A — Claim ledger** (C1, C2, …) with verdicts [VERIFIED] / [PARTIALLY VERIFIED] / [UNSUPPORTED] /
  [INCORRECT] + evidence pointers. ([VERIFIED] needs your own executed evidence at a fresh point.)
- **B — Independent derivations** (with the per-step dimension checks).
- **C — Spot-check script index + verbatim outputs** (re-run from a clean shell before writing this).
