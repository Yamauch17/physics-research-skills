---
name: literature-review-conventions
description: Use at the start of a production calculation to find the standard conventions and published benchmark values you should align with, before deriving or coding. Triggers on 文献调研, 基准值, standard convention, benchmark, "what do papers use", "is there a reference value", "prior art".
---

# Literature Review & Conventions (Stage 0)

## Overview
Before deriving anything, find out what "correct" looks like from the outside. Two questions:
- Is there a **standard convention** for this model / invariant / quantity?
- Are there **published benchmark values** you can reproduce to prove your pipeline works?

## Output: `REFERENCES.md`
List, with citations:
1. **Conventions to adopt** (map each to a row of your `convention-table`): Fourier sign, invariant
   normalization, gauge, units. Note where papers disagree and which you pick.
2. **Benchmarks to hit** — specific numbers from the literature (a benchmark energy, a cross-section, a critical
   parameter) that Stage 5 (`physical-verification`, check ③) will reproduce.
3. **Anchors** available as out-of-pipeline checks (see `external-anchor-doctrine`).

## Common mistakes
- Skipping this and inventing a private convention, then being unable to compare to any paper.
- Citing a paper for a number without checking the number is actually in it (verify existence *and*
  content).
- No benchmark chosen — Stage 5 then has nothing external to reduce to.
