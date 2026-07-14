---
name: phased-git-workflow
description: Use when locking in research results incrementally so nothing finished is ever uncommitted. Triggers on commit results, 提交结果, 阶段提交, 打标签, 锁定结果, 里程碑, lock in, phase gate, git tag, "commit each phase", "tag the milestone", "save this phase", "record progress", "don't lose results", acceptance gate.
---

# Phased Git Workflow

## Overview
Results are locked in the moment they pass. Work proceeds in phases; each finished phase is executed,
asserted, committed, and (at acceptance gates) tagged. Never leave a passing result uncommitted.

## The cycle (per phase)
1. Execute the deliverable headless (see `jupytext-notebook-workflow`).
2. Asserts green (the notebook's acceptance-gate cell / the module self-test).
3. `git commit` — the result is now locked.
4. **Tag at acceptance gates** (`A1`, `A2`, …) so every milestone is a named, recoverable point.
5. Push.

## Deliverables carry no plan codenames
Figures, captions, notebook prose, and theory docs must **not** reference internal plan codenames
(P1…, A1…, "plan §…", "week-…"). Write the physics out instead. Codenames live only in internal
tracking docs (PLAN.md, PROGRESS.md) and git tags.

## Common mistakes
- A passing result left uncommitted "until the next thing works" — then lost or entangled.
- Committing un-executed or stale-output deliverables (see `jupytext-notebook-workflow`).
- Leaking codenames into a figure caption or theory doc.

Pairs with `checkpoint-and-resume` (persist every unit immediately).
