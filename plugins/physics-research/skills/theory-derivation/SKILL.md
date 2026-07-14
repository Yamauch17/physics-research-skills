---
name: theory-derivation
description: Use when deriving the governing model or equations of a problem by hand or symbolically — a Hamiltonian, Lagrangian, effective theory, master/rate equation, or reduced model — before any code is written. Triggers on 推导, 建模, 从头推, 写下哈密顿量, 拉氏量, 有效理论, derive, governing equations, effective theory, "set up the model", "write down the Hamiltonian", "work out the model", "derive the equations", "derive from first principles", master equation, reduction, low-energy model.
---

# Theory Derivation (Stage 2)

## Overview
Derive the model before coding it. The output is a document a referee could check line by line — the
final equations, the conventions they assume, and evidence that each nontrivial step is correct.

## Two mandatory disciplines
- **★ Conventions table.** Record every convention *before* deriving (sign/transform conventions,
  index/component order, unit system, what is set to 1, reference points). Use `convention-table`; code
  will cite these rows by number.
- **★ Per-step numerical spot-check.** After each nontrivial step, verify it at random inputs, random
  parameters, and random unitaries/rotations — with a counter-candidate. Use `numerical-spot-check`. A
  step you did not spot-check is a step you have not verified.

## Output: `DERIVATION.md`
1. The conventions table.
2. The derivation with every step shown (no jumps), each nontrivial step annotated with its spot-check
   result.
3. The final form of the model (numbered), its symmetries, and any reduced/effective model with the
   reduction *and its validity range* stated.

Template: `templates/DERIVATION.md`. `implementation-planning` and `convention-driven-coding` reference
this file by equation/line number. Subject-specific derivations are
carried by your **domain pack's** skills, which produce this same `DERIVATION.md`.

## Common mistakes
- Deriving first, recording conventions later (or never) — the source of interface bugs.
- "This step is obvious" — obvious steps hide sign errors; spot-check anyway.
- Leaving the final equations in a form whose symmetries you never checked (Stage 5 will need them).
