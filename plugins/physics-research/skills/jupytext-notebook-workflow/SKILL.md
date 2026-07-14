---
name: jupytext-notebook-workflow
description: Use when producing results as Jupyter notebooks that must stay reproducible and diff-able in git. Triggers on notebook, jupyter, jupytext, ipynb, 笔记本, 可复现笔记本, 运行笔记本, reproducible notebook, percent script, paired notebook, "run the notebook", "make a notebook", nbconvert, execute notebook, assert cell.
---

# Jupytext Notebook Workflow

## Overview
Notebooks are deliverables, but `.ipynb` diffs are noise and stale outputs lie. Keep a text source of
truth, execute headless, and gate each notebook with an assertion.

## Workflow
1. **Source of truth = jupytext percent `.py`** in `notebooks/` (clean git diffs, reviewable).
2. **Build:** `jupytext --to ipynb notebooks/NN_*.py`.
3. **Execute headless:** `jupyter nbconvert --to notebook --execute --inplace notebooks/NN_*.ipynb`.
4. **Commit both** the `.py` and the executed `.ipynb`, plus `figures/*.png` (see `prl-figure-style`).
5. **End every notebook with an assert cell = acceptance gate.** A failed assert blocks the next
   notebook (fix, or stop and report). This is where the `physical-verification` checks become
   executable gates.

## Common mistakes
- Editing the `.ipynb` directly — the `.py` source drifts and the diff becomes unreviewable.
- Committing an un-executed notebook, or one whose outputs predate the last code change.
- A notebook with no assert cell — nothing stops a silently broken result from flowing downstream.

See `phased-git-workflow` for the commit/tag discipline around executed notebooks.
