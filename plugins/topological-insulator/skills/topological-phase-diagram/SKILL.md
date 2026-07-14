---
name: topological-phase-diagram
description: Use when mapping a topological phase diagram — scanning model parameters to locate phase boundaries and gap-closing transitions where an invariant changes. Triggers on phase diagram, 相图, 拓扑相图, 相变, 相边界, 能隙关闭, 扫参数找相变, phase boundary, gap closing, "where does the gap close", "map the phase diagram", topological transition, phase transition line, parameter scan, critical point, "as a function of the mass".
---

# Topological Phase Diagram

## Overview
Topological phases are separated by **gap closings**: the invariant can change only where the bulk gap
closes. Mapping the diagram = computing the invariant on a parameter grid and locating the boundaries.

## Method
1. **Scan** parameters on a grid; at each point compute the bulk gap and the invariant
   (`berry-curvature-chern` / `z2-invariant`).
2. **Boundaries = gap closings** where the invariant jumps. Cross-check both ways: every invariant jump
   should coincide with gap → 0, and every gap closing should move the invariant.
3. **Resolve boundaries** with a finer scan where the gap is small; the transition is a measure-zero
   locus, so a coarse grid steps over it.
4. **Find the gap closing in k too** — it occurs at specific k-points (often high-symmetry); identifying
   them explains the transition.

## Watch for
- **Scan-edge artifacts:** a "boundary" sitting exactly at the edge of the scanned window usually means
  the real boundary is outside it — widen the scan (a classic false result).
- An invariant jump with no gap closing → numerical error in the invariant, not a real transition.

See `convergence-study` (refine near boundaries) and `physical-verification`.
