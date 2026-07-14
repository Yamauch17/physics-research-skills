---
name: physics-brainstorming
description: Use when starting a production calculation and the real physical question, the observable, or the success criterion is not yet pinned down. Triggers on 头脑风暴, 可观测量, 目标不清楚, 到底算什么, 明确问题, 可证伪, "what am I actually calculating", "define the question", "what's the deliverable", "what would falsify", "what's the observable", "success criterion", vague research goal.
---

# Physics Brainstorming (Stage 1)

## Overview
Socratic questioning to surface the *true* physical problem before any math. Most wasted production
effort computes a quantity nobody can observe or falsify.

## Key questions (answer all three)
1. **What physical quantity are you calculating?** State it precisely, with units.
2. **What is its observable counterpart?** How would an experiment see it? If nothing measures it,
   why compute it?
3. **What result would falsify the hypothesis?** A prediction that cannot fail is not a result.

## Output: a spec
A short document stating **what to calculate, why, and what constitutes success** — the falsifiable
prediction and the number/behavior that would confirm or kill it. This spec drives
`theory-derivation` and the acceptance criteria in `implementation-planning`.

## Common mistakes
- Jumping to "compute quantity X" without saying which observable it feeds.
- A success criterion of "it looks reasonable" — not falsifiable.
- Conflating the quantity with its proxy (what you compute vs what is measured).
