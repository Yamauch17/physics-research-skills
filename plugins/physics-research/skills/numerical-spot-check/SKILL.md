---
name: numerical-spot-check
description: Use when a nontrivial algebraic, symbolic, or index-manipulation step needs verification — plug in random momenta, random parameters, and random unitaries and check the equation holds numerically before trusting it. Triggers on 数值验证, 抽查, 随机抽查, 代入数值, 验证这一步, "is this identity right", "verify this step", "check the algebra", "plug in numbers", "numerically check", "test this equation", random test, sympy check, allclose.
---

# Numerical Spot-Check

## Overview
Every nontrivial derivation step is a claim you can test in seconds: evaluate both sides at random
inputs and compare. This catches sign errors, dropped factors, and transposed indices that reading
the algebra will not. It is the workhorse of `theory-derivation`'s per-step verification.

## Method
1. **Random inputs.** Draw random arguments (momenta, times, positions, fields — whatever the
   expression takes), random parameters, and (where relevant) random unitary matrices / states. Test
   at points the derivation never used.
2. **Compare both sides.** Assert `np.allclose(LHS, RHS, atol=…)`.
3. **Include a counter-candidate.** Also test a deliberately *wrong* variant (e.g. flipped sign) and
   confirm the check *fails* on it — this proves the test can discriminate.
4. **Tolerance from an error budget**, not a wishful round number (float64 identity ≈ 1e-12;
   finite-difference derivative ≈ step-size order).
5. Prefer **exact identities** over fits/series when extracting a quantity — truncation creates false
   alarms.

Harness: `scripts/spot_check.py` (random-input compare + counter-candidate; prints `[PASS]/[FAIL]`,
exits nonzero on failure). Adapt it per identity.

## Common mistakes
- Testing only at symmetric points (k=0, Γ) where many wrong expressions accidentally agree.
- No counter-candidate — a check that passes everything proves nothing.
- Tolerance set to whatever makes it pass.
