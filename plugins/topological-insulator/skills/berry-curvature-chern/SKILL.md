---
name: berry-curvature-chern
description: Use when computing the Berry connection, Berry curvature, or a Chern number of a band. Triggers on Berry curvature, Berry phase, Berry connection, Chern number, 陈数, 贝里曲率, 贝里相位, 贝里联络, 陈绝缘体, 霍尔电导, "compute the Chern number", TKNN, Fukui-Hatsugai-Suzuki, FHS, plaquette, anomalous Hall, quantum anomalous Hall, QAH, Hall conductance.
---

# Berry Curvature & Chern Number

## Overview
Berry connection A_n(k) = i⟨u_n|∇_k u_n⟩, curvature Ω_n = ∇×A_n, Chern C_n = (1/2π)∫_BZ Ω_n. Compute C
with a **gauge-invariant** lattice method so it comes out an exact integer.

## Use the FHS plaquette method
Fukui–Hatsugai–Suzuki: on each plaquette form link variables U_μ(k)=⟨u(k)|u(k+δ_μ)⟩/|·|, and the field
strength F₁₂ = Im ln[ U₁(k) U₂(k+δ₁) U₁(k+δ₂)⁻¹ U₂(k)⁻¹ ]. Then C = (1/2π) Σ_plaquettes F₁₂ — integer
by construction, no gauge fixing. Script: `scripts/chern_fhs.py`.

## ★ Anchor the sign to the massive Dirac limit (permanent self-test)
For a 2-band H = **d**(k)·**σ** with a Dirac mass m, the half-integer Berry flux of each cone has a
known sign. Keep a reduction to this limit as a self-test that runs every time (see
`external-anchor-doctrine`). Two classic **mutually-masking** sign bugs live here:
- `d_x − i d_y` vs `d_x + i d_y` in off-diagonal assembly;
- the **FHS plaquette orientation** (sign of the loop).
Each alone flips the sign; together they cancel and pass a BHZ-only check — only the external Dirac
anchor catches them.

## Numerics
Finite-difference/pythtb Berry curvature needs a **fine k-mesh near small gaps** (nk ≳ 241 for meV-scale
gaps); always run a `convergence-study` on nk. Near-degeneracy noise is expected — smooth it, don't
trust a single mesh.

## Common mistakes
- Direct ∫Ω on a coarse mesh (non-integer, gauge-noisy) instead of FHS.
- No Dirac sign anchor → a sign error that a self-consistent BHZ run never reveals.
- Reading C off before checking mesh convergence near the gap.

See `wilson-loop-wcc` (alternative, and Z2), `edge-states-bulk-boundary` (the bulk-boundary check).
