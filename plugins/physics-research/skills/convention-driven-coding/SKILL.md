---
name: convention-driven-coding
description: Use when writing code for a derived model — implementing the governing equations, observables, or derived quantities — where every symbol must match the derivation's conventions and the object must satisfy structural invariants. Triggers on 写代码, implement the model, "code the equations", "build the operator", turning a derivation into code.
---

# Convention-Driven Coding (Stage 4)

## Overview
Not test-driven — **convention-driven**. The thing under test is the *physical convention* and the
*structural invariants*, not the function signature. Every symbol must trace to a row of the
`DERIVATION.md` conventions table, and the object you build must prove its required properties the
instant it exists.

## Ironclad rules
1. **Every symbol convention matches `DERIVATION.md`**, and the comment cites the line/equation number
   it implements. If you cannot cite it, it is not derived — go back to Stage 2.
2. **Immediately after constructing the core object, assert its structural invariants** — whatever it
   must satisfy by construction: Hermiticity/unitarity, a symmetry, a conservation law, a sum rule, a
   boundary/periodicity condition, positivity, normalization. If you cannot assert it in one line, you
   do not yet understand the object. *(Your domain pack gives the concrete asserts — the specific invariants its objects must satisfy.)*
3. Keep external-anchor self-tests permanent (see `external-anchor-doctrine`): a reduction to a solvable
   limit runs on every execution, not once.

## Rationalizations — STOP
| Excuse | Reality |
|--------|---------|
| "I'll match conventions to the derivation later" | Later = never; the bug is already compiled in. Cite the line now. |
| "The invariant obviously holds by construction" | Assert it anyway — a transposed index or dropped term is invisible until you test it. |
| "TDD says write the failing test first" | Different discipline. Here the test target is the convention and the structural invariant, not a signature. |

## Common mistakes
- Symbols named after the paper but silently using a different sign/transform convention than the table.
- No structural-invariant assertion at construction — the most common source of downstream sign bugs.
- Deleting the invariant assert once "it works" — keep it; it is cheap insurance.
