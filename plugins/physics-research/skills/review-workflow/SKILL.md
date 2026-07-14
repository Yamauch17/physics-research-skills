---
name: review-workflow
description: Use whenever a finished result, repo, figure, or manuscript should be reviewed, checked, or audited and the depth is not yet chosen — routes between the light self-review pass and the hostile adversarial audit. Triggers on review, 评审, 审一下, 帮我检查, 检查一下结果, 把关, review workflow, "review my result", "check my work", "look over this", "is this ready", "ready to submit", 投稿前, 交差前, final review, pre-submission check, sign-off, "how carefully should this be reviewed".
---

# Review Workflow

## Overview
Review is an **independent workflow, not a production stage**. It runs on a *finished* result — one
produced by `production-mode` here, or by anyone else's repo — and it is deliberately decoupled from
production so the reviewer role never inherits the producer's assumptions. This skill picks the review
level; each level has its own skill.

## The two levels

| Level | Role | Skill | Output |
|-------|------|-------|--------|
| 1 | Self-review — your own critical pass | `research-review` | `REVIEW-CHECKLIST.md` sign-off |
| 2 | Adversarial audit — hostile top-tier referee | `adversarial-review` | `REVIEW_REPORT.md` with verdicts |

## Pick the level
- **Level 1** when *you* produced the result and are deciding whether to call it final. Cheap, always
  run it first.
- **Level 2** when the result is heading out the door (submission, report, handoff), when the repo is
  not yours, or when Level 1 raised doubts it could not settle. Level 2 starts from zero trust:
  independent re-derivation before reading the project's own.
- Escalate 1 → 2; never substitute 1 for 2 on anything leaving the project.

## Independence rules (non-negotiable)
- **Producer ≠ reviewer mindset.** Enter review fresh: the production pipeline's docs
  (`DERIVATION.md`, `VERIFICATION.md`) are *inputs to be checked*, not evidence to be trusted.
- **Entry gate for your own production results:** do not start review before `physical-verification`
  is green — review judges a finished result, it is not a substitute for verification.
- **Review does not fix.** Findings go in the report with `file:line`; changing project code is a
  separate, after-the-review decision.

## Common mistakes
- Treating review as the last stage of production — it is a separate workflow with a separate mindset.
- Skipping Level 1 because "the adversarial review will catch it anyway" — Level 1 is cheap and
  catches the overstatements you can see yourself.
- Running Level 2 on your own result while still in producer mode — reuse of your own conventions and
  scripts silently voids the audit (see `external-anchor-doctrine`).
