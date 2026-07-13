---
name: research-review
description: Use when reviewing your own production result before declaring it final — checking code quality and whether the physics conclusions are actually supported by the data. Triggers on 自查, self-review, sign-off, "is my result solid", "before I call this done", finalizing a result.
---

# Research Review (Stage 6)

## Overview
The self-review gate before a result is called final. Two levels. This is *your own* critical pass; a
hostile external audit is a separate, heavier step — see `adversarial-review`. Run this only after
`physical-verification` (Stage 5) is green.

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
