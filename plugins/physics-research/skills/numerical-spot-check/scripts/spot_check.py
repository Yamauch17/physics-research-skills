#!/usr/bin/env python3
"""spot_check.py -- template harness for verifying a derivation step numerically.

Pattern (adapt per identity):
  1. draw RANDOM inputs (never test only at symmetric points),
  2. assert LHS ~ RHS from your derivation,
  3. include a COUNTER-CANDIDATE (a deliberately wrong variant) and assert it FAILS,
  4. set tolerances from an error budget, not wishful round numbers.

Run:  python spot_check.py   ->  [PASS]/[FAIL] lines; exits nonzero on any failure.
Depends: numpy only.
"""
import numpy as np

rng = np.random.default_rng(0)
FAILS = 0


def check(name, ok):
    global FAILS
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if not ok:
        FAILS += 1


def rand_unitary(n):
    """Haar-ish random unitary via QR of a complex Gaussian."""
    z = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
    q, r = np.linalg.qr(z)
    return q @ np.diag(np.exp(1j * np.angle(np.diag(r))))


# --- Example 1: (A B)^H = B^H A^H, at random complex matrices ---
for _ in range(20):
    A = rng.standard_normal((4, 4)) + 1j * rng.standard_normal((4, 4))
    B = rng.standard_normal((4, 4)) + 1j * rng.standard_normal((4, 4))
    check("(AB)^H = B^H A^H", np.allclose((A @ B).conj().T, B.conj().T @ A.conj().T, atol=1e-12))

# --- Counter-candidate: WRONG order must FAIL (proves the test discriminates) ---
A = rng.standard_normal((4, 4)) + 1j * rng.standard_normal((4, 4))
B = rng.standard_normal((4, 4)) + 1j * rng.standard_normal((4, 4))
check("counter-candidate (A^H B^H) correctly rejected",
      not np.allclose((A @ B).conj().T, A.conj().T @ B.conj().T, atol=1e-12))

# --- Example 2: unitary similarity preserves eigenvalues, at random U and Hermitian H ---
for _ in range(20):
    n = 5
    H = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
    H = H + H.conj().T
    U = rand_unitary(n)
    ev1 = np.sort(np.linalg.eigvalsh(H))
    ev2 = np.sort(np.linalg.eigvalsh(U @ H @ U.conj().T))
    check("eig(U H U^H) = eig(H)", np.allclose(ev1, ev2, atol=1e-10))

if FAILS:
    print(f"\n{FAILS} CHECK(S) FAILED")
    raise SystemExit(1)
print("\nALL PASSED")
