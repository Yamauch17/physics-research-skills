---
name: external-anchor-doctrine
description: Use when a result depends on constants, calibration factors, or an internal round-trip that could be self-consistent yet wrong — when a closed loop "agrees with itself" but nothing outside the pipeline pins the value. Triggers on 定标, 外部锚, closed loop, self-consistent, calibration, benchmark, "agrees with itself", "validates itself".
---

# External-Anchor Doctrine

## Overview
A calculation that closes on itself validates *nothing* about the constants it cancels. Two
mutually-masking bugs — a sign error in one stage cancelled by the same error in the next —
survive every end-to-end self-test. The only cure: anchor each interface and constant to something
**outside** the pipeline.

## Doctrine
1. **Every constant or interface needs an external anchor** — an exactly-solvable limit, a published
   literature value, an experimental measurement, or a symmetry/conservation law. *Not* the pipeline's
   own other half.
2. **Keep the anchor as a permanent self-test.** Once an external check catches a bug, freeze it as an
   assert that runs forever (e.g. reduce to a known-solvable limit and compare every run).
3. **Closed loops are where latent convention errors hide.** A self-consistent round-trip is a
   *necessary*, never a *sufficient*, check — demand an external comparison too.
4. **Split deterministic bias from noise before touching a failing gate.** Re-run noise-free first;
   never retune to a random seed. A "−12% noise" that is actually a calibration bias must be modeled,
   not averaged away.

## Common mistakes
- Advertising "two methods agree" when both are *yours* sharing a convention (see `convention-table`)
  — that is internal agreement, not validation.
- Deleting an external-anchor self-test because "it always passes" — that is exactly its job.
- Treating a deterministic offset as noise and smearing over it.

See `numerical-spot-check` (fresh-input tests) and `physical-verification` (known-limit reduction).
