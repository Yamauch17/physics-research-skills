# CLAUDE.md — session bootstrap for <project>

## What this repo is
<one paragraph: the research goal. "Not a software product — deliverables are acceptance-gated
notebooks, figures, and short physics documents.">

## Resume protocol (read first after any interruption)
1. Read `PROGRESS.md` — the first unchecked phase is the next task.
2. `git log --oneline -8` and `git tag` — every finished phase is committed (and tagged at gates).
3. Environment: `.venv` (pinned `requirements.txt`). Sanity check: `python code/<module>.py` → `ALL PASSED`.

## Working rules
- **Phased execution, results locked in immediately** (phased-git-workflow): execute headless → asserts
  green → commit → tag at gates → push. Never leave a passing result uncommitted (checkpoint-and-resume).
- **production-mode** for trusted results; **exploration-mode** for cheap probes (never promoted).
- **review-workflow** (independent of production) before a result is declared final: self-review →
  adversarial audit for anything leaving the project.
- **verification-before-completion:** nothing is "done" without executed evidence (physical-verification).
- Deliverables carry no internal plan codenames; write the physics out. Output language: <English / 中文>.

## Technical conventions (the project convention-table — do not re-derive)
| # | Convention | Choice |
|---|-----------|--------|
| C1 | units / what = 1 | ... |
| C2 | sign / transform | ... |
<!-- fill from literature-review-conventions (REFERENCES.md) + theory-derivation (DERIVATION.md) -->
