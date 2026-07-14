---
name: research-review
description: Use when reviewing your own result before declaring it final — checking code quality and whether the physics conclusions are actually supported by the data. Triggers on 自查, 自我检查, 自审, 收尾检查, 定稿前, self-review, sign-off, "is my result solid", "does the data support this", "am I overclaiming", "before I call this done", "double-check my result", final check, finalizing a result.
---

# Research Review (Self-Review)

## Overview
Level 1 of `review-workflow`: the self-review gate before a result is called final. This is *your
own* critical pass; the hostile external audit is Level 2 — see `adversarial-review`. For a result
out of the production pipeline, run this only after `physical-verification` is green.

## Code level
- **Readability & reuse:** would another person (or you in six months) follow it? Duplicated logic
  factored out?
- **Numerical stability:** behavior in the hard regime — near singularities, degeneracies, stiff or
  ill-conditioned parameters, and boundaries. Test the hard case, not just the generic point.

## Physics level
- **Are the conclusions supported by the data?** Point to the figure/number for each claim.
- **Any overstatements?** Trim claims the data does not carry.
- **Have trivial explanations been ruled out?** Finite-size effects, discretization artifacts,
  numerical noise — explicitly excluded, not ignored. Most "exciting" results are one of these until
  proven otherwise.

## Output
A short sign-off (`templates/REVIEW-CHECKLIST.md`) recording each claim → its evidence, and each
trivial-explanation candidate → why it is excluded.

## Common mistakes
- Reviewing prose, not stability — the bug lives in the singular regime you did not test.
- "The trend is clear" with no ruling-out of finite-size / discretization effects.
- Claiming more than the verified quantity supports.
