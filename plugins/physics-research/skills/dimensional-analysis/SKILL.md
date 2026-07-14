---
name: dimensional-analysis
description: Use before trusting any number and as the first check on any derived expression — when a formula, result, or code output could have a units or dimension error, or when two derivations disagree and you need the fast arbiter. Triggers on 量纲, 量纲分析, 单位, 单位不对, 数量级, 差了个系数, order of magnitude, "check the units", "right units?", "dimensionally", "does the magnitude make sense", "factor of", "off by", unit mismatch, dimensional check.
---

# Dimensional Analysis

## Overview
Units are the cheapest and most powerful check in physics. A dropped factor, a stray 2π, or a wrong
power almost always breaks the units first. Make dimension-checking reflexive: every step, every
result, every plotted axis.

## Practice
1. **Declare a unit system explicitly** and record it in the `convention-table`. State *which*
   quantities are set to 1 — "natural units" is not a spec. (e.g. ħ=c=1 in high-energy physics;
   Gaussian vs SI in electromagnetism; a fixed energy and length unit in condensed matter.) Derived
   quantities then inherit their units from that choice.
2. **Carry units through every line**, not just the final answer. Both sides of every equation must
   share a dimension before you believe it.
3. **Arbitrate disagreements with units first.** When two derivations differ, dimension-check each
   step; the dropped factor usually fails a unit check immediately.
4. **Sanity-check orders of magnitude.** A result 10^±3 off is a units/prefactor bug until proven
   otherwise.

## Common mistakes
- Checking units only on the final formula, not the intermediate step where the error entered.
- A "natural units" hand-wave that never says which constants are 1 — reintroduce them to check.
- Plot axes without units; a physically meaningless magnitude hides in an unlabeled axis.
