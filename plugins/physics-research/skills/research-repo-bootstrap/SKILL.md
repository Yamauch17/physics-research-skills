---
name: research-repo-bootstrap
description: Use when starting a new research project or repository and it needs the standard structure, session bootstrap, and conventions in place. Triggers on new project, 新建项目, scaffold repo, bootstrap, "set up a research repo", "start a new study", project skeleton.
---

# Research Repo Bootstrap

## Overview
Scaffold a new research repo in the house style so every project resumes the same way and enforces the
same discipline from day one. Not a software product — deliverables are notebooks, figures, and short
physics docs.

## Scaffold
```
CLAUDE.md            # session bootstrap: what this is + Resume protocol + working rules + conventions
PROGRESS.md          # phase checklist; first unchecked = next task (see checkpoint-and-resume)
REFERENCES.md        # conventions + benchmarks to align with (literature-review-conventions)
notebooks/           # jupytext percent .py + executed .ipynb (jupytext-notebook-workflow)
code/                # reusable modules, each with a permanent self-test (external-anchor-doctrine)
figures/             # PRL-ready PDF + PNG (prl-figure-style)
scratch/             # exploration only; never promoted (exploration-mode)
docs/refs/           # source PDFs (do not edit)
FINDINGS.md          # one-line exploration log (findings-logger)
.venv/ + requirements.txt   # pinned environment
```

## CLAUDE.md must contain
- **What this repo is** (one paragraph) and the **Resume protocol** (read first after any interruption).
- **Working rules** carried in (phased git, verification-before-completion, output language).
- **Technical conventions** table (units, sign anchors) — the `convention-table` for this project.

Templates: `templates/CLAUDE.md`, `templates/PROGRESS.md`. Pair with `checkpoint-and-resume` and
`phased-git-workflow`.

## Common mistakes
- No Resume protocol — a new session cannot tell what is done.
- Conventions scattered in code comments instead of one table in CLAUDE.md.
- No `scratch/` boundary, so exploration code leaks toward the deliverables.
