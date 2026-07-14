# BUILD-PROGRESS — physics-research-skills

Live manifest for building the skill marketplace. Each `SKILL.md` is written to disk the instant it
is done and ticked here, so an interruption (token/charge cutoff) never loses finished work.
**Resume protocol:** read this file; the first unchecked item is the next task. Then run `validate.ps1`.

Plan: `C:\Users\96136\.claude\plans\kind-booping-perlis.md`. Repo root: `C:\Users\96136\Desktop\skills`.

## Standing decisions (from the conversation)
- Two plugins in one marketplace: `physics-research` (core, 24) + `topological-insulator` (domain, 9) = 33.
  (convergence-study moved core←domain: it is universal to all numerical physics.)
- Layered: core is subject-agnostic; TI specifics live only in the domain pack.
- Skill bodies + descriptions in English, with Chinese trigger keywords in descriptions.
- kdotpy de-emphasized — no skill, not in examples.
- **User removed "avoid subagents" and "token economy" rules — do NOT encode them; use subagents to pressure-test.**
- Save immediately; commit per family once `git init` done.
- Repo/homepage name assumed `Yamauch17/physics-research-skills` (user can rename before publishing).

## Phase 0 — Scaffold
- [x] `.claude-plugin/marketplace.json`
- [x] `plugins/physics-research/.claude-plugin/plugin.json`
- [x] `plugins/topological-insulator/.claude-plugin/plugin.json`
- [x] `LICENSE` (MIT)
- [x] `install-local.ps1`
- [x] `validate.ps1`
- [x] `BUILD-PROGRESS.md` (this file)
- [x] `README.md` (public: modes, install, skill index, add-a-domain-pack recipe, 中文速览)

## Phase 1 — Core Family A: router + 3 modes (4)  ✅ DONE
- [x] research-mode-router
- [x] literature-reading-notes
- [x] exploration-mode
- [x] production-mode

## Phase 2 — Core Family D primitives (referenced by B and C) (4)
- [ ] convention-table
- [ ] dimensional-analysis
- [ ] numerical-spot-check
- [ ] external-anchor-doctrine

## Phase 3 — Core Family B: production stages (7)  ✅ DONE
- [x] literature-review-conventions
- [x] physics-brainstorming
- [x] theory-derivation
- [x] implementation-planning
- [x] convention-driven-coding
- [x] physical-verification
- [x] research-review

## Phase 4 — Core Family D remainder (9)  ✅ DONE
- [x] prl-figure-style
- [x] jupytext-notebook-workflow
- [x] findings-logger
- [x] phased-git-workflow
- [x] obsidian-safe-markdown
- [x] adversarial-review
- [x] research-repo-bootstrap
- [x] checkpoint-and-resume
- [x] convergence-study (universal; moved from domain)

## Phase 5 — Domain Family C: topological band theory (9)  ✅ DONE
- [x] tight-binding-builder
- [x] symmetry-analysis
- [x] berry-curvature-chern
- [x] wilson-loop-wcc
- [x] z2-invariant
- [x] edge-states-bulk-boundary
- [x] kp-effective-model
- [x] topological-phase-diagram
- [x] numerical-tb-backend

## Phase 6 — Bundled resources (templates / scripts)  ✅ DONE
- [x] literature-reading-notes/templates/NOTE-TEMPLATE.md
- [x] exploration-mode/templates/FINDINGS.md
- [x] literature-review-conventions/templates/REFERENCES.md
- [x] physics-brainstorming/templates/SPEC.md
- [x] theory-derivation/templates/DERIVATION.md
- [x] implementation-planning/templates/PLAN.md
- [x] physical-verification/templates/VERIFICATION.md
- [x] research-review/templates/REVIEW-CHECKLIST.md
- [x] numerical-spot-check/scripts/spot_check.py  (self-test: ALL PASSED)
- [x] prl-figure-style/scripts/figstyle.py        (self-test: ALL PASSED)
- [x] adversarial-review/templates/REVIEW_REPORT.md
- [x] research-repo-bootstrap/templates/CLAUDE.md + PROGRESS.md
- [x] berry-curvature-chern/scripts/chern_fhs.py  (self-test: C=+1/-1/0, ALL PASSED)

## Phase 7 — Install + verify
- [x] run `validate.ps1` → ALL PASSED, 33 skills
- [x] run `install-local.ps1` → 33 junctions in ~/.claude/skills
- [x] run self-test scripts: spot_check.py, chern_fhs.py, figstyle.py → ALL PASSED
- [x] finalize `README.md`
- [x] `git init` + commit + push → https://github.com/Yamauch17/physics-research-skills (PUBLIC, main)

## Phase 8 — Quality: subagent pressure-tests (OPTIONAL follow-up, offered to user)
- [ ] Pressure-test discipline skills (exploration-mode, production-mode, convention-driven-coding, physical-verification, checkpoint-and-resume, adversarial-review); close loopholes. Not required for release; refines robustness.

## Phase 9 — Memory  ✅ DONE
- [x] Saved 5 memories: user-physics-researcher, save-immediately-checkpoint, no-subagent-token-rules, physics-skills-must-be-universal, physics-research-skills-project.

## Phase 10 — Review as a 4th mode (2026-07-14)  ✅ DONE
- [x] review-workflow (NEW skill): Level 1 self-review (research-review) → Level 2 adversarial audit (adversarial-review).
- [x] production-mode: pipeline now 6 stages (0–5), ends at physical-verification; hands off to review-workflow.
- [x] research-mode-router: Review added as the 4th mode (Read / Explore / Produce / Review), same standing as the others.
- [x] Trigger descriptions strengthened for ALL 34 skills (more natural EN + 中文 phrasings for better auto-activation).
- [x] Counts 33 → 34 (core 24 → 25): validate.ps1, install-local.ps1, both READMEs, AGENTS.md, GEMINI.md, codex plugin.json.
