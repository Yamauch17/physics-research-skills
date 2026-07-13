---
name: convention-table
description: Use when starting a derivation or code that involves sign conventions, transform conventions, index/component ordering, a reference point, or a unit system — anywhere an implicit convention could silently differ between your derivation, your code, and the literature. Triggers on 约定, 符号约定, sign convention, index order, gauge, unit system, "which convention", ħ=1, c=1.
---

# Convention Table

## Overview
Most cross-checking failures are not math errors — they are two halves of a calculation using
*different* conventions that each look right alone. Pin every convention **once**, in a table, and make
the code cite it. A shared *wrong* convention passes every end-to-end self-test, so conventions must
also be anchored to something external (see `external-anchor-doctrine`).

## Pin these before deriving or coding
| Convention | Example choices to state explicitly |
|-----------|-------------------------------------|
| Transform / Fourier sign | e^{+iωt} vs e^{−iωt}; e^{+ik·r} vs e^{−ik·r} |
| Sign / metric conventions | metric (+,−,−,−) vs (−,+,+,+); sign of a coupling constant |
| Index / component order | which index is first; row- vs column-major; tensor index order |
| Units / what is set to 1 | ħ=1? c=1? k_B=1? which unit system |
| Reference / zero point | energy zero, phase origin, gauge origin |
| Normalization | of states/fields; of transforms (2π and 1/√N factors) |

*(Your domain pack adds its own rows — e.g. a gauge choice or a curvature-sign convention — and cites this
same table.)*

## Usage
1. Create the table at the top of `DERIVATION.md` (see `theory-derivation`).
2. In code, every symbol's comment cites the table row it implements (see `convention-driven-coding`).
3. Comparing to a paper: add a row mapping *their* convention to yours — never assume they coincide.

## Common mistakes
- "Everyone uses the same convention" — they do not (transform sign, metric signature, index order vary).
- Choosing a convention implicitly by how the code happened to be written, then never recording it.
- A table that lists choices but is never cited by the code — the citation is what prevents drift.
