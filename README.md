# Physics Research Skills

Auto-activating [Claude Code](https://claude.com/claude-code) skills for **physics research** — a
subject-agnostic research-process **core** plus **pluggable domain packs**. The first domain pack is
topological insulators; the architecture is built so any physics subject can add its own pack without
touching the core.

Modeled on [`obra/superpowers`](https://github.com/obra/superpowers) (process-skill format + plugin
distribution) and [`K-Dense-AI/scientific-agent-skills`](https://github.com/K-Dense-AI/scientific-agent-skills)
(large SKILL.md library).

> **中文速览:** 面向物理科研的 Claude Code 技能集。核心插件 `physics-research`(24 个技能,**对所有物理学科通用**)
> 把科研分成三种模式——**读**(文献→严谨笔记)、**探索**(低成本、可追溯的快速试探)、**生产**(可信、可发表的
> 七阶段流水线);领域插件 `topological-insulator`(9 个技能)提供拓扑绝缘体的具体方法(紧束缚 H(k)、陈数、Z2、
> 边缘态……)。核心里不出现 H(k) 这类学科专属内容——它们只属于领域插件。技能靠描述里的触发词**自动激活**。

## The idea: three research modes

Every task runs in one mode; picking the wrong one is where research time is wasted or trust is lost.
The `research-mode-router` skill routes you:

| Mode | When | Output |
|------|------|--------|
| **Read** | understand a paper / book / slides / code | thorough notes, full derivations |
| **Explore** | probe a question whose answer you can't yet picture | one-line `FINDINGS.md` + a saved plot |
| **Produce** | a result that must be trusted / published / reused | acceptance-gated deliverable |

A hard **firewall** separates them: exploration code tells you *where to look*, never *what the answer
is*. Trusted results are re-derived from scratch through a 7-stage production pipeline.

## Architecture: core + domain packs

```
physics-research-skills/            (this repo = a Claude Code plugin marketplace)
├── plugins/
│   ├── physics-research/           Tier 1 — subject-agnostic core (24 skills)
│   └── topological-insulator/      Tier 2 — domain pack (9 skills)
└── .claude-plugin/marketplace.json
```

The **core** speaks only of "your model / governing equations / structural invariants". Anything a
different subject wouldn't share (a Bloch Hamiltonian `H(k)`, Berry curvature, edge states) lives
**only** in a domain pack. Add a new subject = add a sibling plugin; the core is untouched.

## Install

### Public (once the repo is on GitHub)
```text
/plugin marketplace add Yamauch17/physics-research-skills
/plugin install physics-research@physics-research-skills
/plugin install topological-insulator@physics-research-skills
```
Install just the core for non-topological work; add domain packs as needed.

### Local (author machine, no marketplace)
```powershell
pwsh -File install-local.ps1     # junctions every skill into ~/.claude/skills
pwsh -File validate.ps1          # structural check (name==folder, description present) — expects 33
```

## Skills

### `physics-research` — core (24), universal to all physics
**Router + the 3 modes:** `research-mode-router` · `literature-reading-notes` · `exploration-mode` ·
`production-mode`
**Production pipeline (7 stages):** `literature-review-conventions` · `physics-brainstorming` ·
`theory-derivation` · `implementation-planning` · `convention-driven-coding` · `physical-verification` ·
`research-review`
**Rigor & infrastructure:** `convention-table` · `dimensional-analysis` · `numerical-spot-check` ·
`external-anchor-doctrine` · `convergence-study` · `prl-figure-style` · `jupytext-notebook-workflow` ·
`findings-logger` · `phased-git-workflow` · `obsidian-safe-markdown` · `adversarial-review` ·
`research-repo-bootstrap` · `checkpoint-and-resume`

### `topological-insulator` — domain pack (9)
`tight-binding-builder` · `symmetry-analysis` · `berry-curvature-chern` · `wilson-loop-wcc` ·
`z2-invariant` · `edge-states-bulk-boundary` · `kp-effective-model` · `topological-phase-diagram` ·
`numerical-tb-backend`

Runnable self-tests ship with the code skills: `numerical-spot-check/scripts/spot_check.py`,
`prl-figure-style/scripts/figstyle.py`, `berry-curvature-chern/scripts/chern_fhs.py` (FHS Chern with a
massive-Dirac sign anchor).

## Add your own domain pack

1. Copy `plugins/topological-insulator/` to `plugins/<your-subject>/`.
2. Edit `.claude-plugin/plugin.json` (name, description, keywords).
3. Add skills under `skills/<name>/SKILL.md`. Keep subject-specific symbols here, not in the core; make
   each skill **reference** core skills (`theory-derivation`, `physical-verification`, …) rather than
   duplicate them.
4. List the plugin in `.claude-plugin/marketplace.json`.
5. `pwsh -File validate.ps1`, then reinstall.

## How auto-activation works

Each `SKILL.md` has a `description` written as pure *triggering conditions* ("Use when …") packed with
English + Chinese keywords. Claude reads descriptions and loads a skill when the task matches — no
manual `/command` needed. Descriptions never summarize the workflow (that would let Claude shortcut the
skill body).

## Credits & license

Method conventions distilled from real research repos (phased-git, PRL figures, external-anchor
doctrine, adversarial review). Format inspired by `superpowers` and `scientific-agent-skills`.
**MIT** — see `LICENSE`.
