---
name: convergence-study
description: Use when a numerical physics result depends on a discretization or truncation — a mesh, grid, system size, basis size, time step, or expansion order — and you must show it is converged. Triggers on convergence, 收敛, 收敛性检查, 网格加密, 有限尺寸, 步长, 截断误差, mesh, grid, grid refinement, system size, finite-size scaling, time step, truncation, cutoff, basis size, "is it converged", "converged with respect to", extrapolation, refinement.
---

# Convergence Study

## Overview
"It looks converged" is not evidence. Every numerical result has discretization/truncation knobs;
convergence means the observable stops changing (to your target tolerance) as you refine them, at a
*measured* rate. This is check ④ of `physical-verification`.

## Method
1. **Identify every knob:** mesh/grid density, system size or volume, basis/mode count, time step,
   expansion/truncation order, inner-solver tolerances.
2. **Scan each** (holding the others fixed at a fine value) and record the observable.
3. **Plot the observable vs the knob** (often vs 1/N or the step size). Refine until the change is below
   your error budget.
4. **Report the measured order/rate** (e.g. the slope on a log–log plot) and extrapolate if useful.
   Compare to the *expected* order — a wrong order signals a bug or an unresolved feature.
5. **Refine hardest where the integrand is sharp** (near singularities, small denominators, boundary
   layers); the generic point converges long before the hard one.

## Common mistakes
- One mesh and an eyeball — no curve, no measured rate.
- Refining one knob while another stays too coarse to reveal the true limit.
- A scan whose "converged plateau" is actually the flat top of an unresolved peak.

See `dimensional-analysis` (sanity) and `external-anchor-doctrine` (compare the limit to something external).
