#!/usr/bin/env python3
"""figstyle.py -- APS/PRL-ready matplotlib style. Import prl_rc / panel_label / save_fig.

Conventions: APS column widths at final size, STIX serif 7-8 pt, inward ticks on all four
sides + minor ticks, bold (a)(b)(c) panel labels, NO plot titles, frameless legends,
save vector PDF (submission) + 600 dpi PNG (preview).
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator

COL_SINGLE = 3.375   # APS single-column width (in)
COL_DOUBLE = 7.0     # APS double-column width (in)


def prl_rc():
    """Apply the publication rcParams (call once at the top of a figure script)."""
    plt.rcParams.update({
        "font.family": "serif",
        "mathtext.fontset": "stix",
        "font.serif": ["STIXGeneral", "DejaVu Serif"],
        "font.size": 8, "axes.labelsize": 8, "axes.titlesize": 8,
        "legend.fontsize": 7, "xtick.labelsize": 7, "ytick.labelsize": 7,
        "axes.linewidth": 0.6,
        "xtick.direction": "in", "ytick.direction": "in",
        "xtick.top": True, "ytick.right": True,
        "xtick.minor.visible": True, "ytick.minor.visible": True,
        "legend.frameon": False,
        "figure.dpi": 150, "savefig.dpi": 600, "savefig.bbox": "tight",
    })


def panel_label(ax, letter, x=-0.18, y=1.02, **kw):
    """Bold (a)/(b)/(c) panel label in axes-fraction coords."""
    ax.text(x, y, f"({letter})", transform=ax.transAxes,
            fontsize=9, fontweight="bold", va="bottom", ha="left", **kw)


def save_fig(fig, stem):
    """Write <stem>.pdf (vector, submission) and <stem>.png (600 dpi, preview)."""
    fig.savefig(f"{stem}.pdf")
    fig.savefig(f"{stem}.png", dpi=600)


if __name__ == "__main__":
    import numpy as np, os, tempfile
    prl_rc()
    x = np.linspace(0, 1, 200)
    fig, ax = plt.subplots(figsize=(COL_SINGLE, 2.6))
    ax.plot(x, np.sin(2 * np.pi * x), lw=1.0)
    ax.set_xlabel("x"); ax.set_ylabel("f(x)")          # NO title -> caption goes in the text
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    panel_label(ax, "a")
    out = os.path.join(tempfile.gettempdir(), "figstyle_selftest")
    save_fig(fig, out)
    ok = os.path.exists(out + ".pdf") and os.path.exists(out + ".png")
    print("ALL PASSED" if ok else "FAILED")
    raise SystemExit(0 if ok else 1)
