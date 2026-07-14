---
name: production-mode
description: Use when a physics result must be trustworthy — going into a paper or report, reused across the project, or costly if wrong; also when an exploration turned up something that now must be made rigorous. Triggers on 正式计算, 正式算, 论文, 发表, 投稿, 要能信, 要可靠, 认真算, "production", "for the paper", "must be correct", "must be right", "publishable result", "make it rigorous", "trusted result".
---

# Production Mode

## Overview
The result must survive a hostile referee. Work is convention-driven, acceptance-gated, and verified
**independently of the code**. This skill sequences the stages; each stage has its own skill.

## The pipeline (in order)
| # | Stage | Skill | Output |
|---|-------|-------|--------|
| 0 | Literature & conventions | `literature-review-conventions` | `REFERENCES.md` |
| 1 | Brainstorm the real question | `physics-brainstorming` | spec |
| 2 | Theory derivation | `theory-derivation` | `DERIVATION.md` |
| 3 | Implementation plan | `implementation-planning` | plan citing DERIVATION.md |
| 4 | Code | `convention-driven-coding` | code, asserts green |
| 5 | Physical verification | `physical-verification` | `VERIFICATION.md` (5 checks) |

**Do not code (4) before `DERIVATION.md` exists (2).** The plan (3) must cite it.

## Handoff
Production ends when `VERIFICATION.md` is green. Reviewing the finished result is its own mode —
`review-workflow` (self-review → adversarial audit).

## The firewall (non-negotiable)
**Never promote exploration code.** If a result came from `exploration-mode`, that told you *where to
look* only. Re-derive from scratch at stage 2. A quick-and-dirty number in a paper is the most
expensive error in research.

## Rationalizations — STOP
| Excuse | Reality |
|--------|---------|
| "The exploration script already gives the number, just tidy it" | Restart at DERIVATION.md. Exploration proves nothing about *what* the answer is. |
| "Skip the derivation doc, it's in my head" | No DERIVATION.md ⇒ no conventions table ⇒ line-level convention bugs stay invisible. |
| "Asserts passed, so it's verified" | A passing self-test caps the claim at *partially* verified. Stage 5 is independent of the code. |
| "It's obviously converged" | Plot the convergence curve (stage 5, check ④). "Looks converged" is not evidence. |

## Red flags
Coding before DERIVATION.md · reusing an exploration script's output · claiming "verified" from the
code's own asserts · skipping any of the 5 physical checks. **All mean: back up a stage.**
