---
name: symmetry-analysis
description: Use when classifying or numerically verifying the symmetries of a Bloch Hamiltonian — time-reversal, particle-hole, chiral/sublattice — and its Altland-Zirnbauer class. Triggers on symmetry, 对称性, TRS, PHS, chiral, sublattice, time-reversal, particle-hole, Altland-Zirnbauer, AZ class, tenfold way.
---

# Symmetry Analysis

## Overview
Topological classification is set by antiunitary/unitary symmetries. Derive the operators, then
**verify them numerically** — a claimed symmetry that H does not actually obey invalidates the whole
classification.

## The three symmetries
| Symmetry | Operator | Relation on H(k) | Square |
|---|---|---|---|
| Time-reversal (TRS) | T = U_T K | T H(k) T⁻¹ = +H(−k) | T² = ±1 |
| Particle-hole (PHS) | C = U_C K | C H(k) C⁻¹ = −H(−k) | C² = ±1 |
| Chiral / sublattice | S = U_S (unitary) | S H(k) S⁻¹ = −H(k) | S² = 1 |

(S = T·C up to a phase.) The signs of T², C² and presence of S select one of the **ten**
Altland–Zirnbauer classes, which fixes which invariant (ℤ, ℤ₂, 2ℤ, or none) exists in each dimension.

## Verify numerically (do not just assert)
At random k and random model parameters, check the relation holds with a counter-candidate (see
`numerical-spot-check`):
```python
assert np.allclose(U_T @ H(k).conj() @ U_T.conj().T, H(-k))   # TRS, T = U_T K
```
This is check ② of `physical-verification`.

## Common mistakes
- Testing only at k=0 / TRIM, where H(−k)=H(k) hides a broken relation.
- Confusing the operator's unitary part U with the full antiunitary T = U K (forgetting the complex
  conjugation K).
- Reading the AZ class off T²/C² signs computed with the wrong convention.
