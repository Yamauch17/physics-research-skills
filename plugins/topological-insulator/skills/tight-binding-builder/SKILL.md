---
name: tight-binding-builder
description: Use when constructing a tight-binding Bloch Hamiltonian H(k) for a lattice model such as SSH, Haldane, Kitaev, or BHZ. Triggers on tight-binding, 紧束缚, 紧束缚模型, 布洛赫哈密顿量, 跳跃项, 晶格模型, Bloch Hamiltonian, H(k), "build the lattice model", "construct H(k)", hopping, SSH, Haldane, Kitaev, BHZ, Qi-Wu-Zhang, QWZ, graphene, honeycomb, Pauli decomposition, lattice model, band structure.
---

# Tight-Binding Builder

## Overview
Build H(k) = Σ_R e^{ik·R} t(R) from hoppings, then prove its basic properties before using it. The one
decision that must be recorded is the **gauge**.

## Gauge (record it in `convention-table`)
- **Periodic (cell) gauge:** atom positions enter the phase; H(k+G) ≠ H(k) in general (obeys a
  quasi-periodic relation with a diagonal position phase). Eigenvalues are periodic.
- **Atomic (lattice) gauge:** only the lattice vector R enters the phase; H(k+G) = H(k) exactly.
Pick one, write it down, and assert the matching periodicity relation (see `convention-driven-coding`).

## Two-band form
Decompose H(k) = d₀(k) 𝟙 + **d**(k)·**σ**. Example (SSH, atomic gauge, intracell v, intercell w):
```python
import numpy as np
sx, sy = np.array([[0,1],[1,0]]), np.array([[0,-1j],[1j,0]])
def H(k, v, w):
    dx, dy = v + w*np.cos(k), w*np.sin(k)
    Hk = dx*sx + dy*sy
    assert np.allclose(Hk, Hk.conj().T)          # Hermiticity
    return Hk
# periodicity (atomic gauge): H(k+2π) == H(k)  -> assert in a test
```

## Common mistakes
- Not recording the gauge, then mixing periodic-gauge H(k) with atomic-gauge Berry code → sign bugs.
- Forgetting the Hermiticity assert (a transposed hopping is silent otherwise).
- Building d(k) with the wrong Fourier sign vs the `convention-table`.

Backends: `numerical-tb-backend`. Symmetry check: `symmetry-analysis`.
