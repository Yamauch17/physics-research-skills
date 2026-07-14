# physics-research

Auto-activating Claude Code skills that make **physics research** rigorous by default — a
**subject-agnostic** research-process core. Pair it with a domain pack (e.g.
[`topological-insulator`](../topological-insulator)) for subject-specific techniques.

Part of the [physics-research-skills](https://github.com/Yamauch17/physics-research-skills) marketplace.

## What it does

Every research task runs in one of **four modes**, and a router picks the right one:

| Mode | When | Output |
|------|------|--------|
| **Read** | understand a paper / book / slides / code | thorough notes, full derivations |
| **Explore** | probe a question you can't yet picture | one-line `FINDINGS.md` + a saved plot |
| **Produce** | a result that must be trusted / published | acceptance-gated deliverable |
| **Review** | judge a finished result / repo / manuscript | sign-off or referee report |

**Produce** is a 6-stage pipeline — literature & conventions → brainstorm → **derivation** (with a
conventions table + per-step numerical spot-checks) → plan → convention-driven code → **5-check
physical verification** (units · symmetries · known-limit reduction · convergence · self-consistency).
A hard firewall keeps quick-and-dirty exploration code out of trusted results.

**Review** runs on a finished result — yours or anyone's — at two levels (self-review sign-off, then
a hostile adversarial audit).

## Skills (25)

- **Router + modes:** `research-mode-router`, `literature-reading-notes`, `exploration-mode`,
  `production-mode`
- **Production pipeline:** `literature-review-conventions`, `physics-brainstorming`,
  `theory-derivation`, `implementation-planning`, `convention-driven-coding`, `physical-verification`
- **Review:** `review-workflow`, `research-review`, `adversarial-review`
- **Rigor & infrastructure:** `convention-table`, `dimensional-analysis`, `numerical-spot-check`,
  `external-anchor-doctrine`, `convergence-study`, `prl-figure-style`, `jupytext-notebook-workflow`,
  `findings-logger`, `phased-git-workflow`, `obsidian-safe-markdown`,
  `research-repo-bootstrap`, `checkpoint-and-resume`

The core stays universal to all of physics — no subject-specific objects leak in; those live in domain packs.

## Install

Run each as a separate `/plugin` command:
```text
/plugin marketplace add Yamauch17/physics-research-skills
```
```text
/plugin install physics-research@physics-research-skills
```

Skills auto-activate from their `description` triggers — no manual command needed. For Codex, Cursor,
Gemini CLI, or Copilot CLI, see the [main README](../../README.md#install--use-in-your-agent).

## Example session

> **You:** 读这篇论文,帮我做详细的推导笔记
> → `literature-reading-notes` (Read): every step derived, physical picture, Chinese notes.
>
> **You:** quick look at how the result scales with the coupling
> → `exploration-mode`: dirty script in `scratch/`, plot saved with params in the filename, one line to `FINDINGS.md`.
>
> **You:** now I need this number for the paper — it has to be right
> → `production-mode`: runs the 6 stages; `physical-verification` blocks the result until all five checks pass.
>
> **You:** 结果出来了,投稿前帮我审一遍
> → `review-workflow`: self-review sign-off, then `adversarial-review` as a hostile referee.

## Security profile

Pure Markdown skills plus two self-test scripts (`numerical-spot-check/scripts/spot_check.py`,
`prl-figure-style/scripts/figstyle.py`) that use only `numpy`/`matplotlib`. **No MCP servers, no
network calls, no hooks, no telemetry.** MIT licensed.
