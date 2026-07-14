---
name: physical-verification
description: Use when a computed physics result must be verified independently of the code before it is trusted or published. Triggers on 物理验证, 五项检查, 验证结果, 结果对不对, 检查物理, 已知极限, verify the result, "is this right", "verify independently", "before I trust this", "check against a known limit", convergence check, symmetry check, self-consistency check, sanity check a result.
---

# Physical Verification (Stage 5)

## Overview
The most important stage, and **independent of code review**. The result passes only when all five
checks pass with recorded evidence. A passing self-test inside the code does *not* count — verification
lives outside the code that produced the number. The five checks are universal; your **domain pack**
supplies the specific symmetries, limits, and correspondences to use in each.

## The five checks
1. **① Dimensions / units.** Every quantity carries the right units. Use `dimensional-analysis`.
2. **② Symmetries.** Numerically verify your model transforms correctly under every symmetry it should
   respect, applying the operators explicitly. *(The domain pack lists which symmetries.)*
3. **③ Reduce to a known limit.** Tune parameters so the model degenerates to a solved sub-case and
   match published numbers (from `REFERENCES.md`). *(The domain pack names the solvable limits.)*
4. **④ Convergence.** Vary every discretization / truncation (mesh, size, order) and **plot the
   convergence curve** — never rely on "it looks converged". Report the measured order. See
   `convergence-study`.
5. **⑤ Self-consistency.** Two independently-computed quantities must agree. *(The domain pack specifies
   which two — e.g. an invariant computed two independent ways.)*

## Output: `VERIFICATION.md`
Check each of the five off one by one, each with evidence (a number or a figure). No check passes on
assertion alone. Template: `templates/VERIFICATION.md`.

## Red flags
"The asserts pass so it's verified" · eyeballed convergence with no curve · a symmetry claimed but
never applied numerically · a benchmark quoted from memory not reproduced · self-consistency between
two of *your own* methods sharing a convention (that is `external-anchor-doctrine`'s trap, not a check).
**Any of these means the check is not done.**
