---
name: implementation-planning
description: Use when writing the implementation plan for a production calculation, after DERIVATION.md exists and before writing code. Triggers on 实现计划, 代码规划, 怎么实现, 先规划再写, implementation plan, plan the code, "how should I implement", "structure the code", "plan before coding", "before I code", writing-plan for a calculation.
---

# Implementation Planning (Stage 3)

## Overview
Turn the derivation into an executable plan. The plan must be anchored to `DERIVATION.md` and must say
in advance how the result will be verified — you plan the checks *before* you write the code they test.

## The plan must include
1. **Reference to `DERIVATION.md`** — which equations/rows each module implements.
2. **Module breakdown** — the model builder, observables, derived quantities — each with the conventions it obeys.
3. **The verification plan (Stage 5 preview):** exactly what `physical-verification` will run — which
   symmetry checks, which known limit to reduce to (the benchmark from `REFERENCES.md`), which
   convergence scans, which self-consistency identity. Write these acceptance gates now.

## Output
A persistent plan file (native plan mode). It is done when someone could implement *and* verify from
the plan without re-deriving.

## Common mistakes
- A plan that lists code modules but no verification — Stage 5 then gets invented after the fact to
  match whatever the code produced.
- Not citing DERIVATION.md, so conventions drift silently during coding.
- Planning the happy path only; no gate for the hard/singular regimes (degeneracies, boundaries, stiff parameters).
