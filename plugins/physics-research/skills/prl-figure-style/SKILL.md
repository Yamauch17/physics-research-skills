---
name: prl-figure-style
description: Use when producing figures for a paper, report, or slides that should look publication-ready. Triggers on 画图, 出图, figure style, publication figure, PRL figure, APS, matplotlib style, panel labels, "make this figure nice".
---

# PRL-Ready Figure Style

## Overview
Every figure is submission-ready as produced — no post-hoc cleanup. Use one shared style module so all
figures in a project match. Helper: `scripts/figstyle.py` (`prl_rc()`, `panel_label()`, `save_fig()`).

## Conventions
- **Size at final scale:** APS widths — 3.375 in single-column, 7.0 in double-column. Do not shrink a
  big figure; author it at final size so fonts land at the right point size.
- **Fonts:** serif (STIX) 7–8 pt to match the journal body text.
- **Ticks:** inward on all four sides, with minor ticks.
- **Panel labels:** bold `(a) (b) (c)`, via `panel_label()`.
- **No plot titles.** Put the ready-to-use caption in a text/markdown cell next to the figure instead.
- **Legends:** frameless.
- **Save both** with `save_fig()`: vector **PDF** (the submission artifact) + **600 dpi PNG**
  (preview). Commit both.

## Usage
```python
from figstyle import prl_rc, panel_label, save_fig
prl_rc()                      # apply rcParams once
fig, ax = plt.subplots(figsize=(3.375, 2.6))
# ... plot ...
panel_label(ax, "a")
save_fig(fig, "figures/03_gap_vs_M")   # writes .pdf + .png
```

## Common mistakes
- Titles on the plot instead of a caption (journals strip titles).
- Authoring large then scaling down — fonts become inconsistent across figures.
- Committing only the PNG; the vector PDF is the submission artifact.

See `jupytext-notebook-workflow` for where figures are generated and committed.
