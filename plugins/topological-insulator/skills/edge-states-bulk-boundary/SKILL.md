---
name: edge-states-bulk-boundary
description: Use when computing edge or surface states, ribbon or open-boundary spectra, or checking bulk-boundary correspondence by counting in-gap modes. Triggers on edge states, surface states, 边缘态, 表面态, 纳米带, 条带计算, 零能模, 拓扑边缘态, ribbon, zigzag, armchair, slab, open boundary, OBC, bulk-boundary correspondence, 体边对应, in-gap states, zero modes, helical edge, chiral edge, surface Dirac cone, domain wall.
---

# Edge States & Bulk-Boundary Correspondence

## Overview
A nontrivial bulk invariant forces protected in-gap modes at a boundary. Computing the boundary spectrum
and counting those modes is the physical realization of self-consistency check ⑤ in
`physical-verification`: the counted edge modes must equal the bulk invariant.

## Method
1. **Make a boundary.** Build a ribbon: keep translational symmetry along one direction (good quantum
   number k∥) and open (finite, OBC) the other; slab for a 3D surface; fully OBC for a 0D count.
2. **Diagonalize** vs k∥ and pick out states localized at the boundary (weight on edge sites) that cross
   the bulk gap.
3. **Count the net number** of chiral/helical branches crossing the gap (co- vs counter-propagating).
4. **Compare to the bulk invariant:** Chern → number of chiral edge modes (`berry-curvature-chern`); ℤ₂ →
   parity of Kramers pairs (`z2-invariant`). Agreement is the check; disagreement means a bug on one side.

## Numerics
Use enough width that the two edges do not hybridize — the finite-size edge gap decays exponentially with
width; run a `convergence-study` in width. `kwant` is convenient for large finite systems, disorder, and
transport signatures.

## Common mistakes
- Ribbon too narrow → edges hybridize, spurious mini-gap, miscount.
- Counting all in-gap states rather than the *net chirality*.
- Comparing to an invariant computed with a different convention/gauge than the ribbon.

Backends: `numerical-tb-backend`.
