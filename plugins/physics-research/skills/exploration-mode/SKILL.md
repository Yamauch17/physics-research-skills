---
name: exploration-mode
description: Use when you do not yet know what the answer looks like and want a cheap fast check — scanning parameters, a quick plot, tweaking a term in the model, sanity-checking an intuition or a dimension. Triggers on 快速看看, 试一下, 随便试试, 扫参数, 看看趋势, 大概什么样, 探索一下, "quick check", "quick and dirty", "does this look right", "let me try", "just curious", "play around", "sanity check", "rough idea", "poke at", "eyeball it", "what happens if".
---

# Exploration Mode

## Overview
Zero-pipeline-overhead probing. The point is to make exploration cheap enough that you'll do it
twenty times a day. The *only* overhead you keep is traceability: a saved plot and a one-line log.

## The loop
1. **State intent in one sentence.** No plan, no tests. Then start.
2. **Iterate fast.** Dirty code, hard-coded params, and globals are all fine. Put it in `scratch/` or
   a notebook — never the main codebase.
3. **Save every plot** with parameters in the filename, e.g. `scratch/signal_vs_x_a0.3_b-0.7.png`.
4. **30-second sanity check** (not a validation): dimensions right? limits sane? orders of magnitude OK?
5. **Log one line** to `FINDINGS.md`: date + one-sentence conclusion + figure path. This is the only
   mandatory output. See `findings-logger`.

## Prohibited here
- Unit tests. Refactoring. Asking "should we make a plan / write tests first?"
- Committing scratch code into the main codebase.

## Upgrade to Production (`production-mode`) when
- The result is going into a paper or report.
- You are about to reuse this code a **third** time.
- You hit an **unexpected** result — **90% of surprises are bugs**, so re-derive it properly.

## Rationalizations — STOP
| Excuse | Reality |
|--------|---------|
| "This plot looks publishable, I'll just clean it up" | Exploration code is never promoted. Restart from `theory-derivation`; see the firewall in `research-mode-router`. |
| "Let me add a quick test to be sure" | Wrong mode. Tests = Production. Stay cheap, or upgrade fully. |
| "I'll skip saving the figure, it's obvious" | Untraceable exploration is worthless tomorrow. Save it with params in the name. |
| "The surprise result is real, ship it" | 90% of surprises are bugs. Upgrade and verify before believing it. |

## Red flags
Writing tests · refactoring · a result heading toward a paper · reusing the script again · an
"exciting" unexpected number. **All mean: stay cheap, or switch to `production-mode` — not in between.**
