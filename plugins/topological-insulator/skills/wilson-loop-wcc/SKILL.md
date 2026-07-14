---
name: wilson-loop-wcc
description: Use when computing Wilson loops, Wannier charge centers, or hybrid-WCC flow to diagnose band topology. Triggers on Wilson loop, 威尔逊环, 瓦尼尔电荷中心, 瓦尼尔中心流, 极化, Wannier charge center, WCC, hybrid Wannier, holonomy, WCC flow, Wilson loop spectrum, Zak phase, polarization, non-abelian Berry phase.
---

# Wilson Loops & Wannier Charge Centers

## Overview
The Wilson loop is the path-ordered non-abelian Berry phase around a closed BZ loop; its eigenphases
are the Wannier charge centers (WCC). Tracking how WCC flow as the perpendicular momentum sweeps the
BZ diagnoses topology **without gauge fixing** — more robust than direct Ω integration.

## Method
For occupied Bloch states, build overlap matrices M^(k_i,k_{i+1})_{mn}=⟨u_m(k_i)|u_n(k_{i+1})⟩ along a
loop; the Wilson loop is W = ∏_i M^(k_i,k_{i+1}). Eigenphases θ_j of W give WCC = θ_j/2π. Sweep the loop
across the other momentum and plot WCC(k_⊥).

## Reading the flow
- **Chern number** = net winding of the WCC around the cylinder.
- **ℤ₂ (TRS)** = whether Kramers-partner WCC **switch partners** (odd crossings of any horizontal
  reference line) across half the BZ — see `z2-invariant`.

## Common mistakes
- Not enforcing a smooth/periodic gauge closure on the loop (the endpoints must match the start with the
  correct G phase).
- Too few points along the loop near an avoided crossing → miscounted winding (run a `convergence-study`).
- Confusing individual WCC continuity with partner-switching — for ℤ₂ it is the switching that matters.

Alternative Chern route: `berry-curvature-chern`. Symmetry setup: `symmetry-analysis`.
