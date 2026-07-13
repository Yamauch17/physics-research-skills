#!/usr/bin/env python3
"""chern_fhs.py -- Chern number of a 2-band lattice model via the Fukui-Hatsugai-Suzuki
plaquette method, with a massive-Dirac SIGN ANCHOR as a permanent self-test.

Model (Qi-Wu-Zhang):  H(k) = sin kx * sx + sin ky * sy + (m + cos kx + cos ky) * sz.
Lower-band Chern number: |C| = 1 for 0 < |m| < 2 (topological), C = 0 for |m| > 2 (trivial),
and the sign FLIPS across m = 0 (fixed by the sz Dirac-mass sign at the gap closing).

Two classic mutually-masking sign bugs live here:
  * d_x - i d_y  vs  d_x + i d_y  in the off-diagonal assembly,
  * the FHS plaquette orientation.
Each alone flips C's sign; together they cancel and pass a single-phase check. The sign-FLIP
across m = 0 (an EXTERNAL analytic fact) is what catches them -- see external-anchor-doctrine.

Run:  python chern_fhs.py   ->  prints C and [PASS]/[FAIL]; exits nonzero on failure.
Depends: numpy only.
"""
import numpy as np

SX = np.array([[0, 1], [1, 0]], complex)
SY = np.array([[0, -1j], [1j, 0]], complex)
SZ = np.array([[1, 0], [0, -1]], complex)


def qwz_H(kx, ky, m):
    H = np.sin(kx) * SX + np.sin(ky) * SY + (m + np.cos(kx) + np.cos(ky)) * SZ
    assert np.allclose(H, H.conj().T)          # Hermiticity (convention-driven-coding)
    return H


def lower_vec(kx, ky, m):
    _, v = np.linalg.eigh(qwz_H(kx, ky, m))
    return v[:, 0]                              # lowest band


def chern_fhs(m, nk=48):
    ks = np.linspace(0.0, 2 * np.pi, nk, endpoint=False)
    U = np.empty((nk, nk, 2), complex)
    for i, kx in enumerate(ks):
        for j, ky in enumerate(ks):
            U[i, j] = lower_vec(kx, ky, m)

    def lk(a, b):                              # normalized link variable
        o = np.vdot(a, b)
        return o / abs(o)

    F = 0.0
    for i in range(nk):
        for j in range(nk):
            ip, jp = (i + 1) % nk, (j + 1) % nk
            u1 = lk(U[i, j],   U[ip, j])
            u2 = lk(U[ip, j],  U[ip, jp])
            u3 = lk(U[ip, jp], U[i, jp])
            u4 = lk(U[i, jp],  U[i, j])
            F += np.angle(u1 * u2 * u3 * u4)   # FHS field strength (principal branch)
    return F / (2 * np.pi)


FAILS = 0
def check(name, ok, detail=""):
    global FAILS
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" : {detail}" if detail else ""))
    if not ok:
        FAILS += 1


if __name__ == "__main__":
    C_p, C_m = chern_fhs(1.0), chern_fhs(-1.0)
    C_t, C_tm = chern_fhs(3.0), chern_fhs(-3.0)
    print(f"C(m=+1)={C_p:+.3f}  C(m=-1)={C_m:+.3f}  C(m=+3)={C_t:+.3f}  C(m=-3)={C_tm:+.3f}")
    check("topological |C|=1 at m=+1", abs(round(C_p)) == 1, f"C={round(C_p)}")
    check("topological |C|=1 at m=-1", abs(round(C_m)) == 1, f"C={round(C_m)}")
    check("Dirac-mass sign anchor: C flips across m=0", round(C_p) == -round(C_m),
          f"{round(C_p)} vs {round(C_m)}")
    check("trivial C=0 at m=+3", round(C_t) == 0)
    check("trivial C=0 at m=-3", round(C_tm) == 0)
    if FAILS:
        print(f"\n{FAILS} CHECK(S) FAILED"); raise SystemExit(1)
    print("\nALL PASSED")
