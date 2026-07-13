# topological-insulator

A **domain pack** of Claude Code skills for topological insulators and topological band structures.
Extends the subject-agnostic [`physics-research`](../physics-research) core with the concrete
techniques — the core supplies the *process*, this supplies the *physics*.

Part of the [physics-research-skills](https://github.com/Yamauch17/physics-research-skills) marketplace.

## Skills (9)

- `tight-binding-builder` — build H(k) for SSH / Haldane / Kitaev / BHZ; record the gauge; assert
  Hermiticity + periodicity
- `symmetry-analysis` — TRS / PHS / chiral operators, Altland–Zirnbauer class, numerically verified
- `berry-curvature-chern` — Berry curvature & Chern number via the gauge-invariant FHS plaquette, with
  a **massive-Dirac sign anchor** as a permanent self-test
- `wilson-loop-wcc` — Wilson loops / Wannier charge centers / hybrid-WCC flow
- `z2-invariant` — Z2 via WCC partner-switching / Fu–Kane parity / Wilson loop
- `edge-states-bulk-boundary` — ribbon & OBC spectra; edge count = bulk invariant
- `kp-effective-model` — k·p / Löwdin reduction (e.g. BHZ from Kane), with validity range
- `topological-phase-diagram` — parameter scans → phase boundaries / gap closings
- `numerical-tb-backend` — choosing/using pythtb, custom NumPy, kwant, Z2Pack / WannierTools

## Install

Run each as a separate `/plugin` command — install the core first, then this pack:
```text
/plugin marketplace add Yamauch17/physics-research-skills
```
```text
/plugin install physics-research@physics-research-skills
```
```text
/plugin install topological-insulator@physics-research-skills
```

## Example session

> **You:** build the BHZ model and give me its Chern number, and I need to trust it
> → `tight-binding-builder` (asserts Hermiticity + periodicity of H(k)) → `berry-curvature-chern`
> (FHS plaquette, sign anchored to the Dirac limit) → `physical-verification` (convergence in k-mesh,
> bulk-boundary check via `edge-states-bulk-boundary`).

Ships a runnable self-test:

```bash
python skills/berry-curvature-chern/scripts/chern_fhs.py
```
Expected output: `C(m=+1)=+1  C(m=-1)=-1  C(m=+3)=0  C(m=-3)=0` → `ALL PASSED`.

## Security profile

Pure Markdown skills plus one self-test script (`berry-curvature-chern/scripts/chern_fhs.py`) that uses
only `numpy`. **No MCP servers, no network calls, no hooks, no telemetry.** MIT licensed.
