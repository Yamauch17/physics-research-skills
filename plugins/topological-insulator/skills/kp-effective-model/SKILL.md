---
name: kp-effective-model
description: Use when deriving or using a k·p or effective low-energy model — expanding around a band extremum and folding out remote bands to get an effective Hamiltonian such as a Dirac or BHZ model. Triggers on k·p, kp, 有效模型, 低能模型, Löwdin, Schrieffer-Wolff, envelope function, effective Hamiltonian, BHZ from Kane.
---

# k·p Effective Models

## Overview
Near a high-symmetry point a few bands dominate the low-energy physics. A k·p expansion plus Löwdin
partitioning folds out the remote bands into an effective Hamiltonian on the retained subspace. Powerful,
but valid only in a limited energy/k window — always state the range.

## Method
1. **Expand** H(k₀+q) = H(k₀) + q·(∂H) + ½ qq:(∂²H) around the extremum k₀.
2. **Partition** the basis into "kept" (A, near the gap) and "remote" (B). Löwdin / Schrieffer–Wolff gives
   H_A^eff = H_AA + H_AB (E − H_BB)⁻¹ H_BA to the desired order in q.
3. **Impose symmetry** to fix which terms are allowed and cut free parameters (see `symmetry-analysis`).
4. **State validity:** holds for |q| and |E − E₀| small compared to the gap to the remote bands; different
   branches (e.g. conduction vs valence) can have *different* valid ranges.

## Verify
Spot-check the effective model against the full model: eigenvalues agree inside the stated window and
diverge outside it — that divergence *is* the validity boundary (plot it, `convergence-study`). This is a
`theory-derivation` output; record conventions and the retained order.

## Common mistakes
- Quoting the effective model without its validity range, then using it where it has already failed.
- Dropping a q² term symmetry actually allows (or keeping one it forbids).
- Assuming one validity window for all branches.
