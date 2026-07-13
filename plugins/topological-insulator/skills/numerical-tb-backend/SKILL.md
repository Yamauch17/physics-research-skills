---
name: numerical-tb-backend
description: Use when choosing or using a numerical backend for tight-binding and topology calculations — building H(k), diagonalizing, Berry/Chern/Wilson, ribbons, or transport. Triggers on pythtb, kwant, Z2Pack, WannierTools, numpy tight-binding, 数值后端, "which library", band structure code, transport code.
---

# Numerical TB Backend

## Overview
Pick the backend by task; keep the same convention discipline (`convention-driven-coding`) whatever you
pick — always assert Hermiticity and the periodicity/gauge relation of H(k) at construction.

## Options
| Backend | Best for | Notes |
|---|---|---|
| **pythtb** | TB models, Berry phase/curvature, Chern, Wilson loops, ribbons | Simple, good default. Finite-difference Berry needs a **fine k-mesh (nk ≳ 241) near small gaps**. |
| **custom NumPy/SciPy** | full control; hand-rolled H(k) + `eigh` + FHS plaquette | Pair every module with a permanent self-test (`external-anchor-doctrine`). |
| **kwant** | transport, disorder, large finite systems, edge/surface spectra | Landauer conductance, scattering; good for `edge-states-bulk-boundary`. |
| **Z2Pack / WannierTools** | dedicated invariant engines (hybrid WCC / Wilson loop) | Excellent independent cross-checks for `z2-invariant` / `wilson-loop-wcc`. |

## Guidance
- Cross-check one backend against another at a known limit rather than trusting a single tool.
- Watch mesh convergence for any Berry-curvature quantity (`convergence-study`); near-degeneracy noise is
  expected.

## Common mistakes
- Trusting a coarse-mesh Chern from finite differences instead of the FHS plaquette (`berry-curvature-chern`).
- Switching backends mid-project without re-checking the H(k) convention/gauge match.
