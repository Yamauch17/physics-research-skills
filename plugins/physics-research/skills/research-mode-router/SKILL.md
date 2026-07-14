---
name: research-mode-router
description: Use when starting a physics or research task and it is not yet decided whether to read existing material, run a quick cheap check, produce a trusted result, or review a finished one. Triggers on starting research, ambiguous scope, 研究, 计算, 帮我算, 帮我研究, 开始一个课题, 怎么入手, "help me look into", "figure out", "study this", "work on this problem", "where do I start", "what should I do first".
---

# Research Mode Router

## Overview
Every research task runs in one of three modes — plus an independent **Review** workflow for judging
finished work. Picking the wrong one is the most common source of waste (over-engineering a throwaway
check) or of costly error (trusting a quick-and-dirty script).
**Decide the mode first, then follow that mode's skill.**

## Pick the mode

```dot
digraph mode {
  rankdir=LR;
  q0 [shape=diamond,label="Goal is to JUDGE a\nFINISHED result / repo?\n(review, audit, referee)"];
  q1 [shape=diamond,label="Goal is to UNDERSTAND\nexisting material?\n(paper / book / slides / code)"];
  q2 [shape=diamond,label="Must the result be TRUSTED?\n(paper, report, reused,\ncostly if wrong)"];
  rev [shape=box,label="REVIEW\nreview-workflow"];
  read [shape=box,label="READ\nliterature-reading-notes"];
  prod [shape=box,label="PRODUCTION\nproduction-mode"];
  expl [shape=box,label="EXPLORATION\nexploration-mode"];
  q0 -> rev [label="yes"];
  q0 -> q1 [label="no"];
  q1 -> read [label="yes"];
  q1 -> q2 [label="no"];
  q2 -> prod [label="yes"];
  q2 -> expl [label="no / not yet"];
}
```

| Mode | You are… | Skill | Output |
|------|----------|-------|--------|
| Review | judging a finished result / repo / manuscript | `review-workflow` | sign-off or referee report |
| Read | understanding a paper/book/slides/code | `literature-reading-notes` | thorough notes |
| Explore | probing a question whose answer shape is unknown | `exploration-mode` | one-line `FINDINGS.md` + saved plot |
| Production | computing a result that must be trusted | `production-mode` | acceptance-gated deliverable |

Review is **independent of production**: it is never a pipeline stage, and it can run on work produced
anywhere (your pipeline, a collaborator's repo, a manuscript).

## The firewall (non-negotiable)
**Exploration code can never be promoted to a production result.** It tells you *where to look*, not
*what the answer is*. To produce a trusted result, restart from `theory-derivation` (DERIVATION.md).
A dirty-script number that reaches a paper is the most expensive mistake in the whole workflow.

## Domain packs
Inside a mode, subject-specific technique skills stack on top automatically (e.g. a
`topological-insulator` pack adds its subject techniques). The router and the three modes are
subject-agnostic; the domain pack supplies the physics.

## Common mistakes
- Defaulting to Production for something 20 minutes of exploration would answer.
- Staying in Exploration when the result is heading into a paper (upgrade — see `exploration-mode`).
- Skipping Read: coding a model you have not yet derived or understood.
- Treating review as the tail of Production — review is a separate workflow with a fresh, zero-trust
  mindset (`review-workflow`).
