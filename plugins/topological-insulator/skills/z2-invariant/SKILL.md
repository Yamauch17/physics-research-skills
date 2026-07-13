---
name: z2-invariant
description: Use when computing a Z2 topological invariant for a time-reversal-invariant insulator in 2D or 3D. Triggers on Z2, 拓扑不变量, 时间反演不变量, Fu-Kane, Kane-Mele, parity invariant, partner switching, strong/weak topological insulator, ν0.
---

# Z2 Invariant

## Overview
The ℤ₂ invariant classifies TRS insulators (class AII): ν=1 topological (odd), ν=0 trivial. In 2D one
ν; in 3D four (ν₀; ν₁ν₂ν₃). Requires TRS with T²=−1 (verify with `symmetry-analysis` first).

## Three routes (prefer 1)
1. **WCC / Wilson-loop partner switching** — general, needs no extra symmetry. Compute WCC flow over
   half the BZ (see `wilson-loop-wcc`); ν = number of times Kramers partners switch, mod 2. Robust and
   gauge-invariant; the default.
2. **Fu–Kane parity** — *only if inversion symmetry is present*: ν = ∏ over TRIM of the product of
   parity eigenvalues of occupied Kramers pairs. Cheap, but inversion-only.
3. **Direct integral of A/Ω over half BZ** — gauge-dependent, fragile; avoid unless you enforce a smooth
   gauge.

## Common mistakes
- Using Fu–Kane parity when the model has no inversion symmetry (invalid).
- Computing ℤ₂ on a model whose T²=−1 you never verified (wrong class).
- Miscounting partner switches from too few k-points (converge the WCC flow).

Verifies against edge counting via `edge-states-bulk-boundary` (an odd ν ⇒ odd number of Kramers edge
pairs).
